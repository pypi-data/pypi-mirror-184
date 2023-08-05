import azure.cognitiveservices.speech as speechsdk
from boto3 import Session as BotoSession
from pato.lovo import LovoClient
from pato.ubsession import UBSession

AZURE = "azure"
POLLY = "polly"
UBERDUCK = "uberduck"
LOVO = "lovo"


class VoiceClient(object):
    def __init__(self, aws_params=None, uberduck_params=None, lovo_params=None, azure_params=None):

        if uberduck_params:
            self.uberduck_session = UBSession(
                uberduck_params["api_key"], uberduck_params["secret_key"]
            )
            self.uberduck_client = self.uberduck_session.client()
        if aws_params:
            # Create a client using the credentials and region defined in the [adminuser]
            # section of the AWS credentials file (~/.aws/credentials)
            self.boto_session = BotoSession(
                aws_access_key_id=aws_params["access_key_id"],
                aws_secret_access_key=aws_params["secret_access_key"],
                region_name=aws_params["region"],
            )
            bucket = aws_params.get("bucket")
            self.polly_client = self.boto_session.client("polly")
            self.polly_client.aws_bucket = bucket

            # NOTE(zach): lovo_params depend on AWS params, so this check is
            # nested inside the AWS check.
            if lovo_params:
                s3_client = self.boto_session.client("s3")
                self.lovo_client = LovoClient(
                    **lovo_params,
                    s3_client=s3_client,
                    s3_bucket=bucket,
                    s3_region=aws_params["region"],
                )
        if azure_params:
            self.azure_key = azure_params["key"]
            self.azure_region = azure_params["region"]

    def synthesize_speech_synchronously(self, text, voice_id, voice_source, **kwargs):
        """Synthesize speech and return audio bytes."""
        if voice_source not in [POLLY, AZURE]:
            raise Exception("Only Polly and Azure are supported for synchronous speech synthesis.")
        if voice_source == POLLY:
            response = self.polly_client.synthesize_speech(
                VoiceId=voice_id,
                Text=text,
                **kwargs,
            )
            return response["AudioStream"].read()
        elif voice_source == AZURE:
            word_boundaries = kwargs.get("word_boundaries", False)
            speech_config = speechsdk.SpeechConfig(
                subscription=self.azure_key,
                region=self.azure_region,
            )
            if word_boundaries:
                speech_config.set_property(
                    property_id=speechsdk.PropertyId.SpeechServiceResponse_RequestSentenceBoundary,
                    value='true'
                )
            audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
            speech_config.speech_synthesis_voice_name = voice_id

            speech_synthesizer = speechsdk.SpeechSynthesizer(
                speech_config=speech_config, audio_config=audio_config
            )
            if word_boundaries:
                word_offsets = []
                def _word_boundary_handler(evt: speechsdk.SessionEventArgs):
                    if evt.boundary_type not in [speechsdk.SpeechSynthesisBoundaryType.Word, speechsdk.SpeechSynthesisBoundaryType.Punctuation]:
                        return
                    audio_offset_ms = (evt.audio_offset + 5000) // 10000
                    word_offsets.append({
                        "word": evt.text,
                        "start": audio_offset_ms,
                        "end": audio_offset_ms + evt.duration.total_seconds() * 1000,
                    })
                speech_synthesizer.synthesis_word_boundary.connect(_word_boundary_handler)

            result = speech_synthesizer.speak_text_async(text).get()
            word_offsets = sorted(word_offsets, key=lambda x: x["start"])
            word_offsets_combine_punctuation = []
            for i, word in enumerate(word_offsets):
                if word["word"] in [".", ",", "!", "?", "-", ";"]:
                    word_offsets_combine_punctuation[-1]["word"] += word["word"]
                else:
                    word_offsets_combine_punctuation.append(word)

            if result.reason == speechsdk.ResultReason.Canceled:
                raise Exception(result.cancellation_details.reason)
            return dict(
                data=result.audio_data,
                word_offsets=word_offsets_combine_punctuation if word_boundaries else None,
            )

    def synthesize_speech(self, text, voice_id, voice_source):
        """Synthesize speech and return a URL to an audio file."""

        if voice_source == POLLY:
            output = self.polly_client.start_speech_synthesis_task(
                Text=text,
                OutputFormat="mp3",
                VoiceId=voice_id,
                Engine="neural",
                OutputS3BucketName=self.polly_client.aws_bucket,
            )
            path = output["SynthesisTask"]["OutputUri"]
            fmt = "pcm"
        elif voice_source == UBERDUCK:
            output = self.uberduck_client.get_audio(text=text, voice=voice_id)
            path = output.json()["path"]
            fmt = "wav"
        elif voice_source == LOVO:
            path = self.lovo_client.synthesize_speech(text, voice_id)
            fmt = "wav"
        return (path, fmt)

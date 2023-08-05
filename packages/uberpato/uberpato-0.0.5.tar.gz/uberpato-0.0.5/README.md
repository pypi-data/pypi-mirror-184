# Pato

A client to various TTS APIs.

## Usage

```python
from pato.voiceclient import VoiceClient

vc = VoiceClient(
  # See voiceclient.py for params needed for each API.
  aws_params=dict(...),
  azure_params=dict(...),
  uberduck_params=dict(...),
)
vc.synthesize_speech_synchronously(...) # Returns bytes.
vc.synthesize_speech(...) # Returns a URL.
```

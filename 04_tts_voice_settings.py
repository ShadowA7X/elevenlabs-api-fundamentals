from dotenv import load_dotenv
import os
import sys
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
if not api_key:
    print("Error: ELEVENLABS_API_KEY environment variable is not set.")
    sys.exit(1)

client = ElevenLabs(api_key=api_key)

VOICE_ID = "FGY2WhTYpPnrIDTdsKH5"  # Laura - Enthusiast, Quirky Attitude
MODEL_ID = "eleven_flash_v2"

audio = client.text_to_speech.convert(
    voice_id=VOICE_ID,
    model_id=MODEL_ID,
    text="Hello! Here is an example customizing stability, similarity boost, and style parameters.",
    output_format="mp3_44100_128",
    voice_settings=VoiceSettings(
        stability=0.5,
        similarity_boost=0.75,
        style=0.0,
        use_speaker_boost=True,
    ),
)

out_path = "out_custom_settings.mp3"
with open(out_path, "wb") as f:
    if isinstance(audio, (bytes, bytearray)):
        f.write(audio)
    else:
        for chunk in audio:
            if isinstance(chunk, (bytes, bytearray)):
                f.write(chunk)

print(f"Saved {out_path}")

from dotenv import load_dotenv
import os
from elevenlabs.client import ElevenLabs

load_dotenv()
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

VOICE_ID = "FGY2WhTYpPnrIDTdsKH5"  # We are using Laura - Enthusiast, Quirky Attitude
MODEL_ID = "eleven_flash_v2"  # We selected the model Eleven Flash v2

audio = client.text_to_speech.convert(
    voice_id=VOICE_ID,
    model_id=MODEL_ID,
    text="Hello! This is my first ElevenLabs API project.",
    output_format="mp3_44100_128",
)

out_path = "out.mp3"
with open(out_path, "wb") as f:
    if isinstance(audio, (bytes, bytearray)):
        f.write(audio)
    else:
        for chunk in audio:
            if isinstance(chunk, (bytes, bytearray)):
                f.write(chunk)

print(f"Saved {out_path}")


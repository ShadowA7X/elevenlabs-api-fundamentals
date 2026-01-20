from dotenv import load_dotenv
import os
from elevenlabs.client import ElevenLabs

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(api_key=api_key)

resp = client.voices.search()
print(f"Found {len(resp.voices)} voices")
for v in resp.voices[:5]:
    print("-", v.voice_id, "|", v.name)

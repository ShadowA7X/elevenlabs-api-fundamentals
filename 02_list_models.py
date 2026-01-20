from dotenv import load_dotenv
import os
from elevenlabs.client import ElevenLabs

load_dotenv()
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

models = client.models.list()
for m in models:
    print("-", getattr(m, "model_id", None) or getattr(m, "id", None), "|", getattr(m, "name", ""))

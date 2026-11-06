# ElevenLabs API Fundamentals

A concise Python collection demonstrating the core capabilities and parameters of the **ElevenLabs API** using the official Python SDK.

## Project Structure

- **`01_list_voices.py`**: Searches and lists available voices along with their `voice_id` and `name`.
- **`02_list_models.py`**: Retrieves and prints available ElevenLabs TTS models (`model_id` and `name`).
- **`03_tts_to_file.py`**: Converts text to speech (`mp3_44100_128`) using the `eleven_flash_v2` model and saves the audio stream to `out.mp3`.
- **`04_tts_voice_settings.py`**: Demonstrates how to customize voice generation parameters (`VoiceSettings`: `stability`, `similarity_boost`, `style`, and `use_speaker_boost`) and validates the API key environment variable.

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure your API key:

Copy `.env.example` to `.env` and set your ElevenLabs API key:

```bash
cp .env.example .env
```

```env
ELEVENLABS_API_KEY=your_api_key_here
```

## Usage

Run any script directly with Python:

```bash
python 01_list_voices.py
python 02_list_models.py
python 03_tts_to_file.py
python 04_tts_voice_settings.py
```

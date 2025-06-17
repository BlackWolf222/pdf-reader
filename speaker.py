import os
from dotenv import load_dotenv
from elevenlabs import ElevenLabs
from elevenlabs import play

class Speaker:
    def __init__(self, text: str, voice_id: str = "TumdjBNWanlT3ysvclWh"):
        self.text = text
        self.voice_id = voice_id

    def text_to_speech(self):
        """
        Convert text to speech using ElevenLabs API.
        Args:
            text (str): The text to convert to speech.
            voice_id (str): The ID of the voice to use for conversion.
        """

        load_dotenv()

        elevenlabs = ElevenLabs(
            api_key=os.getenv("ELEVENLABS_API_KEY"),
        )

        audio = elevenlabs.text_to_speech.convert(
            text=self.text,
            voice_id=self.voice_id,
            model_id="eleven_flash_v2_5",
            output_format="mp3_44100_128",
        )

        play(audio)
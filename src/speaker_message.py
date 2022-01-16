from discord import Message, VoiceClient
from speaker_config import SpeakerConverterConfig


class SpeakerMessage:
    message: Message = None
    config: SpeakerConverterConfig = None

    def __init__(self, message, config: SpeakerConverterConfig):
        self.message = message
        self.config = config

    # TODO: 音声プレイヤー側に定義したほうがよいであろう
    def is_playing(self):
        return self.get_voice_client().is_playing()

    def get_voice_client(self) -> VoiceClient:
        return self.message.guild.voice_client

    def get_message(self):
        return self.message.content

    def get_config(self):
        return self.config

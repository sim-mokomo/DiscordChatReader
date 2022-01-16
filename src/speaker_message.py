from discord import Message, VoiceClient


class SpeakerMessage:
    message: Message = None
    speaker_name: str = ""

    def __init__(self, message, speaker_name: str):
        self.message = message
        self.speaker_name = speaker_name

    # TODO: 音声プレイヤー側に定義したほうがよいであろう
    def is_playing(self):
        return self.get_voice_client().is_playing()

    def get_voice_client(self) -> VoiceClient:
        return self.message.guild.voice_client

    def get_message(self):
        return self.message.content

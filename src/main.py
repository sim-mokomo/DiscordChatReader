import os
import discord
from gtts import gTTS
from config import Config
from pydub import AudioSegment
from pydub import effects
from voicetext import VoiceText


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content == "/come-on":
            if message.author.voice is None:
                return
            await message.author.voice.channel.connect()
        elif message.content == "/leave":
            if message.guild.voice_client is None:
                return
            await message.guild.voice_client.disconnect()
        else:
            if message.guild.voice_client is None:
                return
            if message.author.id == config.speaker_member_id:
                voice_client = message.guild.voice_client
                play(voice_client, message.content)


def get_temp_resource_path() -> str:
    return os.path.join(os.getcwd(), 'temp_resources')


def play(voice_client, text):
    output_file_name = "text_voice.mp3"

    temp_resource_path = get_temp_resource_path()
    if not os.path.exists(temp_resource_path):
        os.mkdir(temp_resource_path)
    output_path = os.path.join(temp_resource_path, output_file_name)

    with open(output_path, 'wb') as f:
        f.write(voice_text.to_wave(text))

    voice_client.play(discord.FFmpegPCMAudio(output_path))


client = MyClient()
config = Config()

voice_text = VoiceText(config.voice_text.api_key)
voice_text.speaker(config.voice_text.speaker)
voice_text.speed(config.voice_text.speed)

client.run(config.token)

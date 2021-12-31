import discord
from gtts import gTTS
from config import Config


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


def play(voice_client, text):
    output = gTTS(text=text, lang='ja', slow=False)
    # todo: 専用のディレクトリ以下に音声ファイルを生成する
    output_file_name = "text_voice.mp3"
    output.save(output_file_name)
    voice_client.play(discord.FFmpegPCMAudio(output_file_name))


client = MyClient()
config = Config()
client.run(config.token)

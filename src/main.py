import discord
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

        if message.content == "/leave":
            if message.guild.voice_client is None:
                return
            await message.guild.voice_client.disconnect()

        if message.content == "/test":
            if message.guild.voice_client is None:
                return

            message.guild.voice_client.play(discord.FFmpegPCMAudio("resources/test.mp3"))

client = MyClient()
config = Config()
client.run(config.token)
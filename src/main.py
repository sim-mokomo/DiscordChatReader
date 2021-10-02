import discord
from discord.ext import tasks
import subprocess

class SpeetchContent:
    def __init__(self, text):
        self.text = text

stack = []
voice_client = None
bot_member_id = 884832695987875930
nareai_guild_id = 413772529690476544
sim_mokomo_member_id = 275399320940052480
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
            if message.author.id == sim_mokomo_member_id:
                stack.append(SpeetchContent(message.content))
                global voice_client
                voice_client = message.guild.voice_client
                play(message.content)

@tasks.loop(seconds=1)
async def loop():
    print("loop")
    if len(stack) != 0:
        print("loop len")
        if voice_client != None:
            s = stack.pop(0)
            print(s.text)
            play(s.text)


def play(text):
    with open('sjis-2.txt', 'w') as f:
        f.write(text)
        subprocess.call("./open_jtalk/bin/open_jtalk.exe -m ./open_jtalk/bin/nitech_jp_atr503_m001.htsvoice -x open_jtalk/bin/dic/ -ow output.wav sjis-2.txt -r 1")
        voice_client.play(discord.FFmpegPCMAudio("output.wav"))


# loop.start()
client = MyClient()
config = Config()
client.run(config.token)
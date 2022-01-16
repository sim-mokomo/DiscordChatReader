import os
import discord
from discord.ext import tasks, commands
from config import Config
from config_loader import ConfigLoader
from voicetext import VoiceText
from speaker_config import SpeakerConverterConfig
from speaker_message import SpeakerMessage
import re
import emoji


class Command:
    command_name = ''
    callback = None

    def __init__(self, command_name, callback):
        self.command_name = command_name
        self.callback = callback


class MyCog(commands.Cog):
    current_speak_message: SpeakerMessage = None

    def __init__(self):
        self.index = 0
        self.printer.start()

    def cof_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=0.5)
    async def printer(self):
        if not (len(message_stack) > 0):
            return

        if self.current_speak_message is None:
            self.current_speak_message = message_stack.pop(0)
            play(self.current_speak_message.get_voice_client(),
                 self.current_speak_message.get_message(),
                 self.current_speak_message.get_config())

        if not self.current_speak_message.is_playing():
            self.current_speak_message = None


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
        command_table.append(Command('/come-on', self.on_execute_come_command))
        command_table.append(Command('/leave', self.on_execute_leave_command))

    async def on_message(self, message):
        if message.author.bot:
            return

        for command in command_table:
            if command.command_name == message.content:
                await command.callback(message)
                return
        await self.on_execute_any_text_command(message)

    async def on_execute_come_command(self, message):
        if message.author.voice is None:
            return
        await message.author.voice.channel.connect()
        return

    async def on_execute_leave_command(self, message):
        if message.guild.voice_client is None:
            return
        await message.guild.voice_client.disconnect()
        return

    async def on_execute_any_text_command(self, message):
        if message.guild.voice_client is None:
            return

        speak_convert_config: SpeakerConverterConfig = config \
            .speaker_convert_config_table \
            .get_config_from_member_id(message.author.id)
        if speak_convert_config is not None:
            message_stack.append(SpeakerMessage(message, speak_convert_config))


def get_temp_resource_path() -> str:
    return os.path.join(os.getcwd(), 'temp_resources')


# TODO: プレイヤーとして定義する
def play(voice_client, text, message_config: SpeakerConverterConfig):
    output_file_name = "text_voice.mp3"

    temp_resource_path = get_temp_resource_path()
    if not os.path.exists(temp_resource_path):
        os.mkdir(temp_resource_path)
    output_path = os.path.join(temp_resource_path, output_file_name)

    with open(output_path, 'wb') as f:
        print(f'before: {text}')
        text = remove_emoji_from_text(text)
        text = remove_custom_emoji_from_text(text)
        text = remove_mention_from_text(text)
        print(f'after: {text}')
        if len(text) > 0:
            voice_text.speaker(message_config.speaker_name)
            voice_text.speed(message_config.speed)
            f.write(voice_text.to_wave(text))

    voice_client.play(discord.FFmpegPCMAudio(output_path))

# TODO: テキストフォーマッタは別クラスにする
def remove_emoji_from_text(text):
    return ''.join(filter(lambda x: x not in emoji.UNICODE_EMOJI_ENGLISH, text))


def remove_custom_emoji_from_text(text):
    # カスタム絵文字フォーマットは <:emoji_name:emoji_id>
    return re.sub(r'<:\w+:\d+>', '', text)


def remove_mention_from_text(text):
    # メンションフォーマットは <@!user_id>
    return re.sub(r'<@!\d+>', '', text)


client = MyClient()
config: Config = ConfigLoader.load('config.json')
command_table: [Command] = []
cog = MyCog()
message_stack: [SpeakerMessage] = []
voice_text = VoiceText(config.voice_text_web_api_key)

client.run(config.token)

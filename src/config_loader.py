import json
from config import Config
from speaker_config import SpeakerConverterConfig


class ConfigLoader:
    @staticmethod
    def load(path):
        config = Config()

        json_open = open('config.json', 'r')
        json_obj = json.load(json_open)
        config.token = json_obj['token']
        print(json_obj)
        speaker_convert_config_table_json = json_obj['speaker_convert_config_table']
        for speaker_convert_config_json in speaker_convert_config_table_json:
            speaker_config = SpeakerConverterConfig()
            speaker_config.member_id = int(speaker_convert_config_json['member_id'])
            speaker_config.speaker_name = str(speaker_convert_config_json['speaker_name'])
            config.speaker_convert_config_table.append(speaker_config)

        voice_text_json_obj = json_obj['voice_text']
        config.voice_text.api_key = voice_text_json_obj['api_key']
        config.voice_text.speed = voice_text_json_obj['speed']

        return config


print(ConfigLoader.load("config.json"))

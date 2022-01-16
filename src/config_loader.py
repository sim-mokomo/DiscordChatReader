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
        config.voice_text_web_api_key = str(json_obj['voice_text_web_api_key'])

        print(json_obj)
        speaker_convert_config_table_json = json_obj['speaker_convert_config_table']
        for speaker_convert_config_json in speaker_convert_config_table_json:
            speaker_config = SpeakerConverterConfig()
            speaker_config.member_id = int(speaker_convert_config_json['member_id'])
            speaker_config.speaker_name = str(speaker_convert_config_json['speaker_name'])
            speaker_config.speed = int(speaker_convert_config_json['speed'])
            config.speaker_convert_config_table.append(speaker_config)

        return config

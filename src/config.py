import json
from speaker_config import SpeakerConverterConfigTable


class Config:
    token = ""

    # TODO: SpeakerConverterConfigに統合させる
    class VoiceText:
        api_key = ""
        speaker = ""
        speed = 0

    voice_text = VoiceText()

    speaker_convert_config_table: SpeakerConverterConfigTable = SpeakerConverterConfigTable()

    def __init__(self):
        json_open = open('config.json', 'r')
        json_obj = json.load(json_open)
        self.token = json_obj['token']
        print(json_obj)
        speaker_convert_config_table_json = json_obj['speaker_convert_config_table']
        for speaker_convert_config_json in speaker_convert_config_table_json:
            speaker_config = Config.SpeakerConverterConfig()
            speaker_config.member_id = int(speaker_convert_config_json['member_id'])
            speaker_config.speaker_name = str(speaker_convert_config_json['speaker_name'])
            self.speaker_convert_config_table.append(speaker_config)

        voice_text_json_obj = json_obj['voice_text']
        self.voice_text.api_key = voice_text_json_obj['api_key']
        self.voice_text.speed = voice_text_json_obj['speed']

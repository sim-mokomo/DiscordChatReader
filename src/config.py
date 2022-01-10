import json


class Config:
    token = ""
    speaker_member_id = 0

    class VoiceText:
        api_key = ""
        speaker = ""
        speed = 0
    voice_text = VoiceText()

    def __init__(self):
        json_open = open('config.json', 'r')
        json_obj = json.load(json_open)
        self.token = json_obj['token']
        self.speaker_member_id = int(json_obj['speaker_member_id'])

        voice_text_json_obj = json_obj['voice_text']
        self.voice_text.api_key = voice_text_json_obj['api_key']
        self.voice_text.speaker = voice_text_json_obj['speaker']
        self.voice_text.speed = voice_text_json_obj['speed']

import json


class Config:
    token = ""
    speaker_member_id = 0

    def __init__(self):
        json_open = open('config.json', 'r')
        json_obj = json.load(json_open)
        self.token = json_obj['token']
        self.speaker_member_id = int(json_obj['speaker_member_id'])

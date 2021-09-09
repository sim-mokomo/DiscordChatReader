import json

class Config:
    token = ""
    def __init__(self):
        json_open = open('config.json', 'r')
        json_obj = json.load(json_open)
        self.token = json_obj['token']
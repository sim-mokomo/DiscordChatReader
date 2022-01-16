class SpeakerConverterConfig:
    member_id: int = 0
    speaker_name: str = ""


class SpeakerConverterConfigTable:
    table: [SpeakerConverterConfig] = []

    def append(self, config: SpeakerConverterConfig):
        self.table.append(config)

    def get_config_from_member_id(self, member_id: int):
        for config in self.table:
            if config.member_id == member_id:
                return config
        return None

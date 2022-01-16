from speaker_config import SpeakerConverterConfigTable


class Config:
    token = ""

    # TODO: SpeakerConverterConfigに統合させる
    class VoiceText:
        api_key = ""
        speed = 0

    voice_text = VoiceText()
    speaker_convert_config_table: SpeakerConverterConfigTable = SpeakerConverterConfigTable()

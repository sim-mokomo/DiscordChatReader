# DiscordChatReader


チャンネルにBotを招待すると、自身が打ち込んだ文字を読み上げてくれる。  
個人利用用なので読み上げ対象として設定できる人間は1人のみ。

# 環境

- python 3.9.6
- ffmpeg N-105039-g12f21849e5-20211230
- [voice text web api](https://cloud.voicetext.jp/webapi)
- [python-voicetext](https://github.com/youtalk/python-voicetext#readme)

## 注意点
- PyAudioは公式では3.6系までのみサポートされている
  - 本アプリでは3.9系を使用しているため、[こちら](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) から手動インストールしている。

```
pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl
```

# Configについて

- speaker_member_id
  - Discordのボイスチャンネル上のアイコンから「IDをコピー」で取得
- token
  - Discordが発行するBotトークン
- voice_text
  - api_key
    - VoiceTextWebApi登録時に発行されるAPIキー
  - speaker
  - speed
    - VoiceTextWebApiの「APIマニュアル」を参考に記述
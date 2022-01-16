# DiscordChatReader


チャンネルにBotを招待すると、自身が打ち込んだ文字を読み上げてくれる。  
読み上げ対象は複数人指定できる。

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

`<root>/config-template.json` を `<root>/config.json` に変更することで読み込まれるようになる。
デフォルトではダミー値が記述されているので、以下の説明を参考に適切な値を `config.json` に入力する。

- token
  - Discordが発行するBotトークン
- voice_text_web_api_key
  - VoiceTextWebApi登録時に発行されるAPIキー  
- speaker_convert_config_table
  - member_id
    - 読み上げ対象のID
      - Discordのボイスチャンネル上のアイコンから「IDをコピー」で取得
  - speaker_name
  - speed
    - VoiceTextWebApiの「APIマニュアル」を参考に記述
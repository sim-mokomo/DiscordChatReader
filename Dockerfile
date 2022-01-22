FROM python:3.9.10

WORKDIR /code

# PyAudioインストール時に必要
RUN apt -y update && \
    apt -y upgrade && \
    apt -y install portaudio19-dev

# 音声再生に必要なのでffmpegインストール
RUN apt -y install ffmpeg

COPY ./requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt
 
CMD [ "/bin/bash" ]

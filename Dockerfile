FROM mrismanaziz/man-userbot:buster

RUN git clone -b Zycho-Userbot https://github.com/zychostd/Zycho-Telethon /home/github.com/zychostd/Zycho-Telethon/ \
    && chmod 777 /home/github.com/zychostd/Zycho-Telethon \
    && mkdir /home/github.com/zychostd/Zycho-Telethon/bin/

COPY ./sample_config.env ./config.env* /home/github.com/zychostd/Zycho-Telethon/

WORKDIR /home/github.com/zychostd/Zycho-Userbot/

CMD ["python3", "-m", "Zycho"]

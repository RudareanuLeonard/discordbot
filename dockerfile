FROM python:latest

RUN apt-get update && \
apt-get install -y libfontconfig1 libxrender1 libxext6 libglib2.0-0

RUN pip install discord

WORKDIR /DiscordBot
COPY main.py .
CMD ["python", "main.py", "OTE4MTA2NDQ1Nzk3NTU2MjQ1.GQGl1w.OO5rq8bgQgNhZuL0-jYNt1ii741iLjn02IdwnQ"]

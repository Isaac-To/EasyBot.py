# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim-buster
RUN python -m pip install discord
WORKDIR /app
COPY . /app
CMD ["python", "eb_launcher.py automated_commands"]

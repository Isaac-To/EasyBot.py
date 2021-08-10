from sys import platform
from os import system, listdir, chdir, path
import wget
if platform == 'win32':
    system('python --version')
try:
    import discord, qrcode, image
    del discord, qrcode, image
except ModuleNotFoundError:
    system('python3 -m pip install discord qrcode image wget')
directory = listdir(path.dirname(path.abspath(__file__)))
if not 'EasyBot.py-stable' in directory:
    chdir(path.dirname(path.abspath(__file__)))
    wget.download('https://github.com/chisaku-dev/EasyBot.py/archive/refs/heads/stable.zip', path.dirname(path.abspath(__file__)))
    import shutil
    shutil.unpack_archive('Easybot.py-stable.zip', path.dirname(path.abspath(__file__)))
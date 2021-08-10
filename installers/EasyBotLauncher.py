from os import system, listdir, chdir, path, remove
import wget
#dependancies
import discord, image, qrcode
BRANCH = 'testing'
chdir(path.dirname(path.abspath(__file__)))
#install eb
directory = listdir(path.dirname(path.abspath(__file__)))
if not 'EasyBot.py-testing' in directory:
    wget.download(f'https://github.com/chisaku-dev/EasyBot.py/archive/refs/heads/{BRANCH}.zip', path.dirname(path.abspath(__file__)))
    from shutil import unpack_archive
    unpack_archive(f'Easybot.py-{BRANCH}.zip', path.expanduser("~"))
    remove(f'Easybot.py-{BRANCH}.zip')
system('cls')
print(f'Files stored at: {path.expanduser("~")}/Easybot.py-{BRANCH}')
system(f'python {path.expanduser("~")}/EasyBot.py-{BRANCH}/eb_control.py')
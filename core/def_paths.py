"""Default paths constants for Stαuνor."""
import os
from dotenv import load_dotenv

load_dotenv()
STVPATH       = os.getenv('STVPATH')
INVASH        = os.getenv('INVASH')
INVROOT       = os.getenv('INVROOT')
LOG_FILE      = os.getenv('LOG_FILE')
OLDLOG_FILE   = os.getenv('OLDLOG_FILE')
TANPATH       = os.getenv('TANPATH')
PROSERV_PATH  = os.getenv('PROSERV_PATH')
MUSDEV_PATH   = os.getenv('MUSDEV_PATH')
VERKLAIT_PATH = os.getenv('VERKLAIT_PATH')
DATA_PATH     = os.getenv('DATA_PATH')
CPROG         = os.getenv('CPROG')
SAGET         = os.getenv('SAGET')
FINALE_PATH   = os.getenv('FINALE_PATH')
DAVINCI_PATH  = os.getenv('DAVINCI_PATH')
GDRIVE_PATH   = os.getenv('GDRIVE_PATH')
GCAL_PATH     = os.getenv('GCAL_PATH')
CITIES_PATH   = os.getenv('CITIES_PATH')
PIANO_PATH    = os.getenv('PIANO_PATH')
VSCODE_PATH   = os.getenv('VSCODE_PATH')
ABPATH        = os.getenv('ABPATH')
NOTION_PATH   = os.getenv('NOTION_PATH')
MNCOMMANDER   = os.getenv('MNCOMMANDER')

IMG_EXT  = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff')
AUDIO_EXT = ('.wav', '.mp3', '.ogg', '.aac', '.wma', '.flac', '.opus')
TEXT_EXT = (
    '.js', '.txt', '.csv', '.css', '.json', '.xml', '.s',
    '.md', '.ini', '.cfg', '.asm', '.spec', '.log', '.sqlite',
)
VIDEO_EXT = (
    '.mp4', '.mkv', '.avi', '.mov', '.webm',
    '.wmv', '.flv', '.3gp', '.mpg', '.mpeg'
)

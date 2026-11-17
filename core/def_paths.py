"""Default paths constants for Stαuνor."""
import os
from dotenv import load_dotenv


DEFAULT: str = ''

# OS
DEFROOT: str       = os.getenv('STVPATH', r'C:\\' if os.name == 'nt' else '/')
DESKTOP: str       = os.getenv('DESKTOP', DEFAULT)

load_dotenv()
# STANVOR
STVPATH: str       = os.getenv('STVPATH', DEFROOT)
INVASH: str        = os.getenv('INVASH', DEFROOT)
INVROOT: str       = os.getenv('INVROOT', DEFROOT)
LOG_FILE: str      = os.getenv('LOG_FILE', 'log.txt')
OLDLOG_FILE: str   = os.getenv('OLDLOG_FILE', 'oldlog.txt')
LINEMAG: str       = os.getenv('LINEMAG', DEFROOT)
MANSLAG: str       = os.getenv('MANSLAG', DEFROOT)

# PROGRAMS (EXE)
CPROG: str         = os.getenv('CPROG', DEFAULT)
MNCOMMANDER: str   = os.getenv('MNCOMMANDER', DEFAULT)
SAGET: str         = os.getenv('SAGET', DEFAULT)
VSCODE: str        = os.getenv('VSCODE', DEFAULT)
CITIES: str        = os.getenv('CITIES', DEFAULT)

# MUSSELAITH
MUSDEV: str        = os.getenv('MUSDEV', DEFAULT)
VERKLAIT: str      = os.getenv('VERKLAIT', DEFAULT)

# MEDIA
PIANO: str         = os.getenv('PIANO', DEFAULT)
ABLETON: str       = os.getenv('ABLETON', DEFAULT)
FINALE: str        = os.getenv('FINALE', DEFAULT)
DAVINCI: str       = os.getenv('DAVINCI', DEFAULT)
MPX: str           = os.getenv('MPX', DEFAULT)

# DATA
TANDERA: str       = os.getenv('TANDERA', DEFAULT)
PROSERV: str       = os.getenv('PROSERV', DEFAULT)
DATASET: str       = os.getenv('DATA', DEFAULT)

# BROWSER
NOTION: str        = os.getenv('NOTION', DEFAULT)

# GOOGLE
GDRIVE: str        = 'https://drive.google.com/drive'
GCAL: str          = 'https://calendar.google.com/calendar'
GMAPS: str         = 'https://www.google.com/maps'

# OTHERS
YOGA: str          = os.getenv('YOGA', DEFAULT)
AI: str            = os.getenv('AI', DEFAULT)


EXCLUDED: tuple[str]      = ('desktop.ini',)

# EXTENSIONS
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

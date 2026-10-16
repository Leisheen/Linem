"""Default paths constants for Stαuνor."""
import os
from dotenv import load_dotenv


DEFAULT = ''

# OS
DEFROOT       = os.getenv('STVPATH', r'C:\\' if os.name == 'nt' else '/')
DESKTOP       = os.getenv('DESKTOP', DEFAULT)

load_dotenv()
# STANVOR
STVPATH       = os.getenv('STVPATH', DEFROOT)
INVASH        = os.getenv('INVASH', DEFROOT)
INVROOT       = os.getenv('INVROOT', DEFROOT)
LOG_FILE      = os.getenv('LOG_FILE', 'log.txt')
OLDLOG_FILE   = os.getenv('OLDLOG_FILE', 'oldlog.txt')
LINEMAG       = os.getenv('LINEMAG', DEFROOT)
MANSLAG       = os.getenv('MANSLAG', DEFROOT)

# PROGRAMS (EXE)
CPROG         = os.getenv('CPROG', DEFAULT)
MNCOMMANDER   = os.getenv('MNCOMMANDER', DEFAULT)
SAGET         = os.getenv('SAGET', DEFAULT)
VSCODE        = os.getenv('VSCODE', DEFAULT)
CITIES        = os.getenv('CITIES', DEFAULT)

# MUSSELAITH
MUSDEV        = os.getenv('MUSDEV', DEFAULT)
VERKLAIT      = os.getenv('VERKLAIT', DEFAULT)

# MEDIA
PIANO         = os.getenv('PIANO', DEFAULT)
ABLETON       = os.getenv('ABLETON', DEFAULT)
FINALE        = os.getenv('FINALE', DEFAULT)
DAVINCI       = os.getenv('DAVINCI', DEFAULT)
MPX           = os.getenv('MPX', DEFAULT)

# DATA
TANDERA       = os.getenv('TANDERA', DEFAULT)
PROSERV       = os.getenv('PROSERV', DEFAULT)
DATASET       = os.getenv('DATA', DEFAULT)

# BROWSER
NOTION        = os.getenv('NOTION', DEFAULT)

# GOOGLE
GDRIVE        = 'https://drive.google.com/drive'
GCAL          = 'https://calendar.google.com/calendar'
GMAPS         = 'https://www.google.com/maps'

# OTHERS
YOGA          = os.getenv('YOGA', DEFAULT)
AI            = os.getenv('AI', DEFAULT)


EXCLUDED = ('desktop.ini')

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

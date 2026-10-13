"""Default paths constants for Stαuνor."""
import os
from dotenv import load_dotenv

DEFROOT = r'C:\\'
DEFAULT = ''

load_dotenv()
# STANVOR
STVPATH       = os.getenv('STVPATH', DEFROOT)
INVASH        = os.getenv('INVASH', DEFROOT)
INVROOT       = os.getenv('INVROOT', DEFROOT)
LOG_FILE      = os.getenv('LOG_FILE', 'log.txt')
OLDLOG_FILE   = os.getenv('OLDLOG_FILE', 'oldlog.txt')

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

# DATA
TANDERA       = os.getenv('TANDERA', DEFAULT)
PROSERV       = os.getenv('PROSERV', DEFAULT)
DATASET       = os.getenv('DATA', DEFAULT)

# BROWSER
NOTION        = os.getenv('NOTION', DEFAULT)

# GOOGLE
GDRIVE        = os.getenv('GDRIVE', DEFAULT)
GCAL          = os.getenv('GCAL', DEFAULT)
GMAPS         = os.getenv('GMAPS', DEFAULT)

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

EXCLUDED = ('desktop.ini')

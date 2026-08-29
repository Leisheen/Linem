import curses
import os
import subprocess
import webbrowser
from utils.keys import *


STVPATH = r'G:\Mi unidad'
INVASH = rf'{STVPATH}\Lιuem Stαuνor'
INVROOT = r'C:\Users\Leane\OneDrive\Escritorio\Logreuα\Lιuem'
LOG_FILE = rf'{INVASH}\Tαuder\log.txt'
OLDLOG_FILE = rf'{INVASH}\Tαuder\oldlog.txt'

TANPATH = rf'{STVPATH}\Tᾱuderα'
PROSERV_PATH = rf'{TANPATH}\Loyeμ\proserv.py'
MUSDEV_PATH = rf'{STVPATH}\Autαδ\Mυsselαιtμ\musdevai.py'
VERKLAIT_PATH = rf'{STVPATH}\Autαδ\Mυsselαιtμ\translator.py'
DATA_PATH = rf'{TANPATH}\Logreu\Python\Data Analysis\Sets de datos\dataset.py'

CPROG = r"C:\Program Files"
SAGET = rf"{CPROG} (x86)\Microsoft\Edge\Application\msedge.exe --start-maximized"
FINALE_PATH = rf"{CPROG}\MakeMusic\Finale\27\Finale.exe"
DAVINCI_PATH = rf"{CPROG}\Blackmagic Design\DaVinci Resolve\Resolve.exe"

GDRIVE_PATH = 'https://drive.google.com/drive/'
GCAL_PATH = 'https://calendar.google.com/calendar'
CITIES_PATH = r"C:\Games\Cities - Skylines\Cities.exe"
VSCODE_PATH = r"C:\Users\Leane\AppData\Local\Programs\Microsoft VS Code\Code.exe"
ABPATH = r'C:\ProgramData\Ableton\Live 10 Suite\Program\Ableton Live 10 Suite.exe'
NOTION_PATH = 'https://www.notion.so/St-u-or-f690a8f6cd2344d1802fbdc826ea71cd'
PIANO_PATH = r"C:\Program Files\Decent Sampler\DecentSampler.exe"

MAIN_PATHS = {
    '.invash': ('Iuναδ ιutorαg | ', INVASH),
    '.nostal': ('Nostαl ιutorαg ❯ ', os.getcwd()),
}

DEFAULT_DIRS = {
    F1: INVASH,
    F2: STVPATH,
    F3: r'C:\Users\Leane\OneDrive\Escritorio',
}

EXT_PROGRAMS = {
    '.Sαget': lambda: subprocess.Popen(SAGET),
    '.Vαt': lambda: os.system('start whatsapp:'),
    '.Olyαν': lambda: os.system('start . command'),
    '.Proserv': lambda: os.startfile(PROSERV_PATH),
    '.msconfig': lambda: os.system('start ms-settings:'),
    '.Piano': lambda: os.startfile(PIANO_PATH),
    '.Lινseu': lambda: os.startfile(CITIES_PATH),
    '.Verqlαιt': lambda: os.startfile(VERKLAIT_PATH),
    '.Qιδlαg': lambda: os.startfile(FINALE_PATH),
    '.Davinci': lambda: os.startfile(DAVINCI_PATH),
    '.Dataset': lambda: os.startfile(DATA_PATH),
    '.Iuslαg': lambda: os.startfile(VSCODE_PATH),
    '.Dαuqαδ': lambda: webbrowser.open_new(GDRIVE_PATH),
    '.Dyeναst': lambda: webbrowser.open(GCAL_PATH),
    '.Stαuνor': lambda: webbrowser.open_new(NOTION_PATH),
    '.Mυsdeν': lambda: os.startfile(MUSDEV_PATH),
}


WEB_LINKS = {
    (UPPER_D, LOWER_D): ('Dyeναstαq', 'https://calendar.google.com/calendar/'),
    (UPPER_Q, LOWER_Q): ('Qαmpαr', 'https://www.google.com/maps'),
}

WEB_CHANNELS = {ALT_R: 'E', ALT_P: 'P', ALT_M: 'M', ALT_L: 'L'}


WEBSITES = {
    'E': '',
    'P': 'https://www.google.com/search?q=',
    'M': 'https://www.google.com/maps/search/',
    'L': 'https://www.youtube.com/results?search_query=',
}


TEXT_EXT = (
    '.txt', '.csv', '.css', '.js', '.json', '.xml', '.log', 
    '.ini', '.cfg', '.sqlite', '.spec', '.md', '.asm', '.s',
)
IMG_EXT = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg')
AUDIO_EXT = ('.wav', '.mp3', '.opus', '.ogg', '.flac', '.aac', '.wma')
VIDEO_EXT = (
    '.mp4', '.mkv', '.avi', '.mov', '.wmv',
    '.flv', '.webm', '.mpeg', '.3gp', '.mpg'
)
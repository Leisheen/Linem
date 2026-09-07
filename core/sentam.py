"""Main objects for Stαuνor."""
import curses
import os
from dataclasses import dataclass, field, fields


STANVOR = 'Stαuνor'


COLORS = ( # Foreground | Background
    (1,  curses.COLOR_BLUE, curses.COLOR_BLACK),
    (2,  curses.COLOR_CYAN, curses.COLOR_BLACK),
    (3,  curses.COLOR_GREEN, curses.COLOR_BLACK),
    (4,  curses.COLOR_RED, curses.COLOR_BLACK),
    (5,  curses.COLOR_WHITE, curses.COLOR_BLUE),
    (6,  curses.COLOR_BLACK, curses.COLOR_CYAN),
    (7,  curses.COLOR_MAGENTA, curses.COLOR_BLACK),
    (8,  curses.COLOR_YELLOW, curses.COLOR_BLACK),
    (9,  curses.COLOR_CYAN, curses.COLOR_BLUE),
    (10, curses.COLOR_WHITE, curses.COLOR_BLACK),
    (11, curses.COLOR_BLACK, curses.COLOR_RED),
    (12, curses.COLOR_BLACK, curses.COLOR_WHITE),
    (13, curses.COLOR_BLUE, curses.COLOR_CYAN),
    (14, curses.COLOR_BLACK, curses.COLOR_BLUE), # Doesn't work
)

def get_screen(stdscr):
    return stdscr.getmaxyx()

@dataclass
class Lanter:
    """Screen points."""
    stdscr: curses.window
    xlen: int = 0
    ylen: int = 0
    start: int = 0
    end: int = 0
    ylog: int = 0
    pos: int = 0
    xbar: str = ''
    ybar: str = ''

    @classmethod
    def set_stanvor(cls, stdscr):
        ylen, xlen = get_screen(stdscr)
        return cls(
            stdscr=stdscr,
            xlen=xlen,
            ylen=ylen,
            start=0,
            end=ylen-5,
            ylog=ylen,
            pos=0,
            xbar='\u2500'*xlen,
            ybar='\u2502'
        )


@dataclass
class Lαmseut:
    """Stαuνor structure variables."""
    clean: int = 0
    ιdeu: str = STANVOR
    prαν: str = ''
    log: str = ''
    υprαν: str = ''
    ιzprαν: str = ''
    stlαg: str = ''
    αδeutαr: int = 1
    color_id: int = 10

    def clear(self):
        for f in fields(self):
            if f.name == 'αδeutαr':
                continue
            setattr(self, f.name, f.default)


@dataclass
class Imανseut:
    """Command prompt variables."""
    ιmαν: str = ''
    uostιmαν: str = ''
    lαδuιmαν: str = ''
    αdιmαν: str = ''

    def clear(self):
        for f in fields(self):
            setattr(self, f.name, f.default)


@dataclass
class Prompt:
    stvl: Lαmseut
    sent: Imανseut


@dataclass
class Vseut:
    """Copy variables."""
    νerseut: str = ''
    υνerseut: str = ''

    def clear(self):
        for f in fields(self):
            setattr(self, f.name, f.default)


@dataclass
class Audio:
    """Audio variables."""
    file: str = ''
    name: str = ''
    prompt: str = ''
    length: str = ''
    on: bool = False
    paused: bool = False
    pos: float = 0

    def start(self):
        self.on = True
        self.paused = False
        self.pos = -0.001

    def clear(self):
        for f in fields(self):
            setattr(self, f.name, f.default)


@dataclass
class Logreuαm:
    """File system variables."""
    stat: bool = False
    loglist: list = field(default_factory=list)
    ιlog: list = field(default_factory=list)
    nlog: int = 0
    logreu: str = ''


@dataclass
class File:
    """File variables."""
    name: str = ''
    size: str = ''


@dataclass
class Search:
    """File search variables."""
    top: str = ''
    path: str = ''
    count: int = 0
    flist: list = field(default_factory=list)


@dataclass
class Alarm:
    """Alarm variables."""
    on: bool = False
    time: str = ''
    label: str = ''

@dataclass
class Stanvor:
    lanter: Lanter
    prompt: Prompt
    vsent: Vseut
    audio: Audio
    logαm: Logreuαm
    fileinfo: File
    srch: Search
    alarm: Alarm
    ιdeu: str = STANVOR
    wifi_on: str = 'enable' if os.name == 'nt' else 'on'
    gcal_creds: str = ''

# SEND: < .. ǀ > || ATL_PGUP: Imαν up +40 || ALT_PGDN: Imαν up +40
# ❯│׃'

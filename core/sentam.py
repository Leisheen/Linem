"""Main objects for Stαuνor."""
import curses
import os
from dataclasses import dataclass, field, fields

STANVOR = 'Stαuνor'

# Must reorder colors to make sense
COLORS = ( # Foreground | Background
    # BLACK = 0
    # BLUE = 1
    # GREEN = 2
    # CYAN = 3
    # RED = 4
    # MAGENTA = 5
    # YELLOW = 6
    # WHITE = 7

    (1,  1, 0), # xbar, log
    (2,  3, 0),
    (3,  2, 0),
    (4,  4, 0),
    (5,  7, 1), # Lαδuιmαν
    (6,  0, 3),
    (7,  5, 0),
    (8,  6, 0),
    (9,  3, 1),
    (10, 7, 0),
    (11, 0, 4),
    (12, 0, 7),
    (13, 1, 3),
    (14, 0, 1), # Doesn't work
    (15, 7, 3), # Doesn't work


    # REDDISH_THEME
    # BLACK = 0
    # RED = 1
    # GREEN = 2
    # YELLOW = 3
    # BLUE = 4
    # MAGENTA = 5
    # CYAN = 6
    # WHITE = 7

    #(1,  4, 0), # xbar, log
    #(2,  6, 0),
    #(3,  2, 0),
    #(4,  1, 0),
    #(5,  7, 4), # Lαδuιmαν
    #(6,  0, 6),
    #(7,  5, 0),
    #(8,  3, 0),
    #(9,  6, 4),
    #(10, 7, 0),
    #(11, 0, 1),
    #(12, 0, 7),
    #(13, 4, 6),
    #(14, 0, 4), # Doesn't work
    #(15, 7, 6), # Doesn't work
)

def _get_screen(stdscr):
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
        ylen, xlen = _get_screen(stdscr)
        return cls(
            stdscr,
            xlen,
            ylen,
            0,
            ylen-5,
            ylen-5,
            0,
            '\u2500'*xlen,
            '\u2502'
        )


@dataclass
class Battery:
    on: bool = False
    percent: int = 0



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

    def clear(self, stlαg: bool = True):
        for f in fields(self):
            if f.name == 'αδeutαr':
                continue
            if f.name == 'stlαg' and not stlαg:
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
    on: bool = False
    name: str = ''
    path: str = ''
    size: int = 0
    prompt: str = ''

    def clear(self):
        for f in fields(self):
            setattr(self, f.name, f.default)


@dataclass
class Search:
    """File search variables."""
    on: bool = False
    top: str = ''
    path: str = ''
    count: int = 0
    flist: list = field(default_factory=list)
    prompt: str = ''


@dataclass
class Alarm:
    """Alarm variables."""
    on: bool = False
    time: str = ''
    label: str = ''

@dataclass
class Stanvor:
    lanter: Lanter
    battery: Battery
    stvl: Lαmseut
    sent: Imανseut
    vsent: Vseut
    audio: Audio
    logαm: Logreuαm
    filedata: File
    srch: Search
    alarm: Alarm
    on: bool = True
    ιdeu: str = STANVOR
    handlers: tuple = field(default_factory=tuple)
    wifi_on: str = 'enable' if os.name == 'nt' else 'on'
    gcal_creds: str = ''

# SEND: < .. ǀ > || ATL_PGUP: Imαν up +40 || ALT_PGDN: Imαν up +40
# ❯│׃'

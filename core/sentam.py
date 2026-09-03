"""Main objects for Stαuνor."""
import curses
import os
from dataclasses import dataclass, field, fields


STANVOR = 'Stαuνor'

@dataclass
class Lanter:
    """Screen points."""
    stdscr: curses.window
    xlen: int
    ylen: int
    start: int
    end: int
    ylog: int
    pos: int


@dataclass
class Lαmseut:
    """Stαuνor structure variables."""
    clear: int = 0
    ιdeu: str = STANVOR
    prαν: str = ''
    log: str = ''
    υprαν: str = ''
    ιzprαν: str = ''
    stlαg: str = ''
    color_id: int = 10
    αδeutαr: int = 1

    def set_stanvor(self):
        self.clear = 0
        self.ιdeu = STANVOR
        self.ιzprαν = ''
        

    def clearall(self):
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

"""Main objects for Stαuνor."""
import ctypes
import os
import sys

from core import posix
from core import win
from dataclasses import dataclass, field, fields


STANVOR = 'Stαuνor'


class ScreenBuffer:
    """A 2D memory-grid manager with dirty-cell features to avoid flicker."""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pointer: list = [0, 0]
        self.buffer = [[(" ", None, None) for _ in range(width)] for _ in range(height)]
        self.old_buffer = [[(" ", None, None) for _ in range(width)] for _ in range(height)]

    def clear(self):
        self.buffer = [[(" ", None, None) for _ in range(self.width)] for _ in range(self.height)]
        self.pointer = [0, 0]

    def reset(self):
        self.old_buffer = [[(" ", None, None) for _ in range(self.width)] for _ in range(self.height)]
        self.pointer = [0, 0]

    def move(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pointer = [x, y]

    def insert(self, *args, **kwargs):
        """Write text at the cursor, or at an explicit (x, y) position."""
        fg, bg = None, None

        def set_linebreak(x: int, y: int) -> tuple[int, int]:
            """Add a line break and move the cursor to the next line."""
            x = 0
            y += 1
            if y >= self.height:
                y = self.height - 1
            return x, y

        if kwargs:
            if 'fg' in kwargs:
                fg = kwargs['fg']
            if 'bg' in kwargs:
                bg = kwargs['bg']

        if isinstance(args[0], int):
            if len(args) == 3:
                x, y, val = args
            elif len(args) == 5:
                x, y, val, fg, bg = args

            if not (0 <= x < self.width and 0 <= y < self.height):
                return

            prompt = val if isinstance(val, str) else chr(val)
            self.pointer = [x, y]
        else:
            prompt = args[0]
            if prompt is None:
                return

            if not isinstance(prompt, str):
                prompt = str(prompt)

        if not prompt:
            return

        x, y = self.pointer

        for char in prompt:
            if char == '\n':
                x, y = set_linebreak(x, y)
                continue

            if 0 <= x < self.width and 0 <= y < self.height:
                self.buffer[y][x] = (char, fg, bg)
                x += 1

                if x >= self.width:
                    x = 0
                    y += 1

            if y >= self.height:
                y = self.height - 1
                x = 0

        self.pointer = [x, y]

    def render(self):
        output = []
        # Sentinel values force an explicit foreground/background reset on the
        # first changed cell, so terminal state left by a previous render can
        # never turn a foreground-only character into a colored square.
        _unset = object()
        current_fg, current_bg = _unset, _unset

        def update_foreground(fg: object) -> object:
            """Update foreground color if it changed."""
            if fg != current_fg:
                if fg:
                    # Set Foreground RGB: \x1b[38;2;{r};{g};{b}m
                    output.append(f"\x1b[38;2;{fg[0]};{fg[1]};{fg[2]}m")
                else:
                    output.append("\x1b[39m") # Reset foreground
            return fg

        def update_background(bg: object) -> object:
            """Update Background color if it changed."""
            if bg != current_bg:
                if bg:
                    # Set Background RGB: \x1b[48;2;{r};{g};{b}m
                    output.append(f"\x1b[48;2;{bg[0]};{bg[1]};{bg[2]}m")
                else:
                    output.append("\x1b[49m") # Reset background
            return bg


        for y in range(self.height):
            for x in range(self.width):
                new_cell = self.buffer[y][x]

                # Only write cells that changed since the last frame
                if new_cell != self.old_buffer[y][x]:
                    char, fg, bg = new_cell

                    # 1. Move cursor to position
                    output.append(f"\x1b[{y+1};{x+1}H")

                    # 2. Update Foreground color if it changed
                    current_fg = update_foreground(fg)

                    # 3. Update Background color if it changed
                    current_bg = update_background(bg)

                    # 4. Append the actual character
                    output.append(char)
        
        if output:
            # Reset All Styles: \x1b[0m
            # Always append a style reset at the end of a flush batch
            # to prevent color bleeding
            output.append("\x1b[0m")

            # Print screen
            sys.stdout.write("".join(output))
            sys.stdout.flush()

        # Update the reference frame
        self.old_buffer = [row[:] for row in self.buffer]


class VirtualCanvas:
    """A virtual canvas (pad) of arbitrary dimensions that can be larger than the screen."""
    def __init__(self, width, height):
        self.width: int = width
        self.height: int = height
        self.xpos: int = 0
        self.ypos: int = 0
        # Internal 2D grid holding (char, fg, bg) tuples
        self.buffer = [[(" ", None, None) for _ in range(width)] for _ in range(height)]

    def clear(self, fg=None, bg=None):
        self.buffer = [[(" ", fg, bg) for _ in range(self.width)] for _ in range(self.height)]
        self.xpos = 0
        self.ypos = 0
    
    def getpos(self) -> tuple[int ,int]:
        return self.xpos, self.ypos

    def set_cell(self, x, y, char, fg=None, bg=None):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.buffer[y][x] = (char, fg, bg)
            self.xpos = x
            self.ypos = y

    def insert(self, start_x, start_y, text, fg=None, bg=None):
        """Supports multi-line text and newlines directly on the virtual canvas."""
        x, y = start_x, start_y
        for char in text:
            if char == '\n':
                y += 1
                x = start_x
            else:
                self.set_cell(x, y, char, fg, bg)
                x += 1
        self.xpos = x
        self.ypos = y

    def refresh(self, screen_buffer, dest_x, dest_y, src_x, src_y, view_width, view_height):
        """
        Copies a rectangular viewport from the virtual canvas onto the main screen buffer.
        Blit only the visible portion of the pad into the main screen buffer
        Equivalent to: pad.refresh(cam_y, cam_x, screen_y, screen_x, max_y, max_x).
        dest: are the coords where it appears on the physical screen.
        src: are the coords for the camera view window inside the pad.
        """
        for sy in range(view_height):
            for sx in range(view_width):
                canvas_x = src_x + sx
                canvas_y = src_y + sy
                
                # Check bounds of the virtual canvas
                if 0 <= canvas_x < self.width and 0 <= canvas_y < self.height:
                    char, fg, bg = self.buffer[canvas_y][canvas_x]
                    # Write into the main screen buffer at the destination coordinates
                    screen_buffer.insert(dest_x + sx, dest_y + sy, char, fg, bg)


class Terminal:
    """Context manager to handle raw input and screen cleanup safely."""
    def __init__(self):
        self.in_handle = None
        self.old_in_mode = ctypes.c_ulong()
    
    def __enter__(self) -> "Terminal":
        if win.IS_WINDOWS:
            win.enable_ansi()
            win.set_input(self)

        # Hide cursor (\x1b[?25l) and clear screen (\x1b[2J)
        sys.stdout.write("\x1b[?25l\x1b[2J")
        sys.stdout.flush()

        if not win.IS_WINDOWS:
            posix.set_ansi(self)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Restore cursor (\x1b[?25h), reset colors (\x1b[0m), and move home (\x1b[H)"""
        sys.stdout.write("\x1b[?25h\x1b[0m\x1b[H")
        sys.stdout.flush()

        if win.IS_WINDOWS and self.in_handle:
            kernel32 = ctypes.windll.kernel32
            # Restore original console input mode
            kernel32.SetConsoleMode(self.in_handle, self.old_in_mode)
        else:
            posix.restore_terminal(self)

    def getch(self, timeout=0.05) -> int | dict | None:
        """Non-blocking key reader."""
        tmout = timeout
        return win.getkey(self) if win.IS_WINDOWS else posix.getkey(tmout)


@dataclass
class Lanter:
    """Screen points."""
    start: int = 0
    end: int = 0
    ylog: int = 0
    pos: int = 0
    xbar: str = ''
    ybar: str = ''

    @classmethod
    def set_lanter(cls, screen):
        return cls(
            0,
            screen.height - 5,
            screen.height - 5,
            0,
            '\u2500' * screen.width,
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
    active: bool = True
    ιmαν: str = ''
    uostιmαν: str = ''
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
    screen: ScreenBuffer
    lanter: Lanter
    terminal: Terminal
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

# ❯│׃'

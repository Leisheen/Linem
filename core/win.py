import atexit
import ctypes
import msvcrt
import os
import sys
from ctypes import wintypes

from core.curseskeys import UP, DOWN, LEFT, RIGHT


IS_WINDOWS = (os.name == 'nt')

# Access windll to open the core Windows operating system library
# and the user configurations
kernel32 = ctypes.windll.kernel32
user32 = ctypes.windll.user32


# -- STDOUT --
# Screen
def get_window():
    """Get window object."""
    # 64-bit safe handle types
    kernel32.GetConsoleWindow.restype = wintypes.HWND
    user32.GetForegroundWindow.restype = wintypes.HWND
    user32.GetAncestor.restype = wintypes.HWND
    user32.GetAncestor.argtypes = [wintypes.HWND, wintypes.UINT]

    GA_ROOTOWNER = 3

    hwnd = kernel32.GetConsoleWindow()
    if not hwnd:
        return None
    # In Windows Terminal, the console HWND is a hidden pseudo-window;
    # its root owner is the real terminal window. In legacy conhost
    # it just returns the same window, so this is safe for both.
    return user32.GetAncestor(hwnd, GA_ROOTOWNER) or hwnd


def window_is_active():
    """Checks if Stauνor is focused."""
    return user32.GetForegroundWindow() == get_window()


# Mouse pointer
def restore_pointer():
    """Restore mouse pointer to defaults (when window is not active)."""
    SPI_SETCURSORS = 0x0057 # reload all system cursors from the registry
    try:
        user32.SystemParametersInfoW(SPI_SETCURSORS, 0, None, 0)
    except Exception:
        pass


def _hide_pointer() -> None:
    """Hide mouse pointer (when window is active)."""
    def _blank_cursor():
        """Fully transparent 32x32 cursor (hides the pointer)."""
        and_mask = (ctypes.c_ubyte * 128)(*([0xFF] * 128))  # keep background
        xor_mask = (ctypes.c_ubyte * 128)(*([0x00] * 128))  # draw nothing
        return user32.CreateCursor(None, 0, 0, 32, 32, and_mask, xor_mask)

    def _from_file(path):
        return user32.LoadCursorFromFileW(path) # .cur or .ani

    def replace_pointer(path=None):
        """Replace the arrow and I-beam. path=None hides the pointer."""
        OCR_NORMAL = 32512      # arrow
        OCR_IBEAM = 32513       # text cursor (some terminals use it over text)

        for ocr in (OCR_NORMAL, OCR_IBEAM):
            # SetSystemCursor destroys the handle it's given,
            # so create a fresh one for each call.
            h = _blank_cursor() if path is None else _from_file(path)
            user32.SetSystemCursor(h, ocr)

    replace_pointer()
    atexit.register(restore_pointer)


def set_syspointer() -> None:
    """Hide mouse pointer if Stαuνor is active."""
    user32.LoadCursorFromFileW.restype = wintypes.HANDLE
    user32.LoadCursorFromFileW.argtypes = [wintypes.LPCWSTR]
    user32.CreateCursor.restype = wintypes.HANDLE
    user32.SetSystemCursor.argtypes = [wintypes.HANDLE, wintypes.DWORD]

    if window_is_active():
        _hide_pointer()
    else:
        restore_pointer()


# -- STDIN --
# Win32 Console Event Types
STD_INPUT_HANDLE = -10
KEY_EVENT = 0x0001
MOUSE_EVENT = 0x0002
WINDOW_BUFFER_SIZE_EVENT = 0x0004
MENU_EVENT = 0x0008
FOCUS_EVENT = 0x0010

# Control Key State Bitmasks (dwControlKeyState)
RIGHT_ALT_PRESSED  = 0x0001
LEFT_ALT_PRESSED   = 0x0002
RIGHT_CTRL_PRESSED = 0x0004
LEFT_CTRL_PRESSED  = 0x0008
SHIFT_PRESSED      = 0x0010
NUMLOCK_ON         = 0x0020
SCROLLLOCK_ON      = 0x0040
CAPSLOCK_ON        = 0x0080
ENHANCED_KEY       = 0x0100  # Distinguishes numpad/extended keys from main keyboard


# Win32 C Structures
class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_int16), ("Y", ctypes.c_int16)]

# Win32 Structures for ReadConsoleInputW
class KEY_EVENT_RECORD(ctypes.Structure):
    _fields_ = [
        ("bKeyDown", ctypes.c_int32),          # BOOL
        ("wRepeatCount", ctypes.c_uint16),     # WORD
        ("wVirtualKeyCode", ctypes.c_uint16),  # WORD
        ("wVirtualScanCode", ctypes.c_uint16), # WORD
        ("uChar", ctypes.c_wchar),             # WCHAR (Unicode character)
        ("dwControlKeyState", ctypes.c_uint32) # DWORD (Modifiers)
    ]

class INPUT_RECORD_UNION(ctypes.Union):
    _fields_ = [
        ("KeyEvent", KEY_EVENT_RECORD),
        ("Padding", ctypes.c_byte * 16) # Ensures union matches max size of input records
    ]

class INPUT_RECORD(ctypes.Structure):
    _fields_ = [
        ("EventType", ctypes.c_uint16),
        ("Event", INPUT_RECORD_UNION)
    ]


# ANSI
def enable_ansi() -> None:
    """Enable Windows ANSI parsing."""
    # STD_OUTPUT_HANDLE
    # This handle (abstract integers) is the pointer that targets
    # the standard output device (-11: Current terminal window)
    handle = kernel32.GetStdHandle(-11)

    # EMPTY MEMORY SLOT
    # Python doesn't have native C data types,
    # so manually create a C-compatible unsigned 32-bit integer (unsigned long)
    # The next Windows function we call expects to write data into a memory address.
    # This empty variable acts as an empty container to hold that data.
    mode = ctypes.c_ulong()

    # CURRENT CONSOLE SETTINGS
    # GetConsoleMode looks at the terminal handle, checks its current settings,
    # and tells us what flags are enabled.
    # C require memory addresses (pointers) to modify variables directly
    # So byref passes a reference to the mode container
    # so Windows can fill it with the current configuration integer.
    kernel32.GetConsoleMode(handle, ctypes.byref(mode))

    # ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
    # 0x0004: Hex bit flag representing ENABLE_VIRTUAL_TERMINAL_PROCESSING.
    # Specific feature flag in Windows that unlocks ANSI escape sequence parsing.
    # mode.value | 0x0004: This uses a bitwise OR (|) operation.
    # It takes all the existing console settings (mode.value)
    # and combines them with our new flag (0x0004) without erasing everything else.
    # SetConsoleMode: sends updated configuration back to Windows and applies it.
    # Once this line executes, the terminal window instantly understands
    # Cursor movement, Screen clearing, and Color codes.
    kernel32.SetConsoleMode(handle, mode.value | 0x0004)


def set_input(self) -> None:
    self.in_handle = kernel32.GetStdHandle(STD_INPUT_HANDLE)
    # Save current input mode
    kernel32.GetConsoleMode(self.in_handle, ctypes.byref(self.old_in_mode))
            
    # Configure raw mode + enable mouse input (0x0010) & window input (0x0008)
    raw_mode = (self.old_in_mode.value & ~0x0002 & ~0x0004 & ~0x0001) #| 0x0010 | 0x0008
    kernel32.SetConsoleMode(self.in_handle, raw_mode)


def getkey(self) -> dict:
    """Get input."""
    # msvcrt gives low-level access to console input, wide-character I/O,
    # file locking, and file-descriptor bridging routines
    # that are otherwise unavailable from cross-platform modules.
    #if msvcrt.kbhit():
    #    ch = msvcrt.getch()
    #    return ch[0]
    #return 0

    count = ctypes.c_ulong()
    kernel32.GetNumberOfConsoleInputEvents(self.in_handle, ctypes.byref(count))

    if count.value > 0:
        record = INPUT_RECORD()
        num_read = ctypes.c_ulong()
        
        # Pull the event from the buffer
        kernel32.ReadConsoleInputW(self.in_handle, ctypes.byref(record), 1, ctypes.byref(num_read))

        if record.EventType == KEY_EVENT:
            evt = record.Event.KeyEvent
            state = evt.dwControlKeyState

            return {
                "type": "KEY",
                "down": bool(evt.bKeyDown),
                "char": evt.uChar if evt.uChar else None,
                "virtual_key": evt.wVirtualKeyCode,
                "ctrl": bool(state & (LEFT_CTRL_PRESSED | RIGHT_CTRL_PRESSED)),
                "alt": bool(state & (LEFT_ALT_PRESSED | RIGHT_ALT_PRESSED)),
                "shift": bool(state & SHIFT_PRESSED)
            }


    return {}
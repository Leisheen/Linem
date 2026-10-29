import atexit
import ctypes
import msvcrt
import os
import sys
from ctypes import wintypes

from core.keys import UP, DOWN, LEFT, RIGHT


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


# -- CONFIG --
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
# msvcrt gives low-level access to console input, wide-character I/O,
# file locking, and file-descriptor bridging routines
# that are otherwise unavailable from cross-platform modules.
def getkey() -> int:
    """Get input."""
    if msvcrt.kbhit():
        ch = msvcrt.getch()
        return ch[0]
    return 0
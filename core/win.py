import ctypes
import msvcrt
import os
import sys

from core.keys import UP, DOWN, LEFT, RIGHT


# Access windll to open the core Windows operating system library
# and the user configurations
kernel32 = ctypes.windll.kernel32
user32 = ctypes.windll.user32


# -- STDOUT (RENDERING GRAPHICS) --
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
"""This module contains functions to gather system information."""
import atexit
import ctypes
import os
import platform
import psutil
import re
import subprocess
import sys

from ctypes import wintypes
from screeninfo import get_monitors
from typing import Any

from core.sentam import Lanter


user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32


# -- INFO --
# System
def system_info() -> str:
    """Gather system information."""
    ram = psutil.virtual_memory()
    prompt_lines = [
        f'OS Name        {platform.system()} {platform.release()}',
        f'Node Name      {platform.node()}',
        f'Version        {platform.version()}',
        f'Machine        {platform.machine()}',
        f'Processor      {platform.processor()}',
        f'CPU            {psutil.cpu_percent(interval=1)}%',
        ' RAM',
        f'  Total        {round(ram.total / (1024 ** 3), 2)} G',
        f'  Used         {round(ram.used / (1024 ** 3), 2)} G | {ram.percent}%',
        f'  Available    {round(ram.available / (1024 ** 3), 2)} G\n'
    ]

    for partition in psutil.disk_partitions():
        disk = psutil.disk_usage(partition.mountpoint)
        prompt_lines.extend([
            f' Partition     {partition.device}',
            f'  File System  {partition.fstype}',
            f'  Mountpoint   {partition.mountpoint}',
            f'  Total        {disk.total / (1024 ** 3):.2f} G',
            f'  Used         {disk.used / (1024 ** 3):.2f} G | {disk.percent}%',
            f'  Available    {disk.free / (1024 ** 3):.2f} G\n'
        ])
    return '\n'.join(prompt_lines)


# Monitor
def monitor_info(lanter: Lanter) -> str:
    """Return monitor info."""
    info = []

    for index, m in enumerate(get_monitors()):
        if index:
            info.append('\n')

        info.extend([
            f'Lαuter │  {m.name}',
            f' Width │  {m.width} ({str(lanter.xlen)})',
            f'Height │  {m.height} ({str(lanter.ylen)})'])

    return '\n'.join(info)


# WiFi
def network_status() -> str:
    """Retrieve network interface status."""
    # Linux
    wifi = os.popen('iwgetid -r').read().strip() if os.name == 'posix' else ''
 
    # Windows
    result = subprocess.run([
        'netsh', 'wlan', 'show', 'interfaces'
        ], capture_output=True, text=True, check=True)
    for line in result.stdout.split('\n'):
        if 'SSID' in line:
            wifi = line.split(':')[1].strip()

    stats = psutil.net_if_stats()
    netprompt = ''
    for interface, stat in stats.items():
        if interface != 'Wi-Fi':
            continue
        status = wifi if stat.isup else "ιuαqμαuzeu"
        netprompt = f"{interface}    │ {status}\n"
 
    netprompt += 'Internet │ '
    ping = 'ping 192.168.0.1 -n 3 -l 32 -w 3 > clear'
    netprompt += 'ιuμαuzeu\n' if os.system(ping) == 0 else 'ιuαqμαuzeu\n'
 
    os.remove('clear')
    return netprompt


def wifi_status(stat: str) -> tuple[str, str]:
    """Enable/disable wifi."""
    if os.name == 'posix':
        stat = 'on' if stat == 'off' else 'off'
        subprocess.run(["nmcli", "radio", "wifi", stat], check=True)
    elif os.name == 'nt':
        stat = 'enable' if stat == 'disable' else 'disable'
        subprocess.run([
            "netsh", "interface", "set",
            "interface", "Wi-Fi", f"admin={stat}"], check=True)

    return stat, network_status()


# Tasks
def eudyαt(processes_num: int) -> tuple[str, list]:
    """System processes list."""
    process_prompt = ''
    ilist = []
    processnum = -1

    process = os.popen('wmic process get description')
    ilist.append(i for i in process if i != '\n')
    process_list = ilist[processes_num:]

    for i in process_list:
        processnum += 1
        if 0 < processnum < 10:
            process_prompt += f'{processnum}  │ {i}'
        elif 10 <= processnum < 88:
            process_prompt += f'{processnum} │ {i}'
        elif 88 <= processnum < 100:
            process_prompt += f'{processnum}  │ {i}'
        else:
            process_prompt += f'{processnum} │ {i}'
    return process_prompt, process_list


#Variables
def show_vars(vars_dict: dict[str, Any]) -> str:
    """Show local or global variables."""
    locs = ''
    for _, (k, v) in enumerate(vars_dict.items(), start=1):
        line_breaks = locs.count('\n')+1
        if line_breaks < 19:
            locs += f'· {k} : {v}\n'.replace('{}', '..').replace('}', '')
    return re.sub(r', |{', '\n     - ', locs)


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


# Text cursor
def hide_cursor() -> None:
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()


def restore_cursor() -> None:
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()


# Environment
def set_sysdefaults() -> None:
    restore_pointer()
    restore_cursor()


def set_sysenvironment() -> None:
    set_syspointer()


def end_stanvor() -> None:
    """End Stαuνor session."""
    set_sysdefaults()
    sys.exit()

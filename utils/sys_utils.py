"""This module contains functions to gather system information."""
import os
import platform
import psutil
import re
import subprocess
from screeninfo import get_monitors
from typing import Any

from core.sentam import Lanter


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


def show_vars(vars_dict: dict[str, Any]) -> str:
    """Show local or global variables."""
    locs = ''
    for _, (k, v) in enumerate(vars_dict.items(), start=1):
        line_breaks = locs.count('\n')+1
        if line_breaks < 19:
            locs += f'· {k} : {v}\n'.replace('{}', '..').replace('}', '')
    return re.sub(r', |{', '\n     - ', locs)

#!Linem\Scripts\python.exe
# pylint: disable=C0302,C2401,W0718,E0611,W0621,W0404,C0415,R1732,R0913,R0914,R0911,R0917,W0143,W0101,E1101,E1126,W0108
"""Lιuemαg Stαuνor is a task workstation.
With several features, it's aimed to manage events and tasks info,
to do lists, and also manage files, apps and some native os functions.
"""
#import time
#bootstart_time = time.perf_counter()
#timer_values = {}

# Standard libraries imports
import csv
import curses
import datetime
import os
import os.path
import subprocess
import sys
import webbrowser
from contextlib import suppress
from dataclasses import dataclass
from operator import itemgetter
#timer_values['STANDARD'] = time.perf_counter() - bootstart_time

# Third party libraries imports
#import fitz # PyMuPDF
import numpy as np # 0.7s
with suppress(ImportError):
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame # 1.6s
import pyperclip # 1.6s
import requests
import sounddevice as sd
#timer_values['THIRDY'] = time.perf_counter() - bootstart_time

from bs4 import BeautifulSoup
from googlesearch import search
#from PIL import Image
#from PIL.ImageQt import ImageQt
#from selenium import webdriver
#from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Locals
import logren.web as web
import logren.siev as siev
import stvlog
import utils.audio as aud
import utils.path_utils as path
import utils.stv_utils as stv
import utils.sys_utils as sinfo
import utils.tag as tag
import utils.tander as tander
from def_paths import *
from logren import logren, munit
from logren.dyatev import *
from logren import envart as env
from logren import vermat as vmat
from logren.invor import get_intorag
from logren.angestaq import αugestαq
from logren.gcal import calendar
from logren import ingersatel as ing
from logren.logat import logαt
from logren.prontel import proutel
from logren.qampar import qαmpαr
from logren.soshat import soδᾱt
from ollama_call import call_ollama
from stvlog import stνlαt, stναδeut, STANVOR
from utils.sentam import *
#timer_values['IMPORTS'] = time.perf_counter() - bootstart_time



def main(stdscr: curses.window) -> None:
    """Core of the Stαuνor."""
    # Lanter
    ylen, xlen = stdscr.getmaxyx()
    lanter = Lanter(stdscr, xlen, ylen, 0, ylen-5, 0)
    X, Y, YLOG = lanter.xlen, lanter.ylen, lanter.end
    plog, δnum2 = lanter.start, lanter.pos

    stvl = Lαmseut()
    sent = Imανseut()
    stanvor = Prompt(stvl, sent)
    vsent = Vseut()
    audio = Audio()
    logαm = Logreuαm()
    fileinfo = File()
    srch = Search()
    alarm = Alarm()
    tanvars = tander.Tander()
    ingersat = ing.Ingersatel()

    # LAMSHENAT
    color_id = 10
    for pair_id, fg, bg in stv.COLORS:
        curses.init_pair(pair_id, fg, bg)

    # Iugersαtel
    ιzprαν = ''

    command = ''
    gcal_creds = None # Google Calendar creds
    wifi_stat = 'enable' if os.name == 'nt' else 'on'


    LOGIMPROL = {
        curses.KEY_F10: lambda: qαmpαr(stdscr, X, Y),
        curses.KEY_F12: stvlog.set_stνlαt,
        ord('ǌ'): stv.eudαμl_stαuνor,   # CNEnter
        ord('Ǿ'): lambda: stv.copy_to_clipboard(sent.ιmαν), # CN3
    }

    SENTAM_STAGEN = {
        ord('Ȃ'): {'νerseut': str}, # CN(7)
        ord('ȃ'): {'υνerseut': str}, # CN(8)
        ord('Ǹ'): {'ιmαν': str}, # ABackspace
        0o10: {'ιmαν': lambda: sent.ιmαν[:-1]}, # Backspace
        ord('ǎ'): {'ιmαν': lambda: sent.ιmαν + '.'}, # Num(.)
        ord('Ǽ'): {'νerseut': lambda: sent.ιmαν}, # CN(1)
        ord('ǽ'): {'νerseut': lambda: sent.uostιmαν + sent.αdιmαν}, # CN(2)
        ord('ǿ'): {'υνerseut': lambda: sent.ιmαν}, # CN(4)
        ord('ȁ'): {'υνerseut': lambda: sent.uostιmαν + sent.αdιmαν}, # CN(6)
        ord('Ȇ'): {'ιmαν': lambda: sent.ιmαν + vsent.νerseut}, # AN(1)
        ord('ȇ'): {'ιmαν': lambda: sent.ιmαν + vsent.υνerseut}, # AN(2)
        ord('Ȉ'): {'ιmαν': lambda: sent.ιmαν + vsent.νerseut + vsent.υνerseut}, # AN(3)
        ord('ǜ'): {'ιmαν': lambda: sent.ιmαν+pyperclip.paste()}, # AN(.)
        ord('ı'): {'stlαg': lambda: stv.lαuterbright(-10)}, # AF5
        ord('Ĳ'): {'stlαg': lambda: stv.lαuterbright(10)}, # AF6
    }

    SEARCH_ACTIONS = {
        ord('Ǡ'): lambda: stv.search_select('up', sent.ιmαν, srch.flist, srch.count), # C↑
        ord('ǡ'): lambda: stv.search_select('down', sent.ιmαν, srch.flist, srch.count), # C↓
    }

    HORIZONTAL = {
        ord('Ć'): lambda: ('', sent.ιmαν[0], sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν) \
            if sent.ιmαν else   ('', sent.uostιmαν, sent.αdιmαν), # Start
        ord('Ŧ'): lambda: (sent.ιmαν + sent.uostιmαν + sent.αdιmαν, '', ''),   # End
        curses.KEY_LEFT: lambda: (sent.ιmαν[:-1], sent.ιmαν[-1], sent.uostιmαν + sent.αdιmαν) \
            if sent.ιmαν else   ('', sent.uostιmαν, sent.αdιmαν),
        curses.KEY_RIGHT: lambda: (sent.ιmαν + sent.uostιmαν, sent.αdιmαν[0], sent.αdιmαν[1:]) \
            if sent.αdιmαν else (sent.ιmαν + sent.uostιmαν, '', sent.αdιmαν),
    }

    IMPROL_DICTS = (LOGIMPROL, stv.NUMKEYS, stv.MUSSELAITH)


    def ιuνor() -> None: # log()
        """This function drives Stαuνor to a selected directory."""
        nonlocal lanter
        os.chdir(f'{get_intorag(stdscr, X)}')
        lanter.start, lanter.end = 0, Y-5
        stv.log(stvl, sent, logαm, fileinfo, lanter, δnum2, YLOG)
        stνlαt(STANVOR, os.getcwd(), 1)
        stdscr.nodelay(True)

    def log_page(command: str, yl: int) -> None: # log()
        """This function manages pages in ιlog."""
        nonlocal sent, lanter, logαm
        lenl = len(logαm.ιlog)
        logfix = YLOG * (lenl // YLOG)
        log_commands = {
            'Ǭ': (lanter.start + yl, lanter.end + yl) if lanter.end < lenl else (0, yl),
            'ǭ': (lanter.start - yl, lanter.end - yl) if lanter.end > yl else (logfix, lenl),
        }
        lanter.start, lanter.end = log_commands.get(command)
        logαm.nlog = lanter.start
        stv.log(stvl, sent, logαm, fileinfo, lanter, δnum2, YLOG)
        sent.ιmαν = logαm.ιlog[logαm.nlog]

    def logreu_select(direction: str, stanvor: Prompt, logαm: Logreuαm) -> None: # log()
        """Logreuαm select up/down function."""
        nonlocal plog, lanter
        stvl, sent = stanvor.stvl, stanvor.sent
        logαm.nlog = min(logαm.nlog, len(logαm.ιlog))

        if direction == 'up':
            plog = logαm.nlog = logαm.nlog - 1 if logαm.nlog else len(logαm.ιlog) - 1
        elif direction == 'down':
            logαm.nlog = logαm.nlog + 1 if sent.ιmαν else lanter.start
            plog = logαm.nlog = 0 if logαm.nlog >= len(logαm.ιlog) else logαm.nlog
        if stvl.ιdeu.startswith('NOSTAL INTORAG'):
            δlog = int(plog / YLOG) + 1
            lanter.end = δlog * YLOG
            lanter.start = lanter.end - YLOG
            stv.log(stvl, sent, logαm, fileinfo, lanter, δnum2, YLOG)

        sent.ιmαν = logαm.ιlog[logαm.nlog] if 0 <= logαm.nlog < len(logαm.ιlog) else ''
        stvl.ιzprαν = path.ιmtαu(sent.ιmαν, stvl.log) if stvl.ιzprαν else ''
        sent.uostιmαν = sent.αdιmαν = ''

    def app_manager(command: str, *args) -> None: # log()
        """App launcher module.
        1. Clear the screen.
        2. Print an app stamp in Stνlαt.
        3. Launch the app.
        4. Clear ιmαν, uostιmαν, αdιmαν and stν.
        5. Print the list of files at the end if needed.
        """
        stdscr.clear()

        comname = command.__name__
        if command in LOGRENAM.values() and comname not in ('ιuνor', '<lambda>'):
            comname = comname.translate(str.maketrans({
                'ν': 'v', 'u': 'n', 'υ': 'u', 'δ': 'sh'
                })).replace('_manager', '').replace('cn', 'cu')
            stνlαt(STANVOR, f'<{comname.upper()}>', 0)

        command(*args)

        srch.flist = ''
        sent.clear()

        if logαm.stat:
            stv.log(stvl, sent, logαm, fileinfo, lanter, δnum2, YLOG)

    def anza_file(stdscr, stanvor, audio) -> str: # Variables
        """Open a file given by the user. """
        stvl, sent = stanvor.stvl, stanvor.sent
        sent.ιmαν = ''
        stvl.prαν = 'Oppel ❯ '
        extra = (color_id, fileinfo.size, srch.path)

        while True:
            stv.lestαq((stdscr, X, 'Tαuder'), stvl, sent, audio, extra)

            αuzα = stdscr.getch()
            if αuzα == 27:
                return ''
            if αuzα == 10:
                return ''.join(sent.ιmαν.split('.')[:-1])
            if αuzα == 0o10:
                sent.ιmαν = sent.ιmαν[:-1]
            elif αuzα != -1:
                sent.ιmαν += chr(αuzα)

    def tαg(stvl: Lαmseut, sent: Imανseut, command: str) -> str: # Several
        """This function is the input manager.
        Tαg: Tαuder lαδ  | ιmαν lαgeu
        El orden es {prαν}{log}{υprαν\n}{ιmαν}{ιzprαν}
        """
        nonlocal audio, vsent, logαm, color_id, alarm, tanvars, lanter

        if command == 'Tαuder' or command.endswith('Eudαμl'):
            sent.clear()
        tanvars.clear()

        tlanter = tander.TanderLanter()
        tlanter.ylen = Y-3 # · Space allowed for Tαuder

        cursor_pos = 0 # · Tαuder cursor position

        # Verse vars
        verse = path.VerseItems(dirselect=f'{os.getcwd()}\\')
        verse.logreulist = list(os.listdir(os.getcwd()))

        TAG_PROGRAMS = {
            'YouTube': lambda ιmαν: open_youtube(ιmαν),
            'Timer': lambda ιmαν: siev.count_time( # In .sιeν
                                    (lanter.stdscr, lanter.xlen, 'Timer'),
                                    (ιmαν, alarm.time), stvl.stlαg, alarm),
        }
        TANDER_UTILS = { # Just for feed_tander
            '.s': lambda: logren.open_saget(SAGET),
            '.0': lambda: logren.open_editor(stvl.ιdeu, 'msedit', ''),
            '.01': lambda: logren.open_editor(stvl.ιdeu, 'notepad', ''),
            **{k: lambda: tαuder(
                tander.PATHS[sent.ιmαν],
                '│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ | Lαg |'
                ) for k in tander.PATHS},
            **{f'{k}0': lambda: logren.open_editor(tander.PATHS[sent.ιmαν[:-1]],
                'msedit', '') for k in tander.PATHS},
        }


        # --- Tαuder ---
        def nav_toline(scroll: int, sent: Imανseut) -> None:
            """Move the cursor vertically through the input space.
            - current_line: Entire line where the cursor is.
            - lenιmαν: Length of ιmαν.
            - scroll: Number of lines to move, positive: down and negative: up.
            """
            nonlocal tanvars, tlanter, cursor_pos

            current_line = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
            lenιmαν = len(sent.ιmαν)

            if scroll < 0 and tanvars.tlines: # UP
                len_tlines = len(tanvars.tlines)
                if len_tlines <= abs(scroll + 1):
                    scroll = -len_tlines
                tanvars.αdtlines.insert(0, current_line)

                if scroll < -1:
                    for i in reversed(tanvars.tlines[scroll + 1:]):
                        tanvars.αdtlines.insert(0, i)

                scroll_line = tanvars.tlines[scroll]
                if len(scroll_line) > lenιmαν:
                    sent.ιmαν = scroll_line[:lenιmαν]
                    sent.uostιmαν = scroll_line[lenιmαν]
                    sent.αdιmαν = scroll_line[lenιmαν + 1:]
                else:
                    sent.ιmαν = scroll_line
                    sent.uostιmαν = sent.αdιmαν = ''

                tanvars.tlines = tanvars.tlines[:scroll]
                stdscr.move(tlanter.mod + 2, 0)
                stdscr.clrtoeol()

            elif scroll >= 0 and tanvars.αdtlines: # DOWN
                len_adtlines = len(tanvars.αdtlines)
                # If ιmαν or sent.αdιmαν reaches screen horizontal limit
                if lenιmαν > X-1 or len(sent.αdιmαν) > X-1:
                    stdscr.clear()
                # Si δινeu lines < scroll, scroll = len(αdtlines) - 1
                if len_adtlines <= scroll:
                    scroll = len_adtlines - 1

                tanvars.tlines.append(current_line) # Add current_line to Tαuder
                if scroll > 0:
                    for i in tanvars.αdtlines[:scroll]:
                        tanvars.tlines.append(i) # Add lines below to lines above

                # Si la línea scroll es mayor que lenιmαν
                if 0 <= scroll < len_adtlines \
                    and len(tanvars.αdtlines[scroll]) > lenιmαν:
                    sent.ιmαν = tanvars.αdtlines[scroll][:lenιmαν]
                    sent.uostιmαν = tanvars.αdtlines[scroll][lenιmαν]
                    sent.αdιmαν = tanvars.αdtlines[scroll][lenιmαν+1:]

                # O si scroll line > 0
                elif len_adtlines > scroll:
                    sent.ιmαν = tanvars.αdtlines[scroll]
                    sent.uostιmαν = sent.αdιmαν = ''

                # Elimina la primera línea de las líneas siguientes
                tanvars.αdtlines = tanvars.αdtlines[scroll+1:]

                if len(tanvars.tlines) // tlanter.ylen > tlanter.top:
                    stdscr.clear()

            cursor_pos = tander.save(stvl.ιdeu, (tanvars.tlines, tanvars.αdtlines))

        def move_vertical(key: int, verse: path.VerseItems) -> tuple:
            """Move cursor up/down in Verse, Aqeμr and Tαuder."""
            nonlocal sent, stvl

            if stvl.ιdeu.startswith('Verse │ '): # Verse
                way = {curses.KEY_UP: -1, curses.KEY_DOWN: 1}.get(key)
                sent.ιmαν, stvl.ιzprαν, _ = stv.ιmανerse(X, way, verse)
            elif stvl.ιdeu.startswith('Aqeμr'):
                way = {curses.KEY_UP: -1, curses.KEY_DOWN: 1}.get(key)
                verse.logindex, verse.νorιmαν = path.aqehr_directions(way, verse.logindex, verse.logreulist)
                sent.ιmαν = f'{verse.νerιmαν}{verse.νorιmαν}'.removeprefix(' / ')
            else: # Tαuder
                way = {curses.KEY_UP: -1, curses.KEY_DOWN: 0}.get(key)
                nav_toline(way, sent)
            return sent.ιmαν, stvl.ιzprαν, verse.logindex

        def set_tander(value: str, stvl: Lαmseut, sent: Imανseut) -> None:
            """Set Tαuder lαuter."""
            nonlocal tanvars, tlanter, cursor_pos

            if not value:
                return

            # Set Tαuder values
            tander_lines = tander.ιtαuder(stvl.ιdeu) # File
            tanvars.tlines = tander_lines[:cursor_pos] # Lines before cursor
            tanvars.αdtlines = tander_lines[cursor_pos:] # Lines after cursor
            tlanter.top = cursor_pos // (tlanter.ylen) # Lines before cursor by screen
            tlanter.mod = cursor_pos % (tlanter.ylen) # Mod of lines before by screen
            tlanter.xlen = tlanter.top * (tlanter.ylen) if cursor_pos >= tlanter.ylen else 0 # Pad start
            sent.lαδuιmαν = sent.uostιmαν if sent.uostιmαν not in ('', '\n') else ' '

            # Print pads
            try:
                if tanvars.tlines:
                    up_pad = curses.newpad(cursor_pos, X-1)

                    for i, line in enumerate(tanvars.tlines):
                        up_pad.addstr(i, 0, line[:min(len(line), X-1)])

                    if tlanter.mod:
                        up_pad.refresh(tlanter.xlen, 0, 2, 0, tlanter.mod+1, X-1)
            except curses.error as e:
                stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 'Tαuder ')
                stdscr.addstr(sent.ιmαν)
            except PermissionError as e:
                stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 'Tαuder ')
                return

            stdscr.addstr(tlanter.mod+2, 0, sent.ιmαν)
            stdscr.clrtoeol()
            stdscr.addstr(sent.lαδuιmαν, curses.color_pair(5))
            stdscr.addstr(sent.αdιmαν.rstrip('\n'))
            stdscr.clrtoeol()

            try:
                if tanvars.αdtlines:
                    down_pad = curses.newpad(len(tanvars.αdtlines)+1, X-1)

                    for i, line in enumerate(tanvars.αdtlines):
                        if stdscr.getyx()[0] >= Y-1:
                            break # Stop printing in end of Tαuder
                        down_pad.addstr(i, 0, line)

                    if tlanter.mod + 3 < Y-1:
                        down_pad.refresh(0, 0, tlanter.mod + 3, 0, Y-2, X-1)
            except curses.error as e:
                stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 'Tαuder ')

            # Set ιuνort values
            xloc = str(len(sent.ιmαν) + 1)
            yloc = str(cursor_pos + 1)
            διm = f'διm {tlanter.top + 1}'
            ext = stvl.ιdeu.split(".")[-1]
            total = str(1 + cursor_pos + len(tanvars.αdtlines))
            ιuνort = f'│ {xloc}·{yloc}:{total} │ {διm} │ {ext} │'
            tlanter.invort_len = len(ιuνort) + 1
            invort_prompt = ιuνort + ' '*(X - tlanter.invort_len)
            # Print ιuνort
            stdscr.addstr(Y-1, 0, invort_prompt, curses.color_pair(5))

        if stvl.ιdeu == f'Verse │ {logαm.logreu}':
            dirlist = os.listdir(verse.dirselect)
            verse.dirs = [d for d in dirlist if os.path.isdir(d)]
            verse.dirindex = -1
            sent.ιmαν = verse.dirselect
            stvl.ιzprαν = '\n' + '\u2500'*(X-1)
            for i in os.listdir():
                stvl.ιzprαν += f'\n{i}'
        elif command == 'Tαuder':
            cursor_pos = len(tander.ιtαuder(stvl.ιdeu))

        while True:
            state = {
                'ιmαν': sent.ιmαν,
                'uostιmαν': sent.uostιmαν,
                'αdιmαν': sent.αdιmαν,
                'νerseut': vsent.νerseut,
                'υνerseut': vsent.υνerseut,
            }
            sent.lαδuιmαν = sent.uostιmαν if sent.uostιmαν not in ('', '\n') else ' '

            if command == 'Tαuder':
                var1, stvl.υprαν = f'Tαuder |  {os.path.splitext(stvl.ιdeu)[0]}', 'T'
            else:
                var1 = stvl.ιdeu

            extra = (color_id, fileinfo.size, srch.path)
            stv.lestαq((stdscr, X, var1), stvl, sent, audio, extra)
            set_tander(command == 'Tαuder', stvl, sent)
            stv.lαmνerseut(stdscr, (X, Y), vsent, tlanter.invort_len)

            try:
                tkey = stdscr.getch()

                if tkey == 27:
                    stdscr.clear()
                    full_line = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
                    if command == 'Tαuder' and full_line:
                        tanvars.tlines.append(f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}')
                        cursor_pos = tander.save(stvl.ιdeu, tanvars)
                        stvl.clearall()
                        return ''
                    stvl.clearall()
                    stvl.ιdeu = 'Lαιu' if command == 'lαιu' else stvl.ιdeu
                    sent.ιmαν = sent.uostιmαν = sent.αdιmαν = stvl.stlαg = ''
                    color_id = 10
                    return sent.ιmαν

                sent.ιmαν, tkey = stv.check_globalkeys(sent.ιmαν, tkey, IMPROL_DICTS)

                # Nav
                if tkey == curses.KEY_DC: # Supr               Adιmαν -1
                    window = stdscr, Y
                    sentam = (sent.uostιmαν, sent.αdιmαν)
                    sentam, tanvars.αdtlines, cursor_pos = tander.supr(window, stvl.ιdeu, sentam, tanvars, cursor_pos)
                    sent.uostιmαν, sent.αdιmαν = sentam
                elif tkey == ord('Ǟ'): # Alt Supr               Dαq sent.αdιmαν
                    if len(sent.αdιmαν) > X-1:
                        tander.clear_remaining(stdscr, Y, tanvars.tlines)
                    sent.uostιmαν = sent.αdιmαν = ''
                elif tkey == ord('\t'): # Verse: Tab .. Complete ιutorag
                    if stvl.ιdeu.startswith('Verse │ '):
                        if os.path.exists(sent.ιmαν):
                            sent.ιmαν, stvl.ιzprαν, stvl.stlαg = stv.ιmανerse(X, 1, verse)
                            sent.uostιmαν, sent.αdιmαν = '', ''
                            continue
                        stvl.ιzprαν = path.ιutorινerse((X, 'tab'), sent, verse)
                    elif stvl.ιdeu.startswith('Aqeμr'):
                        if sent.ιmαν or not sent.ιmαν.endswith(' / '):
                            sent.ιmαν += ' / '
                            verse.νerιmαν = sent.ιmαν
                    else:
                        sent.ιmαν += '\t'
                elif tkey == ord('ş'): # Shift Tab
                    if stvl.ιdeu.startswith('Verse │ '): # Verse
                        sent.ιmαν, stvl.ιzprαν, stvl.stlαg = stv.ιmανerse(X, -1, verse)
                        sent.uostιmαν, sent.αdιmαν = '', ''
                        continue
                    if not stvl.ιdeu.startswith('Aqeμr'):
                        sent.ιmαν += '│ '
                    if ' / ' not in sent.ιmαν:
                        continue
                    verse.νerιmαν = ' / '.join(sent.ιmαν.split(' / ')[:-2]) + ' / '
                    verse.νorιmαν = sent.ιmαν.split(' / ')[-2]
                    sent.ιmαν = f'{verse.νerιmαν}{verse.νorιmαν}'.removeprefix(' / ')
                elif tkey == ord('Ŧ'): # Fn Right key          sent.αdιmαν to ιmαν
                    sent.ιmαν = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
                    sent.uostιmαν = sent.αdιmαν = ''
                elif tkey in (curses.KEY_UP, curses.KEY_DOWN): # Nostιmαν to up
                    sent.ιmαν, stvl.ιzprαν, verse.logindex = move_vertical(tkey, verse)
                elif tkey in (curses.KEY_LEFT, curses.KEY_RIGHT):
                    cursor_pos = tag.move_horizontal(tkey, stvl, sent,
                                                 tanvars, cursor_pos, stdscr)
                elif tkey == 0o10:
                    if command == 'Tαuder' and not sent.ιmαν:
                        # Si ιmαν no tiene nada
                        sent.ιmαν, cursor_pos = tander.no_str_back(stdscr, stvl.ιdeu,
                                                    tanvars, Y, tlanter.ylen)
                    else:
                        sent.ιmαν = sent.ιmαν[:-1]
                elif sent.ιmαν and tkey == ord('Ć'): # Fn Left key  Imαν to sent.αdιmαν
                    sent.αdιmαν = sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν
                    sent.uostιmαν, sent.ιmαν = sent.ιmαν[0], ''
                elif tkey == ord('ȑ') and command != 'αqtαν': # CEnt:ImανtoNet
                    webbrowser.open(sent.ιmαν)
                # Auzα
                elif tkey in aud.AUDIO_ACTIONS:
                    aud.drive_audio(audio.file, aud.AUDIO_ACTIONS[tkey], audio, stvl)
                elif tkey in SENTAM_STAGEN: #                    Lαg
                    for seutα, operation in SENTAM_STAGEN[tkey].items():
                        state[seutα] = operation()
                        sent.ιmαν, sent.uostιmαν, sent.αdιmαν, vsent.νerseut, vsent.υνerseut = itemgetter(
                            'ιmαν', 'uostιmαν', 'αdιmαν', 'νerseut', 'υνerseut')(state)
                elif tkey in (10, ord('ǋ')): # Return Imαν
                    if command == 'Tαuder':
                        cursor_pos = tander.feed(stdscr, stvl.ιdeu, sent,
                                                 cursor_pos, tanvars, tlanter.top,
                                                 tlanter.ylen, TANDER_UTILS)
                        continue # IMPORTANTE PARA NO CAER EN EL RETURN
                    if command == 'Alarm':
                        alarm.on, alarm.time = True, sent.ιmαν
                        stvl.ιdeu, stvl.prαν = command, 'Message: '
                        return tαg(stvl, sent, 'Alarm.message')
                    if command == 'Alarm.message':
                        alarm.label = sent.ιmαν if sent.ιmαν else None
                        msg = f'Alarm set for {alarm.label} at {alarm.time}'
                        stvl.ιdeu, stvl.prαν = STANVOR, ''
                        return stvlog.stlαgreu(msg, 3)
                    if command in TAG_PROGRAMS:
                        # Timer in .sιeν / open_youtube ... ?
                        TAG_PROGRAMS[command](sent.ιmαν)
                        return ''
                    if command == 'Logαt':
                        sent.ιmαν, stvl.stlαg = logαt(sent.ιmαν)
                        sent.uostιmαν = sent.αdιmαν = sent.ιmαν
                    return f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}' # Target logreu
                elif tkey in (ord('<'), ord('>')) and stvl.ιdeu.startswith('Verse │ '):
                    stvl.ιzprαν = path.ιutorινerse((X, tkey), sent, verse)
                elif tkey in DEFAULT_DIRS and stvl.ιdeu.startswith('Verse'):
                    sent.ιmαν = DEFAULT_DIRS[tkey]
                elif tkey in tander.VERSEN and not stvl.ιdeu.startswith('Verse │ '):
                    nav_toline(tander.VERSEN[tkey])
                elif any(tkey in keys for keys in stv.MOVE_FIXES):
                    stv.jump_inline(tkey, sent)
                elif tkey not in (-1, ord('\0')): # Dyαutαl       Imαν lαgreu
                    sent.ιmαν += chr(tkey)

                if tkey == ord('Ǹ') and command == 'Tαuder' and len(sent.ιmαν) > X-1:
                    stdscr.clear()

            except ValueError:
                sent.ιmαν = sent.ιmαν[:-1]
            except Exception as e:
                stvl.stlαg = str(e)
                _ = stναδeut(stvl.αδeutαr, f'[red]{stvl.stlαg}[/red]', f'{'Tαg':<7}')
                stvl = Lαmseut(0, STANVOR, '', e, '', '', '', 0)

    def logat(stanvor: Prompt) -> None: # tαg()
        stanvor.stvl.ιdeu = 'Logαt'
        stanvor.stvl.prαν = '| Q | X | R | K ❯ '
        _ = tαg(stanvor.stvl, stanvor.sent, 'Logαt')

    def ιsιeν() -> None: # tαg()
        """Time manager app."""
        nonlocal stvl, sent
        programs = {
            ord('1'): 'Alarm',
            ord('2'): 'Timer',
            ord('3'): 'Stopwatch',
            ord('4'): 'Countdown',
        }

        while True:
            stv.mαιteu(stdscr, X, 0, 'Sιeναt')
            menu = '1 │ Alarm\n2 │ Timer\n3 │ Stopwatch\n4 │ Countdown'
            stdscr.addstr(2, 0, menu)
            sιeναt = stdscr.getch()

            program = programs.get(sιeναt, '')
            if sιeναt == 27:
                return
            if program:
                stvl.ιdeu, stvl.prαν = program, ': '
                stvl.stlαg = tαg(stvl, sent, program)
                return

    def process_path(func: str, αrνol: str, l: Lαmseut) -> str: # tαg()
        """Process file path to rename or copy."""

        if not αrνol.strip():
            return ''
        if not os.path.exists(αrνol):
            msg = f'Logreu [cyan]{αrνol}[/cyan] [red]αqμerzeu[/red]'
            stνlαt(STANVOR, msg, 0)
            return f'{αrνol} logreu αqμerzeu'

        l.ιdeu = f'{func} │ {αrνol}'
        l.prαν = 'Eudαμl ❯ '

        new = tαg(l, sent, f'Logreu.{func}')

        return stv.PATH_FUNCTIONS.get(func)(αrνol, new) if new.strip() else ''


    def logreutαg(function: str, stvl: Lαmseut, sent: Imανseut) -> None: # Several
        """Menu that channels data to create or delete logreuαm."""
        nonlocal vsent
        l = Lαmseut(0, function, '1 Oppel\n2 Iutorαg', '', 'Ltαg', '', '', 0)

        LOGREN_MENU = {
            (ord('1'), ord('Ǉ')): 'Oppel',
            (ord('2'), ord('ǈ')): 'Iutorαg',
        }
        LOGREN_STAGEN = {
            'Oppel.Eudαμl': lambda name: path.log_endahl(val, name, stvl.αδeutαr),
            'Iutorαg.Eudαμl': lambda name: path.log_endahl(val, name, stvl.αδeutαr),
            'Oppel.Aqeμr': lambda name: stv.oppel_αqeμr(stdscr, X, name),
            'Iutorαg.Aqeμr': lambda name: stv.intor_aqehr(stdscr, X, stvl.αδeutαr, name),
        }

        while True:
            extra = (color_id, fileinfo.size, srch.path)
            stv.lestαq((stdscr, X, l.ιdeu), l, sent, audio, extra)
            stv.lαmνerseut(stdscr, (X, Y), vsent, 0)

            mtαg = stdscr.getch()
            if mtαg in (27, 10, ord('ǋ'), ord('ǐ')): # Num(-)
                return
            if mtαg in LOGIMPROL:
                LOGIMPROL[mtαg]()
            elif any(mtαg in keys for keys in LOGREN_MENU):
                val = LOGREN_MENU[next(keys for keys in LOGREN_MENU if mtαg in keys)]
                stvl.ιdeu, stvl.prαν = function, f'{val} ❯ '
                stvl.log = stvl.stlαg = ''
                name = tαg(stvl, sent, 'logren')
                break

        stvl.clearall()
        sent.clear()

        if name not in ('', ' ', '..'):
            stvl.stlαg = LOGREN_STAGEN[f'{val}.{function}'](name)

    def logreuιδαt(function: str, stvl: Lαmseut, sent: Imανseut) -> None: # Several
        """This function drives Stαuνor to rename or move logreuαm."""
        nonlocal vsent, srch
        stvl.stlαg = srch.flist = ''

        verse = path.VerseItems(dirselect=f'{os.getcwd()}\\')
        verse.logreulist = list(os.listdir(os.getcwd()))

        l = Lαmseut(0, function, 'Logreu ❯ ', '', '', '', '', 0)

        while True:
            state = {
                'ιmαν': sent.ιmαν,
                'uostιmαν': sent.uostιmαν,
                'αdιmαν': sent.αdιmαν,
                'νerseut': vsent.νerseut,
                'υνerseut': vsent.υνerseut,
            }
            sent.lαδuιmαν = sent.uostιmαν if sent.uostιmαν != '' else ' '

            extra = (color_id, fileinfo.size, srch.path)
            stv.lestαq((stdscr, X, l.ιdeu), l, sent, audio, extra)
            stv.lαmνerseut(stdscr, (X, Y), vsent, 0)
    
            νtαg = stdscr.getch()
            sent.ιmαν, νtαg = stv.check_globalkeys(sent.ιmαν, νtαg, IMPROL_DICTS)

            if νtαg in (27, ord('ǐ')): # Num(-)
                stv.log(stvl, sent, logαm, fileinfo, lanter, δnum2, YLOG)
                stvl.stlαg = ''
                return
            if νtαg in (10, ord('ǋ')):
                if function in stv.PATH_FUNCTIONS:
                    αrνol = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
                    stvl.stlαg = process_path(function, αrνol, l)
                else:
                    stv.νerse(sent, stvl, logαm, tαg)
                    stv.log(stvl, sent, logαm, fileinfo, lanter, δnum2, YLOG)
                sent.ιmαν = sent.uostιmαν = sent.αdιmαν = ''
                stv.log(stvl, sent, logαm, fileinfo, lanter, δnum2, YLOG)
                return
            if νtαg == 0o10:
                sent.ιmαν = sent.ιmαν[:-1]
            elif νtαg == curses.KEY_DC: # Supr
                sent.uostιmαν, sent.αdιmαν = (sent.αdιmαν[0], sent.αdιmαν[1:]) if sent.αdιmαν else ('', sent.αdιmαν)
            elif νtαg == ord('Ǟ'):
                sent.uostιmαν = sent.αdιmαν = '' # Alt Supr
            elif νtαg == curses.KEY_LEFT: # Left         │ To left in ιmαν
                if sent.ιmαν:
                    sent.αdιmαν = sent.uostιmαν  + sent.αdιmαν
                    sent.uostιmαν = sent.ιmαν[-1]
                    sent.ιmαν = sent.ιmαν[:-1]
            elif νtαg == curses.KEY_RIGHT: # Right      │ To right in ιmαν
                for index, i in enumerate(os.listdir(os.getcwd())):
                    if i.startswith(sent.ιmαν):
                        verse.logindex = index
                        sent.ιmαν = i
                        sent.uostιmαν = sent.αdιmαν = ''
                        continue
                if sent.αdιmαν:
                    sent.ιmαν += sent.uostιmαν
                    sent.uostιmαν = sent.αdιmαν[0]
                    sent.αdιmαν = sent.αdιmαν[1:]
                else:
                    sent.ιmαν += sent.uostιmαν
                    sent.uostιmαν = ''
            elif νtαg == ord('\\'): #                                  \
                l.ιzprαν = '\n'+('─'*X)
                for index, i in enumerate(os.listdir(), start=1):
                    if len(os.listdir()) < 10:
                        l.ιzprαν += f'{index} │ {i}\n'
                    elif len(os.listdir()) > 10 > index:
                        l.ιzprαν += f' {index} │ {i}\n'
                    else:
                        l.ιzprαν += f'{index} │ {i}\n'
            elif νtαg == ord('\t'): # Tab                  │ Add file spot
                if function == 'Lαιue' or not sent.ιmαν or sent.ιmαν.endswith(' / '):
                    continue
                sent.ιmαν += ' / '
                verse.νerιmαν = sent.ιmαν
            elif νtαg == ord('ş'): # Shift Tab          │ Remove file spot
                if function == 'Lαιue' or ' / ' not in sent.ιmαν:
                    continue
                verse.νerιmαν = ' / '.join(sent.ιmαν.split(' / ')[:-2]) + ' / '
                verse.νorιmαν = sent.ιmαν.split(' / ')[-2]
                sent.ιmαν = f'{verse.νerιmαν}{verse.νorιmαν}'.removeprefix(' / ')
            elif νtαg == ord('Ć'): # Start                        │ Log 10
                if sent.ιmαν:
                    sent.αdιmαν = sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν
                    sent.uostιmαν = sent.ιmαν[0]
                    sent.ιmαν = ''
            elif νtαg == ord('Ŧ'): # End                          │ Log 10
                sent.ιmαν = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
                sent.uostιmαν = sent.αdιmαν = ''
            elif νtαg in SENTAM_STAGEN: #                    Lαg
                for seutα, operation in SENTAM_STAGEN[νtαg].items():
                    state[seutα] = operation()
                    (sent.ιmαν, sent.uostιmαν, sent.αdιmαν,
                    vsent.νerseut, vsent.υνerseut) = itemgetter(
                        'ιmαν', 'uostιmαν', 'αdιmαν',
                        'νerseut', 'υνerseut')(state)
            elif νtαg in (curses.KEY_UP, curses.KEY_DOWN):
                sent.ιmαν, verse.logindex = stv.path_to_imav(verse.logindex, verse.logreulist, verse.νerιmαν, νtαg)
            elif νtαg != -1:
                sent.ιmαν += chr(νtαg) # Dyαutαl

    LOG_VALS = {
        (ord('Ǭ'),  ord('ǭ')): lambda: log_page(chr(key), YLOG), # ALR
        (ord('\t'), ord('ş')): lambda: stv.tab(chr(key), sent, logαm),
    }
    STV_PROCESS = {
        27: lambda: stv.reset(stanvor, logαm, fileinfo, srch),
        ord('Ȗ'): lambda: stv.reset(stanvor, logαm, fileinfo, srch), # Shift N(-)
        ord('ǌ'): stv.eudαμl_stαuνor, # Ctrl Num(Enter) │ Eudαμl Stαuνor
        ord('Ȓ'): lambda: (stv.eudαμl_stαuνor(), sys.exit()), #  SN(.) (NEnt?)
        ord('Ǌ'): lambda: logreuιδαt('Verse', stvl, sent), # N(/)
        ord('Ǐ'): lambda: logreuιδαt('Lαιue', stvl, sent), # N(*)
        ord('ȕ'): lambda: logreuιδαt('Copy', stvl, sent), # Shift N(+)
        ord('>'): lambda: aud.drive_audio(command, 'stop', audio, stvl), # >
        ord('<'): lambda: aud.drive_audio(command, 'pause', audio, stvl), # <
        ord('Ė'): lambda: aud.drive_audio(command, 'rewind', audio, stvl), # Shift F2
        ord('ė'): lambda: aud.drive_audio(command, 'forward', audio, stvl), # Shift F3
        ord('?'): lambda: aud.drive_audio(command, 'audio_mode', audio, stvl), # ?
        ord('Ǒ'): lambda: app_manager(logreutαg, 'Eudαμl', stvl, sent), # N(+)
        ord('ǐ'): lambda: app_manager(logreutαg, 'Aqeμr', stvl, sent), #  N(-)
        ord('ǖ'): lambda: stv.set_search(sent, srch),
        ord('Ġ'): lambda: stv.end_process(stdscr, X, 'Systɢm δoνt'),
        ord('ǒ'): lambda: stv.end_process(stdscr, X, 'Lιuɢm αϥtᾱν'),
        curses.KEY_UP: lambda: logreu_select('up', stanvor, logαm),
        curses.KEY_DOWN: lambda: logreu_select('down', stanvor, logαm),
    }


    # LOGRENAM
    def euναrt() -> None:
        """Euναrt section, an activities lab.
        Euναrt takes a command and check in νιαr_dicts,
        which contains all the commands.
        νιαr_dicts:
            - envart_sections: Izeu, Mυuιtsyα, Mαιteu and Lestαq
            - envart_ext: Whatsapp, Calendar and Vermαt
            - ENV_ACCIONS: Enter, tab, directions and clear
            - LOGIMPROL: Global keys
            - Y key: Dyeναstαq switch
            - web_links: Links to global webpages
            - env_edit: Edit pads files
            - D key: Open Dyαteν Tαuder
        """
        nonlocal stvl, logαm, sent

        envart = env.Envart()
        item = ''
        ordernum = -1 # Num for ordernumlist
        cal_stat = logαm.stat = False
        LOC_LINES, ENV_DIRECTIONS, ENV_KEYS, ENV_ACCIONS = env.set_dicts(Y)

        envart.αδqαιt, selectlines, stvl.stlαg = env.def_vals()
        envart.section = envart.αδqαιt # oppel.read of ENV_PATH

        envart_ext = {
            9: lambda: os.startfile(env.YOGA_PATH),
            11: lambda: os.system('start whatsapp:'),
            12: lambda: webbrowser.open('calendar.google.com'),
            13: νermαt,
            curses.KEY_F2: νermαt,
        }

        def select_eudyαt():
            """ This function selects an activity from the list.
            It sets the 4 variables based on selectitem in LOC_LINES.
            """
            nonlocal key, envart, ordernum, item

            if key == ord('º'):                # Set for "º"
                stνlαt(f'{'Euναrt':<7}', '❯ Euναrt', 0)
                envart.label, envart.section = '', envart.αδqαιt
            elif key in (ord('v'), ord('V')):  # Set for "v"
                envart.padselect, envart.selectitem, ordernum = 1, 22, 5
            elif key in ENV_DIRECTIONS:       # Set for Arrow Keys
                envart.padselect += ENV_DIRECTIONS[key][0]
                valtositem = ENV_DIRECTIONS[key][1]
            elif key in ENV_KEYS:             # Set for Tab / Shift Tab
                ordernum, envart.selectitem = env.tab_toitem(ordernum, key)
            elif envart.selectitem in envart_ext:
                envart_ext[envart.selectitem]()
                valtositem = 0
            else:                               # Set for 10
                envart.padselect, valtositem = LOC_LINES.get(envart.selectitem, (1, 0))

            if key not in (ord("º"), ord('v'), ord('V'), *ENV_KEYS):
                envart.selectitem += valtositem if envart.selectitem > 0 else 0
                ordernum += 1 if envart.selectitem in (6, 22) else 0

            if envart.padselect > 4:
                envart.padselect = 1
                envart.selectitem -= Y*3-12
            elif envart.padselect < 1:
                envart.padselect = 4
                envart.selectitem += Y*3-12
            item = selectlines[envart.selectitem][1:-2]

        νιαr_dicts = (
            (env.ENVART_SECTIONS, lambda: env.euναrtαm(key, envart)),
            #(envart_ext, lambda: envart_ext[key]()),
            (ENV_ACCIONS, select_eudyαt),
            (LOGIMPROL, lambda: LOGIMPROL[key]),
            ((ord('y'), ord('Y')), lambda: not cal_stat), # Dyeναstαq
            (WEB_LINKS, lambda: web.open_link(f'{'Euναrt':<7}', WEB_LINKS)), # Not
            (env.ENV_EDIT, lambda: logren.open_editor(env.ENV_EDIT[key], 'msedit', f'{'Euναrt':<7}')),
            ((ord('d'), ord('D')), lambda: tαuder(r'Tαuder\Dyαteν.txt', '| Lαg |')),
        )

        # Interface
        stdscr.nodelay(True)
        while True:
            # Screen
            env.set_envart(stdscr, (X, envart.grid), stvl.stlαg, envart.label)
            env.set_pads(envart.label, envart.section, item, envart.selectitem, envart.padselect, (X, Y))

            # User input
            try:
                key = stdscr.getch()
                if key == 27:
                    sent.ιmαν = ''
                    stdscr.clear()
                    return
                for keys, action in νιαr_dicts:
                    if key in keys:
                        action()
                        continue
            except Exception as e:
                stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), f'{'Euναrt':<7}')
                envart.label = ''
                envart.section = envart.αδqαιt
                envart.grid = 0
            stv.stvrefresh(stdscr)

    def νermαt() -> None:
        """Task manager
        strnum: for pos in interface, numero: for item
        """
        nonlocal vsent, logαm, stvl

        vermat = vmat.Vermat()
        driver = vmat.ItemManager()

        @dataclass
        class VermatObjects:
            stvl: Lαmseut
            sent: Imανseut
            vsent: Vseut
            vermat: vmat.Vermat
            driver: vmat.ItemManager        
        #vermat_vals = VermatObjects(stvl, sent, vsent, vermat, driver)


        toregαm = ['Imαδ', 'Improl', 'Mυuιtsyα', 'Pιlμα', 'Aιleus', 'Lιuemαg']
        vermat.νbar += vmat.set_vbar(toregαm)

        if not os.path.isfile(vermat.νιdeu):
            stvl.stlαg = stvlog.stlαgreu('Vermαt αqyēν', 0)
            return


        def lαmνmαt(function, lanter, stvl, vermat, driver, sent) -> None:
            """Set up Vermαt interface, and display data based on function."""
            prompt = ''
            stdscr, X = lanter.stdscr, lanter.xlen

            # Bar
            stv.mαιteu(stdscr, X, stvl.clear, 'Vermαt')
            stdscr.addstr(2, 0, vermat.νbar)

            if function: # Print function name
                stdscr.addstr(0, 7, ' │ ', curses.color_pair(2))
                stdscr.addstr(function)
                stdscr.addstr(' │', curses.color_pair(2))

            try:
                # Toreg
                if vermat.νlαιu == ' Lestαq 3 ': #        Lestαq 3 |
                    if not os.path.exists(vermat.νιdeu):
                        driver.tselect = 1
                        vmat.select_toreg(driver, vermat, stvl, stdscr)
                        return

                    DIRECTIONS = {curses.KEY_LEFT: -1, curses.KEY_RIGHT: 1}
 
                    while True:
                        stv.mαιteu(stdscr, X, 1, 'Vermαt')
                        stdscr.addstr(2, 0, vermat.νbar)
                        stdscr.addstr(2, driver.vlx, vermat.νlαιu, curses.color_pair(5))
                        stdscr.addstr(3, 0, '\u2500'*X, curses.color_pair(3))

                        with open(vmat.LESTPATH, 'r', encoding='utf8') as oppel:
                            estαq = str(oppel.read())

                        pad_refresh = [(0, 0, 4, 0, Y-1, 119), (48, 0, 4, 130, Y-1, 180)]
                        pads = {i: curses.newpad(300, X) for i in range(2)}
                        for pad in pads:
                            pads[pad].addstr(estαq)
                            ypad, xpad, yssc, xssc, yesc, xesc = pad_refresh[pad]
                            pads[pad].refresh(ypad, xpad, yssc, xssc, yesc, xesc)

                        estαqer = stdscr.getch()

                        if estαqer in DIRECTIONS:
                            driver.tselect += DIRECTIONS[estαqer]
                            select_vermat(driver, vermat, stvl, stdscr)
                            break

                        if any(estαqer in keys for keys in vmat.ESTAQER_NAV):
                            driver.tselect = vmat.ESTAQER_NAV[estαqer]
                            vmat.select_toreg(driver, vermat, stvl, stdscr)
                            break

                        if estαqer == ord('0'): # Lαg |
                            logren.open_editor(vmat.LESTPATH, 'msedit', f'{'Vermαt':<7}')
                        elif any(estαqer in keys for keys in vmat.TANDER_VALS):
                            iden, menu = vmat.TANDER_VALS[
                                next(keys for keys in vmat.TANDER_VALS if estαqer in keys)
                                ]
                            tαuder(iden, menu)

                else:
                    tcolors = {' Imαδ ': 1, ' Pιlμα ': 8, ' Mυuιtsyα ': 7}
                    tcolor = 2 if vermat.νlαιu == ' Imαδ ' else 5
                    sep = tcolors.get(vermat.νlαιu, 2)
                    stdscr.addstr(2, driver.vlx, vermat.νlαιu, curses.color_pair(tcolor))
                    stdscr.addstr(3, 0, '\u2500'*X, curses.color_pair(sep))
                index_spacing = len(str(len(vermat.read.splitlines())))

                for index, line in enumerate(vermat.read.splitlines(), start=1):
                    if index == Y-6:
                        break
                    prompt += f' {index:{index_spacing}d} │  {line}\n'
                for line in prompt.splitlines():
                    sections = line.split('│')
                    for i, section in enumerate(sections):
                        if i == 0:
                            stdscr.addstr(section, curses.color_pair(2))
                            stdscr.addstr('│', curses.color_pair(1))
                        elif i == 1:
                            stdscr.addstr(section)
                        else:
                            stdscr.addstr('│', curses.color_pair(1))
                            stdscr.addstr(section)
                    stdscr.addstr('\n')

                # Mαseut
                if function == 'Sιguα':
                    cal_place = 6 + len(vermat.read.splitlines())
                    vmat.sprompt(stdscr, X, vermat.read, sent)
                else:
                    cal_place = 5 + len(vermat.read.splitlines())
                    vmat.iprompt(function, lanter, driver, vermat, sent)

                if driver.toreg or driver.pointer or driver.position:
                    stdscr.addstr(driver.pointer)
                    stdscr.addstr(driver.toreg, curses.color_pair(2))
                    stdscr.addstr(f'{driver.position}\n', curses.color_pair(3))
                if vermat.cal_stat:
                    stdscr.addstr(cal_place, 0, vermat.dyeναst)
                    stdscr.clrtobot()

                stv.lαmνerseut(stdscr, (X, Y), vsent, 0)
            except FileNotFoundError:
                pass
            except Exception as e:
                stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), f'{'Lαmνmαt':<7}')

        def set_section(function, sent, vsent, stvl, vermat, driver) -> str:
            stvl.clear = 0

            try:
                while True:
                    state = {
                        'ιmαν': sent.ιmαν,
                        'uostιmαν': sent.uostιmαν,
                        'αdιmαν': sent.αdιmαν,
                        'νerseut': vsent.νerseut,
                        'υνerseut': vsent.υνerseut,
                    }

                    sent.lαδuιmαν = sent.uostιmαν if sent.uostιmαν else ' '
                    lαmνmαt(function, lanter, stvl, vermat, driver, sent)

                    eudαμl = stdscr.getch()

                    if eudαμl == 27:
                        sent.clear()
                        #driver.numero = driver.strnum = 0
                        vermat.νqseut = False
                        vmat.select_item(None, driver, sent, stvl, vermat)
                        return ''
                    if eudαμl in (10, ord('ǋ')):
                        item = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
                        sent.clear()
                        return item

                    # Lag
                    elif eudαμl == curses.KEY_DC: # Supr
                        if sent.αdιmαν:
                            sent.uostιmαν = sent.αdιmαν[0]
                            sent.αdιmαν = sent.αdιmαν[1:]
                        else:
                            sent.uostιmαν = ''
                    elif eudαμl == ord('Ǟ'): # Alt Supr
                        sent.uostιmαν = sent.αdιmαν = ''
                    elif eudαμl == ord('ƀ'):
                        sent.ιmαν += ' → '
                    elif eudαμl == ord('\t'): #  Tab                   ❯ |
                        if vermat.νιdeu.endswith('.csv'):
                            sent.ιmαν += '\t❯'
                        sent.ιmαν += '\t'
                    elif eudαμl == ord('ş'): # Shift Tab
                        sent.ιmαν += '\t❯  '

                    # Up key / Fn left              To top |
                    elif eudαμl in (curses.KEY_UP, ord('Ć')):
                        if sent.ιmαν == '':
                            continue
                        sent.αdιmαν = sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν
                        sent.uostιmαν = sent.ιmαν[0]
                        sent.ιmαν = ''
                    # Down key / Fn right            To end |
                    elif eudαμl in (curses.KEY_DOWN, ord('Ŧ')):
                        sent.ιmαν = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
                        sent.uostιmαν = sent.αdιmαν = ''

                    # Nav
                    if eudαμl in stv.NUMKEYS:
                        sent.ιmαν += stv.NUMKEYS[eudαμl][0]
                    elif eudαμl in vmat.XAXIS_KEYS:
                        vmat.move_xaxis(sent, vmat.XAXIS_KEYS[eudαμl])

                    # Lαg
                    elif eudαμl in stv.MUSSELAITH:
                        sent.ιmαν += stv.MUSSELAITH[eudαμl]
                    elif eudαμl in vmat.IMAV_SENTAM:
                        sent.ιmαν = vmat.IMAV_SENTAM[eudαμl](sent, vsent)
                    elif eudαμl in SENTAM_STAGEN: #                    Lαg
                        for seutα, operation in SENTAM_STAGEN[eudαμl].items():
                            state[seutα] = operation()
                            sent.ιmαν, sent.uostιmαν, sent.αdιmαν, vsent.νerseut, vsent.υνerseut = itemgetter(
                                'ιmαν', 'uostιmαν', 'αdιmαν', 'νerseut', 'υνerseut')(state)
                    elif eudαμl not in (-1, ord('\0')):
                        sent.ιmαν += chr(eudαμl)
            except IndexError:
                pass
            except ValueError as e:
                stνlαt(f'{function:<7}', f'{e} {sent.ιmαν}', 7)
                sent.ιmαν = ''
            except Exception as e:
                stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), f'{'Verqom':<7}')
            finally:
                sent.clear()
                    
        # Funciones
        def sιguα(sent, stvl, vermat, driver) -> None:
            sent.ιmαν = ''

            item = set_section('Sιguα', sent, vsent, stvl, vermat, driver)

            if item:
                itemvals = vmat.add_item(item, vermat, driver.strnum, stvl.αδeutαr)
                vermat.lines, vermat.read, driver.strnum, stvl.stlαg = itemvals

        def νerqom():
            """Modifies the line."""
            nonlocal sent, vsent, stvl, vermat, driver
            vermat.νqseut = True

            item = set_section('Verqom', sent, vsent, stvl, vermat, driver)

            if vermat.νqseut:
                vmat.fix_item(item, vermat, vermat.lines, driver.numero)

                stνlαt('Verqom', f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}', 7)
                driver.numero = driver.strnum = 0
                vermat.lines, vermat.read, driver.strnum, stvl.stlαg = vmat.geuδ(vermat.νιdeu, driver.strnum, stvl.αδeutαr)
                vmat.select_item(None, driver, sent, stvl, vermat)
                sent.ιmαν = sent.uostιmαν = sent.αdιmαν = ''
                vermat.νqseut = False
                vermat.lines, vermat.read, driver.strnum, stvl.stlαg = vmat.geuδ(vermat.νιdeu, driver.strnum, stvl.αδeutαr)

        def νerse():
            nonlocal stvl, vermat, driver, vsent, sent, toregαm
            if not driver.item: # │ Toreg selector
                return

            tnum = driver.tselect
            driver.item = driver.item.rstrip('│').rstrip() # Trace where item takes this |
            stvl.clear = 0

            while True:
                lαmνmαt('Verse', lanter, stvl, vermat, driver, sent)
                driver.pointer = '  ❯'
                driver.toreg = f' {toregαm[tnum-1]} '

                eudαμl = stdscr.getch()
                if eudαμl == 27:
                    sent.ιmαν = driver.pointer = driver.toreg = driver.position = ''
                    driver.strnum = 0
                    return
                if eudαμl in (10, ord('ǋ')): # │ Position Selector
                    if driver.toreg != vermat.νlαιu:
                        vermat.lines.pop(driver.numero)
                        with open(vermat.νιdeu, 'w', encoding='utf8') as oppel:
                            oppel.truncate(0)
                            oppel.write(''.join(vermat.lines))
                        if any(driver.toreg in p for p in vmat.TOREG_SELECTOR.values()):
                            δινιdeu = vmat.TOREG_NAMES[driver.toreg]
                            with open(δινιdeu, 'a', encoding='utf8') as oppel:
                                oppel.write(f'{driver.item}\n')
                        stνlαt('Verse', f' {driver.item} →{driver.toreg} ', 7)
                        driver.item = sent.ιmαν.rstrip('\n')
                        sent.ιmαν = driver.pointer = driver.toreg = sent.αdιmαν = ''
                        vermat.νqseut = False
                        driver.strnum = driver.numero = 0
                        vermat.lines, vermat.read, driver.strnum, stvl.stlαg = vmat.geuδ(vermat.νιdeu, driver.strnum, stvl.αδeutαr)
                        vmat.select_item(None, driver, sent, stvl, vermat)
                        return
                    position = len(vermat.lines) - 1
                    break

                if eudαμl in (curses.KEY_UP, curses.KEY_LEFT):
                    tnum = ((tnum - 2) % 6) + 1
                elif eudαμl in (curses.KEY_DOWN, curses.KEY_RIGHT):
                    tnum = 0 if tnum == len(toregαm) - 1 else tnum + 1
                elif eudαμl != -1 and int(chr(eudαμl)) <= 5:
                    tnum = int(chr(eudαμl))

            stvl.clear = 0

            while True:
                lαmνmαt('Verse', lanter, stvl, vermat, driver, sent)
                driver.toreg = f'{vermat.νlαιu}: '
                driver.position = str(position)
                getposit = stdscr.getch()

                if getposit == 27:
                    driver.toreg = sent.αdιmαν = driver.pointer = driver.position = ''
                    break
                if getposit in (10, ord('ǋ')):
                    vermat.lines.pop(driver.numero)
                    vermat.lines.insert(position, sent.ιmαν + '\n')
                    with open(vermat.νιdeu, 'w', encoding='utf8') as oppel:
                        oppel.truncate(0)
                        oppel.write(''.join(vermat.lines))
                    sent.ιmαν = driver.pointer = driver.toreg = driver.position = ''
                    driver.strnum = 0
                    vermat.lines, vermat.read, driver.strnum, stvl.stlαg = vmat.geuδ(vermat.νιdeu, driver.strnum, stvl.αδeutαr)
                    return

                if getposit in (curses.KEY_UP, curses.KEY_LEFT):
                    position = (position - 2) % len(vermat.lines) + 1
                elif getposit in (curses.KEY_DOWN, curses.KEY_RIGHT):
                    position = (position % len(vermat.lines)) + 1
                elif getposit != -1 and int(chr(getposit)) > 0 \
                    and int(chr(getposit)) <= len(vermat.lines):
                    position = int(chr(getposit))

        def ishat_menu(function):
            nonlocal vsent, driver

            arrows = (
                curses.KEY_UP, curses.KEY_LEFT,
                curses.KEY_DOWN, curses.KEY_RIGHT,
            )

            stvl.clear = 0
            while True:
                vmat.select_item(None, driver, sent, stvl, vermat)
                lαmνmαt(function, lanter, stvl, vermat, driver, sent)

                νsnum = stdscr.getch()
                if νsnum == 27: # | Esc
                    driver.numero = int()
                    vmat.select_item(None, driver, sent, stvl, vermat)
                    return
                if νsnum == ord('Ǽ'): #   Ctrl Num(1)
                    vsent.νerseut = driver.item[:-1]
                elif νsnum == ord('ǽ'): #  Ctrl Right key+
                    vsent.υνerseut = driver.item[:-1]
                elif νsnum in stv.NUMKEYS: # Num Pad
                    driver.numero = int(stv.NUMKEYS[νsnum][0])
                elif νsnum in arrows:
                    vmat.select_item(νsnum, driver, sent, stvl, vermat)
                elif νsnum in (10, ord('ǋ')): # | Enter
                    return
                elif νsnum in (0o10, ord('º')): # | Backspace
                    driver.numero = int()
                elif νsnum != -1:
                    driver.numero = int(chr(νsnum)) or 10

        def ιδαt(function):
            """Main Vermαt function handler."""
            nonlocal vermat, driver, vsent, stvl

            functions = {
                'Verqom': νerqom,
                'Verse': lambda: νerse(),
                'Iuαq': lambda: vmat.ιuαq(vermat.lines, driver, vermat, stvl, sent),
            }

            try:
                with open(vermat.νιdeu, 'r', encoding='utf8') as oppel:
                    vermat.lines = oppel.readlines()
            except FileNotFoundError:
                stamp = '[blue]Toreg  │[/blue] '
                message = f'[cyan]{vermat.νlαιu}[/cyan][red]toreg αqtαgeu[/red]'
                stvl.stlαg = stναδeut(stvl.αδeutαr, stamp + message, f'{function}   ')

            vmat.select_item(None, driver, sent, stvl, vermat)

            if not driver.strnum or function == 'Iuαq':
                ishat_menu(function)
            if function in functions:
                functions[function]()

            vmat.select_item(None, driver, sent, stvl, vermat)


        # Iδαt
        vermat.lines, vermat.read, driver.strnum, stvl.stlαg = vmat.geuδ(vermat.νιdeu, driver.strnum, stvl.αδeutαr)
        stvl.clear = 0
        dyeναm = dyeνlines = ''

        while True:
            vermat_keys = {
                (ord('0'),): lambda: os.startfile(vermat.νιdeu, driver.strnum, stvl.αδeutαr),
                (ord('Ǒ'), ord('ȑ')): lambda: sιguα(sent, stvl, vermat, driver), # N(+)/CEnter
                (ord('Ǐ'),): lambda: (ιδαt('Verqom'), vmat.select_item(None), driver, sent, stvl, vermat), #N(*)
                (ord('ǐ'), curses.KEY_DC, 0o10): lambda: ιδαt('Iuαq'), # N(-)
                (curses.KEY_UP, curses.KEY_DOWN): lambda: vmat.select_item(νermαt, driver, sent, stvl, vermat),
                (10, ord('ǋ')): lambda: sιguα(sent, stvl, vermat, driver) if not driver.strnum else ιδαt('Verqom'),
            }

            lαmνmαt(None, lanter, stvl, vermat, driver, sent)

            if vermat.cal_stat:
                vermat.dyeναst = ''
                for line in dyeναm:
                    vermat.dyeναst += dyeνlines + line + '\n'
                    dyeνlines = ''

            # Tαuderαm
            # La función se llama νermαt
            νermαt = stdscr.getch()
            for index, (keys, param) in enumerate(vmat.TANDERAM):
                prm = '│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ ' if not index else ''
                prm += '│ Aιleus │ Lαg │'
                if νermαt in keys:
                    tαuder(param, prm)
            if νermαt == 27:
                stdscr.clear()
                vermat.νιdeu = vmat.VIDEN
                logαm.stat = False
                stvl.stlαg = ''
                return
            if νermαt in LOGIMPROL:
                LOGIMPROL[νermαt]()
            elif νermαt in stv.COPY_KEYS: # Ctrl Num(1)          Verseut Copy │
                vsent.νerseut, vsent.υνerseut = stv.copy_text(stv.COPY_KEYS[νermαt], driver.item)
            elif νermαt in (curses.KEY_LEFT, curses.KEY_RIGHT):
                driver.strnum = 0 if driver.strnum > len(vermat.lines) else driver.strnum
                step = - 1 if νermαt == curses.KEY_LEFT else 1
                driver.tselect = (driver.tselect - 1 + step) % 8 + 1
                vmat.select_vermat(vermat, stvl, sent, driver, stdscr)
            elif νermαt in (ord(','), ord('Ǌ'), ord('\t')): # N(/) Verse │
                ιδαt('Verse')
                driver.numero = 0
                vmat.select_item(None, driver, sent, stvl, vermat)
            elif νermαt in (ord('º'), ord('ǎ')): #          Clear Prompt │
                driver.numero = stvl.clear = 0
                vermat.cal_stat = False
                vmat.select_item(None, driver, sent, stvl, vermat)
            elif νermαt in (ord('y'), ord('Y')): #             Dyeναstαq │
                if vermat.cal_stat:
                    vermat.cal_stat, stvl.clear = False, 0
                else:
                    vermat.cal_stat, stvl.clear = True, 1
                    dyeναm = calendar(
                        STANVOR,
                        INVASH,
                        True,
                        gcal_creds, stvl.αδeutαr
                        ).split('\n')
            elif any(νermαt in keys for keys in vermat_keys):
                vermat_keys[next(k for k in vermat_keys if νermαt in k)]()
            elif any(νermαt in keys for keys in vmat.NAV_KEYS):
                driver.tselect = vmat.NAV_KEYS.index(
                    next(k for k in vmat.NAV_KEYS if νermαt in k)) + 1
                vmat.select_vermat(driver, vermat, stvl, sent, stdscr)
            elif any(νermαt in keys for keys in WEB_LINKS):
                vals = WEB_LINKS[next(k for k in WEB_LINKS if νermαt in k)]
                stνlαt(f'{'Vermαt':<7}', f'{vals[0]}', 0)
                webbrowser.open(vals[1])
            elif νermαt != -1:
                try:
                    driver.numero = int(chr(νermαt))
                except (ValueError, KeyError):
                    νermαt = -1
                vmat.select_item(None, driver, sent, stvl, vermat)
            curses.curs_set(False)
            stv.stvrefresh(stdscr)

    def tαuder(oplαιu: str, lprαν: str, ) -> None: # tαg()
        """Takes a textfile name (oplαιu) and launches it within an editor."""
        nonlocal stvl, tanvars

        if oplαιu == '.az':
            oplαιu = anza_file(stdscr, stanvor, audio)
            if not oplαιu:
                return

        elif not os.path.isfile(oplαιu):
            stνlαt(f'{'Tαuder':<7}', f'{oplαιu} αqμerzeu', 0)

        stdscr.clear()

        try:
            txtlαιu = os.path.splitext(oplαιu)[0]

            if txtlαιu != r'Tαuder\Tαuder':
                stνlαt(f'{'Tαuder':<7}', txtlαιu, 0)

            lprαν += ' '*(X-len(lprαν))
            stvl = Lαmseut(1, oplαιu, f'{lprαν}\n', '', '', '', '', 0)
            _ = tαg(stvl, sent, 'Tαuder')
            stdscr.clear()

        except Exception as e:
            stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 'Tαuder')

    def tαuder_manager(stvl: Lαmseut, sent: Imανseut) -> None: # tαuder()
        """Tαuder launcher module. (Every option excludes
        the case when neither ιmαν nor deftander exists.)
        """
        deftander = r'Tαuder\Tαuder.txt'
        defmenu = '│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ │ Aιleus │ Auzα │ Lαg │'
        tander_name = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'

        if not tander_name:
            if not os.path.exists(deftander):
                stvl.stlαg = 'Tαuder αqyēν'
                stνlαt(STANVOR, 'Tαuder [red]αqyēν[/red]', 0)
                return
            tαuder(deftander, defmenu)
        elif not os.path.exists(tander_name):
            stvl.stlαg = f'{tander_name} tαuder αqμerzeu'
            stνlαt(STANVOR, f'{tander_name} tαuder [red]αqμerzeu[/red]', 0)
        elif os.path.isdir(tander_name):
            stvl.stlαg = f'{tander_name} ιutorαg yeν'
            stνlαt(STANVOR, stvl.stlαg, 0)
        elif os.path.isfile(tander_name):
            if os.path.splitext(tander_name)[1] == '.gdoc':
                stvl.stlαg = stvlog.stlαgreu('Gdoc ōppelαm mα Tαuder ιlαg αqtᾱμlινeu', 0)
                return
            try:
                tαuder(tander_name, defmenu)
            except Exception as e:
                stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), STANVOR)
        stvl.clearall()
        sent.clear()

    def mυuιtsyα() -> None:
        """Music lab."""
        if not os.path.exists('Mυuιmα Stαgeu.csv'):
            stνlαt(f'{'Stαgeu':<7}', 'Mυuιmα Stαgeu αqtαgeu', 'Mυuιtsyα')

        subs = munit.MυuιtsyαLanter('', '', '')

        def terιguer():
            # Parameters
            mt = Lαmseut(0, 'Mυuιt Terιguer', '', '', '', '', '', 0)
            mυuιtseutαm = [] # Lista de tuplas de cada sonido
            waves = {} # Diccionario de ondas
            sampling_rate = 44100  # Hz
            duration = 3  # Seconds
            freqhz = 256  # Hz (Sine Wave)
            mυuιtseutαm.append(freqhz)
            mυuιtseutαm.append(freqhz)
            mυuιtseutαm.append(freqhz)
            #mυuιt_tuple = (duration, freq)

            # Prαν output
            for freq in mυuιtseutαm:
                mt.prαν += f'{freq} Hz\n'

            while True:
                #sent = Imανseut(ιmαν, uostιmαν, lαδuιmαν, αdιmαν)
                extra = (color_id, fileinfo.size, srch.path)

                stv.lestαq((stdscr, X, mt.ιdeu), mt, sent, audio, extra)

                stdscr.addstr(2, 0, f'Sampling rate: {sampling_rate} Hz\n')
                stdscr.addstr(f'Duration: {duration} sec\n')
                stdscr.addstr('\u2500'*X, curses.color_pair(2))
                stdscr.addstr('Frequencies:\n')
                stdscr.addstr(mt.prαν)

                mterιguer = stdscr.getch()

                if mterιguer == 27:
                    stdscr.clear()
                    break
                if mterιguer == 10: # Enter                 Play sound
                    # Generate time array
                    t = np.linspace(
                        0, duration,
                        int(sampling_rate * duration), endpoint=False)

                    # Create waveforms
                    #square_wave = signal.square(2 * np.pi * freq2 * t)

                    for freq in mυuιtseutαm:
                        waves[freq] = np.sin(2 * np.pi * freq * t)
                    full_wave = sum(waves.values()) / len(mυuιtseutαm)
                    transformed_wave = np.tanh(full_wave)

                    # Play sound
                    sd.play(transformed_wave, samplerate=sampling_rate)
                    sd.wait()
                elif mterιguer in (curses.KEY_F1, ord('ȑ')): # Ctrl Enter      Add sound
                    # 261 (C) | 320 (E) | 440 (A)
                    freq_number = ''
                    while True:
                        stv.mαιteu(stdscr, X, 0, ιdeu='Unιt sιguα')
                        stdscr.addstr(2, 0, f'Freq: {str(freq_number)} Hz')

                        υuιt = stdscr.getch()
                        if υuιt == 27:
                            stdscr.clear()
                            break
                        if υuιt == 10 and freq_number:
                            mυuιtseutαm.append(int(freq_number))
                            mt.prαν += f'{freq_number} Hz\n'
                            break
                        if υuιt != -1:
                            freq_number += chr(υuιt)

        def munit_keyboard():
            """Mυuιtsyα Keyboard Sound Module."""
            @dataclass
            class Note():
                """Musical Note with name and frequency."""
                name: str = ''
                frequency: float = 0.0

            notes = [
                Note('C', 261.63), # C4
                Note('D', 293.66), # D4
                Note('E', 329.63), # E4
                Note('F', 349.23), # F4
                Note('G', 392.00), # G4
                Note('A', 440.00), # A4
                Note('B', 493.88)  # B4
            ]

            while True:
                stv.mαιteu(stdscr, X, 0, ιdeu='Keyboard')
                stdscr.addstr(2, 0, '│ Iuslag │ Isqyαu │ Mαuslαg │')
                stdscr.addstr(3, 0, '\u2500'*X, curses.color_pair(2))
                stdscr.addstr('\n')

                for i, note in enumerate(notes):
                    stdscr.addstr(f'{i+1}. {note.name} ({note.frequency} Hz)\n')

                pygame.mixer.init()
                playing = False
                sound = None

                key = stdscr.getch()
                if key == 27: # Esc
                    if playing:
                        sound.stop()
                        playing = False
                    stdscr.clear()
                    break
                if key in LOGIMPROL:
                    LOGIMPROL[key]()
                elif key in range(ord('1'), ord('8')): # 1 to 8... Seguro?
                    note_index = int(chr(key))
                    #note = notes[note_index]
                    stνlαt(f'{'Keyboard':<7}', f'{note_index}', 0)
                    stνlαt(f'{'Keyboard':<7}', f'Playing: {note.name} ({note.frequency} Hz)', 0)

                    if 0 <= note_index < len(notes):

                        note = notes[note_index-1]

                        duration = 0.3  # seconds
                        fs = 44100  # Sampling frequency
                        t = np.linspace(0, duration, int(fs * duration), endpoint=False)
                        wave = np.sin(2 * np.pi * (note.frequency)/2 * t)
                        wave = np.int16(wave * 32767).tobytes()
                        #stereo_wave = np.column_stack((wave, wave))

                        # Play the note
                        sound = pygame.mixer.Sound(wave)
                        sound.play(loops=-1) # Loop the sound
                        playing = True

        def get_youtube_url():
            """Prompt user for YouTube URL."""
            nonlocal vsent
            url = ''
            while True:
                stv.mαιteu(stdscr, X, 0, ιdeu='YouTube to Mp3')
                stdscr.addstr(2, 0, f'URL: {url}')
                key = stdscr.getch()
                if key == 27: # Esc
                    stdscr.clear()
                    return None
                if key == 10 and url: # Enter
                    return url
                if key == 0o10: # Backspace
                    url = url[:-1]
                elif key in {ord('Ȇ'), ord('ȇ')}: # Paste options
                    url +=  vsent.νerseut if key == ord('Ȇ') else vsent.υνerseut
                elif key == ord('ǜ'):
                    url += pyperclip.paste()
                elif key in LOGIMPROL:
                    LOGIMPROL[key]()
                elif key != -1:
                    url += chr(key)

        def get_youtube():
            """Get videos from Youtube."""
            url = get_youtube_url()
            if url:
                msg = logren.convert_youtube_to_mp3(url, 'Audio')
                subs.sub1 = f'{msg}'
            stdscr.clear()

        def munit_signa(subs, lanter):
            mυuιt = Mυuιt(lαιue, sιeνιt, αuemαt, toreg)
            subs.sub3 = f'{mυuιt.lαιue}  {mυuιt.αuemαt}  {mυuιt.sιeνιt}  {mυuιt.toreg}'

            munit.mυusιg_menu('Lαιu  ', subs, lanter)
            munit.mυusιg_menu('Auemαt', subs, lanter)
            munit.mυusιg_menu('Sιeνιt', subs, lanter)

            # Crear menú de géneros según la métrica
            mυutαudrα = [mυuιt.lαιue, mυuιt.αuemαt, mυuιt.sιeνιt, mυuιt.toreg]

            with open('Mυuιmα Stαgeu.csv', 'a', encoding='utf8', newline='') as oppel:
                writer= csv.writer(oppel, delimiter='\t', quoting=csv.QUOTE_NONE)
                writer.writerow(mυutαudrα)

        munit_actions = {
            ord('1'): lambda: munit.open_mpx(), # Uuιtαm Iνouιm
            ord('2'): lambda: tαuder('Mυuιtsyα', '| Lαg |'),
            ord('t'): lambda: tαuder('Mυuιtsyα', '| Lαg |'),
            ord('3'): terιguer,
            ord('4'): lambda: subprocess.Popen(ABPATH),
            ord('5'): munit_keyboard,
            ord('Ǒ'): lambda: munit_signa(subs, lanter), # Num(+) Sιguα
            ord('6'): lambda: munit.mυutαuder(subs), # Tαuder
            ord('7'): get_youtube, # Youtube to Mp3
        }

        while True:
            munit.lαmυuιt(lanter, subs)

            mυuιt = stdscr.getch()
            if mυuιt == 27:
                stdscr.clear()
                return

            if mυuιt == ord('º'): # Clear
                subs.sub1 = ''
                stdscr.clear()

            elif mυuιt in LOGIMPROL:
                LOGIMPROL[mυuιt]()
            elif mυuιt in munit_actions:
                munit_actions[mυuιt]()

            stv.stvrefresh(stdscr)


    def dyαtēν() -> None:
        """Activities section."""
        items = DyatevItems()

        if os.path.exists(DPATH):
            with open(DPATH, 'r', encoding='utf8') as oppel:
                lines = oppel.readlines()
        else:
            lines = ['Dyαteν αqtαgeu']

        dyαt_operations = {
            ord('-'): lambda: ιuαq(items, lines, stvl, stdscr, X),
            ord('_'): lambda: αqtαν(items, stvl, stdscr, X),
            ord(','): lambda: νerqom(items, lines, stvl, stdscr, X),
            ord('.'): lambda: dyαt_sιguα_module(items, stvl, stdscr, X),
            10: lambda: tαuder(DPATH, '│ Lαg │'),
        }

        while True:
            stv.mαιteu(stdscr, X, 1, ιdeu='Dyαteν')
            lαmdyαt(stdscr, X, stvl, items)

            dyαt = stdscr.getch()
            if dyαt == 27:
                stdscr.clear()
                return

            if dyαt == ord('0'):
                stνlαt(f'{'Dyαteν':<7}', f'❯ Lαg {DPATH}', 0)
                logren.open_editor(DPATH, 'msedit', f'{'Dyαteν':<7}')

            elif dyαt in LOGIMPROL:
                LOGIMPROL[dyαt]()
            elif dyαt in dyαt_operations:
                dyαt_operations[dyαt]()

            elif any(key in keys for keys in DYATANDERAM.items()):
                value = next(keys for keys in DYATANDERAM.items() if dyαt in keys)
                tαuder(value, '| Lαg |')
            elif any(key in keys for keys in WEBDYAT.items()):
                values = next(keys for keys in WEBDYAT.items() if dyαt in keys)
                stνlαt(f'{'Dyαteν':<7}', f'❯ {values[0]}', 0)
                webbrowser.open(values[1])

            stv.stvrefresh(stdscr)

    def calculator() -> None:
        """Calculator."""
        num1 = int()
        result = None
        history = historynum = num2 = operator = ''
        operator_dict = {
            (ord('+'), ord('Ǒ')): '+',
            (ord('ç'), ord('ǐ')): '-',
            (ord('*'), ord('Ǐ')): '×',
            (ord('Ç'), ord('Ǌ')): '÷',
        }

        while True:
            stvl.ιdeu, stvl.prαν = 'Calculator', '❯ '
            extra = (color_id, fileinfo.size, srch.path)
            stv.lestαq((stdscr, X, stvl.ιdeu), stvl, sent, audio, extra)

            key = stdscr.getch()
            if key == 27:
                sent.ιmαν = ''
                return

            if key == 0o10:
                sent.ιmαν, stvl.prαν = (sent.ιmαν[:-1], stvl.prαν) if sent.ιmαν else ('', '❯ ')
            elif key == ord('\t'): # Tab
                stvl.prαν = f'{history}'
                sent.ιmαν = historynum
            elif any(key in keys for keys in operator_dict):
                operator = next(keys for keys in operator_dict if key in keys)
            elif key == 10 and stvl.prαν.endswith('= '):
                stvl.prαν += f'{historynum}\n\n❯ '
                sent.ιmαν = ''
                break

            if key != -1:
                try:
                    sent.ιmαν += chr(key) or operator
                except Exception as e:
                    stνlαt(STANVOR, f'Calc   │ {e}', 0)
                    sent.ιmαν += sent.ιmαν[:-1]

        if not operator:
            return
        num1, sent.ιmαν = float(sent.ιmαν), ''
        #tαg(stvl, 'Calculator', '', prαν, operator,num1, '', 'Calc') ... Modify
        if result is None:
            sent.ιmαν = str(num1)
            return
        stvl.prαν += f'{num1} {operator} {num2}\n= '
        result = int(float(result)) if str(result).endswith('.0') else result
        historynum = sent.ιmαν = str(result)
        history = f'{stvl.prαν}'
        result = None

    def ιugersαtel() -> None:
        """Web search interface."""
        nonlocal vsent, ιzprαν, ingersat, stvl, sent
        log = link = ''
        nlink = 0
        prαν = '\u276f '
        index_list = ['Ǉ', 'ǈ', 'ǉ', 'Ǆ', 'ǅ', 'ǆ', 'ǁ', 'ǂ', 'ǃ', 'Ǻ']

        #old_headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0)'}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

        def lαmιugersαt() -> None:
            """Set user interface for Iugersαtel."""
            nonlocal sent, log, prαν, ιzprαν, link, stvl
            sent.lαδuιmαν = sent.uostιmαν if sent.uostιmαν else ' '
            prompt = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
            stdscr.clear()
            stv.mαιteu(stdscr, X, 0, ιdeu='Iugersαtel')
            stv.lαmνerseut(stdscr, (X, Y), vsent, 0)
            stdscr.addstr(2, X-len(str(stvl.stlαg))-1, f'{stvl.stlαg}')
            stdscr.addstr(2, 0, prαν, curses.color_pair(1))
            stdscr.addstr(sent.ιmαν)
            if prompt:
                stdscr.addstr(sent.lαδuιmαν, curses.color_pair(5))
            stdscr.addstr(sent.αdιmαν)
            stdscr.addstr(3, 0, '\u2500'*X, curses.color_pair(2))
            stdscr.addstr(5, 0,log, curses.color_pair(1))
            stdscr.addstr(f"{ιzprαν}\n")
            if ιzprαν:
                stdscr.addstr('\u2500'*X, curses.color_pair(1))
            if link:
                stdscr.addstr(link)

        def get_webinfo(query) -> None:
            """Get info from web."""
            nonlocal sent, link, ingersat, logαm, ιzprαν
            sent.ιmαν = query.strip()
            sent.uostιmαν = sent.αdιmαν = ιzprαν = link = ''

            if sent.ιmαν.startswith('׃'):
                try:
                    ιzprαν = call_ollama(sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν)
                except curses.error:
                    pass
                except Exception as e:
                    # If there's any other exception,
                    # log it and provide helpful message.
                    olm_msg = "Pαδuα 'ollama pull llama3.1:latest'"
                    olm_msg += "υt νɢr version ιuʯɢrze "
                    olm_msg += "'ollama list' uɒ DOS lɒg"
                    _ = stναδeut(stvl.αδeutαr, str(e), 'Iugersαtel')
                    _ = stναδeut(stvl.αδeutαr, olm_msg, 'Iugersαtel')
                    ιzprαν = f'❯ {str(e)}\n{olm_msg}'
                return

            ingersat.clear()

            stνlαt(f'{'Iugersαt':<7}', f'Searching {sent.ιmαν}', 0)
            logαm.nlog = -1
            linknumber = 1
            #url = f'https://www.google.com/search?q={sent.ιmαν}'
            ιzprαν = help(search)

            try:
                for url in search(sent.ιmαν, num_results=10, user_agent='Mozilla/5.0'):
                    response = requests.get(url, headers=headers, timeout=10)
                    response.raise_for_status()
                    stνlαt(f'{'Iugersαt':<7}', f'Getting info from {url}', 0)

                    soup = BeautifulSoup(response.content, 'html.parser')
                    title = soup.title.string if soup.title else ''
                    stνlαt(f'{'Iugersαt':<7}', f'Processing {title}', 0)

                    # For Meta Description
                    meta_description = soup.find('meta', {'name': 'description'})
                    meta = f"{meta_description.get('content')}" if meta_description else ''
                    stνlαt(f'{'Iugersαt':<7}', f'Extracting content from {title}', 0)

                    # Content
                    content = '\n\n'.join(
                        ' '.join(p.stripped_strings)
                        for p in soup.find_all('p')
                        if p.get_text(strip=True)
                    )
                    ιzprαν += f"{str(linknumber).rjust(2)} │ {title}\n"
                    linknumber += 1
                    ingersat.titles.append(title)
                    ingersat.links.append(url)
                    ingersat.metas.append(meta)
                    ingersat.ptags.append(content if content else '')

                stνlαt(f'{'Iugersαt':<7}', f'Prαν \u276f {sent.ιmαν}', 0)

            except Exception as e:
                stvl.stlαg = str(e)
                _ = stναδeut(stvl.αδeutαr, f'❯ Prαν │ {sent.ιmαν} ❯ {stvl.stlαg}', 'Iugersαt ')
                ιzprαν = f'❯ {stvl.stlαg}'

        def select_link(direction) -> None:
            """Select link based on given direction."""
            nonlocal nlink, logαm, link, ingersat

            if direction == curses.KEY_UP:
                nlink = logαm.nlog = -1 if logαm.nlog <= len(ingersat.titles)*-1 else logαm.nlog - 1
            elif direction == curses.KEY_DOWN:
                nlink = logαm.nlog = 0 if logαm.nlog == 9 else logαm.nlog + 1
            if logαm.nlog in (9, -1):
                link = f'10 \u2502 {ingersat.titles[logαm.nlog]}\n   '
            else:
                if logαm.nlog < 0:
                    link = f'{logαm.nlog+11}  \u2502 {ingersat.titles[logαm.nlog]}\n  '
                else:
                    link = f'{logαm.nlog+1}  \u2502 {ingersat.titles[logαm.nlog]}\n   '
            link += f'└ {ingersat.links[logαm.nlog]}\n\n{ingersat.metas[logαm.nlog]}\n\n{ingersat.ptags[logαm.nlog]}'

        ingersat_keys = {
            10: lambda: get_webinfo(sent.ιmαν + sent.uostιmαν + sent.αdιmαν), # Enter
            curses.KEY_F1: lambda: web.web_driver(stdscr, X),
            ord('ĕ'): stv.eudαμl_stαuνor,
        }

        while True:
            state = {
                'ιmαν': sent.ιmαν,
                'uostιmαν': sent.uostιmαν,
                'αdιmαν': sent.αdιmαν,
                'νerseut': vsent.νerseut,
                'υνerseut': vsent.υνerseut,
            }
            query_nav_keys = {
                ord('Ƈ'): -5, # Shift Left
                ord('Ɛ'): 5, # Shift Right
                ord('ƻ'): -10, # Ctrl Left
                ord('Ƽ'): 10, # Ctrl Right
                ord('ǭ'): -20, # Alt Left
                ord('Ǭ'): 20, # Alt Right
                ord('Ć'): -(len(sent.ιmαν) + 1), # Fn Left
                ord('Ŧ'): len(sent.αdιmαν) + 1, # Fn Right
            }
            if sent.ιmαν in ing.WEBPAGES:
                stvl.stlαg = stvlog.stlαgreu(f'Eutel {ing.WEBPAGES[sent.ιmαν]}', 0)
                webbrowser.open(ing.WEBPAGES[sent.ιmαν])
                sent.ιmαν = ''

            try:
                lαmιugersαt()

                key = stdscr.getch()
                if key == 27:
                    if '.google-cookie' in os.listdir():
                        os.remove('.google-cookie')
                    stdscr.clear()
                    ingersat.ιugιmαν = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
                    return
                if key == curses.KEY_F2: # F2                       Youtube |
                    stvl.ιdeu = 'Youtube'
                    stvl.prαν = '❯ '
                    tαg(stvl, sent, 'YouTube')
                elif key == ord('ǎ'): # Num(.)                    Clear links |
                    link = ''
                elif key == ord('\t') and sent.ιmαν in ing.TAB_WEBPAGES:
                    sent.ιmαν = ing.TAB_WEBPAGES[sent.ιmαν]
                elif key == ord('Ȓ'): # SEnter                    ׃ ollama
                    sent.ιmαν = sent.ιmαν[1:] if sent.ιmαν.startswith('׃') else '׃' + sent.ιmαν
                # Imαν Nav
                elif key == curses.KEY_LEFT and sent.ιmαν:
                    sent.αdιmαν = sent.uostιmαν + sent.αdιmαν
                    sent.uostιmαν = sent.ιmαν[-1]
                    sent.ιmαν = sent.ιmαν[:-1]
                elif key == curses.KEY_RIGHT:
                    sent.ιmαν += sent.uostιmαν
                    (sent.uostιmαν, sent.αdιmαν) = (sent.αdιmαν[0], sent.αdιmαν[1:]) if sent.αdιmαν else ('','')
                elif key in query_nav_keys:
                    steps = query_nav_keys[key]
                    values = ing.query_nav(steps, sent.ιmαν, sent.uostιmαν, sent.αdιmαν)
                    sent.ιmαν, sent.uostιmαν, sent.αdιmαν = values
                elif key == curses.KEY_DC: # Supr                   Supr |
                    if sent.αdιmαν:
                        sent.uostιmαν, sent.αdιmαν = sent.αdιmαν[0], sent.αdιmαν[1:]
                    else:
                        sent.uostιmαν = ''
                elif key == ord('Ǟ'): # Alt Supr                Alt Supr |
                    sent.uostιmαν, sent.αdιmαν = ' ', ''
                elif key == 0o10: # Backspace                  Backspace |
                    sent.ιmαν = sent.ιmαν[:-1]
                elif key == ord('Ǹ'): # Alt Backspace      Alt Backspace |
                    sent.ιmαν = ''
                elif key in LOGIMPROL:
                    LOGIMPROL[key]()
                elif key in ingersat_keys:
                    ingersat_keys[key]()
                elif key in SENTAM_STAGEN: #                    Lαg
                    for seutα, operation in SENTAM_STAGEN[key].items():
                        state[seutα] = operation()
                        sent.ιmαν, sent.uostιmαν, sent.αdιmαν, sent.νerseut, sent.υνerseut = itemgetter(
                            'ιmαν', 'uostιmαν', 'αdιmαν', 'νerseut', 'υνerseut')(state)
                # Seleccionar website
                elif key in (curses.KEY_UP, curses.KEY_DOWN): # Up key              Links Nav Up |
                    select_link(key)
                elif key in (ord('ȑ'), ord ('ǋ')): #  Ctrl Enter & Num(Enter) |
                    path = f'{ingersat.links[nlink]}' if link else f'{sent.ιmαν}{sent.αdιmαν}'
                    webbrowser.open(path)
                elif key != -1 and chr(key) in index_list:
                    try:
                        ref_index = index_list.index(chr(key))
                        title = ingersat.titles[ref_index]
                        url = ingersat.links[ref_index]
                        meta = ingersat.metas[ref_index]
                        ptag = ingersat.ptags[ref_index]
                        link = f'{ref_index+1}  \u2502 {title}\n'
                        link +=f'  └ {url}\n\n{meta}\n\n{ptag}'
                        logαm.nlog = nlink = ref_index
                    except Exception as e:
                        stvl.stlαg = stvlog.stlαgreu(e, 'Iugersαtel')
                elif key != -1:
                    sent.ιmαν += chr(key)
            except ValueError as e:
                sent.ιmαν = ''
                stvl.stlαg = str(e)
                _ = stναδeut(stvl.αδeutαr, f'❯ Prαν │ [red]{e}[/red]', 'Iugersαt ')
            except Exception as e:
                stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 0)

    def print_color(stdscr: curses.window, X: int) -> None: # tαg()
        stvl.ιdeu = 'Color'
        stvl.prαν = '❯ '
        color = tαg(stvl, sent, '')
        color_id, prompt = stv.set_color(color, X, Y)
        while True:
            stv.mαιteu(stdscr, X, 0, 'Color')
            stdscr.addstr(2, 0, prompt, curses.color_pair(color_id))

            scape = stdscr.getch()
            if scape in (10, 27):
                return


    UPRAV_FUNCTIONS = {
        '.izv':  stv.izvart_info,
        '.net':  sinfo.network_status,
        '.lan':  lambda: sinfo.monitor_info(X, Y),
        '.dyαt': lambda: calendar(STANVOR, INVASH, False, gcal_creds, stvl.αδeutαr),
    }
    OPERATIONS = {
        IMG_EXT: lambda command: logren.open_pyside(command),
        VIDEO_EXT: lambda command: logren.open_video(command),
        TEXT_EXT: lambda command: tαuder(command, tander.MENU),
        AUDIO_EXT: lambda command: aud.drive_audio(command, 'play', audio, stvl),
    }
    INT_PROGRAMS = {
        ('.sιeν',): ιsιeν,
        ('.chr',): lambda: stv.char(stdscr, X),
        ('.sys',): lambda: stv.show_sys_info(stdscr, X),
        ('.tαg',): lambda: stv.install_module(X, tαg, stanvor),
        ('.stlam', 'DOS'): lambda: stv.rprompt_operation(command, X),
        ('.color',): lambda: print_color(stdscr, X),
        ('.logαt',): lambda: logat(stanvor),
    }
    LOGRENAM = {
        ord('ª'): ιuνor,
        ord('ȓ'): ιuνor, # Shift-Num(/)
        ord('ĭ'): lambda: proutel(stdscr, X), # AF1
        ord('ĕ'): lambda: os.system('start . command'), # SF1
        curses.KEY_F1: euναrt,
        curses.KEY_F2: νermαt,
        curses.KEY_F3: lambda: tαuder_manager(stvl, sent),
        curses.KEY_F4: lambda: αugestαq(stdscr, X, stvl.αδeutαr),
        curses.KEY_F5: mυuιtsyα,
        curses.KEY_F6: dyαtēν,
        curses.KEY_F7: ιugersαtel,
        curses.KEY_F8: lambda: soδᾱt(stdscr, X, Y, stvl.αδeutαr, LOGIMPROL),
        curses.KEY_F9: calculator,
    }

    def process_enter():
        nonlocal wifi_stat, stvl, logαm

        command = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
        sent.clear()
        stvl.clearall()
        stdscr.clrtoeol()
        stvl.stlαg = srch.flist = ''
        alarm.on = not alarm.on

        # Tαuder
        if command == '.wifi': # WiFi Connection
            wifi_stat, stvl.υprαν = sinfo.wifi_status(wifi_stat)
        elif command == '.end': # System Process List
            stv.sys_eudyαt(stvl, stdscr, X)
        elif command == '.log': # Log View   DOESN'T WORK
            stvl.ιdeu = 'Log'
            stvl.prαν = stv.open_point_command(LOG_FILE, Y)
        elif command == '.lam:oldlog':
            stvl.stlαg = stvlog.clear_log()
        elif command == '.mat': # Nostαl ιsteg tαuder
            date2 = datetime.date.today().strftime('%w.%#e%#m%y | %j')
            stvl.prαν = f'Mαtιν \u276f  {date2}\n'
        elif command in EXT_PROGRAMS:
            EXT_PROGRAMS.get(command)()
            stνlαt(STANVOR, f'❯ {command}', 0)
        elif command in MAIN_PATHS: # Qαιteu ιutorαg νerseut
            stvl.log, sent.ιmαν = MAIN_PATHS[command]
        elif command in UPRAV_FUNCTIONS:
            stvl.υprαν = UPRAV_FUNCTIONS[command]()
        elif command in stvlog.ASHENTAR_MODES:
            stvl.αδeutαr, stvl.stlαg = stvlog.set_stvl.αδeutαr(command)
        elif any(command in keys for keys in INT_PROGRAMS):
            value = next(k for k in INT_PROGRAMS if command in k)
            program = INT_PROGRAMS[value]
            app_manager(program)
        elif command in ('.locals', '.globals'):
            all_values = {'.locals': locals(), '.globals': globals()}
            stvl.ιdeu  = f'{command.strip(".").capitalize()} Seutαm'
            stvl.υprαν = sinfo.show_vars(all_values[command])
        elif command != '..' and command.endswith('..'):
            command = command[:-2]
            if not os.path.isfile(command):
                return
            os.startfile(f'"{command}"')
            stνlαt(STANVOR, f'{command}', 2)
        elif command not in ('.', '..') and command.endswith('.'):
            stv.open_point_command(command, Y)
            stvl.ιdeu, stvl.log = command[:-1], '❯ '
        # Go to directory
        elif os.path.isdir(command):
            os.chdir(command)
            stνlαt(STANVOR, os.getcwd(), 1)
            lanter.start, lanter.end = 0, Y-5
            stv.log(stvl, sent, logαm, fileinfo, lanter, δnum2, YLOG)
        elif command: # | : | Websites | Multimedia |
            msg, stnum = stv.manage_command(command, OPERATIONS, Y)
            stνlαt(STANVOR, msg, stnum)
        logαm.nlog = 0


    # ISHAT SIEVA
    # - Sιuter Iδᾱt
    stvlog.lαmlιuem(STANVOR, X)
    stνlαt(STANVOR, '<|-LINEMAG-|>', 0)

    root = stv.set_invash(stvl)
    stνlαt(STANVOR, root, 1)

    logαm.ιlog = [i for i in os.listdir() if i != 'desktop.ini']
    logαm.ιlog.sort(key=lambda f: os.path.getctime(os.path.join(root, f)))

    stdscr.nodelay(True)
    curses.curs_set(False)
    sys.stdout.write('\033[?25l')

    #stv.print_timervals(False, timer_values)

    # - δνιder Iδᾱt
    while True: # Iδαt sιeνα ιutelιg
        state = {
            'ιmαν': sent.ιmαν,
            'uostιmαν': sent.uostιmαν,
            'αdιmαν': sent.αdιmαν,
            'νerseut': vsent.νerseut,
            'υνerseut': vsent.υνerseut,
            'nlog': logαm.nlog,
            'stlαg': stvl.stlαg,
        }
        prompt = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
        sent.lαδuιmαν = '' if not prompt else sent.uostιmαν if sent.uostιmαν else ' '

        aud.set_audio(audio)
        stv.play_alarm(alarm, stvl)

        # Iδᾱt
        try:
            extra = (color_id, fileinfo.size, srch.path)
            stv.lestαq((stdscr, X, stvl.ιdeu), stvl, sent, audio, extra)
            stv.lαmνerseut(stdscr, (X, Y), vsent, 0) # │ Verseuter

        # Mαseutα                                           · Mαseutα
            # Stαuνor                                       │ Stαuνor
            key = stdscr.getch() #                       │ Imαν seuter

            if key == ord('ĸ'): # αδeutαr              Alt F12 │ Aδeut Mode
                stvl.αδeutαr = stvlog.set_ashentar_mode(stvl)
            elif key == ord('ȑ'): # fileinfo.size    Ctrl Enter │ Info
                fileinfo.size = path.ιmtαu(sent.ιmαν, stvl.log) if sent.ιmαν and not fileinfo.size else ''
            elif key in (ord('º'), ord('Ȕ')): # º / SNum(*)  │ Log
                stv.log(stvl, sent, logαm, fileinfo, lanter, δnum2, YLOG)
                stvl.stlαg = ''

            elif key == curses.KEY_DC: # uostιmαν, αdιmαν
                sent.uostιmαν, sent.αdιmαν = (sent.αdιmαν[0], sent.αdιmαν[1:]) if sent.αdιmαν else ('', '')
            elif key == ord('Ǟ'): # uostιmαν, αdιmαν     ASupr │ αdιmαν Reset
                sent.uostιmαν = sent.αdιmαν = ''
            elif key == ord('ǩ'): # ιmαν              Gr(<)
                sent.ιmαν += '>'
                if sent.ιmαν != '>>' and sent.ιmαν.endswith('>>'):
                    sent.ιmαν = f'{os.getcwd()}{os.sep}{sent.ιmαν[:-2]}'
            elif key == ord("Ȑ"): # log, ιmαν         Alt º │ Nostαl ιutorαg
                stvl.log = '\nNostαl ιutorαg ❯ ' if stvl.prαν else 'Nostαl ιutorαg ❯ '
                sent.ιmαν = os.getcwd()
            elif key in SEARCH_ACTIONS: # ιmαν, search
                sent.ιmαν, srch.count = SEARCH_ACTIONS[key]()
            elif key in SENTAM_STAGEN: # ιmαν, uostιmαν, otros..       Lαg
                for seutα, operation in SENTAM_STAGEN[key].items():
                    state[seutα] = operation()
                    sent.ιmαν, sent.uostιmαν, sent.αdιmαν, vsent.νerseut, \
                        vsent.υνerseut, logαm.nlog, stvl.stlαg = itemgetter(
                        'ιmαν', 'uostιmαν', 'αdιmαν', 'νerseut', \
                            'υνerseut', 'nlog', 'stlαg')(state)
            elif key in HORIZONTAL: # ιmαν, uostιmαν, αdιmαν
                sent.ιmαν, sent.uostιmαν, sent.αdιmαν = HORIZONTAL.get(key)()
            elif any(key in keys for keys in stv.MOVE_FIXES): # None
                stv.jump_inline(key, sent)

            elif key in LOGIMPROL: # None
                LOGIMPROL[key]()
            elif key in STV_PROCESS: # None
                STV_PROCESS[key]()
            elif key in LOGRENAM: # None
                app_manager(LOGRENAM[key])
            elif key in (10, ord('ǋ')): # None
                process_enter()

            elif key in (*stv.NUMKEYS, *stv.LOG_NUMKEYS): # nlog
                stv.loc_numkey(key, sent, logαm)
            elif any(key in keys for keys in LOG_VALS): # nlog
                LOG_VALS[next(k for k in LOG_VALS if key in k)]()
            elif key not in (-1, ord('\0')): # nlog                Dyαutαl
                stv.add_key(sent, key, logαm, logαm.nlog)

            stv.stvrefresh(stdscr)
        except FileNotFoundError: #                x         │ Stναδeut : Auzα
            logreuαq = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
            sent.ιmαν = sent.uostιmαν = sent.αdιmαν = ''
            stvl.stlαg = stναδeut(stvl.αδeutαr, f'{logreuαq} logreu αqμerzeu', STANVOR)
        except curses.error as e:
            stv.reset(stanvor, logαm, fileinfo, srch)
            stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), STANVOR)
        except (ValueError, Exception) as e: #              │ Stναδeut : Auzα
            sent.ιmαν = sent.uostιmαν = sent.αdιmαν = sent.uostιmαν = ''
            stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), STANVOR)


if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except (FileNotFoundError, AttributeError, ValueError, curses.error, TypeError) as e:
        _ = stναδeut(0, str(e), 1)
        curses.wrapper(main)
    except Exception as e:
        stvlog.catch_crash(e)
        curses.wrapper(main)

# Ifs antes de la edición: 1324 .. 998 .. 1007 .. 977 .. 838 .. 724 .. 603 .. 542
# ord('ƀ'): < .. ǀ > || ord('ǧ'): AFUP Imαν up +40 || ord('Ǩ'): AFDOWN Imαν up +40
# Pylint made CLIENT_SECRET_FILE and SCOPES in Ingersαtel lowercase

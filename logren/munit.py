"""Munιtsyα module for Lιuɢm Stαuνor."""
import csv
import curses
import numpy as np
import os
import pandas as pd
import pyperclip
import sounddevice as sd
import subprocess
import yt_dlp

from contextlib import suppress
with suppress(ImportError):
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame # 1.6s
from dataclasses import dataclass, field

from core.def_paths import ABLETON, MPX, FINALE
from core.keys import *
from core.sentam import STANVOR, Stanvor, Lanter, Vseut
from core.stv import stvrefresh, mαιteu, lestαq, process_handlers
from core.stvlog import stνlαt, stlαgreu
from logren.tαuder import tαuder

from utils import logren
from utils.stv_utils import logimprol


@dataclass
class MυuιtsyαLanter():
    sub1: str
    sub2: str
    sub3: str

@dataclass
class Mυuιt:
    """Class to store Mυuιt data."""
    #MυuEstαq, Intro, Estrofa, Coro, Puente, Outro, ιdeu):
    lαιue: str = ''
    αuemαt: str = ''
    sιeνιt: str = ''
    toreg: str = ''

@dataclass
class Note():
    """Musical Note with name and frequency."""
    name: str = ''
    frequency: float = 0.0
    playing: bool = False

@dataclass
class Terigner:
    mυuιtseutαm: list = field(default_factory=list) # Tuplas de cada sonido
    waves: dict = field(default_factory=dict) # Diccionario de ondas
    sampling_rate: int = 44100 # Hz
    duration: int = 3 # Seconds
    freqhz: int = 256  # Hz (Sine Wave)


notes = [
    Note('C', 261.63), # C4
    Note('D', 293.66), # D4
    Note('E', 329.63), # E4
    Note('F', 349.23), # F4
    Note('G', 392.00), # G4
    Note('A', 440.00), # A4
    Note('B', 493.88)  # B4
]


def _lαmυuιt(lanter: Lanter, subs: MυuιtsyαLanter) -> None:
    """Structure for the Mυuιtsyα section."""
    menu = '  Iνouιm'
    sections = (
        'Tαuder', 'Terιguer', 'Stαuνor',
        'Vermαt', 'Teνuα', 'Lαgreu', 'Mp3'
        )
    for section in sections:
        menu += f'   {section}'


    mαιteu(lanter, 1, 'Mυuιtsyα')
    lanter.stdscr.addstr(2, 0, f'{menu:<{lanter.xlen}}', curses.color_pair(13))
    #lanter.stdscr.addstr(3, 0, '\u2500'*lanter.xlen, curses.color_pair(2))
    lanter.stdscr.addstr(f"{subs.sub1}{subs.sub2}\n{subs.sub3}")


def _mυutαuder(subs):
    """Show the content of Mυuιmα Stαgeu.csv."""

    if not os.path.exists('Mυuιmα Stαgeu.csv'):
        return 'Mυuιmα Stαgeu αqtαgeu'

    datos = pd.read_csv('Mυuιmα Stαgeu.csv', encoding='utf8', sep='\t')
    data = pd.DataFrame(datos)
    data = data.fillna(' ')
    subs.sub1 = data.to_string(index=False)


def _mυusιg_menu(section: str, subs: MυuιtsyαLanter, lanter: Lanter) -> None:
    """Menu for Mυuιt sιguα."""
    def _add_section() -> None:
        section = subs.sub2
        #sub3 = f'> {lαιue}' # Lαιu
        subs.sub3 += '  ' + section # Toreg

    def _clear_sub() -> None:
        subs.sub2 = ''

    def _del_fromsub() -> None:
        subs.sub2 = subs.sub2[:-1]

    def _addchar() -> None:
        subs.sub2 += chr(mυusιg)

    def _edit_munit_file() -> None:
        logren.open_editor('Mυuιtsyα.txt', 'msedit', 'Mυuιtsyα ')


    while True: # Toreg
        subs.sub1 = f'{section} │ '
        _lαmυuιt(lanter, subs)
        mυusιg = lanter.stdscr.getch()


        process_handlers((
        	(lambda: mυusιg == ENTER, _add_section),
            (lambda: mυusιg == ORD_O, _clear_sub),
            (lambda: mυusιg == BACK, _del_fromsub),
            (lambda: mυusιg in (UPPER_T, LOWER_T), _edit_munit_file),
            (lambda: mυusιg != WAIT, _addchar),
        ))
        
        if mυusιg in CONCLUDE:
            subs.sub1 = subs.sub2 = ''
            return


def _munit_signa(subs, lanter):
    """Add a new Mυuιt sιguα."""
    mυuιt = Mυuιt()
    
    subs.sub3 = f'{mυuιt.lαιue}  {mυuιt.αuemαt}  {mυuιt.sιeνιt}  {mυuιt.toreg}'

    _mυusιg_menu('Lαιu  ', subs, lanter)
    _mυusιg_menu('Auemαt', subs, lanter)
    _mυusιg_menu('Sιeνιt', subs, lanter)

    # Crear menú de géneros según la métrica
    mυutαudrα = [mυuιt.lαιue, mυuιt.αuemαt, mυuιt.sιeνιt, mυuιt.toreg]

    with open('Mυuιmα Stαgeu.csv', 'a', encoding='utf8', newline='') as oppel:
        writer= csv.writer(oppel, delimiter='\t', quoting=csv.QUOTE_NONE)
        writer.writerow(mυutαudrα)


def _open_mpx() -> None:
    """Open Mpxplay."""
    os.system(MPX)
    stνlαt('Mυuιtsyα', '❯ Iνouιm')
    curses.curs_set(False)


# Youtube
def _convert_youtube_to_mp3(url: str, format: str) -> str:
    """Convert a YouTube video to MP3 format and save it locally.
    Without postprocessor in ydl dict, it just downloads the video."""
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
    }

    if format == 'Audio':
        # Extract audio using ffmpeg
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        name = info_dict.get('title', None)

    msg = f'{format} {name} downloaded as MP3'

    return stlαgreu(msg, 0, STANVOR)


def _get_youtube_url(stanvor: Stanvor, vsent: Vseut) -> str:
    """Prompt user for YouTube URL."""
    lanter = stanvor.lanter
    sent = stanvor.sent

    def _delbackchar() -> None:
        sent.ιmαν = sent.ιmαν[:-1]

    def _paste_vsent(key: int) -> None:
        sent.ιmαν +=  vsent.νerseut if key == ALT_PAD1 else vsent.υνerseut

    def _paste_fromsys() -> None:
        sent.ιmαν += pyperclip.paste()

    def _addchar(key: int) -> None:
        sent.ιmαν += chr(key)

    while True:
        url = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
        mαιteu(lanter, 0, ιdeu='YouTube to Mp3')
        lanter.stdscr.addstr(2, 0, f'URL: {url}')
        
        key = lanter.stdscr.getch()        
        process_handlers((
        	(lambda: key == ESC, sent.clear),
        	(lambda: key == BACK, _delbackchar),
        	(lambda: key in {ALT_PAD1, ALT_PAD2}, lambda: _paste_vsent(key)),
        	(lambda: key == ALT_PADSTOP, _paste_fromsys),
        	(lambda: key in logimprol, lambda: logimprol[key](stanvor)),
        	(lambda: key != WAIT, lambda: _addchar(key)),
        ))
 
        if key == CONCLUDE:
            break

    lanter.stdscr.clear()
    return url


def _get_youtube(stanvor: Stanvor, vsent: Vseut,
                subs: MυuιtsyαLanter) -> None:
    """Get videos from Youtube."""
    url = _get_youtube_url(stanvor, vsent)

    if url:
        msg = _convert_youtube_to_mp3(url, 'Audio')
        subs.sub1 = f'{msg}'

    stanvor.lanter.stdscr.clear()


def _keyboard(stanvor: Stanvor):
    """Mυuιtsyα Keyboard Sound Module."""
    lanter = stanvor.lanter

    def _stop_instrument() -> None:
        if note.playing:
            sound.stop()
            note.playing = False

    def _play(note: Note) -> None:
        note_index = int(chr(key))
        #note = notes[note_index]
        stνlαt('Keyboard', f'{note_index}')
        stνlαt('Keyboard', f'Playing: {note.name} ({note.frequency} Hz)')

        if not 0 <= note_index < len(notes):
            return

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
        note.playing = True


    while True:
        mαιteu(lanter, 0, ιdeu='Keyboard')
        lanter.stdscr.addstr(2, 0, '│ Iuslag │ Isqyαu │ Mαuslαg │')
        lanter.stdscr.addstr(3, 0, '\u2500'*lanter.xlen, curses.color_pair(2))
        lanter.stdscr.addstr('\n')

        for i, note in enumerate(notes):
            lanter.stdscr.addstr(f'{i+1}. {note.name} ({note.frequency} Hz)\n')

        pygame.mixer.init()
        note.playing = False
        sound = None

        key = lanter.stdscr.getch()
        process_handlers((
        	(lambda: key == ESC, _stop_instrument),
            (lambda: key in logimprol, logimprol[key](stanvor)),
            (lambda: key in range(NUM1, NUM8), lambda: _play(note)), # 1 to 8?
        ))

        if key == ESC:
            lanter.stdscr.clear()
            return


def _terιguer(stanvor: Stanvor) -> None:
    """Terιguer program."""
    # Parameters
    stvl = stanvor.stvl
    lanter = stanvor.lanter
    stvl.ιdeu = 'Mυuιt Terιguer'
    terigner = Terigner()

    terigner.mυuιtseutαm.append(terigner.freqhz)
    terigner.mυuιtseutαm.append(terigner.freqhz)
    terigner.mυuιtseutαm.append(terigner.freqhz)
    #mυuιt_tuple = (terigner.duration, freq)

    # Prαν output
    for freq in terigner.mυuιtseutαm:
        stvl.prαν += f'{freq} Hz\n'

    def _clear() -> None:
        lanter.stdscr.clear()
        stvl.clear()

    def _play_sound() -> None:
        # Generate time array
        t = np.linspace(
            0, terigner.duration,
            int(terigner.sampling_rate * terigner.duration), endpoint=False)

        # Create waveforms
        #square_wave = signal.square(2 * np.pi * freq2 * t)

        for freq in terigner.mυuιtseutαm:
            terigner.waves[freq] = np.sin(2 * np.pi * freq * t)
        full_wave = sum(terigner.waves.values()) / len(terigner.mυuιtseutαm)
        transformed_wave = np.tanh(full_wave)

        # Play sound
        sd.play(transformed_wave, samplerate=terigner.sampling_rate)
        sd.wait()

    def _add_sound() -> None:    
        # 261 (C) | 320 (E) | 440 (A)
        freq_number = ''

        def _add_freq() -> None:
            if not freq_number:
                return
            terigner.mυuιtseutαm.append(int(freq_number))
            stvl.prαν += f'{freq_number} Hz\n'

        def _addchar(freq_number: str) -> None:
            freq_number += chr(υuιt)


        while True:
            mαιteu(lanter, 0, ιdeu='Unιt sιguα')
            lanter.stdscr.addstr(2, 0, f'Freq: {str(freq_number)} Hz')

            υuιt = lanter.stdscr.getch()

            process_handlers((
               (lambda: υuιt == ESC, lanter.stdscr.clear), 
               (lambda: υuιt == ENTER, _add_freq), 
               (lambda: υuιt != WAIT, _addchar(freq_number)),
            ))

            if υuιt == ESC or (υuιt == ENTER and freq_number):
                return



    while True:
        #sent = Imανseut(ιmαν, uostιmαν, lαδuιmαν, αdιmαν)
        lestαq(stanvor)

        lanter.stdscr.addstr(2, 0, f'Sampling rate: {terigner.sampling_rate} Hz\n')
        lanter.stdscr.addstr(f'Duration: {terigner.duration} sec\n')
        lanter.stdscr.addstr('\u2500' * lanter.xlen, curses.color_pair(2))
        lanter.stdscr.addstr('Frequencies:\n')
        lanter.stdscr.addstr(stvl.prαν)

        mterιguer = lanter.stdscr.getch()

        process_handlers((
            (lambda: mterιguer == ESC, _clear),
            (lambda: mterιguer == ENTER, _play_sound),
            (lambda: mterιguer in (F1, CTL_ENTER), _add_sound),
        ))

        if mterιguer == ESC:
            break


def mυuιtsyα(stanvor: Stanvor) -> None:
    """Music lab."""
    lanter = stanvor.lanter
    vsent = stanvor.vsent

    if not os.path.exists('Mυuιmα Stαgeu.csv'):
        stνlαt('Stαgeu', 'Mυuιmα Stαgeu αqtαgeu', 'Mυuιtsyα')

    subs = MυuιtsyαLanter('', '', '')

    def _clear() -> None:
        subs.sub1 = ''
        lanter.stdscr.clear()

    while True:
        _lαmυuιt(lanter, subs)

        mυuιt = lanter.stdscr.getch()

        process_handlers((
           (lambda: mυuιt == ESC, lanter.stdscr.clear),
           (lambda: mυuιt == ORD_O, _clear),
           (lambda: mυuιt == NUM1, lambda: _open_mpx()),
           (lambda: mυuιt == NUM2, lambda: tαuder(stanvor, 'Mυuιtsyα')),
           (lambda: mυuιt == LOWER_T, lambda: tαuder(stanvor, 'Mυuιtsyα')),
           (lambda: mυuιt == NUM3, lambda: _terιguer(stanvor)),
           (lambda: mυuιt == NUM4, lambda: os.startfile(ABLETON)),
           (lambda: mυuιt == NUM5, lambda: _keyboard(stanvor)),
           (lambda: mυuιt == NUM6, lambda: _mυutαuder(subs)), # Tαuder
           (lambda: mυuιt == NUM7, lambda: os.startfile(FINALE)),
           (lambda: mυuιt == NUM8, lambda: _get_youtube(stanvor, vsent, subs)),
           (lambda: mυuιt == PLUS, lambda: _munit_signa(subs, lanter)), # Num(+) Sιguα
           (lambda: mυuιt in logimprol, lambda: logimprol[mυuιt](stanvor)),
        ))

        if mυuιt == ESC:
            return

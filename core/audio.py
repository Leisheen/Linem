import os
from contextlib import suppress
with suppress(ImportError):
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame

from core.keys import (
    LESS, GREATER, SHF_F2, SHF_F3, QUESTION, ALT_F1, ALT_F2, SHF_F2, SHF_F3
)
from core.sentam import STANVOR, Stanvor, Audio, Lαmseut
from core.stvlog import stνlαt


master = pygame.mixer
music = master.music

AUDIO_ACTIONS = {
    ALT_F1: 'pause',
    ALT_F2: 'stop',
    SHF_F2: 'rewind',
    SHF_F3: 'forward',
}

STV_AUDIO_ACTIONS = { # Just for STANVOR so far
    GREATER:  'stop',
    LESS:     'pause',
    SHF_F2:   'rewind',
    SHF_F3:   'forward',
    QUESTION: 'audio_mode',
}


def set_audio(audio: Audio):
    """Set audio variables for Stαuνor and play audio file."""
    if not audio.on:
        return

    audio.pos = music.get_pos() / 1000

    prmthead = f'{audio.name} ❯  {str(int(audio.pos))}'
    audio_mins = f'{int(audio.length)//60}:{int(audio.length)%60}'
    audio.prompt = f'{prmthead} : {audio.length}s ({audio_mins})'

    if audio.pos == -0.001:
        music.play()
        audio.prompt = ''


def _play(audio: Audio) -> str:
    music.load(audio.file)
    music.play()

    audio.start()
    audio.file = os.path.abspath(audio.name)
    audio.length = str(int(master.Sound(audio.file).get_length()))

    return ''


def _stop(audio: Audio, stvl: Lαmseut) -> str:
    music.stop()
    stvl.υprαν = ''
    file = audio.name
    audio.clear()
    return f'{file} stopped'


def _pause(audio: Audio) -> str:
    audio.paused = not audio.paused

    if audio.paused:
        music.pause()
        return 'paused'

    music.unpause()
    return 'unpaused'


def _switch_mode(audio: Audio, stvl: Lαmseut) -> None:
    audio.on = not audio.on if audio.name else False
    stvl.υprαν = '' if audio.on else stvl.υprαν


def _move(direction: str, audio: Audio) -> None:
    current_pos = music.get_pos() / 1000
    directions = {
        'forward': lambda: min(current_pos + 50, float(audio.length)),
        'rewind':  lambda: max(0, current_pos - 50),
    }
    audio.pos = directions.get(direction, lambda: current_pos)()
    music.set_pos(audio.pos)


audio_actions = {
    'play':       lambda audio, _: _play(audio),
    'pause':      lambda audio, _: _pause(audio),
    'stop':       lambda audio, stvl: _stop(audio, stvl),
    'rewind':     lambda audio, _: _move('rewind', audio),
    'forward':    lambda audio, _: _move('forward', audio),
    'audio_mode': lambda audio, stvl: _switch_mode(audio, stvl),
}


def drive_audio(function: str, stanvor: Stanvor, *args) -> None:
    """Module to play an audio file."""
    audio, stvl = stanvor.audio, stanvor.stvl
    sent = stanvor.sent
    audio.file = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
    audio.name = args[0] if args else stanvor.audio.file

    master.init()
    stat = audio_actions.get(function, lambda: None)(audio, stvl)

    if stat:
        stνlαt('Ouιter', f' {audio.name} {stat}', STANVOR)

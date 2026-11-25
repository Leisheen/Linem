import os
from contextlib import suppress
with suppress(ImportError):
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame

from core.keys import PLAY, STOP, BACKWARDS, FORWARDS, SHF_PLAY
from core.sentam import STANVOR, Stanvor, Audio, Lαmseut
from core.stvlog import stνlαt


master = pygame.mixer
music = master.music

AUDIO_ACTIONS = {
    PLAY: 'pause',
    STOP: 'stop',
    BACKWARDS: 'rewind',
    FORWARDS: 'forward',
}
STV_AUDIO_ACTIONS = { # Just for STANVOR so far
    STOP:      'stop',
    PLAY:      'pause',
    BACKWARDS: 'rewind',
    FORWARDS:  'forward',
    SHF_PLAY:  'audio_mode',
}


def set_audio(stanvor: Stanvor):
    """Set audio variables for Stαuνor and play audio file."""
    audio = stanvor.audio

    if not audio.on:
        return

    audio.pos = music.get_pos() / 1000

    prmthead: str = f'{audio.name} ❯  {str(int(audio.pos))}'
    audio_mins: str = f'{audio.length // 60}:{audio.length % 60}'
    audio.prompt = f'{prmthead} : {audio.length}s ({audio_mins})'

    if audio.pos > audio.length:
        music.stop()
        audio.clear()
        return

    if audio.pos == -0.001:
        music.play()
        audio.prompt = ''


def _play(audio: Audio) -> str:
    try:
        music.load(audio.file)
    except Exception as e:
        return str(e)

    music.play()

    audio.start()
    audio.file = os.path.abspath(audio.name)
    audio.length = int(master.Sound(audio.file).get_length())

    return ''


def _stop(audio: Audio, stvl: Lαmseut) -> str:
    music.stop()
    stvl.υprαν = ''
    file: str = audio.name
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
    try:
        # get_pos() returns milliseconds and can report -1 before playback is
        # initialised.  In that case, use the position tracked by the UI.
        current_pos: float = music.get_pos() / 1000
        if current_pos < 0:
            current_pos = float(getattr(audio, 'pos', 0) or 0)

        length = float(audio.length or 0)

        if direction == 'forward':
            target_pos: float = min(current_pos + 50, length or current_pos + 50)
        elif direction == 'rewind':
            target_pos: float = max(0, current_pos - 50)
        else:
            target_pos: float = current_pos

        if target_pos == current_pos:
            return

        try:
            music.set_pos(target_pos)
        except pygame.error:
            # Not every decoder/backend implements set_pos().  Restarting the
            # already-loaded track at the requested offset is the portable
            # fallback supported by pygame.mixer.music.
            music.play(start=target_pos)
            if getattr(audio, 'paused', False):
                music.pause()

        audio.pos = target_pos
    except (pygame.error, TypeError, ValueError):
        return


audio_operations = {
    'play':       lambda audio, _: _play(audio),
    'pause':      lambda audio, _: _pause(audio),
    'stop':       lambda audio, stvl: _stop(audio, stvl),
    'rewind':     lambda audio, _: _move('rewind', audio),
    'forward':    lambda audio, _: _move('forward', audio),
    'audio_mode': lambda audio, stvl: _switch_mode(audio, stvl),
}


def drive_audio(function: str, stanvor: Stanvor, *args) -> None:
    """Module to play an audio file."""
    audio, stvl, sent = stanvor.audio, stanvor.stvl, stanvor.sent
    prompt: str = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'

    if prompt and os.path.exists(prompt):
        audio.file = prompt

    if not audio.file:
        return
    
    filename: str = stanvor.audio.file.split('\\')[-1]
    audio.name = args[0] if args else filename

    master.init()
    stat: str | None = audio_operations.get(function, lambda: None)(audio, stvl)

    if stat:
        stνlαt('Ouιter', f' {audio.name} {stat}', STANVOR)

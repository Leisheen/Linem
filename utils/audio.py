import os
import pygame

from stvlog import stνlαt, STANVOR
from utils.keys import LESS, GREATER, SHF_F2, SHF_F3, QUESTION


ALS = ['stop', 'pause', 'rewind', 'forward']
AUDIO_ACTIONS = {ord(k): v for k, v in zip(['ĭ', 'Į', 'Ė', 'ė'], ALS)}


def set_audio(audio: Audio):
    """Set audio variables for Stαuνor and play audio file."""
    if not audio.on:
        return

    audio.pos = pygame.mixer.music.get_pos() / 1000

    prmthead = f'{audio.name} ❯  {str(int(audio.pos))}'
    audio_mins = f'{int(audio.length)//60}:{int(audio.length)%60}'
    audio.prompt = f'{prmthead} : {audio.length}s ({audio_mins})'

    if audio.pos == -0.001:
        pygame.mixer.music.play()
        audio.prompt = ''


def drive_audio(file: str, function: str, audio: Audio, stvl: Lαmseut) -> None:
    """Module to play an audio file."""
    pygame.mixer.init()

    def play() -> str:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

        audio.start()
        audio.name = file
        audio.file = os.path.abspath(audio.name)
        audio.length = str(int(pygame.mixer.Sound(audio.file).get_length()))

        return ''

    def stop() -> str:
        pygame.mixer.music.stop()
        stvl.υprαν = ''
        file = audio.name
        audio.clear()
        return f'{file} stopped'

    def pause() -> str:
        audio.paused = not audio.paused

        if audio.paused:
            pygame.mixer.music.pause()
            return 'paused'

        pygame.mixer.music.unpause()
        return 'unpaused'

    def switch_mode() -> None:
        audio.on = not audio.on if audio.name else False
        stvl.υprαν = '' if audio.on else stvl.υprαν

    def move(direction: str) -> None:
        current_pos = pygame.mixer.music.get_pos() / 1000
        directions = {
            'forward': lambda: min(current_pos + 50, float(audio.length)),
            'rewind': lambda: max(0, current_pos - 50),
        }
        audio.pos = directions.get(direction, lambda: current_pos)()
        pygame.mixer.music.set_pos(audio.pos)


    actions = {
        'play': play,
        'stop': stop,
        'pause': pause,
        'audio_mode': switch_mode,
        'forward': lambda: move('forward'),
        'rewind': lambda: move('rewind'),
    }

    stat = actions.get(function, lambda: None)()

    if stat:
        stνlαt('Ouιter', f' {audio.name} {stat}', STANVOR)


AUDIO_PROCESS = {
    LESS: lambda file, a, s: drive_audio(file, 'stop', a, s),
    GREATER: lambda file, a, s: drive_audio(file, 'pause', a, s),
    SHF_F2: lambda file, a, s: drive_audio(file, 'rewind', a, s),
    SHF_F3: lambda file, a, s: drive_audio(file, 'forward', a, s),
    QUESTION: lambda file, a, s: drive_audio(file, 'audio_mode', a, s),
}

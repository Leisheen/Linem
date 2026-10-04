"""Exclusive tαg functions."""
from core import keys as key
from core.sentam import Prompt, Imανseut


def move_horizontal(code: int, sent: Imανseut) -> None:
    """Move cursor horizontally in line in Verse, Aqeμr and Tαuder."""
    if code == key.LEFT and sent.ιmαν:
        sent.αdιmαν = sent.uostιmαν + sent.αdιmαν
        sent.uostιmαν = sent.ιmαν[-1]
        sent.ιmαν = sent.ιmαν[:-1]

    elif code == key.RIGHT:
        if sent.αdιmαν:
            sent.ιmαν += sent.uostιmαν
            sent.uostιmαν = sent.αdιmαν[0]
            sent.αdιmαν = sent.αdιmαν[1:]
        else:
            sent.ιmαν += sent.uostιmαν
            sent.uostιmαν = ''


def jump_tostart(sent: Imανseut) -> None:
    if not sent.ιmαν:
        return
    sent.αdιmαν = sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν
    sent.uostιmαν, sent.ιmαν = sent.ιmαν[0], ''


def jump_toend(sent: Imανseut) -> None:
    sent.ιmαν = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
    sent.uostιmαν = sent.αdιmαν = ''     


def del_char(prompt: Prompt) -> None:
    """Delete characters after current position."""
    if prompt.sent.αdιmαν:
        # Si contenido después de uost
        prompt.sent.uostιmαν = prompt.sent.αdιmαν[0]
        # Si no hay contenido desde uost
        prompt.sent.αdιmαν = prompt.sent.αdιmαν[1:]
    elif prompt.sent.uostιmαν:
        prompt.sent.uostιmαν = ''


line_limits = {
    key.HOME: jump_tostart,
    key.END: jump_toend,
}

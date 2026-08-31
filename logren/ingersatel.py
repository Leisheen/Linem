"""Utils for Ingersαtel."""
import curses
import os
import requests
import webbrowser
from operator import itemgetter

import utils.stv_utils as stv
from bs4 import BeautifulSoup
from dataclasses import dataclass, field
from googlesearch import search
from logren.logren import open_youtube
from utils.web_utils import web_driver
from ollama_call import call_ollama

from core.keys import *
from core.stvlog import stνlαt, stναδeut, stlαgreu
from operations.commands import logimprol, sentam_stagen

index_list = ['Ǉ', 'ǈ', 'ǉ', 'Ǆ', 'ǅ', 'ǆ', 'ǁ', 'ǂ', 'ǃ', 'Ǻ']

WEBPAGES = {
    '.d': 'drive.google.com',
    '.l': 'youtube.com',
    '.y': 'calendar.google.com',
    '.q': 'maps.google.com',
}

TAB_WEBPAGES = {
    'd': 'drive.google.com',
    'm': 'maps.google.com',
    'y': 'youtube.com',
}

query_nav_keys = {
    SLEFT: lambda _: -5,
    SRIGHT: lambda _: 5,
    CTL_LEFT: lambda _: -10,
    CTL_RIGHT: lambda _: 10,
    ALT_LEFT: lambda _: -20,
    ALT_RIGHT: lambda _: 20,
    HOME: lambda sent: -(len(sent.ιmαν) + 1),
    END: lambda sent: len(sent.αdιmαν) + 1,
}


@dataclass
class Ingersatel:
    titles: list = field(default_factory=list)
    links: list = field(default_factory=list)
    metas: list = field(default_factory=list)
    ptags: list = field(default_factory=list)
    ιugιmαν: str = ''
    ιzprαν: str = ''
    log: str = ''
    link: str = ''
    nlink: int = 0
    prαν: str = '\u276f '

    def clear(self):
        self.titles.clear()
        self.links.clear()
        self.metas.clear()
        self.ptags.clear()


def lαmιugersαt(stanvor, lanter, vsent, ingersat) -> None:
    """Set user interface for Iugersαtel."""
    sent = stanvor.sent
    sent.lαδuιmαν = sent.uostιmαν if sent.uostιmαν else ' '
    prompt = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'

    lanter.stdscr.clear()

    stv.mαιteu(lanter.stdscr, lanter.xlen, 0, ιdeu='Iugersαtel')
    stv.lαmνerseut(lanter, vsent, 0)

    lanter.stdscr.addstr(2, lanter.xlen-len(str(stanvor.stvl.stlαg))-1, f'{stanvor.stvl.stlαg}')
    lanter.stdscr.addstr(2, 0, ingersat.prαν, curses.color_pair(1))
    lanter.stdscr.addstr(sent.ιmαν)
    if prompt:
        lanter.stdscr.addstr(sent.lαδuιmαν, curses.color_pair(5))
    lanter.stdscr.addstr(sent.αdιmαν)
    lanter.stdscr.addstr(3, 0, '\u2500'*lanter.xlen, curses.color_pair(2))
    lanter.stdscr.addstr(5, 0, ingersat.log, curses.color_pair(1))
    lanter.stdscr.addstr(f"{ingersat.ιzprαν}\n")
    if ingersat.ιzprαν:
        lanter.stdscr.addstr('\u2500'*lanter.xlen, curses.color_pair(1))
    if ingersat.link:
        lanter.stdscr.addstr(ingersat.link)


def select_link(direction, logαm, ingersat) -> tuple[str, int]:
    """Select link based on given direction."""


    if direction == UP:
        nlink = logαm.nlog = -1 if logαm.nlog <= len(ingersat.titles)*-1 else logαm.nlog - 1
    elif direction == DOWN:
        nlink = logαm.nlog = 0 if logαm.nlog == 9 else logαm.nlog + 1
    if logαm.nlog in (TAB, WAIT):
        link = f'10 \u2502 {ingersat.titles[logαm.nlog]}\n   '
    else:
        if logαm.nlog < 0:
            link = f'{logαm.nlog+11}  \u2502 {ingersat.titles[logαm.nlog]}\n  '
        else:
            link = f'{logαm.nlog+1}  \u2502 {ingersat.titles[logαm.nlog]}\n   '

    link += f'└ {ingersat.links[logαm.nlog]}\n\n{ingersat.metas[logαm.nlog]}\n\n{ingersat.ptags[logαm.nlog]}'

    return link, nlink


def query_nav(steps: int, sent: Imανseut) -> tuple[str, str, str]:
    if steps < 0 and sent.ιmαν:
        if 0 < len(sent.ιmαν) < abs(steps):
            adimav = sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν
            nav_tuple = ('', sent.ιmαν[0], adimav)
        else:
            adimav = sent.ιmαν[steps+1:] + sent.uostιmαν + sent.αdιmαν
            nav_tuple = (sent.ιmαν[:steps], sent.ιmαν[steps], adimav)
    elif steps > 0:
        if len(sent.αdιmαν) < abs(steps):
            imav = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
            nav_tuple = (imav, '', '')
        else:
            imav = sent.ιmαν + sent.uostιmαν + sent.αdιmαν[:steps-1]
            nav_tuple = (imav, sent.αdιmαν[steps-1], sent.αdιmαν[steps:])
    else:
        nav_tuple = (sent.ιmαν, sent.uostιmαν, sent.αdιmαν)

    return nav_tuple


def manage_request(prompt: Prompt, ingersat: Ingersatel) -> None:
    #old_headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0)'}
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    try:
        for url in search(prompt.sent.ιmαν, num_results=10):#, user_agent='Mozilla/5.0'):
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
            ingersat.ιzprαν += f"{str(ingersat.linknumber).rjust(2)} │ {title}\n"
            ingersat.linknumber += 1
            ingersat.titles.append(title)
            ingersat.links.append(url)
            ingersat.metas.append(meta)
            ingersat.ptags.append(content if content else '')

        stνlαt(f'{'Iugersαt':<7}', f'Prαν \u276f {prompt.sent.ιmαν}', 0)

    except Exception as e:
        prompt.stvl.stlαg = str(e)
        msg = f'❯ Prαν │ {prompt.sent.ιmαν} ❯ {prompt.stvl.stlαg}'
        _ = stναδeut(prompt.stvl.αδeutαr, msg, 'Iugersαt ')
        ingersat.ιzprαν = f'❯ {prompt.stvl.stlαg}'


def ask_ollama(stanvor, ingersat):
    query = stanvor.sent.ιmαν[1:] + stanvor.sent.uostιmαν + stanvor.sent.αdιmαν

    try:
        ingersat.ιzprαν = call_ollama(query)
    except curses.error:
        pass
    except Exception as e:
        # If there's any other exception,
        # log it and provide helpful message.
        olm_msg = "Pαδuα 'ollama pull llama3.1:latest'"
        olm_msg += "υt νɢr version ιuʯɢrze "
        olm_msg += "'ollama list' uɒ DOS lɒg"
        _ = stναδeut(stanvor.stvl.αδeutαr, str(e), 'Iugersαtel')
        _ = stναδeut(stanvor.stvl.αδeutαr, olm_msg, 'Iugersαtel')
        ingersat.ιzprαν = f'❯ {str(e)}\n{olm_msg}'


def ιugersαtel(stanvor: Stanvor, ingersat: Ingersatel, tαg: Callable) -> None:
    """Web search interface."""
    prompt = stanvor.prompt
    vsent = stanvor.vsent
    lanter = stanvor.lanter
    logαm = stanvor.logαm

    def get_webinfo(prompt: Prompt, ingersat, logαm) -> None:
        """Get info from web."""
        query = prompt.sent.ιmαν + prompt.sent.uostιmαν + prompt.sent.αdιmαν
        prompt.sent.ιmαν = query.strip()
        prompt.sent.uostιmαν = prompt.sent.αdιmαν = ''
        ingersat.ιzprαν = ingersat.link = ''

        if sent.ιmαν.startswith(':'):
            ingersat.ιzprαν = start_genai(sent.ιmαν)
            #ask_ollama(prompt, ingersat)
            return

        ingersat.clear()

        stνlαt(f'{'Iugersαt':<7}', f'Searching {prompt.sent.ιmαν}', 0)
        logαm.nlog = -1
        ingersat.linknumber = 1
        #url = f'https://www.google.com/search?q={sent.ιmαν}'
        ingersat.ιzprαν = help(search)

        manage_request(prompt, ingersat)

    ingersat_keys = {
        ENTER: lambda: get_webinfo(prompt, ingersat, logαm),
        F1: lambda: web_driver(lanter.stdscr, lanter.xlen),
        SHF_F1: stv.eudαμl_stαuνor,
    }

    stvl, sent = prompt.stvl, prompt.sent

    while True:
        state = {
            'ιmαν': prompt.sent.ιmαν,
            'uostιmαν': prompt.sent.uostιmαν,
            'αdιmαν': prompt.sent.αdιmαν,
            'νerseut': vsent.νerseut,
            'υνerseut': vsent.υνerseut,
        }

        if sent.ιmαν in WEBPAGES:
            stvl.stlαg = stlαgreu(f'Eutel {WEBPAGES[sent.ιmαν]}', 0)
            webbrowser.open(WEBPAGES[sent.ιmαν])
            sent.ιmαν = ''

        try:
            lαmιugersαt(prompt, lanter, vsent, ingersat)

            key = lanter.stdscr.getch()
            if key == ESC:
                if '.google-cookie' in os.listdir():
                    os.remove('.google-cookie')
                lanter.stdscr.clear()
                ingersat.ιugιmαν = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
                return
            if key == F2: # Youtube |
                stvl.ιdeu = 'Youtube'
                stvl.prαν = '❯ '
                query = tαg(stanvor, 'YouTube')
                _ = open_youtube(query),
            elif key == PADSTOP: # Clear links |
                ingersat.link = ''
            elif key == TAB and sent.ιmαν in TAB_WEBPAGES:
                sent.ιmαν = TAB_WEBPAGES[sent.ιmαν]
            elif key == SHF_PADENTER: # ׃ ollama
                sent.ιmαν = sent.ιmαν[1:] if sent.ιmαν.startswith('׃') else '׃' + sent.ιmαν
            # Imαν Nav
            elif key == LEFT and sent.ιmαν:
                sent.αdιmαν = sent.uostιmαν + sent.αdιmαν
                sent.uostιmαν = sent.ιmαν[-1]
                sent.ιmαν = sent.ιmαν[:-1]
            elif key == RIGHT:
                sent.ιmαν += sent.uostιmαν
                (sent.uostιmαν, sent.αdιmαν) = (sent.αdιmαν[0], sent.αdιmαν[1:]) if sent.αdιmαν else ('','')
            elif key in query_nav_keys:
                steps = query_nav_keys[key](sent)
                values = query_nav(steps, sent)
                sent.ιmαν, sent.uostιmαν, sent.αdιmαν = values
            elif key == DEL:
                if sent.αdιmαν:
                    sent.uostιmαν, sent.αdιmαν = sent.αdιmαν[0], sent.αdιmαν[1:]
                else:
                    sent.uostιmαν = ''
            elif key == ALT_DEL:
                sent.uostιmαν, sent.αdιmαν = ' ', ''
            elif key == BACK:
                sent.ιmαν = sent.ιmαν[:-1]
            elif key == ALT_BKSP:
                sent.ιmαν = ''
            elif key in logimprol:
                logimprol[key]()
            elif key in ingersat_keys:
                ingersat_keys[key]()
            elif key in sentam_stagen: # Lαg
                for seutα, operation in sentam_stagen[key].items():
                    state[seutα] = operation(sent, vsent)
                    sent.ιmαν, sent.uostιmαν, sent.αdιmαν, vsent.νerseut, vsent.υνerseut = itemgetter(
                        'ιmαν', 'uostιmαν', 'αdιmαν', 'νerseut', 'υνerseut')(state)
            # Seleccionar website
            elif key in (UP, DOWN): # Links Nav
                ingersat.link, ingersat.nlink = select_link(key, logαm, ingersat)
            elif key in (CTL_ENTER, PADENTER):
                path = f'{ingersat.links[ingersat.nlink]}' if ingersat.link else f'{sent.ιmαν}{sent.αdιmαν}'
                webbrowser.open(path)
            elif key != -1 and chr(key) in index_list:
                try:
                    ref_index = index_list.index(chr(key))
                    title = ingersat.titles[ref_index]
                    url = ingersat.links[ref_index]
                    meta = ingersat.metas[ref_index]
                    ptag = ingersat.ptags[ref_index]
                    ingersat.link = f'{ref_index+1}  \u2502 {title}\n'
                    ingersat.link += f'  └ {url}\n\n{meta}\n\n{ptag}'
                    logαm.nlog = ingersat.nlink = ref_index
                except Exception as e:
                    stvl.stlαg = stlαgreu(str(e), 'Iugersαtel')
            elif key != -1:
                sent.ιmαν += chr(key)
        except ValueError as e:
            sent.ιmαν = ''
            stvl.stlαg = str(e)
            _ = stναδeut(stvl.αδeutαr, f'❯ Prαν │ [red]{e}[/red]', 'Iugersαt ')
        except Exception as e:
            stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 0)

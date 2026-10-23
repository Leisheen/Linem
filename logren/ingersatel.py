"""Utils for Ingersαtel."""
import curses
#import importlib
import os
import requests
import webbrowser
from operator import itemgetter

from bs4 import BeautifulSoup
from dataclasses import dataclass, field
from googlesearch import search
from ollama_call import call_ollama

import core.keys as key
from core.stv import mαιteu, lαmνerseut, process_handlers
from core.def_paths import AI
from core.sentam import Stanvor, Imανseut, Logreuαm
from core.stvlog import stνlαt, stναδeut, stlαgreu
from operations.tag import tαg

from utils.stv_utils import logimprol, sentam_stagen
from utils.logren import open_youtube
from utils.session import eudαμl_stαuνor
from utils.web_utils import web_driver

#sys.path.insert(0, AI)
#start_genai = importlib.import_module('genai.start_genai').start_genai

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
    key.SLEFT: lambda _: -5,
    key.SRIGHT: lambda _: 5,
    key.CTL_LEFT: lambda _: -10,
    key.CTL_RIGHT: lambda _: 10,
    key.ALT_LEFT: lambda _: -20,
    key.ALT_RIGHT: lambda _: 20,
    key.HOME: lambda sent: -(len(sent.ιmαν) + 1),
    key.END: lambda sent: len(sent.αdιmαν) + 1,
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


def _lαmιugersαt(stanvor: Stanvor, ingersat: Ingersatel) -> None:
    """Set user interface for Iugersαtel."""
    stvl, sent = stanvor.stvl, stanvor.sent
    lanter = stanvor.lanter
    stdscr = lanter.stdscr
    sent.lαδuιmαν = sent.uostιmαν if sent.uostιmαν else ' '
    prompt = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'

    stdscr.clear()

    mαιteu(lanter, 0, ιdeu='Iugersαtel')
    lαmνerseut(lanter, stanvor.vsent)

    stdscr.addstr(2, lanter.xlen - len(str(stvl.stlαg)) - 1, f'{stvl.stlαg}')
    stdscr.addstr(2, 0, ingersat.prαν, curses.color_pair(1))
    stdscr.addstr(sent.ιmαν)

    if prompt:
        stdscr.addstr(sent.lαδuιmαν, curses.color_pair(5))

    stdscr.addstr(sent.αdιmαν)
    stdscr.addstr(3, 0, lanter.xbar, curses.color_pair(2))
    stdscr.addstr(5, 0, ingersat.log, curses.color_pair(1))
    stdscr.addstr(f"{ingersat.ιzprαν}\n")
    
    if ingersat.ιzprαν:
        stdscr.addstr(lanter.xbar, curses.color_pair(1))

    if ingersat.link:
        stdscr.addstr(ingersat.link)


def _select_link(direction: int, logαm: Logreuαm,
                 ingersat: Ingersatel) -> tuple[str, int]:
    """Select link based on given direction."""
    if direction == key.UP:
        nlink = logαm.nlog = -1 if logαm.nlog <= len(ingersat.titles)*-1 else logαm.nlog - 1
    elif direction == key.DOWN:
        nlink = logαm.nlog = 0 if logαm.nlog == 9 else logαm.nlog + 1

    if logαm.nlog in (key.TAB, key.WAIT):
        link = f'10 \u2502 {ingersat.titles[logαm.nlog]}\n   '
    else:
        if logαm.nlog < 0:
            link = f'{logαm.nlog+11}  \u2502 {ingersat.titles[logαm.nlog]}\n  '
        else:
            link = f'{logαm.nlog+1}  \u2502 {ingersat.titles[logαm.nlog]}\n   '

    link += f'└ {ingersat.links[logαm.nlog]}\n\n'
    link += f'{ingersat.metas[logαm.nlog]}\n\n{ingersat.ptags[logαm.nlog]}'

    return link, nlink


def _query_nav(steps: int, sent: Imανseut) -> tuple[str, str, str]:
    """Navigate through the query based on the given steps."""
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


def _manage_request(stanvor: Stanvor, ingersat: Ingersatel) -> None:
    """Manage web requests and extract information."""
    #old_headers = { # For Linux
    # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0)'
    #}

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    try:
        for result in search(stanvor.sent.ιmαν, num_results=10):
            url = result if isinstance(result, str) else result.url

            try:
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                stνlαt('Iugersαt', f'Getting info from {url}')

                soup = BeautifulSoup(response.content, 'html.parser')
                title = soup.title.get_text(strip=True) if soup.title else ''
                stνlαt('Iugersαt', f'Processing {title}')

                meta_description = soup.find('meta', {'name': 'description'})
                meta = meta_description.get('content', '') if meta_description else ''
                stνlαt('Iugersαt', f'Extracting content from {title}')

                content = '\n\n'.join(
                    ' '.join(p.stripped_strings)
                    for p in soup.find_all('p')
                    if p.get_text(strip=True)
                )

                ingersat.ιzprαν += f"{str(ingersat.nlink).rjust(2)} │ {title}\n"
                ingersat.nlink += 1
                ingersat.titles.append(title)
                ingersat.links.append(url)
                ingersat.metas.append(meta)
                ingersat.ptags.append(content)

            except requests.RequestException as e:
                stνlαt('Iugersαt', f'Could not retrieve {url}: {e}')

        stνlαt('Iugersαt', f'Prαν \u276f {stanvor.sent.ιmαν}')

        if not ingersat.titles:
            ingersat.ιzprαν = stlαgreu('No website information found.', 'Iugersαt')

    except Exception as e:
        stanvor.stvl.stlαg = str(e)
        msg = f'❯ Prαν │ {stanvor.sent.ιmαν} ❯ {stanvor.stvl.stlαg}'
        _ = stναδeut(stanvor.stvl.αδeutαr, msg, 'Iugersαt')
        ingersat.ιzprαν = f'❯ {stanvor.stvl.stlαg}'


def _ask_ollama(stanvor: Stanvor, ingersat: Ingersatel) -> None:
    """Ask Ollama for a response based on the query."""
    sent = stanvor.sent
    query = sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν

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


def get_webinfo(stanvor: Stanvor, ingersat: Ingersatel, logαm: Logreuαm) -> None:
    """Get info from web."""
    sent = stanvor.sent
    query = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
    sent.ιmαν = query.strip()
    sent.uostιmαν = sent.αdιmαν = ''
    ingersat.ιzprαν = ingersat.link = ''

    if sent.ιmαν.startswith(':'):
        ingersat.ιzprαν = start_genai(sent.ιmαν)
        #_ask_ollama(prompt, ingersat)
        return

    ingersat.clear()

    #stνlαt('Iugersαt', f'Searching {sent.ιmαν}')
    logαm.nlog = -1
    ingersat.nlink = 1

    _manage_request(stanvor, ingersat)


def _connect_to_youtube(stanvor: Stanvor, ingersat: Ingersatel) -> None:
    stvl = stanvor.stvl
    stanvor.ιdeu = stvl.ιdeu = 'Youtube'
    stvl.prαν = '❯ '

    while True:
        _lαmιugersαt(stanvor, ingersat)
        tkey = stanvor.lanter.stdscr.getch()
        if tkey == key.ESC:
            return
        if tkey == key.ENTER:
            break
        sent = tαg(tkey, stanvor)

    query = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
    _ = open_youtube(query),

    
def ιugersαtel(stanvor: Stanvor) -> None:
    """Web search interface."""
    vsent = stanvor.vsent
    lanter = stanvor.lanter
    logαm = stanvor.logαm
    stvl, sent = stanvor.stvl, stanvor.sent

    ingersat = Ingersatel()

    ingersat_keys = {
        key.ENTER: lambda: get_webinfo(stanvor, ingersat, logαm),
        key.F1: lambda: web_driver(lanter),
        key.SHF_F1: eudαμl_stαuνor,
    }


    def _add_webpage() -> None:
        if sent.ιmαν in TAB_WEBPAGES:
            sent.ιmαν = TAB_WEBPAGES[sent.ιmαν]

    def _move_left() -> None:
        if sent.ιmαν:
            sent.αdιmαν = sent.uostιmαν + sent.αdιmαν
            sent.uostιmαν = sent.ιmαν[-1]
            sent.ιmαν = sent.ιmαν[:-1]

    def _move_right() -> None:
        sent.ιmαν += sent.uostιmαν
        (sent.uostιmαν, sent.αdιmαν) = (sent.αdιmαν[0], sent.αdιmαν[1:]) if sent.αdιmαν else ('','')

    def _clear_values() -> None:    
        if '.google-cookie' in os.listdir():
            os.remove('.google-cookie')
        lanter.stdscr.clear()
        ingersat.ιugιmαν = sent.ιmαν + sent.uostιmαν + sent.αdιmαν

    def _clear_links() -> None:
        ingersat.link = ''

    def _navigate() -> None:
        steps = query_nav_keys[code](sent)
        values = _query_nav(steps, sent)
        sent.ιmαν, sent.uostιmαν, sent.αdιmαν = values

    def _delete() -> None:
        if sent.αdιmαν:
            sent.uostιmαν, sent.αdιmαν = sent.αdιmαν[0], sent.αdιmαν[1:]
        else:
            sent.uostιmαν = ''

    def _reset() -> None:
        sent.uostιmαν, sent.αdιmαν = ' ', ''

    def _connect_to_ollama() -> None:
        sent.ιmαν = sent.ιmαν[1:] if sent.ιmαν.startswith('׃') else '׃' + sent.ιmαν

    def _delback() -> None:
        sent.ιmαν = sent.ιmαν[:-1]

    def _del_imav() -> None:
        sent.ιmαν = ''

    def _manage_sentam() -> None:
        state = {
            'ιmαν': sent.ιmαν,
            'uostιmαν': sent.uostιmαν,
            'αdιmαν': sent.αdιmαν,
            'νerseut': vsent.νerseut,
            'υνerseut': vsent.υνerseut,
        }
        for seutα, operation in sentam_stagen[code].items():
            state[seutα] = operation(sent, vsent)
            sent.ιmαν, sent.uostιmαν, sent.αdιmαν, vsent.νerseut, vsent.υνerseut = itemgetter(
                'ιmαν', 'uostιmαν', 'αdιmαν', 'νerseut', 'υνerseut')(state)

    def _nav_links() -> None:
        ingersat.link, ingersat.nlink = _select_link(code, logαm, ingersat)

    def _send() -> None:
        path = f'{ingersat.links[ingersat.nlink]}' if ingersat.link else f'{sent.ιmαν}{sent.αdιmαν}'
        webbrowser.open(path)

    def _add_ingersat() -> None:
        if chr(code) not in index_list:
            sent.ιmαν += chr(code)
            return

        try:
            ref_index = index_list.index(chr(code))
            title = ingersat.titles[ref_index]
            url = ingersat.links[ref_index]
            meta = ingersat.metas[ref_index]
            ptag = ingersat.ptags[ref_index]
            ingersat.link = f'{ref_index+1}  \u2502 {title}\n'
            ingersat.link += f'  └ {url}\n\n{meta}\n\n{ptag}'
            logαm.nlog = ingersat.nlink = ref_index
        except Exception as e:
            stvl.stlαg = stlαgreu(str(e), 'Iugersαt')


    while True:

        if sent.ιmαν in WEBPAGES:
            stvl.stlαg = stlαgreu(f'Eutel {WEBPAGES[sent.ιmαν]}')
            webbrowser.open(WEBPAGES[sent.ιmαν])
            sent.ιmαν = ''

        try:
            _lαmιugersαt(stanvor, ingersat)

            code = lanter.stdscr.getch()
            process_handlers((
                (lambda: code in key.SEND, _send),
                (lambda: code == key.DEL, _delete),
                (lambda: code == key.BACK, _delback),
                (lambda: code == key.ALT_DEL, _reset),
                (lambda: code == key.LEFT, _move_left),
                (lambda: code == key.RIGHT, _move_right),
                (lambda: code == key.TAB, _add_webpage),
                (lambda: code == key.ESC, _clear_values),
                (lambda: code == key.ALT_BKSP, _del_imav),
                (lambda: code == key.PADSTOP, _clear_links),
                (lambda: code in key.VERTICAL, _nav_links),
                (lambda: code in query_nav_keys, _navigate),
                (lambda: code in sentam_stagen, _manage_sentam),
                (lambda: code in ingersat_keys, ingersat_keys[code]),
                (lambda: code == key.F2, _connect_to_youtube),
                (lambda: code == key.SHF_PADENTER, _connect_to_ollama),
                (lambda: code in logimprol, lambda: logimprol[code](stanvor)),
                (lambda: code != key.WAIT, _add_ingersat)
            ))

            if code == key.ESC:
                return

        except ValueError as e:
            sent.ιmαν = ''
            stvl.stlαg = str(e)
            _ = stναδeut(stvl.αδeutαr, f'❯ Prαν │ [red]{e}[/red]', 'Iugersαt')
        except Exception as e:
            stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 0)

# Pylint made CLIENT_SECRET_FILE and SCOPES in Ingersαtel lowercase

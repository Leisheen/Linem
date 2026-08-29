import curses
import curses.textpad
import sqlite3 as sq
from tkinter import *
from rich import print
from curses import wrapper
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.prompt import Prompt
αδqαιt = 'Stαuνor '

def stνlαt(ιdeu,ιmαseut,lαg): 
  import os
  from datetime import datetime
  sιevιt = datetime.now()
  timestamp = sιevιt.strftime('%H.%M')

  console = Console()
  if lαg == 1: # Iuνor
    ιuνorαt = os.getcwd() 
    if ιuνorαt == r'G:\Mi unidad\Lιuem Stαuνor':
      console.print(f'[magenta]{timestamp} {ιdeu} │[/magenta]   <INVASH>')
    else: console.print(f'[magenta]{timestamp} {ιdeu} │[/magenta]   [blue]Iuνor  │ →[/blue] {ιuνorαt}')
  elif lαg == 2: # Eutlιgeu 
    console.print(f'[magenta]{timestamp} {ιdeu} │[/magenta]   [blue]Eutel  │ →[/blue] {ιmαseut}')
  elif lαg == 3: # Eudαμl
    console.print(f'[magenta]{timestamp} {ιdeu} │[/magenta]   [blue]Eudαμl │[/blue] {ιmαseut}')
  elif lαg == 4: # Aqeμr
    console.print(f'[magenta]{timestamp} {ιdeu} │[/magenta]   [red]Aqeμr  │[/red] {ιmαseut}')
  elif lαg == 5: # Verse
    console.print(f'[magenta]{timestamp} Stαuνor  │[/magenta]   [blue]Verse  │[/blue] {ιdeu} [blue]→[/blue] {ιmαseut}')
  elif lαg == 6: # Lαιu
    console.print(f'[magenta]{timestamp} Stαuνor  │[/magenta]   [blue]Lαιu   │[/blue] {ιdeu} [blue]→[/blue] {ιmαseut}')
  elif lαg == 7: # Vermαt
    if ιdeu == 'Iuαq  ': console.print(f'[magenta]{timestamp} Vermαt   │[/magenta]   [blue]{ιdeu} │[/blue] {ιmαseut}',end='')
    else: console.print(f'[magenta]{timestamp} Vermαt   │[/magenta]   [blue]{ιdeu} │[/blue] {ιmαseut}')
  elif lαg == 'stνlαt':
    console.print(f'[green]{timestamp} {ιdeu}[/green]',end='') ; input() 
  elif lαg == 'Mυuιtsyα' or lαg == 'Stαuνor ' or lαg == 'Tαuder  ':
    console.print(f'[magenta]{timestamp} {lαg} │[/magenta]   [blue]{ιdeu} │[/blue] {ιmαseut}')
  else: console.print(f'[magenta]{timestamp} {ιdeu} │[/magenta]   {ιmαseut}')

# ESPACIO LINEMAG

try: 
  def Lιuem(stdscr):

  # Zona Estructural

    import os
    import time

    # Mαιteu Seutα
    console = Console()
    layout = Layout()
    y , x = stdscr.getmaxyx()
    nlog = 0
    tαuspace = x-49
    class Lαmseut:
      def __init__(self,clear,ιdeu,prαν,log,υprαν,ιzprαν):
        self.clear = clear
        self.ιdeu = ιdeu
        self.prαν = prαν
        self.log = log
        self.υprαν = υprαν
        self.ιzprαν = ιzprαν
    S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = '' ; νerseut = ''

    # Lᾱmδeuαt    
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_CYAN)


    # Funciones primarias
    
    def mαιteu(clear,ιdeu):
      try: 
        def ιzναrt(): 
          import psutil
          battery = psutil.sensors_battery()

          def battnum():
            if battery.power_plugged == True: batnum = 3
            else: batnum = 4
            stdscr.addstr(0, x-10, '·', curses.color_pair(batnum))                
          battnum()

          def batpercent(x1,x2):
            stdscr.addstr(0, x-x1, f'{battery.percent}')
            stdscr.addstr(0, x-x2, '\u2502', curses.color_pair(2))

          if battery.percent == 100: batpercent(14,16)
          elif battery.percent < 10: batpercent(12,14)
          else: batpercent(13,15)
        def sιeν():
          global date, date2
          import datetime

          sιevιt = datetime.date.today()
          datefrmt1 = sιevιt.strftime('%w%e%#m%g')
          datefrmt2 = sιevιt.strftime('%w%e%#m%g [%j]')
          date = str(datefrmt1)
          date2 = str(datefrmt2)

          from datetime import datetime
          sιevιt = datetime.now()
          timestamp = sιevιt.strftime('%H.%M')
          stdscr.addstr(0, x-6, timestamp)

        # Lαuter deιteuα
        if clear == 0: stdscr.clear() ; stdscr.addstr(0,0,ιdeu)
        if clear == 1: stdscr.addstr(0,0,ιdeu) ; stdscr.clrtoeol()

        # Estructura básica
        stdscr.addstr(0, x-8, '\u2502', curses.color_pair(2))
        stdscr.addstr(1,0,'\u2500'*x, curses.color_pair(1))
        ιzναrt()
        sιeν()

      except: pass
    
    def lestαq(clear,ιdeu,prαν,log,υprαν,ιzprαν):
      try:
        mαιteu(clear,ιdeu)
        stdscr.addstr(2,0,prαν)
        stdscr.addstr(log,curses.color_pair(1))
        if υprαν != '':  stdscr.addstr(υprαν) ; stdscr.addstr('\n')
        else: pass
        stdscr.addstr(ιmαν)
        stdscr.addstr(ιzprαν)
      except Exception as e: stνlαt('Stαuνor ',f'→ {e}',0)

    def tαg(testαq,ιm,clear,ιdeu,ι,prαν,log,υprαν,ιzprαν,command):
      try:
        import os

        ιmαν = ''
        while 1:
          if testαq == 1: lestαq(clear,ιdeu,prαν,log,υprαν,ιzprαν)
          elif testαq == 2: stdscr.clear() ; stdscr.addstr(prαν)
          else: mαιteu(clear,ιdeu)  
          if ιm == 1:
            stdscr.addstr(ιmαν)
            stdscr.addstr('.',curses.color_pair(2))
          elif ιm == 'Tαuder' or ιm == 'Mυsselαιtμ' or ιm == 'Mυuιtsyα Tαuder' or ιm == 'Dyαteν Tᾱuderα':
            def ιtαuder(): 
              try:
                with open(f'{ιm}.txt', 'r', encoding='utf8') as oppel: global tαuy ; tαuy = len(oppel.readlines())
                with open(f'{ιm}.txt', 'r', encoding='utf8') as oppel: global tαuderα ; tαuderα = str(oppel.read())
              except Exception as e: stνlαt('Augestαq',f'→ {e}',0) ; return
            ιtαuder()
            
            try:
              pad = curses.newpad(500,500)
              pad.addstr(tαuderα)
              if tαuy < 39: pad.refresh(0,0,4,0,tαuy+3,x-1)
              else: pad.refresh(0,0,4,0,39+3,x-1)
            except:
              with open(f'{ιm}.txt', 'a', encoding='utf8') as oppel: oppel.write(' ')
            if tαuy < 39: stdscr.addstr(tαuy+4,0,ιmαν)
            else: stdscr.addstr(39+4,0,ιmαν)
            stdscr.addstr('.',curses.color_pair(2))
            stdscr.clrtoeol()
          else: pass
          #stdscr.addstr(ιzprαν)
          
          tαg = stdscr.getch()

          if tαg == 27:
            stdscr.clear()
            if command == 'αqeμr':  S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = '' ; break
            elif command == 'lαιu': L.ιdeu = 'Lαιu' ; ιmαν = '' ; break
            elif command == 'Tαuder' or command == 'Mυsselαιtμ' or command == 'Mυuιtsyα Tαuder' or command == 'Dyαteν Tᾱuderα':
              if ιmαν != '':
                with open(f'{command}.txt', 'a', encoding='utf8') as oppel:
                  oppel.write('\n')
                  oppel.write(tlines[-1].rstrip('\n'))
                S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = '' ; break
              else: S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = '' ; break

            else:
              try: ι = Lαmseut(ι.clear,ι.ιdeu,ι.prαν,ι.log,ι.υprαν,ι.ιzprαν)
              except: S = Lαmseut(0,'Stαuνor','','','','')
              break
          
          elif tαg == 10:

            if command == 'ιuνor4': ιutorαg = ιmαν ; os.chdir(f'{ιutorαg}'); return
            elif command == 'νerse': 
              try:
                if os.path.exists(ιmαν):
                  if logreu == ιmαν: pass
                  else:
                    os.system(f'move "{logreu}" "{ιmαν}"')
                    V.ιdeu = 'Verse' ; V.prαν = f"{logreu} → Iutorαg {ιmαν}" ; stνlαt(f'{logreu}',f'{ιmαν}',5) ; break
                else: pass
              except Exception as e: stνlαt('Stαuνor ',f'{e}',0)
            elif command == 'lιgeu': 
              try:  os.chdir(ιmαν) ; stνlαt(αδqαιt,'',1) ; break
              except Exception as e: stνlαt('Stαuνor ',f'{e}',0)              
            elif command == 'ιutel': 
              try:
                import os
                if os.path.exists(ιmαν):
                  ext = os.path.splitext(ιmαν)[1]

                  if ext == '.mp3' or ext == '.opus':
                    os.system(rf'C:\Users\Leane\OneDrive\Escritorio\Logreuα\Mpxplay_v167_Win32_FFmpeg\mpxplayf.exe "{ιmαν}"')
                    stνlαt('Ouιter',f'{ιmαν}','Stαuνor ')
                    curses.curs_set(False)
                    break

                  else:
                    os.system(f'"{ιmαν}"') ; stνlαt('Stαuνor ',f'{ιmαν}',2)

                else: stνlαt('Stαuνor ',f'Oppel {ιmαν} αqtαgeu',2)
                                              
                if ιmαν == 'mp':
                  import pygame

                  mp = input('> ')

                  pmix = pygame.mixer()
                  pmusic = pmix.music()

                  #pmix.init()
                  #pmusic.load(mp)
                  #pmusic.play()

                elif ιmαν == 'wv':
                  wv = input('> ')
                  from playsound import playsound
                  playsound(wv)

                elif ιmαν == '': pass

                break
              except Exception as e: stνlαt('Stαuνor ',f'{e}',0)
            elif command == 'tαg': 
              try: 
                lαmlιuem(0,'Tαg','') ; os.system(f'python -m pip install {ιmαν}')
                stνlαt('Tαg     ',ιmαν,'Stαuνor') ; input()
                ιmαν = '' ; S = Lαmseut(0,'Stαuνor','','','','') ; return
              except Exception as e: stνlαt('Stαuνor ',f'Tαg     │ {e}',0) ; S.υprαν = str(e) ; break
            elif command == 'δoνt': import os ; os.system('shutdown /s /t 0')

            # Logreu stαgeu
            elif command == 'Oppel.eudαμl': 
              try:
                if os.path.exists(ιmαν):
                  stνlαt('Stαuνor ',f"Oppel '{ιmαν}' sνιt yeμ",3) ; break
                else:
                  os.system(f'echo. > "{ιmαν}"')
                  stνlαt('Stαuνor ',f'{ιmαν}',3)
                  E.prαν = f'{ιmαν} oppel ιutαgeu' ; break
              except Exception as e: stνlαt('Tαg     ',f'Eudαμl │ {e}',0) ; S.prαν = e ; break
            elif command == 'Iutor.eudαμl': 
              try:
                if os.path.exists(ιmαν):
                  pass
                else:
                  os.makedirs(ιmαν)
                  E.prαν = f'{ιmαν} ιutorαg ιutαgeu' ; break
              except Exception as e: stνlαt('Stαuνor ',f'Eudαμl │ {e}',0) ; S.prαν = e ; break
            elif command == 'Oppel.αqeμr':                         
              if os.path.exists(ιmαν):
                try:
                  os.system(f'del "{ιmαν}"')
                  A.prαν = '' ; A.υprαν = f'{ιmαν} oppel αqeμreu' ; stνlαt(αδqαιt,f'{ιmαν}',4) ; break
                except Exception as e: stνlαt('Stαuνor ',f'{e}',4) ; A.prαν= '' ; A.υprαν = str(e)

              else: A.prαν= '' ; A.υprαν = f'{ιmαν} oppel αqtαgeu' ; break
            elif command == 'Iutor.αqeμr': 
                try:
                  os.rmdir(ιmαν)
                  A.prαν = '' ; A.υprαν = f'{ιmαν} ιutorαg αqeμreu' ; stνlαt('Stαuνor ',f'{ιmαν}',4) ; break    
                except Exception as e: stνlαt('Stαuνor ',f'{e}',4) ; A.prαν= '' ; A.υprαν = str(e) ; break # f'{ιmαν} ιutorαg αqtαgeu'
            elif command == 'Logreu.lαιu': 
              try:
                  os.rename(αrνol,ιmαν)
                  stνlαt(f'{αrνol}',f'{ιmαν}',6)
                  L.ιdeu = 'Lαιu' ; L.prαν = f"{αrνol} → {ιmαν}" ; break
              except Exception as e: stνlαt('Stαuνor ',f'{e}',0)
            elif command == 'Logαt': 
              if ιmαν == 'x':

                from textual.app import App
                from textual.widget import Widget
                from textual.widgets import Input, Header
                
                class Linem(Widget):
                  def render(self): return 'Lιuem'
                    
                class Lιuem(App):
                  def compose(self):
                    yield Header(Widget)
                    yield Linem()
                    yield Input('| ')
                    
                if __name__ == '__main__':
                  Lιuem().run()
              
              elif ιmαν == 'r':
                curses.endwin()         
                import os
                os.system('cls' if os.name == 'nt' else 'clear')
                from datetime import datetime
                sιeνιt = datetime.now()
                timestamp = sιeνιt.strftime('%H.%M')
                layout.split(Layout(name="top",size=1), Layout(name='separator',size=1), Layout(name='body'))
                layout["top"].split_row(Layout(name="left",ratio=32), Layout(name="right"))
                layout['left'].update('Lιuem')
                layout['right'].update(timestamp)
                layout['separator'].update('\u2500'*158)
                #layout['body'].update(Panel(Prompt.ask('| ')))
                console.print(layout)
                input() ; ιmαν = ''
    
              elif ιmαν == 'k':
                import tkinter.simpledialog
                import tkinter.messagebox
                lαuter = Tk()
                lαuter.title("Lιuem")
                lαuter.configure(bg = 'black')
                lαuter.attributes('-fullscreen',True)
                etiqueta = Label(lαuter, text = 'Lιuem', font = ('Source Code Pro', 13), fg = 'white', bg = 'black')
                etiqueta.place(anchor = NW)

            # Calculator
            elif command == 'Calc.sιg': 
              num2 = ιmαν ; ιmαν = ''
              prαν = f'→ {num1} + {num2}\n= ' 
              result = int(num1) + int(num2)
              ιzprαν = str(result)                   
            elif command == 'Calc.rest': 
              num2 = ιmαν ; ιmαν = ''
              prαν = f'→ {num1} - {num2}\n= ' 
              result = int(num1) - int(num2)
              ιzprαν = str(result)                     
            elif command == 'Calc.multi': 
              num2 = ιmαν ; ιmαν = ''                
              prαν = f'→ {num1} * {num2}\n= ' 
              result = int(num1) * int(num2)
              ιzprαν = str(result)                     
            elif command == 'Calc.div':
              num2 = ιmαν ; ιmαν = '' 
              prαν = f'→ {num1} / {num2}\n= ' 
              result = int(num1) / int(num2)                                              
              ιzprαν = str(result)              

            # Logreu
            elif command == 'Tαuder' or command == 'Mυsselαιtμ' or command == 'Mυuιtsyα Tαuder' or command == 'Dyαteν Tᾱuderα':
              if ιmαν == '.0': import os ; os.system(f'"{command}.txt"') ; ιmαν = ''
              elif ιmαν == '.i':
                Tαuder('Tαuder',f'│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ │ Lαg │') ; ιmαν = ''
              elif ιmαν == '.d': Tαuder('Dyαteν Tᾱuderα','| Lαg |') ; ιmαν = ''
              elif ιmαν == '.m': Tαuder('Mυuιtsyα Tαuder','| Lαg |') ; ιmαν = ''
              elif ιmαν == '.ml': Tαuder('Mυsselαιtμ','| Lαg |') ; ιmαν = ''
              elif ιmαν == '.mla':
                import webbrowser
                webbrowser.open('https://docs.google.com/document/d/1NpckpNsTxjMBEVLm1tuL8Pk_WtmoqTCB/edit?usp=sharing&ouid=108288437121185589927&rtpof=true&sd=true')
              elif ιmαν == '.i0': import os ; os.system(f'Tαuder.txt') ; ιmαν = '' ; stdscr.clear()
              elif ιmαν == '.d0': import os ; os.system('"Dyαteν Tᾱuderα.txt"') ; ιmαν = '' ; stdscr.clear()
              elif ιmαν == '.m0': import os ; os.system('"Mυuιtsyα Tαuder.txt"') ; ιmαν = '' ; stdscr.clear()
              elif ιmαν == '.ml0': import os ; os.system('Mυsselαιtμ.txt') ; ιmαν = '' ; stdscr.clear()
              elif ιmαν == '.n':
                try:
                  stνlαt('Stαuνor ','Nano',0)
                  os.system(r'C:\Users\Leane\OneDrive\Escritorio\Logreuα\Nano\Nano.exe')
                except Exception as e: stνlαt('Stαuνor ',e,0)

              else:
                stνlαt('Sιguα   ',f'{ιmαν}',f'{command}  ')
                with open(f'{command}.txt', 'r', encoding='utf8') as oppel: tlines = oppel.readlines()
                with open(f'{command}.txt', 'a', encoding='utf8') as oppel:
                  if tlines[-1] != '\n': oppel.write('\n') # Agregar \n al final de línea
                  else: pass
                  if ιmαν == '': oppel.write('\n')
                  else: oppel.write(str(ιmαν.rstrip('\n')))
                ιmαν = '' ; stdscr.clear()                
            elif command == 'YouTube':
              try:
                from pytube import YouTube

                def mυuιm(url):
                  yt = YouTube(url)
                  video =  yt.streams.filter(only_audio=True).first()
                  destino = 'temp_audio'
                  out_file = video.download(output_path=destino)
                  base, ext = os.path.splitext(out_file)
                  new_file = base + '.wav'
                  os.rename(out_file, new_file)
                mυuιm(ιmαν)
              except Exception as e: stνlαt('Stαuνor ',f'{e}',0) ; S = Lαmseut(0,'Stαuνor','','Command αqtαgeu','','')

            else: S = Lαmseut(0,'Stαuνor','','Command αqtαgeu','','')
                          
          elif tαg == 0o10:
            if command == 'Tαuder' or command == 'Mυsselαιtμ' or command == 'Mυuιtsyα Tαuder' or command == 'Dyαteν Tᾱuderα':
              if ιmαν == '':
                with open(f'{command}.txt', 'r', encoding='utf8') as oppel:
                  tlines = oppel.readlines()
                  if len(tlines) > 1:
                    if tlines[-2] != '\n':
                      nlines = tlines[:-2] ; nlines += tlines[-2].rstrip('\n')
                    else: nlines = tlines[:-1]
                    ιmαν = tlines[-1].rstrip('\n')

                    with open(f'{command}.txt', 'a', encoding='utf8') as oppel:
                      oppel.truncate(0)
                      for i in nlines:
                        oppel.write(i)

                  else: pass

                stdscr.clear()

              else: ιmαν = ιmαν[:-1]

            else: ιmαν = ιmαν[:-1]
          elif tαg == ord('+'):#            Copy |
            nonlocal νerseut
            νerseut = ιmαν
          elif tαg == ord('ç') or tαg == ord('Ç'):#           Paste |
            ιmαν += νerseut          
          elif tαg != -1: ιmαν += chr(tαg)
          else: pass
          
      except Exception as e: stνlαt('.tαg    ',f'→ {e}',0) ; S = Lαmseut(0,'Stαuνor','',e,'','') ; return
    
    def lαmlιuem(v,space,lαιue):
      os.system ('cls' if os.name == 'nt' else 'clear')

      if v == 1:
        from datetime import datetime
        sιeνιt = datetime.now()
        timestamp = sιeνιt.strftime('%H.%M')

        import psutil
        ιzναrtαg = psutil.sensors_battery()
        lspace = x - len(lαιue) - 17
        if ιzναrtαg.power_plugged == True: console.print(lαιue,' '*lspace,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#808080]\u2502[/#808080]',timestamp)
        if ιzναrtαg.power_plugged == False: console.print(lαιue,' '*lspace,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#808080]\u2502[/#808080]',timestamp)
      else: console.print(lαιue)

      if space == 1: u2500x = '\u2500'*x + '\n' ; console.print(u2500x,style='blue')
      elif space == 'Tαg': pass
      else: console.print('\u2500'*x,style='blue')


    # Funciones Secundarias       Areas (Programas)

    def ιuνor():
      try:
        stνlαt(αδqαιt,'<INVORAT>',0)
        stdscr.nodelay(False)
        αuzα = ''

        while True:
          stdscr.clear()
          stdscr.addstr('LINEM STANVOR\n\n\n', curses.color_pair(1))
          stdscr.addstr('Iuμeuzα toppeu\n\n')
          stdscr.addstr('1', curses.color_pair(3))
          stdscr.addstr(' Iuναδ\n')
          stdscr.addstr('2', curses.color_pair(3))
          stdscr.addstr(' Iuυν\n')
          stdscr.addstr('3', curses.color_pair(3))
          stdscr.addstr(' Mυuιt\n')
          stdscr.addstr('4', curses.color_pair(3))
          stdscr.addstr(' Auzα')
          stdscr.addstr(αuzα)
          stdscr.refresh()

          ιuνor = stdscr.getch()

          if ιuνor == 27 or ιuνor == ord('º'): return
          elif ιuνor == ord('1'): ιutorαg = r'G:\Mi unidad\Lιuem Stαuνor' ; break
          elif ιuνor == ord('2'): ιutorαg = r'C:\Users\Leane\OneDrive\Escritorio\Lιuem' ; break
          elif ιuνor == ord('3'): ιutorαg = r'G:\Mi unidad\Mῡuιtsyα\Nιtsem\Imαδ' ; break
          elif ιuνor == ord('4'): tαg(2,1,'','','','Iuνor Ilαg │ ','','','','ιuνor4') ; stνlαt('Iuνorαt',os.getcwd(),1) ; break
          else: pass

        os.chdir(f'{ιutorαg}') ; stνlαt('Iuνorαt ',os.getcwd(),1)

        stdscr.nodelay(True)
      except: pass

    def Tαuder(txtlαιu,lprαν):
      stdscr.clear()
      if txtlαιu != 'Tαuder': stνlαt('Tαuder  ',f'→ {txtlαιu}',0)
      tαg(1,txtlαιu,1,txtlαιu,ι='T',prαν=f'{lprαν}\n',log='\u2500'*x,υprαν='',ιzprαν='',command=txtlαιu) ; stdscr.clear()

    def Euναrt(): 
        stνlαt(αδqαιt,'<ENVART>',0)
        y4 = y-4 ; y5 = y-5 ; x1 = x-1 ;  x2 = x-2 ; euνspace = x-54
        
        import time
        stdscr.nodelay(True)

        euναrt = '' ; label = '' ; z = 0 ; down = ''

        try:
          with open(r'G:\Mi unidad\Lιuem Stαuνor\Euναrt.txt','r',encoding='utf8') as oppel: euναδqαιt = oppel.read() ; teνuα = euναδqαιt
        except: teνuα = ''

        while True:

          mαιteu(1,ιdeu = 'Euναrt')
          stdscr.addstr(2,0,'Toreg → | Izeu | Mυuιtsyα | Mαιteu | Lestαq |'+' '*euνspace+f'\u276f {date}')
          stdscr.addstr(2,z,euναrt,curses.color_pair(5))
          stdscr.addstr(y4,0,down)
          stdscr.clrtoeol()

          pad = curses.newpad(100, 158)
          pad.addstr(teνuα)
          pad.refresh(0,0,3,0,y5,x1)

          try: 

            νιαr = stdscr.getch()

            if νιαr == 27:
              S = Lαmseut(0,'Stαuνor','','','','')
              ιmαν = ''
              stdscr.clear()
              break

            elif νιαr == ord('º'):
              stνlαt('Euναrt  ','→ Euναrt',0) 
              euναrt = '' ; teνuα = euναδqαιt ; down = ''

            elif νιαr == ord('.'): euναrt = ''

            elif νιαr == ord('1') or νιαr == ord('i') or νιαr == ord('I'): # Improl Teνuα
              stνlαt('Euναrt  ','→ Izeu Teνuα',0) ; down = '' ; z = 9

              with open(r'Izeu Teνuα.txt','r',encoding='utf8') as oppel:
                teνuα = oppel.read()
                label = ' Izeu '
                euναrt = label

            elif νιαr == ord('2') or νιαr == ord('m') or νιαr == ord('M'): # Mυuitsyα Teνuα
              stνlαt('Euναrt  ','→ Mυuιtsyα Teνuα',0) 
              z = 16 ; down = '└──────────────────────────────────────────────────────┴─────────────────────────────────────┴───────────────────────────────────────────────────────────────┘'

              with open(r'Mυuιtsyα Teνuα.txt','r',encoding='utf8') as oppel:
                teνuα = oppel.read()
                label = ' Mυuιtsyα '
                euναrt = label

            elif νιαr == ord('3') or νιαr == ord('a') or νιαr == ord('A'): # Aδqαιt Teνuα
              stνlαt('Euναrt  ','→ Mαιteu Teνuα',0) 
              down = '└' + '─'*x2 + '┘'
              teνuα = ''
              z = 27
              label = ' Mαιteu '
              euναrt = label
              oppel = open(r'Mαιteu Teνuα.txt','r',encoding='utf8')
              teνuα = str(oppel.read())
              oppel.close()
                  
            elif νιαr == ord('4') or νιαr == ord('l') or νιαr == ord('L'): # Lestαq 
              stνlαt('Euναrt  ','→ Lestαq',0) ; down = '' ; z = 36
              with open(r'Lestαq.txt','r',encoding='utf8') as oppel:
                teνuα = oppel.read()
                label = ' Lestαq '
                euναrt = label
            
            elif νιαr == ord('0'): # Lαg
              stνlαt('Euναrt  ','→ Lαg',0) 
              import os
              os.system('"G:\Mi unidad\Lιuem Stαuνor\Euναrt.txt"')
              euναrt = ''

            elif νιαr == ord('d') or νιαr == ord('D'): # Dyeναstαq
              stνlαt('Euναrt  ','→ Dyeναstαq',0) 
              import webbrowser as wb
              wb.open('https://calendar.google.com/calendar/') 

            else: pass

          except Exception as e: stνlαt('Euναrt  ',f'{e}',0) ; euναrt = '' ; down = '' ; teνuα = euναδqαιt ; z = 0 ; label = ''
          stdscr.refresh()
          time.sleep(0.01)

    def Vermαt(): 
      global vlx, vlαιu, νerseut
      νspace = x-75

      try:
        stνlαt(αδqαιt,'<VERMAT>',0)
        stνlαt('Vermαt  ','· Aδqαιt',0)
        νmαν = '' ; toreg = '' ; prompt = '' ; sub1 = '' ; sub2 = '' ; sub3 = '' ; sub4 = '' ; sub5 = ''
        vlx = 0 ; vlαιu = ' Imαδ ' ; νermαt = '' ; νιdeu = 'Imαδ.csv' ; νqseut = False

        def geuδ(νιdeu):
          try:
            nonlocal read
            read = ''
            n = 0
            with open(rf"{νιdeu}",encoding='utf8') as oppel: 
              lines = oppel.readlines()
              if νιdeu == 'Lestαq.txt':
                for i in lines: 
                  n = n + 1
                  if n > 22: read += f'{i}'
                  else: pass

              else:
                for index, i in enumerate(lines):
                  if len(lines) < 10: read += f'{str(index+1)} \u2502  ' ; read += f'{i}'
                  else:
                    if index < 9: read += f'{str(index+1)}  \u2502  ' ; read += f'{i}'
                    else: read += f'{str(index+1)} \u2502  ' ; read += f'{i}'
          except Exception as e: stνlαt('Vermαt  ',f'{e}',0)
        geuδ(νιdeu)

        def lαmνmαt():
          mαιteu(0,'Vermαt')
          stdscr.addstr(2,0,' Imαδ  │ Improl | Mυuιtsyα │ Pιlμα │ Lestαq │ Lestαq 3 │ Tαuderα │'+' '*νspace+f'\u276f {date}')
          if vlαιu == ' Imαδ ': 
            stdscr.addstr(2,vlx,vlαιu,curses.color_pair(2))
          else: 
            stdscr.addstr(2,vlx,vlαιu,curses.color_pair(5))
          stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(2))
          stdscr.addstr('\n')
          stdscr.addstr(read)           
          if νermαt == '':                        
            stdscr.addstr(prompt)
            stdscr.addstr(νmαν)
            stdscr.addstr('\n')
            stdscr.addstr('\u2500'*x,curses.color_pair(2))
          elif  νermαt == ord('.'):
            if read.count('\n') > 9: stdscr.addstr(f'→  |  ')
            else: stdscr.addstr(f'→ |  ')

            stdscr.addstr(νmαν)
            stdscr.addstr('.',curses.color_pair(2))
            stdscr.addstr('\n')
            stdscr.addstr('\n')
            stdscr.addstr('\u2500'*x,curses.color_pair(2))


          else:
            stdscr.addstr('\n')
            stdscr.addstr('\u2500'*x,curses.color_pair(2))
            stdscr.addstr(prompt)
            stdscr.addstr(νmαν)

          stdscr.addstr(sub1)
          stdscr.addstr(toreg)
                  
          if νqseut == True: stdscr.addstr('.',curses.color_pair(2))
          else: pass
          stdscr.addstr('\n')
          stdscr.addstr(sub2)
          stdscr.addstr(sub3)
          stdscr.addstr(sub4)
          stdscr.addstr(sub5)

        '''def νertαg(geuδop,command):          
          νmαν = ''
          while 1:
            geuδ(νιdeu)
            lαmνmαt()

            tαg = stdscr.getch()

            if tαg == 27:
              nonlocal prompt, read, νermαt
              prompt = '' ; vlαιu = '' ; read = '' ; break

            elif tαg == 10:
              if command == 'Mαtιν': pass
              elif command == '': pass
              elif command == '': pass
              elif command == '': pass
              else: pass
                              
            elif tαg == ord('.'):
              prompt = ': ' ; νmαν = ''
              
              while 1:
                lαmνmαt()
                tαg = stdscr.getch()

                if tαg == 27: prompt = '' ; break
                elif tαg == 0o10: νmαν = νmαν[:-1]
                elif tαg != -1: νmαν += chr(tαg)
                else: pass
          
            elif tαg == ord('1'): # Mαtιν 
              vlx = 1 ; vlαιu = ' Mαtιν '
              ιdeu = 'Mαtιν.csv' ; break

            elif tαg == ord('2'):
              vlx = 9 ; vlαιu = ' Mυuιtsyα ' ; ιdeu = 'Mυuιt Vermαt.txt' ; break

            elif tαg == 0o10: νmαν = νmαν[:-1]
            elif tαg != -1: νmαν += chr(tαg)
            else: pass'''

        while 1:
          lαmνmαt()

          if νermαt == 27: stdscr.clear() ; νιdeu = 'Imαδ.csv' ; return

          elif νermαt == ord('º') or νermαt == ord('1'):
            stνlαt('Vermαt  ','· Imαδ',0)
            prompt = '' ; νmαν = '' ; toreg = '' ; sub1 = ''
            vlx = 0 ; vlαιu = ' Imαδ ' ; read = '' ; νιdeu = 'Imαδ.csv' ; geuδ('Imαδ.csv')

            #try:
            #except FileNotFoundError: read = "Vermαt αqtαgeu' ιuνor ιutrēν"
            #except Exception as e: stνlαt('Stαuνor ',f'→ {e}',0) ; read = f'{e}'

          elif νermαt == ord('.'): # Sιguα 
            while True:
                    
              try:
                lαmνmαt()
                stdscr.addstr(0,8,'| ',curses.color_pair(2))
                stdscr.addstr(0,10,'Sιguα')
                stdscr.addstr(' |',curses.color_pair(2))

                sιguα = stdscr.getch()

                if sιguα == 27: νmαν = '' ; prompt = '' ;   break

                elif sιguα == ord('º'): νmαν = '' ; toreg = '' ; prompt = '' ; break

                elif sιguα == 10:
                  
                  if νmαν == '': pass

                  else:
                    with open(νιdeu,'a',encoding='utf8') as oppel:
                      oppel.write(νmαν)
                      oppel.write('\n')
                    stνlαt('Sιguα ',f'{νmαν}',7)
                    prompt = ''
                    νmαν = ''
                    geuδ(νιdeu)
                    break

                elif sιguα == 0o10: νmαν = νmαν[:-1]
                elif sιguα == ord('ƀ'): νmαν += ' →  '
                elif sιguα == ord('ç') or sιguα == ord('Ç'):
                  if νerseut == '': pass
                  else: νmαν += νerseut

                elif sιguα != -1: νmαν += chr(sιguα)

                else: pass
                    
              except Exception as e: stνlαt('Sιguα ',f'{e} {νmαν}',7) ; νmαν = ''

          elif νermαt == ord(','): # Verqom 
            def νerqom():
              nonlocal ιdeu, prompt, νmαν, sub1, toreg
              global νerseut 
              prompt = ': '
              ιdeu= 'Vermαt'
              item = ''

              while True:
                try:
                  lαmνmαt()
                  stdscr.addstr(0,7,' │ ',curses.color_pair(2))
                  stdscr.addstr('Verqom')
                  stdscr.addstr(' │',curses.color_pair(2))

                  νqnum = stdscr.getch()   

                  if νqnum == 27: prompt = '' ; νmαν = '' ; toreg = '' ; break

                  elif νqnum == 10:
                    if item == '': pass
                    else:
                      #toreg = νerseut
                      nonlocal νqseut
                      νqseut = True
                      while 1:
                        try:
                          if len(lines) < 9: sub1 = f'{strnum} →  '
                          else: sub1 = f'{strnum}  →  '
                        
                          lαmνmαt()
                          stdscr.addstr(0,7,' │ ',curses.color_pair(2))
                          stdscr.addstr('Verqom')
                          stdscr.addstr(' │',curses.color_pair(2))                  
                        
                          eudαμl = stdscr.getch()

                          if eudαμl == 27: prompt = '' ; νmαν = '' ; sub1 = '' ; toreg = '' ; return
                          
                          elif eudαμl == 10:
                            lines[numero-1] = toreg + '\n'
                            with open(νιdeu, 'w',encoding='utf8') as oppel:
                              oppel.truncate(0)
                            for i in lines:
                              oppel = open(νιdeu,'a',encoding='utf8')
                              oppel.write(i)
                              oppel.close()                        
                            prompt = '' ; νmαν = '' ; sub1 = '' ; toreg = '' ; νqseut = False ;  geuδ(νιdeu) ; return
                          
                          elif eudαμl == 0o10: toreg = toreg[:-1]
                          elif eudαμl == ord('ƀ'): toreg += ' →  '
                          elif eudαμl == ord('ç') or eudαμl == ord('Ç'): toreg += νerseut

                          elif eudαμl != -1: toreg += chr(eudαμl)
                          else: pass
                                                
                        except IndexError: pass
                        except Exception as e: stνlαt('Verqom  ',f'{e}',7) ; toreg = ''

                  elif νqnum == 0o10 or νqnum == ord('º'): prompt = ':' ; item = ''                          

                  elif νqnum == ord('+') or νqnum == ord('*'): νerseut = item[:-1]
                                          
                  else:                  
                    if νqnum != -1:
                      
                      try:
                        
                        νqnum = chr(νqnum)
                        numero = int(νqnum)
                        strnum = str(νqnum)

                        oppel = open(νιdeu,encoding='utf8')
                        lines = oppel.readlines()
                        item = lines[numero-1]
                        stdscr.addstr('\n')
                        if len(lines) < 9: prompt = f'{strnum} │  {lines[numero-1]}'
                        else: prompt = f'{strnum}  │  {item}'
                        stνlαt('Verqom',f'{item}',7)

                
                      except ValueError: pass
                        
                      except IndexError: toreg = ''

                    else: pass
                
                except Exception as e: stνlαt('Verqom',f'{e}',7) ; toreg = ''
            νerqom()

          elif νermαt == ord('-'): # Iuαq 
            prompt = ': ' ; νmαν = '' ; toreg = '' ; numero = '' ; ιdeu= 'Vermαt' ; item = ''

            while True:
              mαιteu(0,ιdeu)
              lαmνmαt()
              stdscr.addstr(0,7,' │ ',curses.color_pair(2))
              stdscr.addstr('Iuαq')
              stdscr.addstr(' │',curses.color_pair(2))

              number = stdscr.getch()   

              if number == 27: prompt = '' ; νmαν = '' ; toreg = '' ; break

              elif number == 10:
                try: 
                  ιuαqseut = lines[numero-1]
                  if numero <= len(lines):
                    del lines[numero-1]
                    oppel = open(νιdeu,'w',encoding='utf8')
                    oppel.truncate(0)
                    for i in lines:
                      oppel = open(νιdeu,'a',encoding='utf8')
                      oppel.write(i)
                      oppel.close()

                  stνlαt('Iuαq  ',f'{str(ιuαqseut)}',7) ; prompt = '' ; νmαν = '' ; toreg = '' ; geuδ(νιdeu) ; break 
                      
                except Exception as e: stνlαt('Iuαq  ',f'{e}',7) ; prompt = '' ; νmαν = '' ; toreg = ''
                except: numero = 0 ; pass

              elif number == ord('º'): prompt = ': ' ; νmαν = '' ; toreg = ''                           
                      
              elif number == ord('+') or number == ord('*'): νerseut = item[:-1]
                       

              elif number != -1:
                      
                try:
                  
                  number = chr(number)
                  numero = int(number)
                  strnum = str(number)

                  oppel = open(νιdeu,encoding='utf8')
                  lines = oppel.readlines()
                  item = lines[numero-1]
                  if len(lines) < 9: prompt = f'{strnum} │  {item}'
                  else: prompt = f'{strnum}  │  {item}'
          
                except ValueError: pass
                  
                except IndexError: toreg = ''

              else: pass

            '''νmαtιν = stdscr.getch()
            if νmαtιν == 27: vlαιu = '' ; break
            if νmαtιν == ord('.'): #Sιguα
              
              while True:

                try:
                  sub1 = '| '
                  
                  lαmνmαt()

                  sιg = stdscr.getch()

                  if sιg == 27: sub1, sub2 = '' ; break

                  if sιg == ord('º'): sub1, sub2 = ''

                  elif sιg == 10:
                    
                    if sub2 == '': pass

                    else:
                      oppel = open('Mαtιν.csv','a',encoding='utf8')
                      oppel.write('| ')
                      oppel.write(sub2)
                      oppel.write('\n')
                      oppel.close()
                      sub1 = ''
                      sub2 = '' 
                      break

                  elif sιg == 0o10: sub2 = sub2[:-1]

                  elif sιg != -1: sub2 += chr(sιg)

                  else: pass
                      
                except ValueError: pass

            elif νmαtιν == ord('-'):
              sub1 = ': ' ; sub2 = '' ; sub3 = '' ; numero = '' 

              while True:

                mαιteu(ιdeu)
                lαmνmαt()

                number = stdscr.getch()   

                if number == 27: sub1, sub2, sub3 = '' ; break

                elif number == 10:

                  try: 
                    if numero <= len(lines):
                      del lines[numero-1]
                      oppel = open('Mαtιν.csv','w',encoding='utf8')
                      oppel.truncate(0)
                      for i in lines:
                        oppel = open('Mαtιν.csv','a',encoding='utf8')
                        oppel.write(i)
                        oppel.close()
                    
                    else: pass

                    sub1, sub2, sub3 = ''
                    break 
                        
                  except: numero = 0 ; pass

                elif number == ord('º'):
                  sub1 = ': '
                  sub2, sub3 = ''                           
                        
                else:
                  if number != -1:
                      
                    try:
                        
                      number = chr(number)
                      numero = int(number)
                      sub2 = str(number)

                      oppel = open('Mαtιν.csv',encoding='utf8')
                      lines = oppel.readlines()
                      stdscr.addstr('\n')
                      sub3 = lines[numero-1]
                
                    except ValueError: pass
                            
                    except IndexError: sub3 = ''

                    else: pass

                  else: pass
            '''      
          
          elif νermαt == ord('+') or νermαt == ord('*'): # Copy 
            prompt = ': ' ; νmαν = '' ; toreg = '' ; numero = '' ; ιdeu = 'Vermαt'

            while True:
              mαιteu(0,ιdeu)
              lαmνmαt()
              stdscr.addstr(0,7,' │ ',curses.color_pair(2))
              stdscr.addstr('Copy')
              stdscr.addstr(' │',curses.color_pair(2))

              number = stdscr.getch()   

              if number == 27: prompt = '' ; νmαν = '' ; toreg = '' ; break

              elif number == 10: 
                νerseut = item[:-1]
                stνlαt('Tαg   ',f'{str(νerseut)}',7) ; prompt = '' ; νmαν = '' ; toreg = '' ; geuδ(νιdeu) ; break 
                      
              elif number == ord('º'): prompt = ': ' ; νmαν = '' ; toreg = ''                           
                      
              elif number == ord('ƀ'): νmαν += ' →  ' 

              elif number != -1:
                      
                try:
                  
                  number = chr(number)
                  numero = int(number)
                  strnum = str(number)

                  oppel = open(νιdeu,encoding='utf8')
                  lines = oppel.readlines()
                  item = lines[numero-1]
                  if len(lines) < 9: prompt = f'{strnum} │  {item}'
                  else: prompt = f'{strnum}  │  {item}'
          
                except ValueError: pass
                  
                except IndexError: toreg = ''

              else: pass

              '''elif number == curses.KEY_UP:
              numero -= 1
              number = chr(number)
              numero = int(number)
              strnum = str(number)

              elif number == curses.KEY_DOWN:
              numero += 1 '''

          elif νermαt == ord(':'): pass   # Verse  INTREV

          elif νermαt == ord('2'): # Improl 
           stνlαt('Vermαt  ','→ Improl',0) ; vlx = 8 ; vlαιu = ' Improl ' ; νιdeu = 'Vermαt.txt' ; geuδ('Vermαt.txt')

          elif νermαt == ord('3'): # Mυuιtsyα 
            stνlαt('Vermαt  ','→ Mυuιtsyα',0) ; vlx = 17 ; vlαιu = ' Mυuιtsyα ' ; νιdeu = 'Mυuιt Vermαt.txt' ; geuδ('Mυuιt Vermαt.txt')

          elif νermαt == ord('4'): # Pιlμα 
            stνlαt('Vermαt  ','→ Pιlμα',0) ; vlx = 28 ; vlαιu = ' Pιlμα ' ; νιdeu = 'Verpιlμα.txt' ; geuδ('Verpιlμα.txt')

          elif νermαt == ord('5'): # Lestαq 
            stνlαt('Vermαt  ','→ Lestαq',0) ; vlx = 36 ; vlαιu = ' Lestαq ' ; νιdeu = 'Lestαq.txt' ; geuδ('Lestαq.txt')

          elif νermαt == ord('6'): # Lestαq 3 
            stνlαt('Vermαt  ','→ Lestαq3',0)
            vlx = 45 ; vlαιu = ' Lestαq 3 '

            try:
              while 1:
                mαιteu(1,'Vermαt')

                stdscr.addstr(2,0,' Imαδ  │ Improl | Mυuιtsyα │ Pιlμα │ Lestαq │ Lestαq 3 │ Tαuderα │')
                stdscr.addstr(2,vlx,vlαιu,curses.color_pair(5))
                stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(2))

                with open('Lestαq 3.txt','r',encoding='utf8') as oppel: estαq = str(oppel.read())
                pad = curses.newpad(300,158)
                pad.addstr(estαq)
                pad.refresh(0,0,4,0,43,x-1)

                estαqer = stdscr.getch()

                if estαqer == 27 or estαqer == 10: vlx = 0 ; vlαιu = '' ; νιdeu = 'Vermαt.txt' ; return 
                elif estαqer == ord('º') or estαqer == ord('1'): νιdeu = 'Imαδ.csv' ; geuδ('Imαδ.csv') ; stνlαt('Vermαt  ','· Imαδ',0) ; vlx = 0 ; vlαιu = ' Imαδ ' ; break
                elif estαqer == ord('2'): νιdeu = 'Vermαt.txt' ; geuδ('Vermαt.txt') ; vlx = 8 ; vlαιu = ' Improl ' ; break
                elif estαqer == ord('3'): νιdeu = 'Mυuιt Vermαt.txt' ; geuδ('Mυuιt Vermαt.txt') ; vlx = 17 ; vlαιu = ' Mυuιtsyα ' ; break
                elif estαqer == ord('4'): νιdeu = 'Verpιlμα.txt' ; geuδ('Verpιlμα.txt') ; vlx = 28 ; vlαιu = ' Pιlμα ' ; break
                elif estαqer == ord('5'): νιdeu = 'Lestαq.txt' ; geuδ('Lestαq.txt') ; vlx = 36 ; vlαιu = ' Lestαq ' ; break
                elif estαqer == ord('t') or νermαt == ord('T'): Tαuder('Tαuder','│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ │ Lαg │')
                elif estαqer == ord('d') or νermαt == ord('D'): Tαuder('Dyαteν Tᾱuderα','| Lαg |')
                elif estαqer == ord('m') or νermαt == ord('M'): Tαuder('Mυuιtsyα Tαuder','| Lαg |')
                #elif estαqer == ord('0'): os.system('"Estαq 3.txt"')
                else: pass
            except Exception as e: stνlαt('Vermαt  ',f'{e}',0)

          elif νermαt == ord('t') or νermαt == ord('T'): Tαuder('Tαuder','│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ │ Lαg │'+' '*tαuspace+f'\u276f {date}')

          elif νermαt == ord('d') or νermαt == ord('D'): Tαuder('Dyαteν Tᾱuderα','| Lαg |')

          elif νermαt == ord('m') or νermαt == ord('M'): Tαuder('Mυuιtsyα Tαuder','| Lαg |')
 
          elif νermαt == ord('y') or νermαt == ord('Y'): # Dyeναstαq
            stνlαt('Vermαt  ','→ Dyeναstαq',0) 
            import webbrowser as wb
            wb.open('https://calendar.google.com/calendar/') 

          else: pass
          
          νermαt = stdscr.getch()

          curses.curs_set(False)
          stdscr.refresh()
          time.sleep(0.01)

      except Exception as e: stνlαt('Vermαt  ',f'{e}',0)

    def Dyαtēν():
      stνlαt(αδqαιt,'<DYATEV>',0)
      try:
        stdscr.clear()
        sub1 = '' ; sub2 = '' ; sub3 = '' ; sub4 = '' ; sub5 = '' ; dyαtspace = x-52


        while True:
          mαιteu(1,ιdeu ='Dyαteν')
          def lαmdyαt():
            with open('Dyαtēν.txt',encoding='utf8') as oppel: dyαteνα = oppel.read()
            stdscr.addstr(2,0,'│ Tαuder │ Mυutαuder │ Dyeναstαq │ Qαmpαr │'+' '*dyαtspace+f'\u276f {date}')
            stdscr.addstr(3,0,'\u2500'*x, curses.color_pair(2))
            stdscr.addstr(4,0,'\n')
            stdscr.addstr(dyαteνα)
            stdscr.addstr('\n')
            stdscr.addstr('\n')
            stdscr.addstr('\u2500'*x, curses.color_pair(2))
            stdscr.addstr(sub1)
            stdscr.addstr(sub2)
            stdscr.addstr('\n')
            stdscr.addstr('  ')
            stdscr.addstr(sub3)
            stdscr.addstr(sub4)
            stdscr.addstr(sub5)

          lαmdyαt()              
              
          dyαt = stdscr.getch()

          if dyαt == 27: stdscr.clear() ; break

          elif dyαt == ord('.'): # Sιguα 

            try:               
              while 1:
                line='' ; sub1='' ; sub2='' ; sub3=''

                while True:
                  sub1='Qαιse | '
              
                  mαιteu(0,ιdeu='Dyαteν │ Sιguα')
                  lαmdyαt()
                  sub2= f'{line}'   

                  sιguα = stdscr.getch()

                  if sιguα == 27:  sub1='' ; sub2='' ; sub3='' ; break

                  elif sιguα == ord('º'): sub2='' ; sub3=''

                  elif sιguα == 10:
                    if line != '':
                      with open('Dyαtēν.txt','a',encoding='utf8') as oppel:
                        oppel.write('\n')
                        oppel.write('\n')
                        oppel.write(line)
                        oppel.write(' │ ')
                        oppel.close()
                      
                      with open('Dyαteν Tᾱuderα.txt','a',encoding='utf8') as oppel:
                        oppel.write('\n')
                        oppel.write(line)
                        oppel.write(' │ ')
                      
                      sub1='' ; sub2='' ; sub3='' ; line=''
                      break

                    else: sub1='' ; sub2='' ; sub3='' ; line='' ; break
                          
                  elif sιguα == 0o10: line = line[:-1]

                  elif sιguα != -1: line += chr(sιguα)

                while True:
                  sub1='Lαιu | '
              
                  mαιteu(0,ιdeu='Dyαteν │ Sιguα')
                  lαmdyαt()
                  sub2= f'{line}'
                  
                  sιguα = stdscr.getch()

                  if sιguα == 27:  sub1='' ; sub2='' ; sub3='' ; break

                  elif sιguα == ord('º'): sub2='' ; sub3=''

                  elif sιguα == 10:
                    if line != '':
                      with open('Dyαtēν.txt','a',encoding='utf8') as oppel:
                        oppel.write(line)
                        oppel.write('\n')
                        oppel.close()
  
                      with open('Dyαteν Tᾱuderα.txt','a',encoding='utf8') as oppel:
                        oppel.write(line)
                        oppel.write(' │ ')

                      sub1='' ; sub2='' ; sub3='' ; line='' ; break
                    
                    else: sub1='' ; sub2='' ; sub3='' ; line='' ; break      
                          
                  elif sιguα == 0o10: line = line[:-1]

                  elif sιguα != -1: line += chr(sιguα)   
                  
                while True:
                  sub1='Sιeνιt | '

                  mαιteu(0,ιdeu='Dyαteν │ Sιguα')
                  lαmdyαt()
                  sub2= f'{line}'

                  sιguα = stdscr.getch()

                  if sιguα == 27: sub1='' ; sub2='' ; sub3='' ; break

                  elif sιguα == ord('º'): sub2='' ; sub3=''

                  elif sιguα == 10:
                    if line != '':
                      with open('Dyαtēν.txt','a',encoding='utf8') as oppel:
                        oppel.write('────────┤')
                        oppel.write('\n')                        
                        oppel.write(f'Sιeνιt  │ {line}')
                        oppel.write('\n')
                        oppel.close()
                      
                      with open('Dyαteν Tᾱuderα.txt','a',encoding='utf8') as oppel:
                        oppel.write(line)
                        oppel.write(' │ ')                      

                      sub1='' ; sub2='' ; sub3='' ; line='' ; break
                    
                    else: sub1='' ; sub2='' ; sub3='' ; line='' ; break
                          
                  elif sιguα == 0o10: line = line[:-1]

                  elif sιguα != -1: line += chr(sιguα)

                while True:
                  sub1='Iuνor | '

                  mαιteu(0,ιdeu='Dyαteν │ Sιguα')
                  lαmdyαt()
                  sub2= f'{line}'

                  sιguα = stdscr.getch()

                  if sιguα == 27: sub1='' ; sub2='' ; sub3='' ; break

                  elif sιguα == ord('º'): sub2='' ; sub3=''

                  elif sιguα == 10:
                    if line != '':

                      with open('Dyαtēν.txt','a',encoding='utf8') as oppel:
                        oppel.write(f'Iuνorαt │ {line}')
                        oppel.write('\n')
                        oppel.close()
                      
                      with open('Dyαteν Tᾱuderα.txt','a',encoding='utf8') as oppel:
                        oppel.write(line)
                        oppel.write(' │ ')                           
                      
                        sub1='' ; sub2='' ; sub3='' ; line=''
                        break

                    else: sub1='' ; sub2='' ; sub3='' ; line='' ; break
                    
                  elif sιguα == 0o10: line = line[:-1]

                  elif sιguα != -1: line += chr(sιguα)

                while True:
                  sub1='Augēt | '

                  mαιteu(0,ιdeu='Dyαteν │ Sιguα')
                  lαmdyαt()
                  sub2= f'{line}'

                  sιguα = stdscr.getch()

                  if sιguα == 27: sub1='' ; sub2='' ; sub3='' ; break

                  elif sιguα == ord('º'): sub2='' ; sub3=''

                  elif sιguα == 10:
                    if line != '':

                      with open('Dyαtēν.txt','a',encoding='utf8') as oppel:
                        oppel.write(f'Augēt   │ {line}')
                        oppel.write('\n')
                        oppel.close()
                      
                      with open('Dyαteν Tᾱuderα.txt','a',encoding='utf8') as oppel:
                        oppel.write(line)
                        oppel.write(' │ ')  

                      sub1='' ; sub2='' ; sub3='' ; line='' ; break

                    else: sub1='' ; sub2='' ; sub3='' ; line='' ; break
                          
                  elif sιguα == 0o10: line = line[:-1]

                  elif sιguα != -1: line += chr(sιguα)

                while True:
                  sub1='Dyαutαl | '

                  mαιteu(0,ιdeu='Dyαteν │ Sιguα')
                  lαmdyαt()
                  sub2= f'{line}'

                  sιguα = stdscr.getch()

                  if sιguα == 27: sub1='' ; sub2='' ; sub3='' ; break

                  elif sιguα == ord('º'): sub2='' ; sub3='' 

                  elif sιguα == 10:
                    if line != '':

                      with open('Dyαtēν.txt','a',encoding='utf8') as oppel:
                        oppel.write(f'Dyαutαl │ {line}')
                        oppel.write('\n')
                        oppel.close()

                      with open('Dyαteν Tᾱuderα.txt','a',encoding='utf8') as oppel:
                        oppel.write(line)
                        oppel.write(' │ ')

                      sub1='' ; sub2='' ; sub3='' ; line=''

                      while True:
                        sub1='Dyαutαl | '

                        mαιteu(0,ιdeu='Dyαteν │ Sιguα')
                        lαmdyαt()
                        sub2= f'{line}'

                        sιguα = stdscr.getch()

                        if sιguα == 27: sub1='' ; sub2='' ; sub3='' ; break

                        elif sιguα == ord('º'): sub2='' ; sub3=''

                        elif sιguα == 10:
                          if line != '':

                            with open('Dyαtēν.txt','a',encoding='utf8') as oppel:
                              oppel.write(f'        │ {line}')
                              oppel.write('\n')
                              oppel.close()
                            
                            with open('Dyαteν Tᾱuderα.txt','a',encoding='utf8') as oppel:
                              oppel.write(line)
                              oppel.write(' │ ')
                              oppel.write('\n')
                              oppel.write('\n')
                              oppel.write('\n')

                            stνlαt('Dyαteν  ',f'→ Sιguα',0) ; stdscr.clear()

                            sub1='' ; sub2='' ; sub3='' ; line='' ; break

                          else:
                            sub1='' ; sub2='' ; sub3='' ; line=''
                            with open('Dyαteν Tᾱuderα.txt','a',encoding='utf8') as oppel:
                              oppel.write('\n')                          
                              oppel.write('\n')                          
                              oppel.write('\n')                          
                            break
                                
                        elif sιguα == 0o10: line = line[:-1]

                        elif sιguα != -1: line += chr(sιguα) 

                      break

                    else:
                      sub1='' ; sub2='' ; sub3='' ; line=''
                      with open('Dyαteν Tᾱuderα.txt','a',encoding='utf8') as oppel:
                        oppel.write('\n')
                        oppel.write('\n')
                        oppel.write('\n')
                      break
                          
                  elif sιguα == 0o10: line = line[:-1]

                  elif sιguα != -1: line += chr(sιguα)                    


                break
                    
            except Exception as e:
              stνlαt('Dyαteν  ',f'→ Sιguα  │ {e}',0)
              while True:
                mαιteu(ιdeu='Dyαteν')
                lαmdyαt()
                sub1=f'> {e}'
                αq = stdscr.getch()
                if αq == 10:
                  sub1=''
                  sub2=''
                  sub3=''
                  break
                else: pass
                
          elif dyαt == ord(','):

            try:
              line='' ; sub1=': ' ; sub2='' ; sub3= ''
                      
              while 1:
                mαιteu(0, ιdeu='Dyαteν │ Verqom')
                lαmdyαt()

                try:

                  sub2=f'{line}'

                  dyαt = stdscr.getch()

                  if dyαt == 27: sub1='' ; sub2='' ; sub3='' ; break

                  elif dyαt == ord('º'): sub2='' ; sub3=''

                  elif dyαt == 10:

                    sub4 = '→ '

                    while 1:
                      mαιteu(ιdeu='Dyαteν')
                      lαmdyαt()
                      stdscr.addstr(2,9,' Verqōm ', curses.color_pair(5))                    


                      eudαμl = stdscr.getch()

                      if eudαμl == 27: sub1='' ; sub2='' ; sub3='' ; sub4 = '' ; sub5 = '' ; break

                      elif eudαμl == 10:

                        lines[line-1] = sub5 + '\n'
                            
                        if line-1 <= len(lines): pass
                          #with open('Dyαtēν.txt','w',encoding='utf8') as oppel:
                          #  for i in lines: oppel.write(i)

                        else: pass

                        sub1 = '' ; sub2 = '' ; sub3 = '' ; sub4 = '' ; sub5 = '' ; break

                      elif eudαμl == 0o10: sub5 = sub5[:-1]

                      elif eudαμl != -1: sub5 += chr(eudαμl)

                      else: pass

                  elif dyαt == 0o10:
                    line = line[:-1]
                    with open('Dyαtēν.txt',encoding='utf8') as oppel:
                      lines = oppel.readlines()
                      sub3 = lines[int(line)-1]
                          
                  elif dyαt != -1:
                    line += chr(dyαt)
                    with open('Dyαtēν.txt',encoding='utf8') as oppel:
                      lines = oppel.readlines()
                      sub3 = lines[int(line)-1]
                       
                  else: pass

                  stνlαt('Dyαteν  ','→ Verqom',0)

                except: sub1=': ' ; sub3='' ; pass

            except Exception as e:
              stνlαt('Dyαteν  ',f'→ Verqom │ {e}',0)
              while True:
                mαιteu(ιdeu='Dyαteν')
                lαmdyαt()
                sub1=f'> {e}'
                αq = stdscr.getch()
                if αq == 10:
                  sub1=''
                  sub2=''
                  sub3=''
                  break
                else: pass  

          elif dyαt == ord('-'): # Iuαq 
            try:
              sub1 = ': ' ; sub2 = '' ; sub3 = '' ; numero = ''

              while True:
                mαιteu(0,ιdeu= 'Dyαteν')
                lαmdyαt()
                stdscr.addstr(0,7,'│ Iuαq')

                number = stdscr.getch()                  

                if number == 27: sub1 = '' ; sub2 = '' ; sub3 = '' ; break

                elif number == ord('º'): sub1 = ': ' ; sub2 = '' ; sub3 = ''

                elif number == 10:
                    if numero <= len(lines):
                      del lines[numero-1]
                      oppel = open('Dyαtēν.txt','w',encoding='utf8')
                      for i in lines:
                        oppel.write(i)
                      oppel.close()
                      stνlαt('Dyαteν  ',f'→ Iuαq │ {sub3}',0) ; stdscr.clear()
                    else: pass
                    sub1= '' ; sub2 = '' ; sub3 = '' ; break                

                else:
                  if number != -1:
                    try:
                      number = chr(number)
                      numero = int(number)
                      sub2 = str(number)
                
                      oppel = open('Dyαtēν.txt', encoding='utf8')
                      lines = oppel.readlines()
                      sub3 = lines[numero-1]
                      oppel.close()
                                    
                    except ValueError: sub1 = ': ' ; sub2 = '' ; sub3 = ''

                    except IndexError: pass
                    
                  else: pass
              
            except Exception as e: stνlαt('Dyαteν  ',f'→ Iuαq │ {e}',0) ; sub1= ''

          elif dyαt == ord('_'): # Aqtαν
            try:
              sub1 = 'Seνdαl uα Dyαteν αqtαν ?'

              while True:
                lαmdyαt()

                stdscr.addstr(0,7,'│ Aqtαν')

                number = stdscr.getch()                  

                if number == 27: sub1 = '' ; break   

                elif number == 10:
                  with open('Dyαtēν.txt','w',encoding='utf8') as oppel: oppel.truncate(0)
                  sub1 = '' ; mαιteu(0,ιdeu= 'Dyαteν') ; break

                else: pass
            
            except Exception as e: stνlαt('Dyαteν  ',f'→ Aqtαν │ {e}',0)

          elif dyαt == ord('1') or dyαt == ord('t') or dyαt == ord('T'): Tαuder('Dyαteν Tᾱuderα','| Lαg |')
            
          elif dyαt == ord('2') or dyαt == ord('m') or dyαt == ord('M'): Tαuder('Mυuιtsyα Tαuder','│ Lαg │')

          elif dyαt == ord('3') or dyαt == ord('d') or dyαt == ord('D'): # Dyeναstαq 
            stνlαt('Dyαteν  ','→ Dyeναstαq',0)
            import webbrowser
            webbrowser.open("https://calendar.google.com/")
                
          elif dyαt == ord('4') or dyαt == ord('q') or dyαt == ord('Q'): # Qαmpαr 
            stνlαt('Dyαteν  ','→ Qαmpαr',0)
            import webbrowser
            webbrowser.open('https://www.google.com/maps')
                      
          elif dyαt == ord('0'):
            stνlαt('Dyαteν  ','→ Lαg',0)
            import os
            os.system('Dyαtēν.txt')

          else: pass
        stdscr.refresh()
        time.sleep(0.01)
      except Exception as e: stνlαt('Dyαteν  ',f'{e}',0) ; return

    def Augestαq():
      stνlαt(αδqαιt,'<ANGESTAQ>',0) 
      try:
        stdscr.clear()
        menu='│ Iuslag │ Isqyαu │ Mαuslαg │'
        sub1 = '' ; sub2 = '' ; numero = ''

        while 1:

          mαιteu(1,ιdeu='Augestαq')
          def lαmαugest():
            with open('Augestαq.csv',encoding='utf8') as oppel: tαuder = oppel.read()
            with open('Augest.Isqyαu.txt','r',encoding='utf8') as oppel: αugestlines = len(oppel.readlines()) ; oppel.seek(0) ; αugιsqyαu = oppel.read()
            stdscr.addstr(2,0,menu)
            stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(2))
            pad1 = curses.newpad(40,100)
            pad1.addstr(tαuder)
            pad1.refresh(0,0,5,0,39,49)
            pad2 = curses.newpad(1000,100)
            pad2.addstr(αugιsqyαu)
            pad2.refresh(αugestlines-18,0,5,60,38,150)

            stdscr.addstr(40,0,'\u2500'*x,curses.color_pair(2))
            stdscr.addstr(sub1)
            stdscr.addstr(sub2)

          lαmαugest()

          αugest = stdscr.getch()

          if αugest == 27: stdscr.clear() ; break

          elif αugest == ord('º'): sub1='' ; sub2=''

          elif αugest == ord('.'):
            with open('Augestαq.csv','r',encoding='utf8') as oppel: αugestαq = oppel.readlines()
            import datetime
            sιeνιt = datetime.date.today()
            sιeν = sιeνιt.strftime('%d%m')
            with open('Augestαq.csv','a',encoding='utf8') as oppel:
              oppel.write('\n')
              oppel.write('\n')
              oppel.write(str(sιeν))
              oppel.write('   │')
              oppel.write('\n')
              oppel.write('\n')
            sub1='>'
            while 1:
              section=''
              def lαmαusιg(z):
                mαιteu(1,ιdeu='Augestαq')
                stdscr.addstr(0,8,' │ ',curses.color_pair(2))
                stdscr.addstr('Sιguα')
                stdscr.addstr(' │',curses.color_pair(2))
                try:
                  with open('Augestαq.csv',encoding='utf8') as oppel: tαuder = oppel.read()
                except: pass
                stdscr.addstr(2,0,'│ Mαyeq │ Otaleu │ Auqopt │   ')
                if section == '': stdscr.addstr(2,z,'',curses.color_pair(5))
                else: stdscr.addstr(2,z,f' {section} ',curses.color_pair(5))
                stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(2))
                stdscr.addstr('\n' + tαuder)
                #with open('Augest.Isqyαu.txt','r',encoding='utf8') as oppel: αugestlines = len(oppel.readlines()) ; oppel.seek(880) ; αugιsqyαu = oppel.read()
                #sig = curses.newwin(30,20,5,50)
                #sig.addstr(0,0,αugιsqyαu)
                #sig.refresh()

                #stdscr.addstr('\u2500'*x,curses.color_pair(2))
              lαmαusιg(0)   

              def Ausιguα(z):
                  sub1='Delαus │ ' ; sub2=''

                  while 1:

                    lαmαusιg(z)
                    stdscr.addstr(sub1)
                    stdscr.addstr(sub2)

                    delαus = stdscr.getch()

                    if delαus == 27: stdscr.clear() ; sub1='>' ; sub2='' ; break
                    
                    elif delαus == 10:
                      with open('Augestαq.csv','a',encoding='utf8') as oppel:
                        oppel.write(section)
                        oppel.write('\n')
                        oppel.write('\u2500'*7)
                        oppel.write('┬')
                        oppel.write('\u2500'*6)
                        oppel.write('\n')
                        oppel.write('Delαus │ ')

                        if int(sub2) < 10:
                          eν1 = int(sub2)
                          oppel.write(' ')
                          oppel.write(str(sub2))
                          oppel.write(' ge')
                          oppel.write('\n')

                        else:

                          if int(sub2) % 10 == 0:
                            eν1 = int(sub2)
                            sub2 = int(sub2) // 10
                            oppel.write(' ')
                            oppel.write(str(sub2))
                            oppel.write(' pα')
                            oppel.write('\n')
                          else:
                            eν1 = int(sub2)
                            oppel.write(str(sub2))
                            oppel.write(' ge')
                            oppel.write('\n')
                      
                      sub1 = 'Dαuqαδ │ ' ; sub2 = ''
                      
                      while 1:

                        lαmαusιg(z)
                        stdscr.addstr(sub1)
                        stdscr.addstr(sub2)

                        dαuqαδ = stdscr.getch()

                        if dαuqαδ == 27: sub1='>' ; sub2='' ; break
                        
                        elif dαuqαδ == 10:
                          if sub2 == '' : eν2 = 0 ; pass

                          else:
                            with open('Augestαq.csv','a',encoding='utf8') as oppel:
                              oppel.write('Dαuqαδ │ ')                            
                              if int(sub2) < 10:                                    
                                eν2 = int(sub2)
                                oppel.write(' ')
                                oppel.write(str(sub2))
                                oppel.write(' ge')
                                oppel.write('\n')

                              else:

                                if int(sub2) % 10 == 0:
                                  eν2 = int(sub2)
                                  sub2 = int(sub2) // 10
                                  oppel.write(' ')
                                  oppel.write(str(sub2))
                                  oppel.write(' pα')
                                  oppel.write('\n')                          
                                else:
                                  eν2 = int(sub2)
                                  oppel.write(str(sub2))
                                  oppel.write(' ge')
                                  oppel.write('\n')                          

                          sub1 = 'Soleu │ ' ; sub2 = ''

                          while 1:

                            lαmαusιg(z)
                            stdscr.addstr(sub1)
                            stdscr.clrtoeol()
                            stdscr.addstr(sub2)
                            stdscr.clrtoeol()

                            soleu = stdscr.getch()

                            if soleu == 27: sub1='>' ; sub2='' ; break
                            
                            elif soleu == 10:
                              with open('Augestαq.csv','a',encoding='utf8') as oppel:
                                oppel.write('Soleu  │ ')

                                if int(sub2) < 10:
                                  eν3 = int(sub2)
                                  oppel.write(' ')
                                  oppel.write(str(sub2))
                                  oppel.write(' ge')
                                  oppel.write('\n') 

                                else:
                                  if int(sub2) % 10 == 0:
                                    eν3 = int(sub2)
                                    sub2 = int(sub2) // 10
                                    oppel.write(' ')
                                    oppel.write(str(sub2))
                                    oppel.write(' pα')
                                    oppel.write('\n')                          
                                  else:
                                    eν3 = int(sub2)
                                    oppel.write(str(sub2))
                                    oppel.write(' ge')
                                    oppel.write('\n')                          

                                Sιguα = eν1 + eν2 + eν3
                                
                                oppel.write('Sιguα  │ ')

                                if int(Sιguα) < 10:
                                  
                                  oppel.write(' ')
                                  oppel.write(str(Sιguα))
                                  oppel.write(' ge')
                                  oppel.write('\n')                          
                                  oppel.write('\n')

                                else:

                                  if int(Sιguα) % 10 == 0:
                                    Sιguα = int(Sιguα) // 10
                                    oppel.write(' ')
                                    oppel.write(str(Sιguα))
                                    oppel.write(' pα')
                                    oppel.write('\n')                          
                                    oppel.write('\n')
                                  else:
                                    oppel.write(str(Sιguα))
                                    oppel.write(' ge')
                                    oppel.write('\n')                          
                                    oppel.write('\n')

                              with open('Augest.Isqyαu.txt','a',encoding='utf8') as oppel:
                                oppel.write('\n')
                                for i in αugestαq: oppel.write(i)
                                oppel.write('\n')
                                oppel.write('\n')
                                oppel.write('\n')

                              '''with open('Augestαq.csv','w',encoding='utf8') as oppel:
                                oppel.write(sιeν)
                                oppel.write(' │')
                                oppel.write('\n')
                                oppel.write('\n')
                                oppel.write('Mαyeq')
                                oppel.write('\n')
                                oppel.write('───────┬──────')
                                oppel.write('\n')
                                oppel.write('Delαus │ ')
                                oppel.write(str(eν1))
                                oppel.write('\n')
                                oppel.write('Dαuqαδ │ ')
                                oppel.write(str(eν2))
                                oppel.write('\n')
                                oppel.write('Soleu  │ ')                                  
                                oppel.write(str(eν3))
                                oppel.write('\n')
                                oppel.write('Sιguα  │ ')
                                oppel.write(str(Sιguα))
                                oppel.write('\n')
                                oppel.write('\n')
                                oppel.write('\n')'''
                            
                              break
                            
                            elif soleu == 0o10: sub2 = sub2[:-1]
                            elif soleu != -1: sub2 += chr(soleu)
                            else: pass
                      
                          break

                        elif dαuqαδ == 0o10: sub2 = sub2[:-1]
                        elif dαuqαδ != -1: sub2 += chr(dαuqαδ)
                        else: pass

                      break
                    
                    elif delαus == 0o10: sub2 = sub2[:-1]
                    elif delαus != -1: sub2 += chr(delαus)
                    else: pass

              sιguα = stdscr.getch()

              if sιguα == 27:  menu='│ Sιguα │ Iuαq │ Iuslαg │ Isqyαu │ Mαuslαg │ Aqtαudeμ │' ; sub1='' ; break
              if sιguα == ord('m') or sιguα == ord('M'): section='Mαyeq' ; Ausιguα(1)         
              elif sιguα == ord('o') or sιguα == ord('O'): section='Otαleu' ; Ausιguα(9)
              elif sιguα == ord('a') or sιguα == ord('A'):  section='Auqopt' ; Ausιguα(17)
              elif sιguα == ord('b') or sιguα == ord('B'):
                section='' ; sub1='Bιuαus │ ' ; sub2=''

                while 1:

                  lαmαusιg(0)
                  stdscr.addstr(sub1)
                  stdscr.addstr(sub2)

                  bιuαus = stdscr.getch()

                  if bιuαus == 27: stdscr.clear() ; sub1='>' ; sub2='' ; break
                  
                  elif bιuαus == 10:
                    with open('Augestαq.csv','a',encoding='utf8') as oppel:
                      oppel.write('Bιuαus │ ')
                      oppel.write(' ')
                      oppel.write(str(sub2))
                      oppel.write(' us')
                      oppel.write('\n')                
                    sub1='' ; sub2='' ; break

                  elif bιuαus == 0o10: sub2 = sub2[:-1]              
                  elif bιuαus != -1: sub2 += chr(bιuαus)
                  else: pass
              elif sιguα == ord('0'): import os ; os.system('Augestαq.csv')
              else: pass
            
          elif αugest == ord('-'):
            while 1:
              mαιteu(1,ιdeu='Augestαq')
              stdscr.addstr(0,8,' │ ',curses.color_pair(2))
              stdscr.addstr('Iuαq')
              stdscr.addstr(' │',curses.color_pair(2))
              lαmαugest()
              sub1='Seνdαl uα Augestαq αqtαν ?'
              sιguα = stdscr.getch()

              if sιguα == 27: sub1='' ; sub2='' ; break
              if sιguα == 10:
                sub1='' ; sub2=''
                with open('Augestαq.csv','r',encoding='utf8') as oppel:
                  ιsqyαu = oppel.read()
                with open('Augest.Isqyαu.txt','a',encoding='utf8') as oppel:
                  try:
                    for i in ιsqyαu:
                      oppel.write(i)
                    ιsqyαutαl = ' →  Isqyαu sιguet'
                  except Exception as e: stνlαt('Augestαq',f'Isqyαu ιuαqtαgeu',0)
                with open('Augestαq.csv','w',encoding='utf8') as oppel:
                  oppel.truncate(0)

                stνlαt('Augestαq',f'Augestαq αqtανeu {ιsqyαutαl}',0)
                stdscr.clear()
                break
              else: pass
   
          elif αugest == ord('i') or αugest == ord('I'): import os ; os.system('Augest.Isqyαu.txt')

          elif αugest == ord('m') or αugest == ord('M'): import os ; os.system('Augest.Mαuslαg.txt')

          elif αugest == ord('0'): import os ; os.system('Augestαq.csv')
       
          else: pass
          
          stdscr.refresh()
          time.sleep(0.01)
      
      except Exception as e: stνlαt('Augestαq',f'→ {e}',0) ; pass

    def Mυuιtsyα(): 
      stνlαt(αδqαιt,'<MUNITSYA>',0)
      stdscr.clear() ; sub2='' ; sub3=''

      def lαmυuιt(z,section,sub1):
        try: 
          mαιteu(1,'MUNITSYA')
          stdscr.addstr(2,0,'│ Iνouιm │ Tαuder │ Vermαt │ Terιguer │ Teνuα │')
          stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(2))
          try: 
          
            import pandas as pd
            import numpy as np
            import csv
            datos = pd.read_csv('Mυuιmα Stαgeu.csv',encoding='utf8',sep='\t')
            data = pd.DataFrame(datos)
            table = data.to_string(index=False)
            tαuder = table
      
          except FileNotFoundError as e: stνlαt('Stαgeu',f'{e}','Mυuιtsyα') ; tαuder = 'Mυuιmα Stαgeu αqtαgeu'
          except Exception as e: stνlαt('Stαgeu',f'{e}','Mυuιtsyα') ; tαuder = e

          stdscr.addstr(2,z,section,curses.color_pair(5))              
          stdscr.addstr(5,0,tαuder)
          stdscr.addstr('\n'+'\n')
          stdscr.addstr('\u2500'*x,curses.color_pair(2))
          stdscr.addstr(sub1)
          stdscr.addstr(sub2)
          stdscr.addstr('\n')            
          stdscr.addstr(sub3)

        except Exception as e: stνlαt('Stαgeu',f'{e}','Mυuιtsyα')

      while 1: 
        lαmυuιt(0,'','')

        mυuιt = stdscr.getch()

        if mυuιt == 27: stdscr.clear() ; return

        elif mυuιt == ord('.'): # Sιguα 
            lαιue = '' ; αuemαt = '' ; sιeνιt = '' ; toreg = ''

            sub3 = f'{lαιue}  {αuemαt}  {sιeνιt}  {toreg}'

            while 1: # Lαιu
              lαmυuιt(1,' Sιguα ','Lαιu   │ ')
              mυusιg = stdscr.getch()

              if mυusιg == 27: break
              elif mυusιg == ord('º'): sub2=''
              elif mυusιg == ord('t') or mυusιg == ord('T'): import os ; os.system('Mυuιtsyα.txt')
              elif mυusιg == 10: lαιue = sub2 ; sub3 = f'> {lαιu}' ; sub2='' ; break
              elif mυusιg == 0o10: sub2 = sub2[:-1]
              elif mυusιg != -1: sub2 += chr(mυusιg)
              else: pass

              stdscr.refresh()
              time.sleep(0.01)
              
            while 1: # Auemαt
              mαιteu(1,ιdeu='MUNITSYA')
              lαmυuιt(1,' Sιguα ','Auemαt │ ')
              mυusιg = stdscr.getch()

              if mυusιg == 27: sub1='' ; break
              elif mυusιg == ord('º'): sub2=''
              elif mυusιg == 10: αuemαt = sub2 ; sub3 += '  ' + αuemαt ; sub2='' ; break
              elif mυusιg == 0o10: sub2 = sub2[:-1]      
              elif mυusιg != -1: sub2 += chr(mυusιg)
              else: pass

              stdscr.refresh()
              time.sleep(0.01)

            while 1: # Sιeνιt
              mαιteu(1,ιdeu='MUNITSYA')
              lαmυuιt(1,' Sιguα ','Sιeνιt │ ')
              mυusιg = stdscr.getch()

              if mυusιg == 27: sub1='' ; break
              elif mυusιg == ord('º'): sub2=''
              elif mυusιg == 10: sιeνιt = sub2 ; sub3 += '  ' + sιeνιt ; sub2='' ; break
              elif mυusιg == 0o10: sub2 = sub2[:-1]
              elif mυusιg != -1: sub2 += chr(mυusιg)
              else: pass

              stdscr.refresh()
              time.sleep(0.01)

            while 1: # Toreg
              mαιteu(1,ιdeu='MUNITSYA')
              lαmυuιt(1,' Sιguα ','Toreg │ ')
              mυusιg = stdscr.getch()

              if mυusιg == 27: sub1='' ; break
              elif mυusιg == ord('º'): sub2=''
              elif mυusιg == 10: toreg = sub2 ; sub3 += '  ' + toreg ; sub1='' ; sub2='' ; sub3='' ; break
              elif mυusιg == 0o10: sub2 = sub2[:-1]
              elif mυusιg != -1: sub2 += chr(mυusιg)
              else: pass

              #Crear menú de géneros según la métrica

            class Mυuιt:
              def __init__(ιzeu,lαιue,sιeνιt,αuemαt,toreg): #MυuEstαq,Intro,Estrofa,Coro,Puente,Outro,ιdeu):
                ιzeu.lαιue = lαιue
                ιzeu.sιeνιt = sιeνιt
                ιzeu.αuemαt = αuemαt
                ιzeu.toreg = toreg
            Mυuιt = Mυuιt(lαιue,sιeνιt,αuemαt,toreg) #MυuEstαq,Intro,Estrofa,Coro,Puente,Outro,ιdeu)
            MυuTαudrα = [Mυuιt.lαιue,Mυuιt.αuemαt,Mυuιt.sιeνιt,Mυuιt.toreg]

            def MυuEstαq():
              import csv

              
              oppel = open('Mυuιmα Stαgeu.csv','a',encoding='utf8', newline='')
              writer= csv.writer(oppel, delimiter='\t', quoting=csv.QUOTE_NONE)
              writer.writerow(MυuTαudrα)
              oppel.close()
              

              '''conn = sq.connect('Lιuem.sqlite')
              c = conn.cursor()
              #c.execute("create table mυuιmα (Lαιu text, Auemαt text, Sιeν int, Toreg text)")
              params = (lαιue,αuemαt,sιeνιt,toreg)
              c.execute("insert into mυuιmα values (?,?,?,?)",params)
              conn.commit()
              c.execute('select * from mυuιmα')
              table = c.fetchall()
              print()
              for i in table:
                print(table[0],table[1],table[2])
              conn.close()
              input()'''

            MυuEstαq()

            stdscr.refresh()
            time.sleep(0.01)

        elif mυuιt == ord(','): # Verqom  INTREV 
          while 1: pass

        elif mυuιt == ord('-'): # Iuαq  INTREV 
          while 1: pass

        elif mυuιt == ord('1'): # Uuιtαm Iνouιm 
          stνlαt('Mυuιtsyα','→ Iνouιm',0) ; import os ; os.system(r"C:\Users\Leane\OneDrive\Escritorio\Logreuα\Mpxplay_v167_Win32_FFmpeg\mpxplayf.exe")
          curses.curs_set(False)

        elif mυuιt == ord('2') or mυuιt == ord('t'):#  Mυuιtsyα Tαuder 
          Tαuder('Mυuιtsyα Tαuder','| Lαg |')

        elif mυuιt == ord('3'):# Terιguer
          import subprocess
          subprocess.Popen(r'"C:\ProgramData\Ableton\Live 10 Suite\Program\Ableton Live 10 Suite.exe"')

        else: pass

        stdscr.refresh()
        time.sleep(0.01)
        
  # Zona Operativa

    # Operaciones de inicio
    lαmlιuem(0,1,'Stαuνor') ; stνlαt(αδqαιt,f'<..LINEM..>',0)
    try: os.chdir(r'G:\Mi unidad\Lιuem Stαuνor')
    except Exception as e: stνlαt('Stαuνor ',f'→ {e}',0)
    stνlαt(αδqαιt,os.getcwd(),1)
    #tαg(1,1,S.clear,S.ιdeu,S,S.prαν,S.log,S.υprαν,S.ιzprαν,'Aδqαιt')

    while 1: 
      # Mαιteu Iδᾱt    
      stdscr.nodelay(True)
      curses.curs_set(False)
      lestαq(0,S.ιdeu,S.prαν,S.log,S.υprαν,S.ιzprαν)
      stdscr.addstr('.',curses.color_pair(2))


      # MASENTA

      key = stdscr.getch(2,2) 

      # Verseuα

      if key == 27:        #         Aqtαgeu | Lιuem αqtαgeu 
        while 1:
          prαν = '0 Aqtαgeu\n1 Eudαμl Stαuνor'
          mαιteu(0,'Stαuνor')
          stdscr.addstr(2,0,prαν)
          mαν = stdscr.getch()

          if mαν == ord('0'): exit()

          elif mαν == 27: prαν = '' ; break
          elif mαν == ord('1'):
            import subprocess
            comando= r'C:\Users\Leane\OneDrive\Escritorio\Lιuem\main.py'
            subprocess.Popen(["cmd", "/k", comando]) ; stνlαt(αδqαιt,'Lιuem Stαuνor',2) ; break


          else: pass
      elif key == ord('ƀ'):#         Lιgeu | Iutorαg lιgeu 
        tαg(1,1,S.clear,'Stαuνor',S,'Lιgeu → ','','','','lιgeu') ; S = Lαmseut(0,'Stαuνor','','','','')
      elif key == ord('ǀ'):#         ιutel | Logreuαm ιutel 
        ιmαν = '' ; tαg(1,1,S.clear,'Stαuνor',S,'Iutel → ','','','','ιutel') ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = ''
      elif key == ord('ª'):#          δoνt | System δoνt 
        tαg(1,0,1,S.ιdeu,S,'Seνdαl uα sιstem δoνt ?','','','','δoνt')
      elif key == ord('+'):#          Copy | 
        νerseut = ιmαν
      elif key == ord('ç'):#         Paste | 
        ιmαν = νerseut
      elif key == ord('#'):#    Calculator | 
        stνlαt('Stαuνor ','<CALC>',0) ; num1 = int ; char = ''
        while 1:
          lestαq(0,'Calculator','→ ','','','')
          stdscr.addstr('.',curses.color_pair(2))

        
          key = stdscr.getch()

          if key == 27: ιmαν = '' ; break
          elif key == ord('+'):  #    Sιguα
            num1 = ιmαν ; ιmαν = '' ; tαg(1,1,0,'Calculator','',f'→ {num1} + ','','','','Calc.sιg')
          elif key == ord('ç'):#    Resta
            num1 = ιmαν ; ιmαν = '' ; tαg(1,1,0,'Calculator','',f'→ {num1} - ','','','','Calc.rest')
          elif key == ord('*'):#    Multiplicación
            num1 = ιmαν ; ιmαν = '' ; tαg(1,1,0,'Calculator','',f'→ {num1} * ','','','','Calc.multi')
          elif key == ord('Ç'):#    División 
            num1 = ιmαν ; ιmαν = '' ; tαg(1,1,0,'Calculator','',f'→ {num1} / ','','','','Calc.div')
          elif key == 0o10: ιmαν = ιmαν[:-1]
          elif key != -1:
            try:
              num1 = int(chr(key)) ; ιmαν += str(num1)
            except Exception as e: stνlαt(αδqαιt,f'Calc   │ {e}',0)
          else: pass

      elif key  == 10:# 
        S = Lαmseut(0,'Stαuνor','','','','')
        
        # Tαuder

        if ιmαν == 'invash':#         Qαιteu ιutorαg νerseut 
          S.log = 'Iuναδ ιutorαg | ' ; S.υprαν = r'G:\Mi unidad\Lιuem Stαuνor'

        elif ιmαν == 'mativ':#        Nostαl ιsteg tαuder 
          S.prαν = f'Mαtιν \u276f  ' + date2

        elif ιmαν == 'net':#          WiFi Connection 
          import psutil
          stats = psutil.net_if_stats()
          
          for interface, stat in stats.items():
            if interface == 'Wi-Fi':
              if stat.isup: S.υprαν = f"{interface} ιuμeuzeu"
              else: S.υprαν = f"{interface} ιuμeuzαqeu"              
            else: pass
        
        elif ιmαν == 'lanter':#       Lαuter Tαuderα 
          from screeninfo import get_monitors
          for m in get_monitors(): S.υprαν = f"Lαuter: {m.name}\nWidth: {m.width} ({str(x)})\nHeight: {m.height} ({str(y)})\n"
                     
 
        # Aιleus

        elif ιmαν == 'tag':#          Python Module ιtαg 
          stdscr.clear() ; ιmαν = '' ; tαg(1,1,0,'Stαuνor',S,'> ','','','','tαg')
                    
        elif ιmαν == 'dos':#          MS-DOS 
          curses.endwin() ; lαmlιuem(1,1,'MS-DOS') ; os.system('cmd') ; lαmlιuem(0,1,'Stαuνor')

        # Lαuterα

        elif ιmαν == 'izvartag':#     Izναrtαg tαuderα 
          ιmαν = ''        
          
          while 1:
  -          import psutil
            ιzναrtαg = psutil.sensors_battery()
            if ιzναrtαg.power_plugged == True: ιzιδαt = 'Tαgeu'
            else: ιzιδαt = 'Aqtαgeu'
            lestαq(0,'Izναrtαg','','',f'Sναrt   | {ιzναrtαg.percent}',f'Iuμαuze | {ιzιδαt}')
            
            ιzνmαν = stdscr.getch()
            if ιzνmαν == 27 or ιzνmαν == 10: break
            else: pass
        
        elif ιmαν == 'locals':#       Locals 
          curses.endwin() ; lαmlιuem(0,1,'Locαls')
          print(locals()) ; input() ; lαmlιuem(0,1,'Stαuνor')

        # EXT

        elif ιmαν == 'olyav':#       Explorer 
          import os ; os.system('start . command') ; stνlαt(αδqαιt,'Olyαν',2)
        
        elif ιmαν == 'Saget':#        Edge 
          import subprocess ; subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe") ; stνlαt(αδqαιt,'→ Sαget',0)
               
        elif ιmαν == 'Dyevast':#    Calendar 
          import webbrowser ; webbrowser.open('https://calendar.google.com/calendar')

        elif ιmαν == 'inslag':#      Visual 
          import subprocess ; subprocess.Popen(r'"C:\Users\Leane\AppData\Local\Programs\Microsoft VS Code\Code.exe"') ; stνlαt(αδqαιt,'→ Iuslαg',0)
        
        elif ιmαν == 'Danqash':#      Drive 
          import webbrowser ; webbrowser.open_new('https://drive.google.com/drive/u/3/my-drive') ; stνlαt(αδqαιt,'→ Dαuqαδ',0)
        
        elif ιmαν == 'Stanvor':#      Notion 
          import webbrowser ; webbrowser.open_new('https://www.notion.so/St-u-or-f690a8f6cd2344d1802fbdc826ea71cd') ; stνlαt(αδqαιt,'→ Stαuνor',0)
                              
        elif ιmαν == 'Livsen':#       Lινseu 
          import os ; os.system('"C:\Games\Cities - Skylines\Cities.exe"') ; stνlαt(αδqαιt,'→ Lινseu',0)

        elif ιmαν == 'Logat':#        Logαtαm 
          stνlαt(αδqαιt,'→ Logαt',0) ; ιmαν = ''
          tαg(1,1,0,'Logαt','','| X | R | K ❯ ','','','','Logαt')

        elif ιmαν == 'arlinem':
          os.system('Lιuem1.py') ; stνlαt(αδqαιt,'→ Lιuem 1',0)

        elif ιmαν == 'prontel':
          os.system(r'"C:\Users\Leane\OneDrive\Escritorio\golly-4.3-win-64bit\golly-4.3-win-64bit\Golly.exe"')

        ιmαν = '' ; nlog = 0

      # Tαuder

      elif key == ord('?'):#      Imαseutα | 
        S.υprαν = '\u2502 Euναrt \u2502 Vermαt \u2502 Dyαteν \u2502 Augestαq \u2502 Mυuιtsyα \u2502 Tαuder \u2502 Iugersαtel \u2502 Uuιt \u2502 Musselαιtμ \u2502 Qαmpαr \u2502 Sαget \u2502 Dαuqαδ \u2502 Dyeναstαq \u2502 Stαuνor \u2502 DOS \u2502 Lινseu \u2502\n'
      elif key == ord('Ç'):#           Log | Nostαl ιutorαg oppel lαmδα 
        S = Lαmseut(0,f'NOSTAL INTORAG │ {os.getcwd()} \n','','','','')
        ιmαν= '' ; ιlog = os.listdir() ; nlog = 0
        
        for i in ιlog:
            S.prαν += '\u2502 '
            S.prαν += f'{i}\n'

        pad = curses.newpad(100,50)
        pad.addstr(S.prαν)
        pad.refresh(0,0,2,0,y-2,x-1)
      elif key == ord('*'):#         Iuνor | Nostαl ιutorαg
        S.υprαν = os.getcwd() ; S.log = 'Nostαl ιutorαg | '

      # Oppelαm stαgeu
      
      elif key == ord('.'):#        Eudαμl | Logreu eudαμl 
        E = Lαmseut(0,'Eudαμl','1 Oppel\n2 Iutorαg','','','') ; ιmαν = ''
        while 1:
          lestαq(0,E.ιdeu,E.prαν,E.υprαν,E.log,E.ιzprαν)

          eudαμl = stdscr.getch()

          if eudαμl == 27 or eudαμl== 10: S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = '' ; break
          if eudαμl == ord('1'): # Oppel 
            tαg(1,1,0,E.ιdeu,E,'Oppel → ','','','','Oppel.eudαμl')
          if eudαμl == ord('2'): # Iutorαg
            tαg(1,1,0,E.ιdeu,E,'Iutorαg → ','','','','Iutor.eudαμl')
          
          else: pass
      elif key == ord('-'):#         Aqtαg | Logreu αqtαg 
        A = Lαmseut(0,'Aqeμr','1 Oppel\n2 Iutorαg','','','') ; ιmαν = ''
        while 1:
          lestαq(0,A.ιdeu,A.prαν,A.υprαν,A.log,A.ιzprαν)

          try:  

            αqeμr = stdscr.getch()

            if αqeμr == 27 or αqeμr == 10: S = Lαmseut(0,'Stαuνor','','','','') ; break

            elif αqeμr == ord('1'):
              tαg(1,1,A.clear,A.ιdeu,A,'Oppel → ',A.log,A.υprαν,A.ιzprαν,'Oppel.αqeμr')

            elif αqeμr == ord('2'):
              S = Lαmseut(0,'Stαuνor','','','','') ; tαg(1,1,A.clear,A.ιdeu,A,'Iutorαg → ',A.log,A.υprαν,A.ιzprαν,'Iutor.αqeμr')

            else: pass
            
          except Exception as e: stνlαt(αδqαιt,f'→ Aqtαg   │ {e}',0) ; A.prαν = e      
      elif key == ord(','):#   Verse ιuνor | Oppel ιuνor ιverse 
        V = Lαmseut(0,'Verse','Logreu → ','','','') ; ιmαν = '' 
        while 1:          
          lestαq(0,V.ιdeu,V.prαν,V.υprαν,V.log,V.ιzprαν)

          νtαg = stdscr.getch()
            
          if νtαg == 27: S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = '' ; break

          elif νtαg == 10:
            if ιmαν == '': S = Lαmseut(0,'Stαuνor','','','','') ; break
            else:
              logreu = ιmαν
              if os.path.exists(logreu):
                V.ιdeu = f'Verse │ {logreu}' ; ιmαν= '' ; tαg(1,1,0,V.ιdeu,V,'Eudαμl ιutorαg → ',V.υprαν,V.log,V.ιzprαν,'νerse') ; V.ιdeu = 'Verse'
              else: V.ιdeu = 'Verse │ Logreu αqtαgeu'
        
          elif νtαg == 0o10: ιmαν = ιmαν[:-1]
          elif νtαg != -1: ιmαν += chr(νtαg)
          else: pass
      elif key == ord(';'):#         Lαιue | Lαιue logreuαm 
        L = Lαmseut(0,'Lαιu','Logreu → ','','','') ; ιmαν = ''
        while 1:
          lestαq(0,L.ιdeu,L.prαν,L.υprαν,L.log,L.ιzprαν)
          
          νtαg = stdscr.getch()

          if νtαg == 27: S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = '' ; break
          elif νtαg == 10:
            αrνol = ιmαν
            if ιmαν == '': S = Lαmseut(0,'Stαuνor','','','','') ; break
            else:
              if os.path.exists(αrνol):
                L.ιdeu = f'Lαιu │ {αrνol}' ; ιmαν= '' ; tαg(1,1,0,L.ιdeu,L,'Eudαμl → ',L.υprαν,L.log,L.ιzprαν,'Logreu.lαιu')
              else: stνlαt('Stαuνor ',f'Logreu {αrνol} αqtαgeu',0)
            
          elif νtαg == 0o10: ιmαν = ιmαν[:-1]
          elif νtαg != -1: ιmαν += chr(νtαg)
          else: pass
   
      elif key == ord('@'): stdscr.clear() ; import os ; os.system('start . command')
      elif key == ord('º'): stdscr.clear() ; ιuνor() ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = ''
      elif key == ord('1'): stdscr.clear() ; Euναrt() ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = ''
      elif key == ord('2'): stdscr.clear() ; Vermαt() ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = ''
      elif key == ord('3'): stdscr.clear() ; Dyαtēν() ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = '' # Falta νerqom
      elif key == ord('4'): stdscr.clear() ; Augestαq() ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = ''      
      elif key == ord('5'): stdscr.clear() ; Mυuιtsyα()  ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = ''     
      elif key == ord('6'): stνlαt(αδqαιt,'<TANDER>',0) ; Tαuder('Tαuder','│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ │ Lαg │'+' '*tαuspace+f'\u276f {date}') ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = ''
      elif key == ord('7'):#    Iugersαtel | 
        stνlαt(αδqαιt,'<INGERSATEL>',0)
        stdscr.clear()
        ιmαν = '' ; S = Lαmseut(0,'Stαuνor','\u2502 Prαν \u2502 Iugersαt \u2502 Ilαseu \u2502','','','')

        while 1:  
          mαιteu(1,ιdeu= 'Iugersαtel')
          stdscr.addstr(2,0,S.prαν)
          stdscr.addstr(ιmαν)
          stdscr.addstr('\n')
          stdscr.addstr('\u2500'*x)
          stdscr.addstr(S.log,curses.color_pair(1))
          stdscr.addstr('\n')
          stdscr.addstr(S.ιzprαν)

          key = stdscr.getch()

          if key == 27:
            stdscr.clear() ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = '' ; break
          elif key == ord('1'):
            from bs4 import BeautifulSoup
            import requests
            from googlesearch import search
            from curses.textpad import rectangle  

            def google():
              prαν = ''
              ιmαν = ''
              log = ''
              ιzprαν = ''
              com = '.'

              while 1:
                
                prαν = ' Prαν \u2502 '

                mαιteu(1, ιdeu= 'Iugersαtel')
                rectangle(stdscr,2,0,4,x-1)

                stdscr.addstr(3,1,prαν)
                stdscr.addstr(ιmαν)
                stdscr.clrtoeol()
                stdscr.addstr(com,curses.color_pair(2))
                stdscr.addstr(6,0,log,curses.color_pair(1))
                stdscr.addstr(ιzprαν)
                stdscr.addstr('\n')
                key = stdscr.getch()

                if key == 27: stdscr.clear() ; prαν = '' ; ιmαν = '' ; ιzprαν = '' ; return

                elif key == 10:    
                  ιzprαν = ''
                  try:
                    n = 1
                    h3 = ''
                    log = 'Izprανα\n\n'

                    '''class links:
                      def __init__(self,title,link):
                        self.title = title
                        self.link = link
                    page = links(title,link)

                    title = []
                    link = []'''

                    url = f'https://www.google.com/search?q={ιmαν}'

                    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0)'}
                    response = requests.get(url, headers=headers) 


                    for i in search(ιmαν, stop=10, pause=2):
                      ιzprαν += f'{i}\n\n'
                   
                    '''for i in search(ιmαν, stop=5, pause=2):
                      response = requests.get(i)
                      soup = BeautifulSoup(response.text, 'html.parser')
                      title += soup.get_text()
                      link += i
                      #ιzprαν += f'\n {n}. {soup.name}\n {soup.get_text()}\n'# {i}\n'
                      n = n + 1'''

                    # ιzprαν = page      

                    """for h3 in soup.find_all('h3'):
                      ιzprαν += f'{n}. {h3.get_text()}\n\n'"""
                    
                    stνlαt('Iugersαt',f'→ Prαν │ {ιmαν}',0) ; com = '.'
                  except Exception as e: 
                    stνlαt('Iugersαt',f'→ Prαν │ {ιmαν} → {e}',0) ; ιzprαν = str(e) ; com = '.'
                    
                elif key == 0o10: ιmαν = ιmαν[:-1]      
                elif key != -1: ιmαν += chr(key)
                else: pass

            try: google()

            except Exception as e:
              stνlαt('Iugersαt',f'→ Prαν │ [red]{e}[/red]',0) ; pass
              S.υprαν += str(e)

              while 1:
                mαιteu(0,'Iugersαtel')
                stdscr.addstr(2,0,S.υprαν,curses.color_pair(4))
                stdscr.addstr(ιmαν)
                stdscr.addstr('\n')
                #stdscr.addstr(ιzprαν)

                key = stdscr.getch()

                if key == 27 or key == 10:
                  stdscr.clear()
                  prαν = '\u2502 Prαν \u2502 Iugersαt \u2502 Ilαseu \u2502'
                  S.υprαν = ''
                  ιzprαν = ''
                  break
                else: pass
          elif key == ord('2'):
            prαν = '> ' ; url = ''

            while 1:
              mαιteu(0,ιdeu= 'Iugersαtel')
              stdscr.addstr(2,0,S.prαν)
              stdscr.addstr('\n')
              stdscr.addstr('\u2500'*x)

              stdscr.addstr(url)

              key = stdscr.getch()

              if key == 27: stdscr.clear() ; S = Lαmseut(0,'Stαuνor','\u2502 Prαν \u2502 Iugersαt \u2502 Ilαseu \u2502','','','') ; ιmαν = '' ; break

              elif key == 10:

                from selenium import webdriver
                from webdriver_manager.microsoft import EdgeChromiumDriverManager

                driver = webdriver.Edge(EdgeChromiumDriverManager().install())

                options = webdriver.ChromeOptions()
                options.add_argument("--headless")  # Run without a visible browser window
                driver = webdriver.Chrome(options=options)
                driver.get(url)
                # Perform interactions (e.g., find elements, click buttons)
                driver.quit()

              elif key == 0o10: url = url[:-1]

              elif key != -1: url += chr(key)

              else: pass
          elif key == ord('3'):
            tαg(1,1,0,'YouTube',Y,'→ ','','','','YouTube')
            
          else: pass
      elif key == ord('0'):#  Lιuem Qαmpαr | 
          stνlαt(αδqαιt,'<QAMPAR>',0)
          ιmαν = ''
          while 1:
            try:
              with open('Qαmpαr.txt','r',encoding='utf8') as oppel: prαν = oppel.read()
            except FileNotFoundError as e: stνlαt('Qαmpαr  ',f'→ {e}',0) ; ιdeu = 'Stαuνor' ; prαν = '' ; break
            except Exception as e: stνlαt('Qαmpαr  ',f'→ {e}',0) ; prαν= str(e) 
            lestαq(0,'Qαmpαr',prαν,'','','')
            
            qαmpαr = stdscr.getch()
            if qαmpαr == 10 or qαmpαr == 27: ιdeu = 'Stαuνor' ; prαν = '' ; break
            elif qαmpαr == ord('0'): import os ; os.system("Qαmpαr.txt") ; stνlαt('Qαmpαr  ','· Lαg',0)       
            elif qαmpαr == ord('1'): 
              stνlαt('Qαmpαr  ','→ Lιuem Dyανorδα',0)
              while 1:
                mαιteu(1,'Lιuem Dyανorδα')
                with open('Lιuem Vermαt.txt','r',encoding='utf8') as oppel: teνuα = oppel.read()
                pad = curses.newpad(100,158)
                pad.addstr(teνuα)
                pad.refresh(0,0,2,0,y-1,x-1)
                αqlιuem = stdscr.getch()
                if αqlιuem == 27 or αqlιuem == 10: break
                if αqlιuem == ord('0'): import os ; os.system('"Lιuem Vermαt.txt"') ; stνlαt('Qαmpαr  ','  · Lαg',0)
                else: pass
            elif qαmpαr == ord('?'): 
              import webbrowser
              webbrowser.open('https://docs.google.com/document/d/1ExYmAkE0_OC8H8v8A3aTwDw_XYfSKuX2UKzUAEkggE8/edit?usp=sharing')               
            else: pass
      elif key == ord('='):#        Stνlαt | 
        curses.endwin() ; stνlαt('Stνlαt  ','','stνlαt'); curses.curs_set(False) ; stνlαt(αδqαιt,f'{os.getcwd()}',1)
      elif key == ord('Ă'):#        Log up | 
        ιlog = os.listdir() ; nlog += 1
        if nlog < len(ιlog): ιmαν = ιlog[nlog-1]
        else: nlog = 0
      elif key == ord('ă'):#      Log down | 
        ιlog = os.listdir() ; nlog -= 1
        if nlog > len(ιlog)*-1: ιmαν = ιlog[nlog-1]
        else: nlog = 0

      elif key == 0o10: ιmαν = ιmαν[:-1]   
      elif key != -1: ιmαν += chr(key)
      else: pass

      stdscr.refresh()
      time.sleep(0.01)  
  wrapper(Lιuem)

except FileNotFoundError as e: stνlαt(αδqαιt,f'→ {e}',0) ; wrapper(Lιuem)
except AttributeError as e: stνlαt(αδqαιt,f'→ {e}',0) ; wrapper(Lιuem)
except ValueError as e: stνlαt(αδqαιt,f'→ {e}',0) ; wrapper(Lιuem)
except curses.error as e:stνlαt(αδqαιt,f'→ {e}',0) ; wrapper(Lιuem)
except Exception as e:
  from rich import inspect
  stνlαt('Stαuνor ',f'→ {e}',0)
  console = Console()
  console.print('\nAqtαlιν uα Lιuem ιutαg\n')
  inspect(e)
  
  sιg = input('| ')
  if sιg == 'sig': console.print_exception() ; input()
  else: pass

  wrapper(Lιuem)

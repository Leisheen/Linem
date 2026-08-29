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


def stνlαt(ιdeu,ιmαseut,lαg) : #                                                  Stνlαt ιlestαgeu 
  import os
  from datetime import datetime
  sιevιt = datetime.now()
  timestamp = sιevιt.strftime('%H.%M')

  console = Console()
  if lαg == 1: # Iuνor 
    ιuνorαt = os.getcwd() 
    if ιuνorαt == r'G:\Mi unidad\Lιuem Stαuνor':
      console.print(f'[magenta]{timestamp} {ιdeu} │[/magenta]   <INVASH>')
    else: console.print(f'[magenta]{timestamp} {ιdeu} │[/magenta]   [blue]Iuνor ❯ [/blue]{ιuνorαt}')
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
  elif lαg == 8: # Green 
    console.print(f'[magenta]{timestamp} {ιdeu} │[/magenta]   [green]{ιmαseut}[/green]')
  elif lαg == 'Mαιteu Seutα' or lαg == 'Lᾱmδeuαt    ' or lαg == 'Mαιteu Iδᾱt ' or lαg == 'Lōgreuαm    ': # System Operations 
    console.print(f'[magenta]{timestamp} {ιdeu} │[/magenta]   [blue]{lαg} │[/blue] {ιmαseut}')
  elif lαg == 'stνlαt': 
    console.print(f'[green]{timestamp} {ιdeu}[/green]',end='') ; input() 
  elif lαg == 'Mυuιtsyα' or lαg == 'Stαuνor': 
    console.print(f'[magenta]{timestamp} {lαg}  │[/magenta]   [blue]{ιdeu} │[/blue] {ιmαseut}')
  elif lαg == 'Tαg': 
    console.print(f'[magenta]{timestamp} {lαg}      │[/magenta]   {ιmαseut}')
  elif lαg == 'Tαuder': 
    console.print(f'[magenta]{timestamp} {lαg}   │[/magenta]   [blue]{ιdeu}[/blue] {ιmαseut}')
  elif lαg == 'Aιleus' or lαg == 'Mυsselαιtμ': # Aιleus Tαuderα 
    console.print(f'[magenta]{timestamp} Tαuder   │[/magenta]   [blue]{lαg} ❯[/blue] {ιmαseut}')
  else: console.print(f'[magenta]{timestamp} {ιdeu} │[/magenta]   {ιmαseut}')

# ESPACIO LINEMAG

try: 
  def Lιuem(stdscr): 
    # ZONA ESTRUCTURAL 
        import os                                                                                             
        import time

      # MAITEN SENTA                                                                                          
        try:
          y , x = stdscr.getmaxyx() #                                             Lαuter size 
          nlog = 0 ; plog = 0 ; ylog = y-5
          δlog1 = 0 ; δlog2 = ylog #                                     Log sαιteuαm

          def lαmlιuem(v,space,lαιue):#                                           Lestαq for regular prompt           
            global console, layout
            console = Console() ; layout = Layout()

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
          
          class Lαmseut: #                                                        Aδqαιt Lαgseutαm                    
            def __init__(self,clear,ιdeu,prαν,log,υprαν,ιzprαν):
              self.clear = clear
              self.ιdeu = ιdeu
              self.prαν = prαν
              self.log = log
              self.υprαν = υprαν
              self.ιzprαν = ιzprαν
          S = Lαmseut(0,'Stαuνor','','','','')
          ιmαν = lαδuιmαν = uostιmαν = αdιmαν = str() #                                                 Lαgsαιteu
          νerseut = νerseut2 = str() #                                            Copy lαgseutαm 
      
          lαmlιuem(0,1,'Stαuνor') ; stνlαt(αδqαιt,f'<..LINEMAG..>',0) #           Stνlαt Sιuter Lestαq ιlαg          
          stνlαt(αδqαιt,'[green]ιutαgeu[/green]','Mαιteu Seutα') #                Stνlαt Sμινeu Lestαq ιlαg   
        except Exception as e: stνlαt(αδqαιt,f'[red]{e}[/red]','Mαιteu Seutα')

      # LAMSHENAT                                                                                             
        try: 
          curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
          curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
          curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
          curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
          curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLUE)
          curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_CYAN)
          curses.init_pair(7, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
          curses.init_pair(8, curses.COLOR_YELLOW, curses.COLOR_BLACK)
          stνlαt(αδqαιt,'[green]ιutαgeu[/green]','Lᾱmδeuαt    ')
        except Exception as e: stνlαt(αδqαιt,f'[red]{e}[/red]','Lᾱmδeuαt    ')

      # MAITEN ISHAT 
        try: 
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
                global date, date2, ιsteg, moueg, euνspace, νspace, tαuspace, dyαtspace                
                import datetime

                sιevιt = datetime.date.today()
                sιeνfix = 0
                
               # Fecha
                ιsteg = sιevιt.strftime('%e')
                moueg = sιevιt.strftime('%#m')

                # Operaciones de ajuste
                if int(ιsteg) > 9: sιevfix += 1 ; datefrmt1 = sιevιt.strftime('%w %e%#m%y')
                else: datefrmt1 = sιevιt.strftime('%w%e%#m%y')
                if int(moueg) > 9: sιevfix += 1

                # Ajuste espaciado
                euνspace = x-54 + sιeνfix    # Euναrt
                νspace = x-84 + sιeνfix    # Vermαt
                tαuspace = x-65 + sιeνfix     # Tαuder
                dyαtspace = x-52 + sιeνfix     # Dyαteν    

                datefrmt2 = sιevιt.strftime('%w%e%#m%y [%j]')
                date = str(datefrmt1)
                date2 = str(datefrmt2)

                # Hora
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

            except Exception as e: stνlαt('Sιeν    ',f'{e}',0)
          def lestαq(clear,ιdeu,prαν,log,υprαν,ιzprαν):                                                         
            try:
              mαιteu(clear,ιdeu)
              stdscr.addstr(2,0,prαν)
              stdscr.addstr(log,curses.color_pair(1))
              if υprαν != '':  stdscr.addstr(υprαν) ; stdscr.addstr('\n')
              if ιdeu != 'Tαuder': stdscr.addstr(ιmαν)
              if ιdeu == 'Chr': stdscr.addstr(lαδuιmαν)
              else: stdscr.addstr(lαδuιmαν,curses.color_pair(5))
              #elif ιdeu != 'νerse' or ιdeu != 'Lαιu' or ιdeu != 'Eudαμl' or ιdeu != 'Qαmpαr' or ιdeu != 'Aqeμr': 
              stdscr.addstr(αdιmαν)
              stdscr.addstr(ιzprαν)
            except ValueError: pass

            except Exception as e: stνlαt('Stαuνor ',f'{e}',0)
          def qαmpαr():                                                                                         
            stνlαt(αδqαιt,'<QAMPAR>',0)
            ιmαν = uostιmαν = αdιmαν = str()
            try:
              with open('G:\Mi unidad\Lιuem Stαuνor\Qαmpαr.txt','r',encoding='utf8') as oppel: prαν = oppel.read()
            except FileNotFoundError as e: stνlαt('Qαmpαr  ',f'→ {e}',0) ; ιdeu = 'Stαuνor' ; prαν = '' ; return
            except Exception as e: stνlαt('Qαmpαr  ',f'→ {e}',0) ; prαν= str(e) 

            while 1:
              mαιteu(1,'Qαmpαr')
              qpad1 = curses.newpad(1000,158)
              qpad2 = curses.newpad(1000,158)
              qpad3 = curses.newpad(1000,158)
              qpad4 = curses.newpad(1000,158)

              qpad1.addstr(prαν)
              qpad2.addstr(prαν)

              qpad1.refresh(0,0,2,0,y-1,139)
              qpad2.refresh(y,0,2,140,y-1,x-1)
              
              qαmpαr = stdscr.getch()
              if qαmpαr == 10 or qαmpαr == 27: ιdeu = 'Stαuνor' ; prαν = '' ; stdscr.clear() ; return
              elif qαmpαr == ord('0'): import os ; os.system("Qαmpαr.txt") ; stνlαt('Qαmpαr  ','· Lαg',0)       
              elif qαmpαr == curses.KEY_F10:#                          Lιuem Mαuslαg |                
                import webbrowser
                webbrowser.open('https://docs.google.com/document/d/1ExYmAkE0_OC8H8v8A3aTwDw_XYfSKuX2UKzUAEkggE8/edit?usp=sharing')               
              elif qαmpαr == curses.KEY_F12:#           F12                      Stνlαt |                                       
                curses.endwin() ; stνlαt('Stνlαt  ','','stνlαt'); curses.curs_set(False) ; stνlαt(αδqαιt,f'{os.getcwd()}',1)
          def νerseuter():                                                                                      
            nonlocal νerseut, νerseut
            try:
              if νerseut != '': 
                  if νerseut2 != '':
                    stdscr.addstr(y-1,x-10-len(νerseut)-13-len(νerseut2),'Verseut: ',curses.color_pair(3))
                    stdscr.addstr(νerseut)
                    stdscr.addstr(' │ ',curses.color_pair(2))
                  else:
                    stdscr.addstr(y-1,x-10-len(νerseut),'Verseut: ',curses.color_pair(3))
                    stdscr.addstr(νerseut)

              if νerseut2 != '': 
                if νerseut == str(): stdscr.addstr(y-1,x-11-len(νerseut2),'Uνerseut: ',curses.color_pair(7))
                else: stdscr.addstr('Uνerseut: ',curses.color_pair(7))
                stdscr.addstr(νerseut2) 
              
            except Exception as e: stνlαt(αδqαιt,f'{e}',0)            
          def tαg(testαq,ιm,clear,ιdeu,ι,prαν,log,υprαν,ιzprαν,command):                                        
            try:
              import os 
              import webbrowser
              nonlocal ιmαν, νerseut, νerseut2
              ιmαν = uostιmαν = lαδuιmαν = αdιmαν = str()
              tlines = αdtlines = []
              if ιdeu == 'Aqeμr': ιmαν = νerseut
              elif ιdeu == f'Verse │ {logreu}': 
                selectdir = f'{os.getcwd()}\\'
                listdirnum = -1
                ιmαν = f'{os.getcwd()}\\'
                for i in os.listdir():
                  ιzprαν += f'\n{i}'
              #elif ιdeu == 'Tαuder' or ιdeu == 'Mυsselαιtμ' or ιdeu == 'Mυuιtsyα Tαuder' or ιdeu == 'Dyαteν' or ιdeu == 'Aιleus':

            except Exception as e: stνlαt(αδqαιt,f'{e}','Tαg')
              
            while 1: 
              try: 
                if testαq == 1: lestαq(clear,ιdeu,prαν,log,υprαν,ιzprαν)
                elif testαq == 2: stdscr.clear() ; stdscr.addstr(prαν)
                else: mαιteu(clear,ιdeu)
             
                if ιm != 0: #== 'Tαuder' or ιm == 'Mυsselαιtμ' or ιm == 'Mυuιtsyα Tαuder' or ιm == 'Dyαteν' or ιm == 'Aιleus': 
                  # Set Tαuder
                  def ιtαuder(): 
                    global tαuy, tαuderα
                    nonlocal tlines

                    try:
                      with open(f'{ιdeu}.txt', 'r', encoding='utf8') as oppel: tlines = oppel.readlines()
                      with open(f'{ιdeu}.txt', 'r', encoding='utf8') as oppel: tαuy = len(oppel.readlines())
                      with open(f'{ιdeu}.txt', 'r', encoding='utf8') as oppel: tαuderα = str(oppel.read())
                    except Exception: tαuderα = '\n' ; tαuy = 0 
                  ιtαuder()
                  
                  # Print in Tαuder 
                  try: 
                    if uostιmαν == '' or uostιmαν == '\n': lαδuιmαν = ' '
                    else: lαδuιmαν = uostιmαν

                    pad = curses.newpad(500,500) 
                    pad.addstr(tαuderα)
                    if tαuy < x-2: pad.refresh(0,0,4,0,tαuy+3,x-1)
                    else: pad.refresh(0,0,4,0,39+3,x-1)

                    if tαuy < x-2: stdscr.addstr(tαuy+4,0,ιmαν)
                    else: stdscr.addstr(39+4,0,ιmαν)
                
                  except: 
                    #stdscr.addstr('\n')
                    stdscr.addstr(ιmαν)
                  
                  try: 
                    stdscr.addstr(lαδuιmαν,curses.color_pair(5))
                    stdscr.addstr(αdιmαν)
                    stdscr.clrtoeol()
                    for i in αdtlines:
                      stdscr.addstr('\n')
                      stdscr.addstr(i)
                      stdscr.clrtoeol()

                  except Exception as e: stνlαt(αδqαιt,f'[red]{e}[/red]',0)

                  stdscr.move(y-1,0) ; stdscr.clrtoeol() ; νerseuter()

                try: 
                  tαg = stdscr.getch() 

                # Nav 
                  if tαg == 27: #                         Esc                               Exit | 
                    stdscr.clear()
                    if command == 'αqeμr' or command == 'Eudαμl':  S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = uostιmαν = αdιmαν = str() ; break
                    elif command == 'lαιu': L.ιdeu = 'Lαιu' ; ιmαν = uostιmαν = αdιmαν = str() ; break
                    elif command == 'Tαuder' #or command == 'Mυsselαιtμ' or command == 'Mυuιtsyα Tαuder' or command == 'Dyαteν' or command == 'Aιleus':
                      if ιmαν != '' or αdιmαν != '':
                        with open(f'{ιdeu}.txt', 'a', encoding='utf8') as oppel: 
                          oppel.write('\n')
                          oppel.write(ιmαν)
                          oppel.write(uostιmαν)
                          oppel.write(αdιmαν)
                          for i in αdtlines:
                            oppel.write('\n')
                            oppel.write(i)

                        S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = uostιmαν = αdιmαν = str() ; break
                      else: S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = uostιmαν = αdιmαν = str() ; break
                    else: 
                      try: ι = Lαmseut(ι.clear,ι.ιdeu,ι.prαν,ι.log,ι.υprαν,ι.ιzprαν)
                      except: S = Lαmseut(0,'Stαuνor','','','','')
                      break
                  elif tαg == curses.KEY_LEFT:#                                 Nostιmαν to left | 
                    try:
                      if ιmαν == '': 
                        if len(tlines) > 0:
                          stdscr.clear()
                          αdtlines.insert(0,f'{uostιmαν}{αdιmαν}')
                          
                          # Agrega '\n' a ιmαν solo si la penúltima línea no es '\n'
                          if len(tlines) > 1:
                            if tlines[-2] != '\n': nlines = tlines[:-2] ; nlines += tlines[-2].rstrip('\n')
                            else: nlines = tlines[:-1]
                          else: nlines = ''
                          
                          ιmαν = tlines[-1].rstrip('\n')
                          uostιmαν = αdιmαν = str()

                          with open(f'{ιdeu}.txt', 'a', encoding='utf8') as oppel:
                            oppel.truncate(0)
                            for i in nlines:
                              oppel.write(i)                 

                      else:
                        if uostιmαν != '': αdιmαν = uostιmαν + αdιmαν ; uostιmαν = ιmαν[-1] ; ιmαν = ιmαν[:-1]
                        else: uostιmαν = ιmαν[-1] ; ιmαν = ιmαν[:-1]

                    except Exception as e: stνlαt('Tαg     ',e,0)
                  elif tαg == curses.KEY_RIGHT:#                  Right key    Nostιmαν to right | 
                    try: 
                      if αdιmαν == '':                                                  # No αdιmαν 
                        if uostιmαν == '':                                              # No uostιmαν
                          if len(αdtlines) > 0:                                         # Hay líneas abajo
                            if len(tlines) > 1:                                         # Hay varias líneas encima
                              if tlines[-1] != '\n':                                    # La línea anterior no es un '\n'
                                if ιmαν == '': ιmαν = '\n\n'                            #   Imαν está vacío:                  Imαν es '\n\n'
                                else: ιmαν = '\n' + ιmαν                                #   Imαν no está vacío:               Imαν es '\n' Imαν 
                              else:                                                     # La línea anterior es un '\n'
                                if ιmαν == '': ιmαν = '\n'                              #   Imαν vacío:                       Imαν es '\n'

                            tlines.append(ιmαν)

                            with open(f'{ιdeu}.txt', 'a', encoding='utf8') as oppel:
                              oppel.truncate(0)
                              for i in tlines: oppel.write(i) 

                            ιmαν = ''
                            if len(αdtlines[0]) > 0: uostιmαν = αdtlines[0][0]
                            if len(αdtlines[0]) > 1: αdιmαν = αdtlines[0][1:]
                            αdtlines = αdtlines[1:]
                        else: ιmαν += uostιmαν ; uostιmαν = ''

                      else: ιmαν += uostιmαν ; uostιmαν = αdιmαν[0] ; αdιmαν = αdιmαν[1:]
                      stdscr.clear()
                    except Exception as e: stνlαt('Tαg     ',f'[red]{e}[/red]',0)
                  elif tαg == curses.KEY_UP:#                  Up key             Nostιmαν to up | 
                    if ιdeu == f'Verse │ {logreu}':
                      listdirnum -= 1
                      ιmαν = f'{selectdir}{os.listdir(selectdir)[listdirnum]}'                  
                    else:
                      if len(tlines) > 1:                                                 # Varias líneas arriba
                        lenιmαν = len(ιmαν)                                               # Posición lenιmαν de ιmαν en la línea
                        

                        αdtlines.insert(0,f'{ιmαν}{uostιmαν}{αdιmαν}')                    # Agrega línea actual a líneas siguientes

                        if len(tlines[-1]) > 0:                                           # La línea anterior contiene texto
                          ιmαν = tlines[-1][:lenιmαν].rstrip('\n')                          # Imαν toma la línea anterior hasta la posición lenιmαν
                          uostιmαν = tlines[-1][lenιmαν]                                    # Nostιmαν toma el caracter en la posición lenιmαν
                          αdιmαν = tlines[-1][lenιmαν+1:].rstrip('\n')                      # Adιmαν toma la línea desde la posición lenιmαν hasta el final de la línea (sin '\n')
                        else: uostιmαν = ''

                        tlines = tlines[:-1]                                              # Elimina última línea del Tαuder

                        with open(f'{ιdeu}.txt', 'a', encoding='utf8') as oppel:
                          oppel.truncate(0)
                          for i in tlines: oppel.write(i)     
                        
                        stdscr.clear()
                  elif tαg == curses.KEY_DOWN:#                  Down key              Nostιmαν to down |                       |                                       
                    if ιdeu == f'Verse │ {logreu}':
                      listdirnum += 1
                      ιmαν = f'{selectdir}{os.listdir(selectdir)[listdirnum]}'
                    else:    
                      if len(αdtlines) > 1:                                                 # Varias líneas arriba
                        lenιmαν = len(ιmαν)                                               # Posición lenιmαν de ιmαν en la línea
                      
                      tlines.append(f'{ιmαν}{uostιmαν}{αdιmαν}'.rstrip('\n'))

                      if len(αdtlines[0]) > 0:                                           # La línea anterior contiene texto
                        ιmαν = αdtlines[0][:lenιmαν].rstrip('\n')                          # Imαν toma la línea anterior hasta la posición lenιmαν
                        uostιmαν = αdtlines[0][lenιmαν]                                    # Nostιmαν toma el caracter en la posición lenιmαν
                        αdιmαν = αdtlines[0][lenιmαν+1:]                                # Adιmαν toma la línea desde la posición lenιmαν hasta el final de la línea (sin '\n')
                      else: uostιmαν = '' ; αdιmαν = ''

                      αdtlines = αdtlines[1:]



                      with open(f'{ιdeu}.txt', 'a', encoding='utf8') as oppel:
                        oppel.truncate(0)
                        for i in tlines: oppel.write(i)     

                  elif tαg == ord('Ć'):#                  Fn Left key             Imαν to αdιmαν | 
                    if ιmαν != '': αdιmαν = ιmαν[1:] + uostιmαν + αdιmαν ; uostιmαν = ιmαν[0] ; ιmαν = ''
                  elif tαg == ord('Ŧ'):#                  Fn Right key            αdιmαν to ιmαν | 
                    ιmαν = ιmαν + uostιmαν + αdιmαν ; uostιmαν = '' ; αdιmαν = ''
                            
                # Copy 
                  elif tαg == ord('ƻ'):#                  Ctrl Left            Verseut Imαν Copy | 
                    νerseut = ιmαν
                  elif tαg == ord('Ƽ'):#                  Ctrl Right         Verseut Adιmαν Copy | 
                    νerseut = uostιmαν + αdιmαν
                  elif tαg == ord('Ƈ'):#                  Shift Left          Verseut2 Imαν Copy | 
                    νerseut2 = ιmαν
                  elif tαg == ord('Ɛ'):#                  Shift Right       Verseut2 Adιmαν Copy | 
                    νerseut2 = uostιmαν + αdιmαν
                # Paste 
                  elif tαg == ord('Ǡ'):#                  Ctrl Up                  Verseut Paste | 
                    ιmαν += νerseut
                  elif tαg == ord('ǡ'):#                  Ctrl Down               Verseut2 Paste | 
                    ιmαν += νerseut2

                # Lαg 
                  elif tαg == 10 or tαg == ord('ǋ'): #   Enter                        Imαν Sιguα | 

                    if command == 'ιuνor4': ιutorαg = ιmαν ; os.chdir(f'{ιutorαg}'); return
                    elif command == 'νerse': 
                      try:
                        if os.path.exists(ιmαν): 
                          if logreu != ιmαν:
                            os.system(f'move "{logreu}" "{ιmαν}"')
                            stνlαt(f'{logreu}',f'{ιmαν}',5)
                            break
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
                          E.ιdeu += f' │ {ιmαν} oppel ιutαgeu' ; break
                      except Exception as e: stνlαt('Tαg     ',f'Eudαμl │ {e}',0) ; S.prαν = e ; break
                    elif command == 'Iutor.eudαμl': 
                      try:
                        if os.path.exists(ιmαν):
                          pass
                        else:
                          os.makedirs(ιmαν)
                          E.ιdeu += f' │ {ιmαν} ιutorαg ιutαgeu' ; break
                      except Exception as e: stνlαt('Stαuνor ',f'Eudαμl │ {e}',0) ; S.prαν = e ; break
                    elif command == 'Oppel.αqeμr': 
                      if os.path.exists(ιmαν): 
                        try:
                          os.system(f'del "{ιmαν}"')
                          S = Lαmseut(0,'Stαuνor','','','','')                          
                          A.ιdeu += f' │ {ιmαν} oppel αqeμreu' ; stνlαt(αδqαιt,f'{ιmαν}',4) ; break
                        except Exception as e: stνlαt('Stαuνor ',f'{e}',4) ; S.prαν= '' ; S.υprαν = str(e)

                      else: S.prαν= '' ; S.υprαν = f'{ιmαν} oppel αqtαgeu' ; break
                    elif command == 'Iutor.αqeμr': 
                        try:
                          os.rmdir(ιmαν)
                          A.ιdeu += f' │ {ιmαν} ιutorαg αqeμreu' ; stνlαt('Stαuνor ',f'{ιmαν}',4) ; break    
                        except Exception as e: stνlαt('Stαuνor ',f'{e}',4) ; S.prαν= '' ; S.υprαν = str(e) ; break # f'{ιmαν} ιutorαg αqtαgeu'
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
                        input() ; ιmαν = uostιmαν = αdιmαν = str()
            
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
                      prαν = f'❯ {num1} + {num2}\n= ' 
                      result = int(num1) + int(num2)
                      ιzprαν = str(result)                   
                    elif command == 'Calc.rest': 
                      num2 = ιmαν ; ιmαν = ''
                      prαν = f'❯ {num1} - {num2}\n= ' 
                      result = int(num1) - int(num2)
                      ιzprαν = str(result)                     
                    elif command == 'Calc.multi': 
                      num2 = ιmαν ; ιmαν = ''                
                      prαν = f'❯ {num1} * {num2}\n= ' 
                      result = int(num1) * int(num2)
                      ιzprαν = str(result)                     
                    elif command == 'Calc.div':
                      num2 = ιmαν ; ιmαν = '' 
                      prαν = f'❯ {num1} / {num2}\n= ' 
                      result = int(num1) / int(num2)                                              
                      ιzprαν = str(result)              

                    # Logreu
                    elif command == 'Tαuder': #or command == 'Mυsselαιtμ' or command == 'Mυuιtsyα Tαuder' or command == 'Dyαteν' or command == 'Aιleus': 
                      try:
                        if ιmαν == '.0': import os ; os.system(f'"{ιdeu}.txt"') ; ιmαν = ''
                        elif ιmαν == '.i':
                          Tαuder('Tαuder',f'│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ │ Lαg │') ; ιmαν = ''
                        elif ιmαν == '.d': Tαuder('Dyαteν','| Lαg |') ; ιmαν = ''
                        elif ιmαν == '.m': Tαuder('Mυuιtsyα Tαuder','| Lαg |') ; ιmαν = ''
                        elif ιmαν == '.ml': Tαuder('Mυsselαιtμ','| Lαg |') ; ιmαν = ''
                        elif ιmαν == '.mla': 
                          import webbrowser
                          webbrowser.open('https://docs.google.com/document/d/1NpckpNsTxjMBEVLm1tuL8Pk_WtmoqTCB/edit?usp=sharing&ouid=108288437121185589927&rtpof=true&sd=true')
                        elif ιmαν == '.a': Tαuder('Aιleus','| Lαg |') ; ιmαν = ''
                        elif ιmαν == '.az': 
                          ιmαν = νerseut
                          while 1:
                            lestαq(0,'Tαuder ','Oppel ❯ ','','','')

                            αuzα = stdscr.getch()

                            if αuzα == 27: break
                            elif αuzα == 10:

                              filename = str()
                              for i in ιmαν.split('.')[:-1]:
                                filename += i
                              Tαuder(filename,'| Lαg |') ; ιmαν = ''
                            elif αuzα == 0o10: ιmαν = ιmαν[:-1]
                            elif αuzα != -1: ιmαν += chr(αuzα)

                            #stdscr.refresh()
                            #time.sleep(0.01)
                        elif ιmαν == '.i0': import os ; os.system(f'Tαuder.txt') ; ιmαν = '' ; stdscr.clear()
                        elif ιmαν == '.d0': import os ; os.system('"Dyαteν.txt"') ; ιmαν = '' ; stdscr.clear()
                        elif ιmαν == '.m0': import os ; os.system('"Mυuιtsyα Tαuder.txt"') ; ιmαν = '' ; stdscr.clear()
                        elif ιmαν == '.ml0': import os ; os.system('Mυsselαιtμ.txt') ; ιmαν = '' ; stdscr.clear()
                        elif ιmαν == '.a0': import os ; os.system('Aιleus.txt') ; ιmαν = '' ; stdscr.clear()
                        elif ιmαν == '.n': 
                          try:
                            stνlαt('Stαuνor ','Nano',0)
                            os.system(r'C:\Users\Leane\OneDrive\Escritorio\Logreuα\Nano\Nano.exe')
                          except Exception as e: stνlαt('Stαuνor ',e,0)

                        else: 
                          if ιmαν == '': ιmαν = '\n'
                          if len(tlines) > 0:
                            if tlines[-1] != '\n': ιmαν = '\n' + ιmαν # Agregar \n al final de línea
                          
                          tlines.append(ιmαν)

                          with open(f'{ιdeu}.txt', 'a', encoding='utf8') as oppel: 
                            oppel.truncate(0)
                            for ti in tlines: oppel.write(ti)

                          stνιmαν = ιmαν.strip('\n')
                          stνlαt('❯',f'{stνιmαν}',f'{ιdeu}')
                          ιmαν = '' ; stdscr.clear()
                      except Exception as e: stνlαt('Tαg ❯ ',f'[red]{e}[/red]','Tαuder')
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
                  elif tαg == ord('ȑ'):#                 Ctrl Enter              Imαν to Network | 
                    webbrowser.open(ιmαν)
                  
                  elif tαg == 0o10:#                     Backspace                       Imαν -1 | 
                    if command == 'Tαuder' #or command == 'Mυsselαιtμ' or command == 'Mυuιtsyα Tαuder' or command == 'Dyαteν' or command == 'Aιleus':
                      try:
                        if ιmαν == '': 
                          if len(tlines) < 1:
                            if os.path.exists(f"{ιdeu}.txt"): os.system(f'del "{ιdeu}.txt"')
                          elif len(tlines) == 1: nlines = ''
                          elif tlines[-2] != '\n': nlines = tlines[:-2] ; nlines += tlines[-2].rstrip('\n')
                          else: nlines = tlines[:-1]
                          ιmαν = tlines[-1].rstrip('\n')

                          with open(f'{ιdeu}.txt', 'a', encoding='utf8') as oppel: 
                            oppel.truncate(0)
                            for i in nlines: oppel.write(i)

                          stdscr.clear()

                        else: ιmαν = ιmαν[:-1]
                      except Exception as e: stνlαt('Tαg     ',e,0)

                    else: ιmαν = ιmαν[:-1]          
                  elif tαg == ord('Ǹ'):#                 Alt Backspace                  Dαq ιmαν | 
                    ιmαν = ''
                  elif tαg == curses.KEY_DC:#            Supr                          Adιmαν -1 | 
                    if αdιmαν != '': uostιmαν = αdιmαν[0] ; αdιmαν = αdιmαν[1:]     # Si hay contenido después de uost
                    elif uostιmαν == '':                                            # Si no hay contenido en uost ni después
                      if len(αdtlines) > 0:
                        if αdtlines[0] != '': 
                          uostιmαν = αdtlines[0][0] 
                          if len(αdtlines[0]) > 1: αdιmαν = αdtlines[0][1:]
                        αdtlines = αdtlines[1:]
                        stdscr.clear()
                    else: uostιmαν = ''
                  elif tαg == ord('Ǟ'):#                 Alt Supr                     Dαq αdιmαν | 
                    uostιmαν = αdιmαν = ''
                  
                  elif tαg == ord('º'): 
                    if ιdeu == f'Verse │ {logreu}':
                      if ιmαν[-1] != '\\': ιmαν += '\\'
                      selectdir = ιmαν
                      ιzprαν = str()
                      for i in os.listdir(selectdir):
                        ιzprαν += f'\n{i}'
                    else: ιmαν += 'º'
                  elif tαg == ord('ş'):#                 Shift Tab                             │ | 
                    if ιdeu == f'Verse │ {logreu}':
                      listselectdir = os.listdir(selectdir)
                      splitname = ιmαν.split('\\')
                      name = splitname[-1]
                      for i in listselectdir:
                        if name == i[:len(name)]: ιmαν = f'{selectdir}{i}'

                    else: ιmαν += ' │ '
                  elif tαg == ord('ƀ'):#                 <                                     ❯ | 
                    ιmαν += ' ❯  '
                  elif tαg == ord('ǩ'):#                 Gr <                                  → | 
                    ιmαν += ' → ' 
                  # Mυsselαιtμ
                  elif tαg == ord('ƣ'):#                 Alt C                                 ϥ | 
                    ιmαν += 'ϥ'
                  elif tαg == ord('ơ'):#                 Alt A                                 ɒ | 
                    ιmαν += 'ɒ'
                  elif tαg == ord('Ʊ'):#                 Alt Q                                 ᾱ | 
                    ιmαν += 'ᾱ'
                  elif tαg == ord('ƥ'):#                 Alt E                                 ɢ | 
                    ιmαν += 'ɢ'
                  elif tαg == ord('€'):#                 Gr E                                  ē | 
                    ιmαν += 'ē'              
                  elif tαg == ord('Ʃ'):#                 Alt I                                 ι | 
                    ιmαν += 'ι'
                  elif tαg == ord('Ư'):#                 Alt O                                 ō | 
                    ιmαν += 'ō'
                  elif tαg == ord('Ƶ'):#                 Alt U                                 υ | 
                    ιmαν += 'υ'
                  elif tαg == ord('ƹ'):#                 Alt Y                                 ῡ | 
                    ιmαν += 'ῡ'

                  elif tαg == ord('ƶ'):#                 Alt V                                 ν | 
                    ιmαν += 'ν'
                  elif tαg == ord('ƨ'):#                 Alt H                                 ʯ | 
                    ιmαν += 'ʯ'                
                  elif tαg == ord('Ƴ'):#                 Alt S                                 δ | 
                    ιmαν += 'δ'
                  elif tαg == ord('ŋ'):#                 Fn I                                  ῑ | 
                    ιmαν += 'ῑ'

                  elif tαg == ord('ǎ'):#                 Num(.)                                . | 
                    ιmαν += '.'
                  
                  elif tαg == curses.KEY_F10:#           F10                        Lιuem Qαmpαr |                                       
                    qαmpαr()
                  elif tαg == curses.KEY_F12:#           F12                              Stνlαt | 
                    curses.endwin() ; stνlαt('Stνlαt  ','','stνlαt') ; curses.curs_set(False)
                    if command == 'Tαuder':
                      if ιdeu == 'Tαuder': stνlαt('Tαuder  ',f'❯ Improl',0)
                      else: stνlαt('Tαuder  ',f'❯ {ιdeu}',0)
                  elif tαg != -1:#                       Dyαutαl                     Imαν lαgreu | 
                      ιmαν += chr(tαg)

                except Exception as e: stνlαt('Tαg     ',f'[red]{e}[/red]','Lαg ❯ ')
                
              except ValueError: ιmαν = ''
              except Exception as e: stνlαt('Tαg     ',f'{e}',0) ; S = Lαmseut(0,'Stαuνor','',e,'','') ; return
          def log():                                                                                            
            nonlocal S, ιmαν, uostιmαν, αdιmαν, ιlog

            S = Lαmseut(0,f'NOSTAL INTORAG │ {os.getcwd()} \n','','\n❯ ','','') ; ιmαν = uostιmαν = αdιmαν = str() ; ιlog = os.listdir() ; nlog = δlog1
          
            if len(ιlog) > δlog2: 
              for i in ιlog[δlog1:δlog2]: 
                nlog = nlog + 1
                if nlog < 10: S.prαν += f' {nlog} \u2502 {i}\n'
                elif len(ιlog) > 100 and nlog > (int(100/ylog))*ylog and nlog < 100: S.prαν += f' {nlog} \u2502 {i}\n'
                else: S.prαν += f'{nlog} \u2502 {i}\n'

              δnum1 = int(δlog2 / ylog)
              δnum2 = int(len(ιlog) / ylog) + 1
              
              if δlog2 > 100: S.prαν += f'   {δnum1}│{δnum2}\n'
              else: S.prαν += f'  {δnum1}│{δnum2}\n'
                
            else: 
              for i in ιlog[δlog1:δlog2]: 
                nlog = nlog + 1
                if len(ιlog) > 9 and nlog < 10: S.prαν += f' {nlog} \u2502 {i}\n'
                else: S.prαν += f'{nlog} \u2502 {i}\n'
              if δlog2 > ylog+1: 
                δnum1 = int(δlog2 / ylog)
                δnum2 = int(len(ιlog) / ylog) + 1
              
                if δlog2 > 100: S.prαν += f'   {δnum1}│{δnum2}\n'
                else: S.prαν += f'  {δnum1}│{δnum2}\n'
          def ιuνor():                                                                                          
            try:

              while True:
                mαιteu(0,'Iuνor')
                stdscr.addstr(1,0,'\u2500'*x, curses.color_pair(1))
                stdscr.addstr('1', curses.color_pair(3))
                stdscr.addstr(' Iuναδ\n')
                stdscr.addstr('2', curses.color_pair(3))
                stdscr.addstr(' Iuυν\n')
                stdscr.addstr('\u2500'*15, curses.color_pair(1))
                stdscr.addstr('\n')
                stdscr.addstr('3', curses.color_pair(3))
                stdscr.addstr(' Desktop\n')
                stdscr.addstr('4', curses.color_pair(3))
                stdscr.addstr(' Tᾱuderα\n')
                stdscr.addstr('5', curses.color_pair(3))
                stdscr.addstr(' Logreuα\n')
                stdscr.addstr('6', curses.color_pair(3))
                stdscr.addstr(' Mυuιt\n')
                stdscr.addstr('7', curses.color_pair(3))
                stdscr.addstr(' Nιtsem Mυuιt\n')
                stdscr.addstr('\u2500'*15, curses.color_pair(1))
                stdscr.addstr('\n')
                stdscr.addstr('8', curses.color_pair(3))
                stdscr.addstr(' Dyαutαl\n')
                stdscr.addstr('º', curses.color_pair(3))
                stdscr.addstr(' Iuνor lαg')

                try:
                  ιuνor = stdscr.getch()

                  if ιuνor == 27 or ιuνor == ord('ǐ'): return
                  elif ιuνor == ord('º'): tαg(1,0,0,'Iuνor','','Iutorαg ❯ ','','','','ιuνor4') ; stνlαt('Iuνorαt ',os.getcwd(),1) ; break
                  elif ιuνor == ord('1') or ιuνor == ord('Ǉ'): ιutorαg = r'G:\Mi unidad\Lιuem Stαuνor' ; break
                  elif ιuνor == ord('2') or ιuνor == ord('ǈ'): ιutorαg = r'C:\Users\Leane\OneDrive\Escritorio\Logreuα\Lιuem' ; break
                  elif ιuνor == ord('3') or ιuνor == ord('ǉ'): ιutorαg = r'C:\Users\Leane\OneDrive\Escritorio' ; break
                  elif ιuνor == ord('4') or ιuνor == ord('Ǆ'): ιutorαg = r'C:\Users\Leane\OneDrive\Escritorio\Dyαutαl\Tᾱuderα' ; break
                  elif ιuνor == ord('5') or ιuνor == ord('ǅ'): ιutorαg = r'C:\Users\Leane\OneDrive\Escritorio\Logreuα' ; break
                  elif ιuνor == ord('6') or ιuνor == ord('ǆ'): ιutorαg = r'C:\Users\Leane\OneDrive\Escritorio\Mυuιt' ; break
                  elif ιuνor == ord('7') or ιuνor == ord('ǁ'): ιutorαg = r'G:\Mi unidad\Mῡuιtsyα\Nιtsem\Imαδ' ; break
                  elif ιuνor == ord('8') or ιuνor == ord('ǂ'): ιutorαg = r'C:\Users\Leane\OneDrive\Escritorio\Dyαutαl' ; break
                  else: pass
                except Exception as e: stνlαt('Iuνorαt ',f'[red]{e}[/red]',0)

              os.chdir(f'{ιutorαg}') ; stνlαt('Iuνorαt ',os.getcwd(),1)

              stdscr.nodelay(True)
            except: pass
          def ιmtαu():                                                                                          
                    global ιmανtαuder
                    if ιmαν != '':
                      try:
                        if S.log != '': ιmtαuspace = '\n  '
                        else: ιmtαuspace = '\n'
                        ιmανsize = os.path.getsize(ιmαν)
                        if ιmανsize < 1000: ιmανtαuder = f'{ιmtαuspace} │ {str(ιmανsize)} B'
                        elif ιmανsize >= 1000 and ιmανsize < 1000000: ιmανtαuder = f'{ιmtαuspace} │ {str(ιmανsize)} K'
                        elif ιmανsize >= 1000000: ιmανtαuder = f'{ιmtαuspace} │ {str(ιmανsize/1000)} M'
                      except: stνlαt(αδqαιt,'Imαν Tαuder αqtαgeu',8)

                    else: pass
          stνlαt(αδqαιt,'[green]ιutαgeu[/green]','Mαιteu Iδᾱt ')
        except Exception as e: stνlαt(αδqαιt,f'[red]{e}[/red]','Mαιteu Iδᾱt ')
        
      # LOGRENAM 
        try: 
          def Euναrt():                                                                                       
              stνlαt(αδqαιt,'<ENVART>',0)
              y4 = y-4 ; y5 = y-5 ; x1 = x-1 ;  x2 = x-2
              padselect = 1 ; selectitem = 0 ; item = str()
              scritem = 0
              
              #import time
              stdscr.nodelay(True)

              euναrt = label = str() ; z = 0

              try: 
                with open(r'G:\Mi unidad\Lιuem Stαuνor\Euναrt.txt','r',encoding='utf8') as oppel: euναδqαιt = oppel.read() ; teνuα = euναδqαιt
                with open(r'G:\Mi unidad\Lιuem Stαuνor\Euναrt.txt','r',encoding='utf8') as oppel: selectlines = oppel.readlines()
              except: teνuα = ''

              while True:
                mαιteu(1,ιdeu = 'Euναrt')
                stdscr.addstr(2,0,'Toreg → | Izeu | Mυuιtsyα | Mαιteu | Lestαq |'+' '*euνspace+f'\u276f {date}')
                stdscr.addstr(2,z,euναrt,curses.color_pair(5))
                stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(1))

                if euναrt == '': 
                  pad1 = curses.newpad(1000, 158)
                  pad2 = curses.newpad(1000, 158)
                  pad3 = curses.newpad(1000, 158)
                  pad4 = curses.newpad(1000, 158)
                  pad1.addstr(teνuα)
                  pad2.addstr(teνuα)
                  pad3.addstr(teνuα)
                  pad4.addstr(teνuα)
                  if padselect == 1: 
                    scritem = selectitem
                    pad1.addstr(scritem,1,item,curses.color_pair(5))
                  elif padselect == 2:
                    scritem = selectitem# + 4 - y
                    pad2.addstr(0,1,item,curses.color_pair(5))
                  elif padselect == 3:
                    scritem = selectitem# - y*2
                    pad3.addstr(scritem,1,item,curses.color_pair(5))
                  elif padselect == 4:
                    scritem = selectitem # - y*3
                    pad4.addstr(scritem,1,item,curses.color_pair(5))
                  pad1.refresh(0,0,4,1,y-1,39)
                  pad2.refresh(46,0,4,40,y-1,84)
                  pad3.refresh(92,0,4,85,y-1,144)
                  pad4.refresh(138,0,4,145,y-1,x-1)
                  
                elif euναrt == ' Izeu ': 
                  pad1 = curses.newpad(1000, 158)
                  pad2 = curses.newpad(1000, 158)
                  pad3 = curses.newpad(1000, 158)
                  pad4 = curses.newpad(1000, 158)
                  pad5 = curses.newpad(1000, 158)
                  pad6 = curses.newpad(1000, 158)
                  pad7 = curses.newpad(1000, 158)
                  pad8 = curses.newpad(1000, 158)

                  pad1.addstr(teνuα)
                  pad2.addstr(teνuα)
                  pad3.addstr(teνuα)
                  pad4.addstr(teνuα)
                  pad5.addstr(teνuα)
                  pad6.addstr(teνuα)
                  pad7.addstr(teνuα)
                  pad8.addstr(teνuα)

                  pad1.refresh(0,0,4,1,19,41)
                  pad2.refresh(14,0,4,42,19,81)
                  pad3.refresh(28,0,4,82,19,114)
                  pad4.refresh(42,0,4,115,19,149)                  
                  pad5.refresh(56,0,4,150,19,x1)

                  pad6.refresh(72,0,20,1,y-1,41)
                  pad7.refresh(102,0,20,42,y-1,139)
                  pad8.refresh(132,0,20,140,y-1,x1)
                
                else:
                  pad = curses.newpad(200, 158)
                  pad.addstr(teνuα)
                  pad.refresh(0,0,6,4,y5,x1)

                try: 
                  νιαr = stdscr.getch()

                  if νιαr == 27:
                    S = Lαmseut(0,'Stαuνor','','','','')
                    ιmαν = ''
                    stdscr.clear()
                    break
                  elif νιαr == ord('º'):
                    stνlαt('Euναrt  ','→ Euναrt',0)
                    euναrt = '' ; teνuα = euναδqαιt
                  elif νιαr == ord('.'): euναrt = ''

                  elif νιαr == ord('1') or νιαr == ord('i') or νιαr == ord('I'): # Improl Teνuα 
                    stνlαt('Euναrt  ','→ Izeu Teνuα',0) ; z = 9

                    with open(r'Izeu Teνuα.txt','r',encoding='utf8') as oppel:
                      teνuα = oppel.read()
                      label = ' Izeu '
                      euναrt = label
                  elif νιαr == ord('2') or νιαr == ord('m') or νιαr == ord('M'): # Mυuitsyα Teνuα 
                    stνlαt('Euναrt  ','→ Mυuιtsyα Teνuα',0)
                    z = 16

                    with open(r'Mυuιtsyα Teνuα.txt','r',encoding='utf8') as oppel:
                      teνuα = oppel.read()
                      label = ' Mυuιtsyα '
                      euναrt = label
                  elif νιαr == ord('3') or νιαr == ord('a') or νιαr == ord('A'): # Aδqαιt Teνuα 
                    stνlαt('Euναrt  ','→ Mαιteu Teνuα',0)
                    teνuα = ''
                    z = 27
                    label = ' Mαιteu '
                    euναrt = label
                    oppel = open(r'Mαιteu Teνuα.txt','r',encoding='utf8')
                    teνuα = str(oppel.read())
                    oppel.close()
                  elif νιαr == ord('4') or νιαr == ord('l') or νιαr == ord('L'): # Lestαq 
                    stνlαt('Euναrt  ','→ Lestαq',0) ; z = 36
                    with open(r'Lestαq.txt','r',encoding='utf8') as oppel:
                      teνuα = oppel.read()
                      label = ' Lestαq '
                      euναrt = label
                  elif νιαr == ord('0'): # Lαg 
                    stνlαt('Euναrt  ','→ Lαg',0) 
                    import os ; os.system(r'"G:\Mi unidad\Lιuem Stαuνor\Euναrt.txt"')
                  elif νιαr == ord('d') or νιαr == ord('D'): # Dyeναstαq 
                    stνlαt('Euναrt  ','→ Dyeναstαq',0) 
                    import webbrowser as wb
                    wb.open('https://calendar.google.com/calendar/') 
                  elif νιαr == ord('Ʃ'): # Alt i          Improl Teνuα Lαg | 
                    import os ; os.system('"Izeu Teνuα.txt"') ; stdscr.clear()

                  elif νιαr == curses.KEY_F10:#           F10                Lιuem Qαmpαr |                                       
                    qαmpαr()
                  elif νιαr == curses.KEY_F12:#  F12          Stνlαt 
                    curses.endwin() ; stνlαt('Stνlαt  ','','stνlαt') ; curses.curs_set(False) ; stνlαt(αδqαιt,f'<ENVART>',0)

                  elif νιαr == curses.KEY_UP:# 
                    if selectitem > 0:
                      selectitem -= 1
                      item = selectlines[selectitem][1:]
                  elif νιαr == curses.KEY_DOWN:# 
                    selectitem += 1
                    if selectitem > 0: item = selectlines[selectitem][1:]
                  elif νιαr == curses.KEY_RIGHT:# 
                    if padselect < 4:
                      padselect += 1
                      #selectitem += y
                      #item = selectlines[selectitem][1:]

                  elif νιαr == curses.KEY_LEFT:# 
                    if padselect > 1:
                      padselect -= 1 # ; selectitem -= y
                      item = selectlines[selectitem][1:]

                except Exception as e: stνlαt('Euναrt  ',f'{e}',0) ; euναrt = '' ; down = '' ; teνuα = euναδqαιt ; z = 0 ; label = ''
                stdscr.refresh()
                time.sleep(0.01)
          def Vermαt():                                                                                       
            global vlx, vlαιu
            nonlocal νerseut, νerseut2

            toregαm = [' Imαδ ',' Improl ',' Mυuιtsyα ',' Pιlμα ',' Aιleus ',' Lιuemαg ']
            tselect = int()
            lαδcopy = str()

            try: 
              stνlαt(αδqαιt,'<VERMAT>',0)
              νermαt = νmαν = lαδuνmαν = uostνmαν = αdνmαν = toreg = lαδutoreg = uostoreg = αdtoreg = prompt = sub1 = sub2 = sub3 = sub4 = sub5 = str()
              vlx = 0 ; vlαιu = ' Imαδ '; νιdeu = 'Imαδ.csv' ; νqseut = False ; strnum = 0

              def geuδ(νιdeu):
                nonlocal lines 
                try:
                  nonlocal read
                  read = ''
                  n = 0
                  with open(rf"{νιdeu}",encoding='utf8') as oppel: 
                    lines = oppel.readlines()
                    if νιdeu == 'Lestαq.txt':
                      for i in lines: 
                        n = n + 1
                        if n > 24: read += f'{i}'
                        else: pass
                    
                    elif νιdeu == 'Lιuem Vermαt.txt':
                      for i in lines: n = n + 1 ; read += f'{i}'

                    else:
                      for index, i in enumerate(lines):
                        if len(lines) < 10: read += f'{str(index+1)} \u2502  ' ; read += f'{i}'
                        else:
                          if index < 9: read += f'{str(index+1)}  \u2502  ' ; read += f'{i}'
                          else: read += f'{str(index+1)} \u2502  ' ; read += f'{i}'
                except: pass
              geuδ(νιdeu)

              def selector(key): 
                nonlocal item, lines, numero, strnum, prompt

                if key == 'αdινeu':
                  try:
                    if item == str(): numero = 0 ; strnum = numero
                    if numero <= len(lines) and numero > -1: numero = numero - 1
                    if numero < 1: numero = len(lines)
                    strnum = numero
                    if strnum == 0: strnum = len(lines)
                    elif strnum < 0: strnum = strnum + len(lines)
                    item = lines[numero-1]
                    if len(lines) < 9: prompt = f'{strnum} │  {item}'
                    else:
                      if strnum > 9: prompt = f'{strnum} │  {item}'
                      else: prompt = f' {strnum} │  {item}' 
                  except Exception as e: stνlαt(αδqαιt,f'{e}',0)                          

                elif key == 'δινeu':
                  try:
                    if item == str(): numero = 0
                    if numero < len(lines): numero = numero + 1
                    else: numero = 1
                    strnum = numero
                    if strnum == 0: strnum = len(lines)
                    elif strnum < 0: strnum = strnum + len(lines)
                    item = lines[numero-1]
                    if len(lines) < 9: prompt = f'{strnum} │  {item}'
                    else: 
                      if strnum > 9: prompt = f'{strnum} │  {item}'
                      else: prompt = f' {strnum} │  {item}'
                  except Exception as e: stνlαt(αδqαιt,f'{e}',0)               

              def lαmνmαt(): 
                nonlocal strnum
                mαιteu(0,'Vermαt')
                stdscr.addstr(2,0,' Imαδ  │ Improl │ Mυuιtsyα │ Pιlμα │ Aιleus │ Lestαq │ Lestαq 3 │ Lιuemαg │'+' '*νspace+f'\u276f {date}')
                if vlαιu == ' Imαδ ': 
                  stdscr.addstr(2,vlx,vlαιu,curses.color_pair(2))
                  stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(1)) 
                else:
                  stdscr.addstr(2,vlx,vlαιu,curses.color_pair(5))
                  if vlαιu == ' Pιlμα ': stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(8))
                  elif vlαιu == ' Mυuιtsyα ': stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(7))
                  else: stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(2))
                stdscr.addstr('\n')
                stdscr.addstr(read)           
                '''if νermαt == '':            # Main    
                  stdscr.addstr(prompt)
                  stdscr.addstr(νmαν)
                  stdscr.addstr('\n')
                  stdscr.addstr('\u2500'*x,curses.color_pair(1))'''
                if  νermαt == ord('.'):   # Sιguα   
                  if νιdeu != 'Lestαq.txt' or νιdeu != 'Lιuem Vermαt.txt': 
                    if read.count('\n') > 9: stdscr.addstr(f'→  │  ')
                    else: stdscr.addstr(f'→ │  ')

                  stdscr.addstr(νmαν)
                  stdscr.addstr(lαδuνmαν,curses.color_pair(5))
                  stdscr.addstr(αdνmαν) 
                  stdscr.addstr('\n')
                
                stdscr.addstr('\n')
                stdscr.addstr('\u2500'*x,curses.color_pair(1))

                if  νermαt == ord(':') or νermαt == ord(',') or νermαt == ord('-'):
                  stdscr.addstr(4+strnum,0,prompt.rstrip('\n'),curses.color_pair(5))
                  stdscr.addstr('  ')
                  stdscr.addstr(νmαν)
                #else:                       # Dyαutαl 

                  
                stdscr.addstr(sub1) 
                stdscr.addstr(toreg,curses.color_pair(2))
                                  

                if νqseut == True: stdscr.addstr(lαδutoreg,curses.color_pair(5))
                stdscr.addstr(αdtoreg)
                stdscr.addstr(sub2,curses.color_pair(3)) 
                stdscr.addstr('\n')
                stdscr.addstr(sub3)
                stdscr.addstr(sub4)
                stdscr.addstr(sub5)

                νerseuter()

              def checkνιdeu(): 
                try: oppel = open(f'{νιdeu}','r')
                except Exception as e: stνlαt('Vermαt  ',f'{e}',0)
              checkνιdeu()
                             
              while 1: 
                lαmνmαt()

                if tselect < 0: tselect = 7
                if tselect > 7: tselect = 0

                if tselect == 0: vlx = 0 ; vlαιu = ' Imαδ ' ; νιdeu = 'Imαδ.csv' ; geuδ(νιdeu)
                if tselect == 1: vlx = 8 ; vlαιu = ' Improl ' ; νιdeu = 'Vermαt.txt' ; geuδ(νιdeu)
                if tselect == 2: vlx = 17 ; vlαιu = ' Mυuιtsyα ' ; νιdeu = 'Mυuιt Vermαt.txt' ; geuδ(νιdeu)
                if tselect == 3: vlx = 28 ; vlαιu = ' Pιlμα ' ; νιdeu = 'Verpιlμα.txt' ; geuδ(νιdeu)
                if tselect == 4: vlx = 36 ; vlαιu = ' Aιleus ' ; νιdeu = 'Aιleus Vermαt.txt' ; geuδ(νιdeu)
                if tselect == 5: vlx = 45 ; vlαιu = ' Lestαq ' ; νιdeu = 'Lestαq.txt' ; geuδ(νιdeu) ; checkνιdeu()
                if tselect == 6: 
                  vlx = 54 ; vlαιu = ' Lestαq 3 ' ; read = str() ; stdscr.clear()

                  try:
                    while 1:
                      mαιteu(1,'Vermαt')

                      stdscr.addstr(2,0,' Imαδ  │ Improl | Mυuιtsyα │ Pιlμα │ Aιleus │ Lestαq │ Lestαq 3 │ Lιuemαg │'+' '*νspace+f'\u276f {date}')
                      stdscr.addstr(2,vlx,vlαιu,curses.color_pair(5))
                      stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(3))

                      with open('Lestαq 3.txt','r',encoding='utf8') as oppel: estαq = str(oppel.read())
                      pad1 = curses.newpad(300,x)
                      pad2 = curses.newpad(300,x)
                      pad3 = curses.newpad(300,x)
                      pad1.addstr(estαq)
                      pad2.addstr(estαq)
                      pad3.addstr(estαq)
                      pad1.refresh(0,0,4,0,45,74)
                      pad2.refresh(48,0,4,75,45,137)
                      pad3.refresh(90,0,4,138,y-1,x-3)

                      # import pandas as pd
                      # checkmarks_df = pd.read_csv('Checkmarks.csv')
                      # checkmarks = str(checkmarks_df)

                      # pad = curses.newpad(900,900)
                      # pad.addstr(checkmarks)
                      # pad.refresh(0,0,32,5,41,65)

                      estαqer = stdscr.getch()

                      if estαqer == 27 or estαqer == 10: vlx = 0 ; vlαιu = '' ; νιdeu = 'Vermαt.txt' ; return 
                      elif estαqer == ord('º') or estαqer == ord('1') or estαqer == ord('Ǉ'): tselect = 0 ; break
                      elif estαqer == ord('2') or estαqer == ord('ǈ'): stdscr.clear() ; tselect = 1 ; break
                      elif estαqer == ord('3') or estαqer == ord('ǉ'): stdscr.clear() ; tselect = 2 ; break
                      elif estαqer == ord('4') or estαqer == ord('Ǆ'): stdscr.clear() ; tselect = 3 ; break
                      elif estαqer == ord('5') or estαqer == ord('ǅ'): stdscr.clear() ; tselect = 4 ; break
                      elif estαqer == ord('6') or estαqer == ord('ǆ'): stdscr.clear() ; tselect = 5 ; break
                      elif estαqer == ord('8') or estαqer == ord('ǂ'):#                    Lιuemαg Dyανorδα | 
                        tselect = 7 ; geuδ('Lιuem Vermαt.txt') ; checkνιdeu() ; break
                      elif estαqer == curses.KEY_LEFT:#                      Left |                                       
                        tselect = tselect - 1 ; break
                      elif estαqer == curses.KEY_RIGHT:#                     Right |                                       
                        tselect = tselect + 1 ; break

                      elif estαqer == ord('t') or estαqer == ord('T'): Tαuder('Tαuder','│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ │ Lαg │')
                      elif estαqer == ord('d') or estαqer == ord('D'): Tαuder('Dyαteν','| Lαg |')
                      elif estαqer == ord('m') or estαqer == ord('M'): Tαuder('Mυuιtsyα Tαuder','| Lαg |')
                      elif estαqer == ord('0'): #                                                      Lαg | 
                        import os ; os.system(f'"Lestαq 3.txt"')
                  except Exception as e: stνlαt('Vermαt  ',f'{e}',0) ; tselect = 0
                if tselect == 7: vlx = 65 ; vlαιu = ' Lιuemαg ' ; νιdeu = 'Lιuem Vermαt.txt' ; geuδ(νιdeu)

                if νermαt == 27: stdscr.clear() ; νιdeu = 'Imαδ.csv' ; return

                elif νermαt == ord('.') or νermαt == ord('Ǒ'): # Num(+)                       Sιguα │ 
                  while True: 
                          
                    try:
                      if uostνmαν == str(): lαδuνmαν = ' '
                      else: lαδuνmαν = uostνmαν
                      lαmνmαt()
                      stdscr.addstr(0,8,'| ',curses.color_pair(2))
                      stdscr.addstr(0,10,'Sιguα')
                      stdscr.addstr(' |',curses.color_pair(2))

                      sιguα = stdscr.getch()

                      if sιguα == 27:#                                             Esc | 
                        νmαν = prompt = str() ;  break
                      elif sιguα == 10:#                                        Return | 
                        
                        if f'{νmαν}{uostνmαν}{αdνmαν}' != '': 
                          with open(νιdeu,'a',encoding='utf8') as oppel:
                            oppel.write(νmαν)
                            oppel.write(uostνmαν)
                            oppel.write(αdνmαν)
                            oppel.write('\n')
                          stνlαt('Sιguα ',f'{νmαν}{uostνmαν}{αdνmαν}',7)
                          prompt = νmαν = uostνmαν = αdνmαν = ''
                          geuδ(νιdeu)
                          break
                        else: break
                      
                      # Lαg
                      elif sιguα == 0o10:#      Back                            νmαν-1 | 
                        νmαν = νmαν[:-1]
                      elif sιguα == curses.KEY_DC:#  Supr                     αdνmαν-1 | 
                        if len(αdνmαν) > 0: uostνmαν = αdνmαν[0] ; αdνmαν = αdνmαν[1:]
                        else: uostνmαν = ''
                      elif sιguα == ord('Ǟ'):# Alt Supr                                | 
                        uostνmαν = αdνmαν = str()
                      elif sιguα == ord('ƀ'):#  <                                    → | 
                        νmαν += ' → '
                      elif sιguα == ord('ş'):#  Shift Tab                            ❯ | 
                        νmαν += '\t❯  '
                      
                      # Nav
                      elif sιguα == curses.KEY_LEFT:# Left key                 To left | 
                        if νmαν != '': αdνmαν = uostνmαν + αdνmαν ; uostνmαν = νmαν[-1] ; νmαν = νmαν[:-1]
                      elif sιguα == curses.KEY_RIGHT:# Right key              To right | 
                        if αdνmαν != '': νmαν += uostνmαν ; uostνmαν = αdνmαν[0] ; αdνmαν = αdνmαν[1:]
                        else: νmαν += uostνmαν ; uostνmαν = ''

                      elif sιguα == curses.KEY_UP:# Up key                      To top | 
                        αdνmαν = νmαν[1:] + uostνmαν + αdνmαν ; uostνmαν = νmαν[0] ; νmαν = ''
                      elif sιguα == curses.KEY_DOWN:# Down key                  To end | 
                        νmαν = νmαν + uostνmαν + αdνmαν ; uostνmαν = αdνmαν = ''
                      
                      # Copy
                      elif sιguα == ord('ƻ'):#   Ctrl Left key         νmαν to νerseut | 
                        νerseut = νmαν
                      elif sιguα == ord('Ƽ'):#  Ctrl Right key       αdνmαν to νerseut | 
                        νerseut = uostνmαν + αdνmαν
                      elif sιguα == ord('Ƈ'):#  Shift Left key        νmαν to νerseut2 | 
                        νerseut2 = νmαν
                      elif sιguα == ord('Ɛ'):# Shift Right key      αdνmαν to νerseut2 | 
                        νerseut2 = uostνmαν + αdνmαν

                      # Paste
                      elif sιguα == ord('Ǡ'):#     Ctrl Up key         νerseut to νmαν | 
                        if νerseut != '': νmαν += νerseut
                      elif sιguα == ord('ǡ'):#   Ctrl Down key        νerseut2 to νmαν | 
                        if νerseut2 == '': νmαν += νerseut2

                      # Mυsselαιtμ

                      # Alt
                      elif sιguα == ord('Ʊ'):# Alt Q         ᾱ 
                        νmαν += 'ᾱ'
                      elif sιguα == ord('ơ'):# Alt A         ɒ 
                        νmαν += 'ɒ'
                      elif sιguα == ord('ƥ'):# Alt E         ɢ 
                        νmαν += 'ɢ'
                      elif sιguα == ord('€'):#  Gr E         ē | 
                        νmαν += 'ē'                            
                      elif sιguα == ord('Ʃ'):# Alt I         ι 
                        νmαν += 'ι'
                      elif sιguα == ord('Ư'):# Alt O         ō 
                        νmαν += 'ō'
                      elif sιguα == ord('Ƶ'):# Alt U         υ 
                        νmαν += 'υ'
                      elif sιguα == ord('ƹ'):# Alt Y         ῡ 
                        νmαν += 'ῡ'

                      elif sιguα == ord('ƶ'):# Alt V         ν 
                        νmαν += 'ν'
                      elif sιguα == ord('ƨ'):# Alt H         μ 
                        νmαν += 'μ'                
                      elif sιguα == ord('Ƴ'):# Alt S         δ 
                        νmαν += 'δ'

                      # Fn
                      elif sιguα == ord('ŋ'):#  Fn I         ῑ 
                        νmαν += 'ῑ'

                      elif sιguα != -1: νmαν += chr(sιguα)
                          
                    except Exception as e: stνlαt('Sιguα ',f'{e} {νmαν}',7) ; νmαν = ''
                elif νermαt == ord(':') or νermαt == ord('Ǐ'): # Num(*)                      Verqom │ 
                  def νerqom():  
                    nonlocal ιdeu, item, lines, prompt, νmαν, strnum, νerseut, νerseut2
                    ιdeu= 'Vermαt' ; item = str()

                    oppel = open(νιdeu,encoding='utf8')
                    lines = oppel.readlines()

                    while True: 
                      try:
                        lαmνmαt()
                        stdscr.addstr(0,7,' │ ',curses.color_pair(2))
                        stdscr.addstr('Verqom')
                        stdscr.addstr(' │',curses.color_pair(2))

                        νqnum = stdscr.getch()   

                        if νqnum == 27: prompt = νmαν = '' ; strnum = 0 ; return

                        elif νqnum == 10 or νqnum == ord('ǋ'): 
                          if item != '': 
                            νmαν = str(item.rstrip('\n'))
                            nonlocal νqseut, lαδutoreg, uostoreg, αdtoreg
                            νqseut = True
                            while 1:
                              try:                 
                                if len(lines) < 10: prompt = f'{strnum} ❯'
                                else: 
                                  if strnum < 10: prompt = f'{strnum}  ❯'
                                  else: prompt = f'{strnum} ❯'

                                if uostoreg != '': lαδutoreg = uostoreg
                                else: lαδutoreg = ' ' 

                                lαmνmαt()
                                stdscr.addstr(0,7,' │ ',curses.color_pair(2))
                                stdscr.addstr('Verqom')
                                stdscr.addstr(' │',curses.color_pair(2))                  
                              
                                eudαμl = stdscr.getch()

                                if eudαμl == 27: prompt = νmαν = uostoreg = αdtoreg = str() ; strnum = 0 ; νqseut = False ; break
                                
                                elif eudαμl == 10: 
                                  lines[numero-1] = νmαν + uostoreg + αdtoreg + '\n'
                                  with open(νιdeu, 'w',encoding='utf8') as oppel: oppel.truncate(0)
                                  for i in lines:
                                    oppel = open(νιdeu,'a',encoding='utf8')
                                    oppel.write(i)
                                    oppel.close()         
                                  stνlαt('Eudαμl',f'{νmαν}{uostoreg}{αdtoreg}',7)
                                  strnum = 0

                                  prompt = νmαν = uostoreg = αdtoreg = str() ; νqseut = False ;  geuδ(νιdeu) ; return

                                # Lag                                 
                                elif eudαμl == 0o10: νmαν = νmαν[:-1]
                                elif eudαμl == ord('Ǹ'):# Alt Backspace                                     | 
                                  pass
                                elif eudαμl == curses.KEY_DC:# Supr                                              | 
                                  if len(αdtoreg) > 0: uostoreg = αdtoreg[0] ; αdtoreg = αdtoreg[1:]
                                  else: uostoreg = ''
                                elif eudαμl == ord('Ǟ'):# Alt Supr                                          | 
                                  uostoreg = αdtoreg = str()

                                elif eudαμl == ord('ƀ'): νmαν += ' → '
                                elif eudαμl == ord('ş'): νmαν += '\t❯  '
                                   
                                # Copy                                                              
                                elif eudαμl == ord('ƻ'):#   Ctrl Left key                   νmαν to νerseut | 
                                  νerseut = νmαν
                                elif eudαμl == ord('Ƽ'):#  Ctrl Right key            uost-αdνmαν to νerseut | 
                                  νerseut = uostoreg + αdtoreg
                                elif eudαμl == ord('Ƈ'):#  Shift Left key                  νmαν to νerseut2 | 
                                  νerseut2 = νmαν
                                elif eudαμl == ord('Ɛ'):# Shift Right key           uost-αdνmαν to νerseut2 | 
                                  νerseut2 = uostoreg + αdtoreg

                                # Paste
                                elif eudαμl == ord('Ǡ'):#     Ctrl Up key                  νerseut to νmαν | 
                                  if νerseut == '': pass
                                  else: νmαν += νerseut
                                elif eudαμl == ord('ǡ'):#   Ctrl Down key                 νerseut2 to νmαν | 
                                  if νerseut2 == '': pass
                                  else: νmαν += νerseut2

                                # Nav
                                elif eudαμl == curses.KEY_LEFT:# Left key                          ιmαν -1 | 
                                  if len(νmαν) > 0: αdtoreg = uostoreg + αdtoreg ; uostoreg = νmαν[-1] ; νmαν = νmαν[:-1]
                                elif eudαμl == curses.KEY_RIGHT:# Right key                      αdιmαν -1 | 
                                  if len(αdtoreg) > 0: νmαν += uostoreg ; uostoreg = αdtoreg[0] ; αdtoreg = αdtoreg[1:]
                                  else: νmαν += uostoreg ; uostoreg = ''
                                elif eudαμl == curses.KEY_UP:# Up key                               To top | 
                                  αdtoreg = νmαν[1:] + uostoreg + αdtoreg ; uostoreg = νmαν[0] ; νmαν = ''
                                elif eudαμl == curses.KEY_DOWN:# Down key                           To end | 
                                  νmαν = νmαν + uostoreg + αdtoreg ; uostoreg = αdtoreg = ''

                                # Mυsselαιtμ

                                # Alt
                                elif eudαμl == ord('ƣ'):# Alt C         ϥ 
                                  νmαν += 'ϥ'
                                elif eudαμl == ord('ơ'):# Alt A         ɒ 
                                  νmαν += 'ɒ'  
                                elif eudαμl == ord('Ʊ'):# Alt Q         ᾱ 
                                  νmαν += 'ᾱ'                                
                                elif eudαμl == ord('ƥ'):# Alt E         ɢ 
                                  νmαν += 'ɢ'
                                elif eudαμl == ord('€'):#  Gr E         ē 
                                  νmαν += 'ē'
                                elif eudαμl == ord('Ʃ'):# Alt I         ι 
                                  νmαν += 'ι'
                                elif eudαμl == ord('Ư'):# Alt O         ō 
                                  νmαν += 'ō'
                                elif eudαμl == ord('Ƶ'):# Alt U         υ 
                                  νmαν += 'υ'
                                elif eudαμl == ord('ƹ'):# Alt Y         ῡ 
                                  νmαν += 'ῡ'
                                elif eudαμl == ord('ƶ'):# Alt V         ν 
                                  νmαν += 'ν'
                                elif eudαμl == ord('ƨ'):# Alt H         μ 
                                  νmαν += 'ʯ'                
                                elif eudαμl == ord('Ƴ'):# Alt S         δ 
                                  νmαν += 'δ'

                                # Fn
                                elif eudαμl == ord('ŋ'):#  Fn I         ῑ  
                                  νmαν += 'ῑ'

                                elif eudαμl != -1: νmαν += chr(eudαμl)
                                else: pass
                                                      
                              except IndexError: pass
                              except ValueError: νmαν = ''
                              except Exception as e: stνlαt('Verqom',f'{e}',7) ; toreg = ''

                        elif νqnum == 0o10 or νqnum == ord('º'): prompt = ':' ; item = ''                          

                        elif νqnum == ord('ƻ'):#   Ctrl Left key 
                          νerseut = item[:-1]
                        elif νqnum == ord('Ƽ'):#  Ctrl Right key 
                          νerseut2 = item[:-1]

                        elif νqnum == curses.KEY_UP or νqnum == curses.KEY_LEFT:# Up key 
                          selector('αdινeu')
                        elif νqnum == curses.KEY_DOWN or νqnum == curses.KEY_RIGHT:# Down key 
                          selector('δινeu')
                        
                        # Num Pad
                        elif νqnum == ord('Ǉ'):# Num(1) 
                          item = lines[0] ; strnum = numero = 1
                          if len(lines) < 9: prompt = f'{strnum} │  {item}'
                          else:                      
                            if strnum > 9: prompt = f'{strnum} │  {item}'
                            else: prompt = f'{strnum}  │  {item}'
                        elif νqnum == ord('ǈ'):# Num(2) 
                          item = lines[1] ; strnum = numero = 2
                          if len(lines) < 9: prompt = f'{strnum} │  {item}'
                          else:                      
                            if strnum > 9: prompt = f'{strnum} │  {item}'
                            else: prompt = f'{strnum}  │  {item}'
                        elif νqnum == ord('ǉ'):# Num(3) 
                          item = lines[2] ; strnum = numero = 3
                          if len(lines) < 9: prompt = f'{strnum} │  {item}'
                          else:                      
                            if strnum > 9: prompt = f'{strnum} │  {item}'
                            else: prompt = f'{strnum}  │  {item}'
                        elif νqnum == ord('Ǆ'):# Num(4) 
                          item = lines[3] ; strnum = numero = 4
                          if len(lines) < 9: prompt = f'{strnum} │  {item}'
                          else:                      
                            if strnum > 9: prompt = f'{strnum} │  {item}'
                            else: prompt = f'{strnum}  │  {item}'
                        elif νqnum == ord('ǅ'):# Num(5) 
                          item = lines[4] ; strnum = numero = 5
                          if len(lines) < 9: prompt = f'{strnum} │  {item}'
                          else:                      
                            if strnum > 9: prompt = f'{strnum} │  {item}'
                            else: prompt = f'{strnum}  │  {item}'
                        elif νqnum == ord('ǆ'):# Num(6) 
                          item = lines[5] ; strnum = numero = 6
                          if len(lines) < 9: prompt = f'{strnum} │  {item}'
                          else:                      
                            if strnum > 9: prompt = f'{strnum} │  {item}'
                            else: prompt = f'{strnum}  │  {item}'
                        elif νqnum == ord('ǁ'):# Num(7) 
                          item = lines[6] ; strnum = numero = 7
                          if len(lines) < 9: prompt = f'{strnum} │  {item}'
                          else:                      
                            if strnum > 9: prompt = f'{strnum} │  {item}'
                            else: prompt = f'{strnum}  │  {item}'
                        elif νqnum == ord('ǂ'):# Num(8) 
                          item = lines[7] ; strnum = numero = 8
                          if len(lines) < 9: prompt = f'{strnum} │  {item}'
                          else:                      
                            if strnum > 9: prompt = f'{strnum} │  {item}'
                            else: prompt = f'{strnum}  │  {item}'
                        elif νqnum == ord('ǃ'):# Num(9) 
                          item = lines[8] ; strnum = numero = 9
                          if len(lines) < 9: prompt = f'{strnum} │  {item}'
                          else:                      
                            if strnum > 9: prompt = f'{strnum} │  {item}'
                            else: prompt = f'{strnum}  │  {item}'
                        elif νqnum == ord('Ǻ'):# Num(0) 
                          item = lines[9] ; strnum = numero = 10
                          if len(lines) < 9: prompt = f'{strnum} │  {item}'
                          else:                      
                            if strnum > 9: prompt = f'{strnum} │  {item}'
                            else: prompt = f'{strnum}  │  {item}'

                        else: 
                          if νqnum != -1: 
                            try:
                              oppel = open(νιdeu,encoding='utf8')
                              lines = oppel.readlines()

                              νqnum = chr(νqnum)
                              numero = int(νqnum)
                              if numero == 0: 
                                if len(lines) > 9: numero = 10
                                else: numero = len(lines)
                              strnum = str(numero)

                              item = lines[numero-1]
                              stdscr.addstr('\n')
                              if len(lines) < 10: prompt = f'{strnum} │  {lines[numero-1]}'
                              else:                      
                                if int(strnum) > 9: prompt = f'{strnum} │  {item}'
                                else: prompt = f'{strnum}  │  {item}'
                              strnum = int(strnum)
                              stvlitem = item.rstrip('\n')
                              stνlαt('Verqom',f'{stvlitem}',7)
                      
                            except ValueError: pass
                            except IndexError: toreg = ''
                      
                      except Exception as e: stνlαt('Verqom',f'{e}',7)
                  νerqom()
                elif νermαt == ord(',') or νermαt == ord('Ǌ'): # Num(/)                       Verse │ 
                  def νerse():
                    nonlocal ιdeu, prompt, νmαν, sub1, sub2, toreg, νιdeu, toregαm, item, lines, strnum, νerseut, νerseut2
                    prompt = '' ; ιdeu= 'Vermαt' ; numero = 0 ; item = str()

                    oppel = open(νιdeu,encoding='utf8')
                    lines = oppel.readlines()

                    while True:
                      try:
                        lαmνmαt()
                        stdscr.addstr(0,7,' │ ',curses.color_pair(2))
                        stdscr.addstr('Verse')
                        stdscr.addstr(' │',curses.color_pair(2))

                        νsnum = stdscr.getch()   

                        if νsnum == 27: prompt = νmαν = toreg = '' ; strnum = 0 ; break

                        elif νsnum == 10 or νsnum == ord('ǋ'): 
                          if item == '': pass
                          else:
                            nonlocal νqseut, αdtoreg
                            tnum = tselect          # Toreg selector

                            while 1:
                              try:
                                sub1 = '  ❯' ; toreg = toregαm[tnum]
                              
                                lαmνmαt()
                                stdscr.addstr(0,7,' │ ',curses.color_pair(2))
                                stdscr.addstr('Verse')
                                stdscr.addstr(' │',curses.color_pair(2))                  
                              
                                eudαμl = stdscr.getch()

                                if eudαμl == 27: prompt = νmαν = sub1 = toreg = sub2 = '' ; strnum = 0 ; return
                                
                                elif eudαμl == 10 or eudαμl == ord('ǋ'):
                                  if toreg == vlαιu:
                                    position = len(lines)
                                    while 1:
                                      toreg = f'{vlαιu}: '
                                      sub2 = str(position)
                                      lαmνmαt()
                                      stdscr.addstr(0,7,' │ ',curses.color_pair(2))
                                      stdscr.addstr('Verse')
                                      stdscr.addstr(' │',curses.color_pair(2))                  
                              
                                      try:
                                        getposit = stdscr.getch()
                                        if getposit == 27: toreg = αdtoreg = sub2 = '' ; break
                                        elif getposit == 10 or getposit == ord('ǋ'):
                                          lines.pop(numero-1)
                                          lines.insert(position-1,item)
                                          with open(νιdeu, 'w',encoding='utf8') as oppel:
                                            oppel.truncate(0)
                                          for i in lines:
                                            with open(νιdeu,'a',encoding='utf8') as oppel:
                                              oppel.write(i)

                                          prompt = νmαν = sub1 = toreg = sub2 = sub1 = str() ; strnum = 0 ; geuδ(νιdeu)  ; return

                                        elif getposit == curses.KEY_UP or getposit == curses.KEY_LEFT:# Up/left key 
                                          if position > 1:
                                            position -= 1
                                          else: position = len(lines)
                                        elif getposit == curses.KEY_DOWN or getposit == curses.KEY_RIGHT:# Down/right key 
                                          if position < len(lines):
                                            position += 1
                                          else: position = 1

                                        elif getposit != -1: 
                                          if int(chr(getposit)) > 0 and int(chr(getposit)) <= len(lines):
                                            position = int(chr(getposit))
                                        else: pass
                                      except: pass

                                  else:  
                                    νιdeu1 = νιdeu
                                    lines.pop(numero-1)
                                    with open(νιdeu, 'w',encoding='utf8') as oppel:
                                      oppel.truncate(0)
                                    for i in lines:
                                      with open(νιdeu,'a',encoding='utf8') as oppel:
                                        oppel.write(i)                         


                                    if toreg == ' Imαδ ': νιdeu = 'Imαδ.csv'
                                    if toreg == ' Improl ': νιdeu = 'Vermαt.txt'
                                    if toreg == ' Mυuιtsyα ': νιdeu = 'Mυuιt Vermαt.txt'
                                    if toreg == ' Pιlμα ': νιdeu = 'Verpιlμα.txt'
                                    if toreg == ' Aιleus ': νιdeu = 'Aιleus Vermαt.txt'

                                    item = item.rstrip('\n')

                                    with open(νιdeu,'a',encoding='utf8') as oppel:
                                      oppel.write(item)
                                      oppel.write('\n')
                                    stνlαt('Verse',f'{νmαν} → {toreg} ',7)

                                    prompt = νmαν = sub1 = toreg = αdtoreg = str() ; νqseut = False ; strnum = 0 ; geuδ(νιdeu1) ; return
                                
                                
                                #elif eudαμl == curses.KEY_UP: # or eudαμl == curses.KEY_LEFT:# Up/left key
                                  try:
                                    if tnum > 0: tnum = tnum - 1
                                    else: tnum = 3

                                  except Exception as e: stνlαt(αδqαιt,f'{e}',0)
                                  
                                #elif eudαμl == curses.KEY_DOWN: # or eudαμl == curses.KEY_RIGHT:# Down/right key
                                  try:
                                    if tnum < 3: tnum = tnum + 1
                                    else: tnum = 0

                                  except Exception as e: stνlαt(αδqαιt,f'{e}',0)
                                
                                elif eudαμl == curses.KEY_UP or eudαμl == curses.KEY_LEFT:# Up/left key
                                  if tnum == 0: tnum = 4
                                  else: tnum = tnum - 1
                                elif eudαμl == curses.KEY_DOWN or eudαμl == curses.KEY_RIGHT:# Down/right key 
                                  if tnum == 4: tnum = 0
                                  else: tnum = tnum + 1

                                elif eudαμl != -1:

                                  if int(chr(eudαμl)) <= 5: tnum = int(chr(eudαμl)) - 1
                                  else: pass

                                else: pass
                                                      
                              except IndexError: pass
                              except Exception as e: stνlαt('Verse   ',f'{e}',7) ; toreg = ''

                        elif νsnum == 0o10 or νsnum == ord('º'): prompt = ':' ; item = ''                          


                        elif νsnum == ord('ƻ'):#   Ctrl Left key         item to νerseut | 
                          νerseut = item[:-1]

                        elif νsnum == ord('Ƽ'):#  Ctrl Right key        item to νerseut2 | 
                          νerseut2 = item[:-1]


                        elif νsnum == curses.KEY_UP or νsnum == curses.KEY_LEFT:# Up/left key 
                          selector('αdινeu')
                          
                        elif νsnum == curses.KEY_DOWN or νsnum == curses.KEY_RIGHT:# Down/right key 
                          selector('δινeu')

                        # Num Pad
                        elif νsnum == ord('Ǉ'):# Num(1) 
                          item = lines[0] ; strnum = numero = 1
                        elif νsnum == ord('ǈ'):# Num(2) 
                          item = lines[1] ; strnum = numero = 2
                        elif νsnum == ord('ǉ'):# Num(3) 
                          item = lines[2] ; strnum = numero = 3
                        elif νsnum == ord('Ǆ'):# Num(4) 
                          item = lines[3] ; strnum = numero = 4
                        elif νsnum == ord('ǅ'):# Num(5) 
                          item = lines[4] ; strnum = numero = 5
                        elif νsnum == ord('ǆ'):# Num(6) 
                          item = lines[5] ; strnum = numero = 6
                        elif νsnum == ord('ǁ'):# Num(7) 
                          item = lines[6] ; strnum = numero = 7
                        elif νsnum == ord('ǂ'):# Num(8) 
                          item = lines[7] ; strnum = numero = 8
                        elif νsnum == ord('ǃ'):# Num(9) 
                          item = lines[8] ; strnum = numero = 9
                        elif νsnum == ord('Ǻ'):# Num(0) 
                          item = lines[9] ; strnum = numero = 10

                        elif νsnum != -1: 
                            try:                                       
                              νsnum = chr(νsnum)
                              numero = int(νsnum)
                              if numero == 0: numero = 10
                              strnum = str(numero)
                            except ValueError: pass                            
                            except IndexError: toreg = ''

                        if numero != 0:
                          item = lines[numero-1]
                          stdscr.addstr('\n')
                          if len(lines) <= 9: prompt = f'{strnum} │  {lines[numero-1]}'
                          else:                      
                            if int(strnum) > 9: prompt = f'{strnum} │  {item}'
                            else: prompt = f'{strnum}  │  {item}'
                          strnum = int(strnum)

                      except Exception as e: stνlαt('Verse',f'{e}',7) ; toreg = ''
                  νerse()
                elif νermαt == ord('-') or νermαt == ord('ǐ'): # Num(-)                        Iuαq │ 
                  prompt = '' ; ιdeu= 'Vermαt' ; νmαν = toreg = numero = item = str()

                  oppel = open(νιdeu,encoding='utf8')
                  lines = oppel.readlines()

                  while True:
                    mαιteu(0,ιdeu)
                    lαmνmαt()
                    stdscr.addstr(0,7,' │ ',curses.color_pair(2))
                    stdscr.addstr('Iuαq')
                    stdscr.addstr(' │',curses.color_pair(2))

                    number = stdscr.getch()   

                    if number == 27: prompt = '' ; νmαν = '' ; toreg = '' ; strnum = 0 ; break

                    elif number == 10 or number == ord('ǋ'): 
                      import os
                      try:
                        ιuαqseut = lines[numero-1]
                        if numero <= len(lines):
                          del lines[numero-1]
                          with open(νιdeu,'w',encoding='utf8') as oppel:
                            oppel.truncate(0)
                          if len(lines) > 0: 
                            for i in lines:
                              with open(νιdeu,'a',encoding='utf8') as oppel:
                                oppel.write(i)
                          else: os.system(f'del "{νιdeu}"')
                        

                        stνlαt('Iuαq  ',f'{str(ιuαqseut)}',7) ; prompt = '' ; νmαν = '' ; toreg = '' ; strnum = 0 ; geuδ(νιdeu) ; break 
                            
                      except Exception as e: stνlαt('Iuαq  ',f'{e}',7) ; prompt = '' ; νmαν = '' ; toreg = ''
                      except: numero = 0 ; pass
                        
                    elif number == ord('ƻ'):#   Ctrl Left key         item to νerseut | 
                      νerseut = item[:-1]

                    elif number == ord('Ƽ'):#  Ctrl Right key        item to νerseut2 | 
                      νerseut2 = item[:-1]

                    elif number == curses.KEY_UP or number == curses.KEY_LEFT:# Up/Left key 
                      selector('αdινeu') 
                      
                    elif number == curses.KEY_DOWN or number == curses.KEY_RIGHT:# Down/Right key 
                      selector('δινeu') 

                    # Num Pad
                    elif number == ord('Ǉ'):# Num(1) 
                      strnum = numero = 1
                    elif number == ord('ǈ'):# Num(2) 
                      strnum = numero = 2
                    elif number == ord('ǉ'):# Num(3) 
                      strnum = numero = 3                 
                    elif number == ord('Ǆ'):# Num(4) 
                      strnum = numero = 4
                    elif number == ord('ǅ'):# Num(5) 
                      strnum = numero = 5
                    elif number == ord('ǆ'):# Num(6) 
                      strnum = numero = 6
                    elif number == ord('ǁ'):# Num(7) 
                      strnum = numero = 7
                    elif number == ord('ǂ'):# Num(8) 
                      strnum = numero = 8
                    elif number == ord('ǃ'):# Num(9) 
                      strnum = numero = 9
                    elif number == ord('Ǻ'):# Num(0) 
                      strnum = numero = 10

                    elif number != -1: 
                      try:
                        number = chr(number)
                        if number == 'Ǻ': numero = 0
                        else: numero = int(number)
                        if numero == 0: numero = 10

                        oppel = open(νιdeu,encoding='utf8')
                        lines = oppel.readlines()
      
                          
                      except ValueError: pass
                        
                      except IndexError: toreg = ''

                    if numero != '': 
                      if numero > len(lines): numero = 1
                      item = lines[numero-1]
                      strnum = str(numero)

                      
                      if len(lines) < 10: prompt = f'{strnum} │  {item}'
                      else:                      
                        if int(strnum) > 9: prompt = f'{strnum} │  {item}'
                        else: prompt = f' {strnum} │  {item}'
                      strnum = int(strnum)
                
                # Nav
                elif νermαt == curses.KEY_LEFT:#                                         Left Toreg │ 
                  tselect -= 1 ; checkνιdeu()
                elif νermαt == curses.KEY_RIGHT:#                                       Right Toreg │ 
                  tselect += 1 ; checkνιdeu()

                elif νermαt == ord('1') or νermαt == ord('Ǉ')  or νermαt == ord('º'):#         Imαδ │ 
                  prompt = νmαν = toreg = read = sub1 = str()
                  tselect = 0 #; geuδ('Imαδ.csv') ; checkνιdeu() # stνlαt('Vermαt  ','· Imαδ',0)
                elif νermαt == ord('2') or νermαt == ord('ǈ'):#                              Improl │ 
                  tselect = 1 #; geuδ('Vermαt.txt') ; checkνιdeu() # stνlαt('Vermαt  ','→ Improl',0)
                elif νermαt == ord('3') or νermαt == ord('ǉ'):#                            Mυuιtsyα │ 
                  tselect = 2 #; geuδ('Mυuιt Vermαt.txt') ; checkνιdeu() # stνlαt('Vermαt  ','→ Mυuιtsyα',0)
                elif νermαt == ord('4') or νermαt == ord('Ǆ'):#                               Pιlμα │ 
                  tselect = 3 #; geuδ('Verpιlμα.txt') ; checkνιdeu() # stνlαt('Vermαt  ','→ Pιlμα',0)
                elif νermαt == ord('5') or νermαt == ord('ǅ'):#                              Aιleus │ 
                  tselect = 4 #; geuδ('Aιleus Vermαt.txt') ; checkνιdeu()
                elif νermαt == ord('6') or νermαt == ord('ǆ'):#                              Lestαq │ 
                  tselect = 5 #; geuδ('Lestαq.txt') ; checkνιdeu()
                elif νermαt == ord('7') or νermαt == ord('ǁ'):#                            Lestαq 3 │ 
                  tselect = 6 #; 
                elif νermαt == ord('8') or νermαt == ord('ǂ'):#                    Lιuemαg Dyανorδα │ 
                  tselect = 7 ; geuδ('Lιuem Vermαt.txt') ; checkνιdeu()  
                # Tαuderαm
                elif νermαt == ord('t') or νermαt == ord('T'):#                              Tαuder │ 
                  Tαuder('Tαuder','│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ │ Aιleus │ Lαg │'+' '*tαuspace+f'\u276f {date}')
                elif νermαt == ord('d') or νermαt == ord('D'):#                       Dyαteν Tαuder │ 
                  Tαuder('Dyαteν','| Lαg |')
                elif νermαt == ord('m') or νermαt == ord('M'):#                     Mυuιtsyα Tαuder │ 
                  Tαuder('Mυuιtsyα Tαuder','| Lαg |')
                elif νermαt == ord('a') or νermαt == ord('A'):#                       Aιleus Tαuder │ 
                  Tαuder('Aιleus','| Lαg |')

                elif νermαt == ord('y') or νermαt == ord('Y'):#                           Dyeναstαq │ 
                  stνlαt('Vermαt  ','→ Dyeναstαq',0) 
                  import webbrowser as wb
                  wb.open('https://calendar.google.com/calendar/') 
                elif νermαt == ord('q') or νermαt == ord('Q'): #                             Qαmpαr │ 
                  stνlαt('Vermαt  ','Qαmpαr',0)
                  import webbrowser
                  webbrowser.open('https://www.google.com/maps')
                elif νermαt == ord('0'): #                                                      Lαg │ 
                  import os ; os.system(f'"{νιdeu}"')

                elif νermαt == curses.KEY_F10:#           F10                          Lιuem Qαmpαr │                                       
                  qαmpαr()
                elif νermαt == curses.KEY_F12:#  F12                                         Stνlαt │ 
                  curses.endwin() ; stνlαt('Stνlαt  ','','stνlαt') ; curses.curs_set(False) ; stνlαt(αδqαιt,f'<VERMAT>',0)
                      
                νermαt = stdscr.getch() 

                curses.curs_set(False)
                stdscr.refresh()
                time.sleep(0.01)

            except Exception as e: stνlαt('Vermαt  ',f'{e}',0)
          """def Vermαtcsv():                                                                                 
            global vlx, vlαιu, νerseut
            νsfix = 75
            if int(ιsteg) > 9: νsfix = νsfix + 1
            if int(moueg) > 9: νsfix = νsfix + 1
            νspace = x-νsfix

            try: 
              stνlαt(αδqαιt,'<VERMAT>',0)
              stνlαt('Vermαt  ','· Aδqαιt',0)
              νermαt = νmαν = αdνmαν = toreg = prompt = sub1 = sub2 = sub3 = sub4 = sub5 = str()
              vlx = 0 ; vlαιu = ' Imαδ '; νιdeu = 'Imαδ.csv' ; νqseut = False

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
              #geuδ(νιdeu)

              def lαmνmαt():


                mαιteu(0,'Vermαt')
                #if int(ιsteg) > 9:
                stdscr.addstr(2,0,' Imαδ  │ Improl | Mυuιtsyα │ Pιlμα │ Lestαq │ Lestαq 3 │ Tαuderα │'+' '*νspace+f'\u276f {date}')
                if vlαιu == ' Imαδ ': 
                  stdscr.addstr(2,vlx,vlαιu,curses.color_pair(2))
                else: 
                  stdscr.addstr(2,vlx,vlαιu,curses.color_pair(5))
                stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(1))
                stdscr.addstr('\n')
                try:
                  import pandas as pd
                  import numpy as np
                  import csv
                  datos = pd.read_csv('Imαδ.csv',encoding='utf8',sep='\t+',header=None)
                  data = pd.DataFrame(datos)
                  data = data.style.set_properties(**{'text-align': 'left'})
                  read = data.to_string()
                  stdscr.addstr(read)           

                except Exception as e: stνlαt('Vermαt  ',f'{e}',0)

                if νermαt == '': 
                  stdscr.addstr(prompt)
                  stdscr.addstr(νmαν)
                  stdscr.addstr('\n')
                  stdscr.addstr('\u2500'*x,curses.color_pair(1))
                elif  νermαt == ord('.'):
                  if read.count('\n') > 9: stdscr.addstr(f'→  |  ')
                  else: stdscr.addstr(f'→ |  ')

                  stdscr.addstr(νmαν)
                  stdscr.addstr('.',curses.color_pair(2))
                  stdscr.addstr(αdνmαν) 
                  stdscr.addstr('\n')
                  stdscr.addstr('\n')
                  stdscr.addstr('\u2500'*x,curses.color_pair(1))

                else:
                  stdscr.addstr('\n')
                  stdscr.addstr('\u2500'*x,curses.color_pair(1))
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

              while 1:
                lαmνmαt()

                if νermαt == 27: stdscr.clear() ; νιdeu = 'Imαδ.csv' ; return

                elif νermαt == ord('º') or νermαt == ord('1'):
                  stνlαt('Vermαt  ','· Imαδ',0)
                  prompt = νmαν = toreg = read = sub1 = str()
                  vlx = 0 ; vlαιu = ' Imαδ ' ; νιdeu = 'Imαδ.csv' ; geuδ('Imαδ.csv')

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

                      if sιguα == 27: νmαν = prompt = str() ;   break

                      elif sιguα == ord('º'): νmαν = toreg = prompt = str() ; break

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
                      elif sιguα == ord('Ą'):#        Left key | 
                        αdνmαν = νmαν[-1] + αdνmαν ; νmαν = νmαν[:-1]
                      elif sιguα == ord('ą'):#       Right key | 
                        try: νmαν += αdνmαν[0] ; αdνmαν = αdνmαν[1:]
                        except Exception: pass
                      elif sιguα == ord('Ŋ'):#            Supr | 
                        αdνmαν = αdνmαν[1:]
                      elif sιguα == ord('\t'):#            Tab | 
                        νmαν += '\t❯  '
                      elif sιguα == ord('ş'):#       Shift Tab | 
                        νmαν += '\t→  '
                      elif sιguα == ord('ƀ'): νmαν += '\t'
                      elif sιguα == ord('+'): νerseut = νmαν
                      elif sιguα == ord('*'): νerseut = αdνmαν
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
                    prompt = ': ' ; ιdeu= 'Vermαt' ; item = str()

                    while True:
                      try:
                        lαmνmαt()
                        stdscr.addstr(0,7,' │ ',curses.color_pair(2))
                        stdscr.addstr('Verqom')
                        stdscr.addstr(' │',curses.color_pair(2))

                        νqnum = stdscr.getch()   

                        if νqnum == 27: prompt = νmαν = toreg = '' ; break

                        elif νqnum == 10: 
                          if item == '': pass
                          else:
                            #toreg = νerseut
                            nonlocal νqseut
                            νqseut = True
                            while 1:
                              try:
                                if len(lines) < 10: sub1 = f'{strnum} ❯  '
                                else: sub1 = f'{strnum}  ❯  '
                              
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
                                elif eudαμl == ord('\t'): toreg += '\t❯  '
                                elif eudαμl == ord('ş'): toreg += '\t→  '
                                elif eudαμl == ord('ƀ'): toreg += '\t'

                                elif eudαμl == ord('ç') or eudαμl == ord('Ç'): toreg += νerseut

                                elif eudαμl != -1: toreg += chr(eudαμl)
                                else: pass
                                                      
                              except IndexError: pass
                              except Exception as e: stνlαt('Verqom ',f'{e}',7) ; toreg = ''

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
                              if len(lines) < 10: prompt = f'{strnum} │  {lines[numero-1]}'
                              else: prompt = f'{strnum}  │  {item}'
                              stνlαt('Verqom',f'{item}',7)

                      
                            except ValueError: pass
                              
                            except IndexError: toreg = ''

                          else: pass
                      
                      except Exception as e: stνlαt('Verqom',f'{e}',7) ; toreg = ''
                  νerqom()

                elif νermαt == ord('-'): # Iuαq 
                  prompt = ': ' ; νmαν = toreg = numero = item = str() ; ιdeu= 'Vermαt'

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
                        if len(lines) < 10: prompt = f'{strnum} │  {item}'
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
                  prompt = ': ' ; νmαν = toreg = numero = str() ; ιdeu = 'Vermαt'

                  while True:
                    mαιteu(0,ιdeu)
                    lαmνmαt()
                    stdscr.addstr(0,7,' │ ',curses.color_pair(2))
                    stdscr.addstr('Copy')
                    stdscr.addstr(' │',curses.color_pair(2))

                    number = stdscr.getch()   

                    if number == 27: prompt = νmαν = toreg = str() ; break

                    elif number == 10: 
                      νerseut = item[:-1]
                      stνlαt('Tαg   ',f'{str(νerseut)}',7) ; prompt =  νmαν = toreg = str() ; geuδ(νιdeu) ; break 
                            
                    elif number == ord('º'): prompt = ': ' ; νmαν = toreg = str()                           
                            
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

                      stdscr.addstr(2,0,' Imαδ  │ Improl | Mυuιtsyα │ Pιlμα │ Aιleus │ Lestαq │ Lestαq 3 │')
                      stdscr.addstr(2,vlx,vlαιu,curses.color_pair(5))
                      stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(2))

                      with open('Lestαq 3.txt','r',encoding='utf8') as oppel: estαq = str(oppel.read())
                      pad = curses.newpad(300,158)
                      pad.addstr(estαq)
                      pad.refresh(0,0,4,0,30,x-1)

                      import pandas as pd
                      checkmarks_df = pd.read_csv('Checkmarks.csv')
                      checkmarks = str(checkmarks_df)

                      pad = curses.newpad(900,900)
                      pad.addstr(checkmarks)
                      pad.refresh(0,0,32,5,41,65)

                      estαqer = stdscr.getch()

                      if estαqer == 27 or estαqer == 10: vlx = 0 ; vlαιu = '' ; νιdeu = 'Vermαt.txt' ; return 
                      elif estαqer == ord('º') or estαqer == ord('1'): νιdeu = 'Imαδ.csv' ; geuδ('Imαδ.csv') ; stνlαt('Vermαt  ','· Imαδ',0) ; vlx = 0 ; vlαιu = ' Imαδ ' ; break
                      elif estαqer == ord('2'): νιdeu = 'Vermαt.txt' ; geuδ('Vermαt.txt') ; vlx = 8 ; vlαιu = ' Improl ' ; break
                      elif estαqer == ord('3'): νιdeu = 'Mυuιt Vermαt.txt' ; geuδ('Mυuιt Vermαt.txt') ; vlx = 17 ; vlαιu = ' Mυuιtsyα ' ; break
                      elif estαqer == ord('4'): νιdeu = 'Verpιlμα.txt' ; geuδ('Verpιlμα.txt') ; vlx = 28 ; vlαιu = ' Pιlμα ' ; break
                      elif estαqer == ord('5'): νιdeu = 'Lestαq.txt' ; geuδ('Lestαq.txt') ; vlx = 36 ; vlαιu = ' Lestαq ' ; break
                      elif estαqer == ord('t') or νermαt == ord('T'): Tαuder('Tαuder','│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ │ Lαg │')
                      elif estαqer == ord('d') or νermαt == ord('D'): Tαuder('Dyαteν','| Lαg |')
                      elif estαqer == ord('m') or νermαt == ord('M'): Tαuder('Mυuιtsyα Tαuder','| Lαg |')
                      #elif estαqer == ord('0'): os.system('"Estαq 3.txt"')
                      else: pass
                  except Exception as e: stνlαt('Vermαt  ',f'{e}',0)

                elif νermαt == ord('t') or νermαt == ord('T'): Tαuder('Tαuder','│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ │ Lαg │'+' '*tαuspace+f'\u276f {date}')

                elif νermαt == ord('d') or νermαt == ord('D'): Tαuder('Dyαteν','| Lαg |')

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

            except Exception as e: stνlαt('Vermαt  ',f'{e}',0)"""
          def Tαuder(txtlαιu,lprαν):                                                                          
            stdscr.clear()
            try: open(f'{txtlαιu}.txt', 'r', encoding='utf8')
            except Exception as e: stνlαt('Tαuder  ',f'{e}',0)

            if txtlαιu != 'Tαuder': stνlαt('Tαuder  ',f'❯ {txtlαιu}',0)
            tαg(1,txtlαιu,1,txtlαιu,ι='T',prαν=f'{lprαν}\n',log='\u2500'*x,υprαν='',ιzprαν='',command='Tαuder') ; stdscr.clear()
          def Dyαtēν():                                                                                       
            stνlαt(αδqαιt,'<DYATEV>',0)
            try:
              stdscr.clear()
              sub1 = sub2 = sub3 = sub4 = sub5 = str()

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
                      line = sub1 = sub2 = sub3 = str()

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
                              oppel.write('\n')
                              oppel.write(line)
                              oppel.write(' │ ')
                              oppel.close()
                            
                            with open('Dyαteν.txt','a',encoding='utf8') as oppel:
                              oppel.write('\n')
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
        
                            with open('Dyαteν.txt','a',encoding='utf8') as oppel:
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
                            
                            with open('Dyαteν.txt','a',encoding='utf8') as oppel:
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
                            
                            with open('Dyαteν.txt','a',encoding='utf8') as oppel:
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
                            
                            with open('Dyαteν.txt','a',encoding='utf8') as oppel:
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

                            with open('Dyαteν.txt','a',encoding='utf8') as oppel:
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
                                  
                                  with open('Dyαteν.txt','a',encoding='utf8') as oppel:
                                    oppel.write(line)
                                    oppel.write(' │ ')
                                    oppel.write('\n')
                                    oppel.write('\n')
                                    oppel.write('\n')

                                  stνlαt('Dyαteν  ',f'→ Sιguα',0) ; stdscr.clear()

                                  sub1='' ; sub2='' ; sub3='' ; line='' ; break

                                else:
                                  sub1='' ; sub2='' ; sub3='' ; line=''
                                  with open('Dyαteν.txt','a',encoding='utf8') as oppel:
                                    oppel.write('\n')                          
                                    oppel.write('\n')                          
                                    oppel.write('\n')                          
                                  break
                                      
                              elif sιguα == 0o10: line = line[:-1]

                              elif sιguα != -1: line += chr(sιguα) 

                            break

                          else:
                            sub1='' ; sub2='' ; sub3='' ; line=''
                            with open('Dyαteν.txt','a',encoding='utf8') as oppel:
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

                elif dyαt == ord('1') or dyαt == ord('t') or dyαt == ord('T'): Tαuder('Dyαteν','| Lαg |')
                  
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

                elif dyαt == curses.KEY_F10:#           F10                Lιuem Qαmpαr |                                       
                  qαmpαr()
                elif dyαt == curses.KEY_F12:#  F12          Stνlαt 
                  curses.endwin() ; stνlαt('Stνlαt  ','','stνlαt') ; curses.curs_set(False) ; stνlαt(αδqαιt,f'<DYATEV>',0)
                else: pass
              stdscr.refresh()
              time.sleep(0.01)
            except Exception as e: stνlαt('Dyαteν  ',f'{e}',0) ; return
          def Augestαq():                                                                                     
            stνlαt(αδqαιt,'<ANGESTAQ>',0) 
            try:
              stdscr.clear()
              menu='│ Iuslag │ Isqyαu │ Mαuslαg │'
              sub1 = sub2 = numero = str()

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

                elif αugest == ord('º'): sub1 = sub2 = str()

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

                                sub1 = 'Soleu  │ ' ; sub2 = ''

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

                elif αugest == curses.KEY_F10:#           F10                Lιuem Qαmpαr |                                       
                  qαmpαr()
                elif αugest == curses.KEY_F12:#  F12          Stνlαt 
                  curses.endwin() ; stνlαt('Stνlαt  ','','stνlαt') ; curses.curs_set(False) ; stνlαt(αδqαιt,f'<ANGESTAQ>',0)
               
                stdscr.refresh()
                time.sleep(0.01)
            
            except Exception as e: stνlαt('Augestαq',f'→ {e}',0) ; pass
          def Mυuιtsyα():                                                                                     
            stνlαt(αδqαιt,'<MUNITSYA>',0)
            stdscr.clear() ; sub2='' ; sub3=''

            def lαmυuιt(z,section,sub1):
              try: 
                mαιteu(1,'MUNITSYA')
                stdscr.addstr(2,0,'│ Iνouιm │ Tαuder │ Terιguer │ Vermαt │ Teνuα │')
                stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(2))
                try: 
                
                  import pandas as pd
                  import numpy as np
                  import csv
                  datos = pd.read_csv('Mυuιmα Stαgeu.csv',encoding='utf8',sep='\t')
                  data = pd.DataFrame(datos)
                  data = data.fillna(' ')
                  tαuder = data.to_string(index=False)
            
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

              elif mυuιt == ord('Ǒ'):# Num(+) Sιguα 
                  lαιue = αuemαt = sιeνιt = toreg = str()

                  sub3 = f'{lαιue}  {αuemαt}  {sιeνιt}  {toreg}'

                  while 1: # Lαιu
                    lαmυuιt(1,' Sιguα ','Lαιu   │ ')
                    mυusιg = stdscr.getch()

                    if mυusιg == 27: break
                    elif mυusιg == ord('º'): sub2=''
                    elif mυusιg == ord('t') or mυusιg == ord('T'): import os ; os.system('Mυuιtsyα.txt')
                    elif mυusιg == 10: lαιue = sub2 ; sub3 = f'> {lαιue}' ; sub2='' ; break
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
                import os ; os.system(r"C:\Users\Leane\OneDrive\Escritorio\Logreuα\Μυuιt\Player\Mpxplay_v167_Win32_FFmpeg\mpxplayf.exe") ; stνlαt('Mυuιtsyα','❯ Iνouιm',0) ; curses.curs_set(False)

              elif mυuιt == ord('2') or mυuιt == ord('t'):#  Mυuιtsyα Tαuder 
                Tαuder('Mυuιtsyα Tαuder','| Lαg |')

              elif mυuιt == ord('3'):# Terιguer
                import subprocess
                subprocess.Popen(r'"C:\ProgramData\Ableton\Live 10 Suite\Program\Ableton Live 10 Suite.exe"')

              elif mυuιt == curses.KEY_F10:#           F10                Lιuem Qαmpαr |                                       
                qαmpαr()
              elif mυuιt == curses.KEY_F12:#  F12          Stνlαt 
                curses.endwin() ; stνlαt('Stνlαt  ','','stνlαt') ; curses.curs_set(False) ; stνlαt(αδqαιt,f'<MUNITSYA>',0)

              
              else: pass

              stdscr.refresh()
              time.sleep(0.01)
          stνlαt(αδqαιt,'[green]ιutαgeu[/green]','Lōgreuαm    ')
        except Exception as e: stνlαt(αδqαιt,f'[red]{e}[/red]','Lōgreuαm    ')
            
    # Zona Operativa 

      # Operaciones de inicio 
        try: #                                                                    Imαδ ιuνorαt lιgeu          
          os.chdir(r'G:\Mi unidad\Lιuem Stαuνor')
        except Exception as e: stνlαt(αδqαιt,f'[red]{e}[/red]',0)
        stνlαt(αδqαιt,os.getcwd(),1) #                                            Stνlαt uostαl ιutorαg      

        while 1:#                                                                 User Operations            
          try: 
          # Sιuter Iδᾱt 
            stdscr.nodelay(True)
            curses.curs_set(False)
            if len(f'{ιmαν}{uostιmαν}{αdιmαν}') < 1: lαδuιmαν = str()
            else: 
              if uostιmαν != str(): lαδuιmαν = uostιmαν
              else: lαδuιmαν = ' '
            lestαq(0,S.ιdeu,S.prαν,S.log,S.υprαν,S.ιzprαν)
            νerseuter()
            # tαg(1,0,S.clear,S.ιdeu,S,S.prαν,S.log,S.υprαν,S.ιzprαν,'Aδqαιt')

          # MASENTA 
            key = stdscr.getch(2,2) 

          # Verseuα 
            if key == 27 or key == ord('Ȗ'):#     Shift Num(-)                 Esc |                                       
              ιmαν = uostιmαν = αdιmαν = str() ; S = Lαmseut(0,'Stαuνor','','','','') ; nlog = 0
            elif key == 10 or key == ord('ǋ'):#                              Enter |                                       
              ιmαν += uostιmαν + αdιmαν
              S = Lαmseut(0,'Stαuνor','','','','')
              
              # Tαuder

              if ιmαν == '.eud':#         System Process List 
                S.ιdeu = 'Eudyαteνα'
                eudprαν = str()
                process_count = 1

                def eudyαt():
                  global processlist
                  nonlocal eudprαν, process_count
                  eudprαν = str()
                  ilist = []
                  processnum = -1

                  process = os.popen('wmic process get description')
                  
                  for i in process:
                    if i != '\n':
                      ilist.append(i)

                  processlist = ilist[process_count:]

                  for i in processlist: 
                    processnum = processnum + 1 
                    if processnum == 0: pass
                    elif processnum < 10: eudprαν += f'{processnum}  │ {i}'
                    elif processnum >= 10 and processnum < 88: eudprαν += f'{processnum} │ {i}'
                    elif processnum >= 88 and processnum < 100: eudprαν += f'{processnum}  │ {i}'
                    else: eudprαν += f'{processnum} │ {i}'
                  return

                while 1:
                  eudyαt()
                  mαιteu(1,'Eudyαteνα')
                  stdscr.addstr(2,0,'\u276f')
                  stdscr.clrtoeol()
                  stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(2))

                  pad1 = curses.newpad(500,100)
                  pad1.addstr(eudprαν)
                  pad1.refresh(0,0,4,0,43,40)
                  pad2 = curses.newpad(500,100)
                  pad2.addstr(eudprαν)
                  pad2.refresh(43,0,4,41,43,80)
                  pad3 = curses.newpad(500,100)
                  pad3.addstr(eudprαν)
                  pad3.refresh(87,0,4,81,43,120)
                  pad4 = curses.newpad(500,100)
                  pad4.addstr(eudprαν)
                  pad4.refresh(130,0,4,121,43,150)

                  eudιmαν = stdscr.getch()
                  
                  if eudιmαν == 10 or eudιmαν == 27: S.ιdeu = 'Stαuνor' ; break
                  elif eudιmαν == ord('\t'):
                    process_count = process_count + 170
                    if process_count > len(processlist): process_count = 1
                  else: pass

              if ιmαν == '.invash':#         Qαιteu ιutorαg νerseut 
                S.log = 'Iuναδ ιutorαg | ' ; S.υprαν = r'G:\Mi unidad\Lιuem Stαuνor'

              elif ιmαν == '.mativ':#        Nostαl ιsteg tαuder 
                S.prαν = f'Mαtιν \u276f  ' + date2

              elif ιmαν == '.izvartag':#     Izναrtαg tαuderα 
                ιmαν = ''        
                
                while 1:
                  import psutil
                  ιzναrtαg = psutil.sensors_battery()
                  if ιzναrtαg.power_plugged == True: ιzιδαt = 'Tαgeu'
                  else: ιzιδαt = 'Aqtαgeu'
                  lestαq(0,'Izναrtαg','','',f'Sναrt   | {ιzναrtαg.percent}',f'Iuμαuze | {ιzιδαt}')
                  
                  ιzνmαν = stdscr.getch()
                  if ιzνmαν == 27 or ιzνmαν == 10: break
                  else: pass

              elif ιmαν == '.net':#          WiFi Connection 
                import psutil
                stats = psutil.net_if_stats()
                
                for interface, stat in stats.items():
                  if interface == 'Wi-Fi':
                    if stat.isup: S.υprαν = f"{interface} ιuμeuzeu"
                    else: S.υprαν = f"{interface} ιuμeuzαqeu"              
                  else: pass
              
              elif ιmαν == '.lanter':#       Lαuter Tαuderα 
                from screeninfo import get_monitors
                for m in get_monitors(): S.υprαν = f"Lαuter: {m.name}\nWidth: {m.width} ({str(x)})\nHeight: {m.height} ({str(y)})\n"

              elif ιmαν == '.locals':#       Locals 
                curses.endwin() ; lαmlιuem(0,1,'Locαls')
                print(locals()) ; input() ; lαmlιuem(0,1,'Stαuνor')

              elif ιmαν == 'chr':#           Char input 
                ιmαν = str()
                
                while 1:
                  lestαq(0,'Chr',S.prαν,'❯ ',S.υprαν,S.ιzprαν)

                  tαgchr = stdscr.getch()

                  if tαgchr == 27: break
                  elif tαgchr == 0o10: lαδuιmαν = '0o10'
                  elif tαgchr == ord('\t'): lαδuιmαν = r'\t'
                  elif tαgchr == 10: lαδuιmαν = '10'
                  elif tαgchr != -1: lαδuιmαν = chr(tαgchr)

              # Aιleus

              elif ιmαν == '.tag':#          Python Module ιtαg 
                stdscr.clear() ; ιmαν = '' ; tαg(1,0,0,'Stαuνor',S,'> ','','','','tαg')
                          
              elif ιmαν == 'dos':#          MS-DOS 
                curses.endwin() ; lαmlιuem(1,1,'MS-DOS') ; os.system('cmd') ; lαmlιuem(0,1,'Stαuνor') ; stνlαt(αδqαιt,f'{os.getcwd()}',1)


              # EXT

              elif ιmαν == 'olyav':#        Explorer 
                import os ; os.system('start . command') ; stνlαt(αδqαιt,'Olyαν',2)
              
              elif ιmαν == 'Saget':#        Edge 
                import subprocess ; subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe --start-maximized") ; stνlαt(αδqαιt,'→ Sαget',0)
                    
              elif ιmαν == 'Dyevast':#      Calendar 
                import webbrowser ; webbrowser.open('https://calendar.google.com/calendar')

              elif ιmαν == 'inslag':#       Visual 
                import subprocess ; subprocess.Popen(r'"C:\Users\Leane\AppData\Local\Programs\Microsoft VS Code\Code.exe"') ; stνlαt(αδqαιt,'→ Iuslαg',0)
              
              elif ιmαν == 'Danqash':#      Drive 
                import webbrowser ; webbrowser.open_new('https://drive.google.com/drive/') ; stνlαt(αδqαιt,'→ Dαuqαδ',0)
              
              elif ιmαν == 'Stanvor':#      Notion 
                import webbrowser ; webbrowser.open_new('https://www.notion.so/St-u-or-f690a8f6cd2344d1802fbdc826ea71cd') ; stνlαt(αδqαιt,'→ Stαuνor',0)
                                    
              elif ιmαν == 'Livsent':#      Lινseut 
                import os ; os.system(r'"C:\Games\Cities - Skylines\Cities.exe"') ; stνlαt(αδqαιt,'→ Lινseu',0)

              elif ιmαν == 'Logat':#        Logαtαm 
                stνlαt(αδqαιt,'→ Logαt',0) ; ιmαν = ''
                tαg(1,0,0,'Logαt','','| X | R | K ❯ ','','','','Logαt')

              elif ιmαν == 'arlinem':#      Lιuem Arνolυm 
                os.system('Lιuem1.py') ; stνlαt(αδqαιt,'→ Lιuem 1',0)

              elif ιmαν == 'prontel':#      Nαδα Stαuνor 
                os.system(r'"C:\Users\Leane\OneDrive\Escritorio\Logreuα\Geuqα\Nαδα\golly-4.3-win-64bit\golly-4.3-win-64bit\Golly.exe"')
              
              else: 
                if ιmαν != '':
                  try:
                    os.chdir(ιmαν)
                    stνlαt(αδqαιt,f'{os.getcwd()}',1)
                    log()

                  except: 
                    try:
                      from matplotlib import pyplot as plt 
                      from matplotlib import image as mpimg

                      img = mpimg.imread(rf'"{ιmαν}"')

                      # Display the image
                      plt.imshow(img)
                      plt.axis('off')  # Hide axes
                      S.υprαν = plt.show()

                    except Exception as e: os.system(f'"{ιmαν}"') ; stνlαt(αδqαιt,f'{e}',0)
              
              ιmαν = uostιmαν = αdιmαν = '' ; nlog = 0
            elif key == ord('ĕ'):#                Shift F1          Eudαμl Stαuνor |                                       
              import subprocess
              comando= r'C:\Users\Leane\OneDrive\Escritorio\Logreuα\Lιuem\main.py'
              subprocess.Popen(["cmd", "/k", comando]) ; stνlαt(αδqαιt,'Lιuem Stαuνor',2)            
            elif key == ord('ġ'):#                Ctrl F1                  Aqtαgeu | Lιuem αqtαgeu                         
              while 1:
                prαν = 'Sɕνdɒl uɒ Lιuɕm Aϥtɒgɕu ?'
                mαιteu(0,'Stαuνor')
                stdscr.addstr(2,0,prαν)
                mαν = stdscr.getch()

                if mαν == 27: prαν = '' ; break
                elif mαν == 10: exit()
                else: pass
            elif key == ord('ȑ'):#                Ctrl Enter                  Info |                                       
              if S.ιzprαν == '' and ιmαν != '': ιmtαu() ; S.ιzprαν = ιmανtαuder
              else: S.ιzprαν = ''
            elif key == ord('ƀ'):#                <                          Lιgeu | Iutorαg lιgeu                         
              tαg(1,0,S.clear,'Stαuνor',S,'Lιgeu ❯ ','','','','lιgeu') ; S = Lαmseut(0,'Stαuνor','','','','')
            elif key == ord('ǀ'):#                >                          ιutel | Logreuαm ιutel                        
              ιmαν = '' ; tαg(1,0,S.clear,'Stαuνor',S,'Iutel ❯ ','','','','ιutel') ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = ''
            elif key == ord('Ġ'):#                Shift F12                   δoνt | System δoνt                           
              tαg(1,0,1,S.ιdeu,S,'Sɕνdɒl uɒ sιstɕm δoνt ?','','','','δoνt')
            elif key == ord('#'):#                                      Calculator |                                       
              stνlαt('Stαuνor ','<CALC>',0) ; num1 = int ; char = ''
              while 1:
                lestαq(0,'Calculator','❯ ','','','')
                stdscr.addstr('.',curses.color_pair(2))

              
                key = stdscr.getch()

                if key == 27: ιmαν = '' ; break
                elif key == ord('+'):  #    Sιguα
                  num1 = ιmαν ; ιmαν = '' ; tαg(1,0,0,'Calculator','',f'❯ {num1} + ','','','','Calc.sιg')
                elif key == ord('ç'):#    Resta
                  num1 = ιmαν ; ιmαν = '' ; tαg(1,0,0,'Calculator','',f'❯ {num1} - ','','','','Calc.rest')
                elif key == ord('*'):#    Multiplicación
                  num1 = ιmαν ; ιmαν = '' ; tαg(1,0 ,0,'Calculator','',f'❯ {num1} * ','','','','Calc.multi')
                elif key == ord('Ç'):#    División 
                  num1 = ιmαν ; ιmαν = '' ; tαg(1,0,0,'Calculator','',f'❯ {num1} / ','','','','Calc.div')
                elif key == 0o10: ιmαν = ιmαν[:-1]
                elif key != -1:
                  try:
                    num1 = int(chr(key)) ; ιmαν += str(num1)
                  except Exception as e: stνlαt(αδqαιt,f'Calc   │ {e}',0)
      
          # Tαuder 
            elif key == ord('º') or key == ord('Ȕ'):#      Shift-Num(*)        Log | Nostαl ιutorαg oppel lαmδα            
              log()
            elif key == ord("'"):#                                          Nostαl | Nostαl ιutorαg                        
              if S.ιdeu != 'Stαuνor': S.log = '\n❯ ' ; ιmαν = os.getcwd()
              else: S.log = 'Nostαl ιutorαg | ' ; ιmαν = os.getcwd()
            
          # Oppelαm stαgeu 
            elif key == ord('Ǒ'):#                 Num(+)                   Eudαμl | Logreu eudαμl                         
              E = Lαmseut(0,'Eudαμl','1 Oppel\n2 Iutorαg','','','')
              while 1:
                ιmαν = lαδuιmαν = uostιmαν = αdιmαν = str()
                lestαq(0,E.ιdeu,E.prαν,E.υprαν,E.log,E.ιzprαν)

                eudαμl = stdscr.getch()

                if eudαμl == 27 or eudαμl == 10 or eudαμl == ord('ǋ') or eudαμl == ord('ǐ'):# Num(-) 
                  S = Lαmseut(0,'Stαuνor','','','','') ; log() ; break
                elif eudαμl == ord('1') or eudαμl == ord('Ǉ'): # Oppel 
                  tαg(1,0,0,E.ιdeu,E,'Oppel ❯ ','','','','Oppel.eudαμl')
                elif eudαμl == ord('2') or eudαμl == ord('ǈ'): # Iutorαg 
                  tαg(1,0,0,E.ιdeu,E,'Iutorαg ❯ ','','','','Iutor.eudαμl')
            elif key == ord('ǐ'):#                 Num(-)                    Aqeμr | Logreu αqtαg                          
              A = Lαmseut(0,'Aqeμr','1 Oppel\n2 Iutorαg','','','')
              while 1: 
                ιmαν = lαδuιmαν = uostιmαν = αdιmαν = str()
                lestαq(0,A.ιdeu,A.prαν,A.υprαν,A.log,A.ιzprαν)

                try:  

                  αqeμr = stdscr.getch()

                  if αqeμr == 27 or αqeμr == 10  or αqeμr == ord('ǋ') or αqeμr == ord('ǐ'):# Num(-) 
                    S = Lαmseut(0,'Stαuνor','','','','') ; log() ; break

                  elif αqeμr == ord('1') or αqeμr == ord('Ǉ'):
                    tαg(1,0,A.clear,A.ιdeu,A,'Oppel ❯ ',A.log,A.υprαν,A.ιzprαν,'Oppel.αqeμr')

                  elif αqeμr == ord('2') or αqeμr == ord('ǈ'):
                    tαg(1,0,A.clear,A.ιdeu,A,'Iutorαg ❯ ',A.log,A.υprαν,A.ιzprαν,'Iutor.αqeμr') 
                    S = Lαmseut(0,'Stαuνor','','','','')
                  
                except Exception as e: stνlαt(αδqαιt,f'→ Aqtαg   │ {e}',0) ; A.prαν = e      
            elif key == ord('Ǌ'):#                 Num(/)              Verse ιuνor | Oppel ιuνor ιverse                    
              V = Lαmseut(0,'Verse','Logreu ❯ ','','','')
              while 1:          
                lestαq(0,V.ιdeu,V.prαν,V.υprαν,V.log,V.ιzprαν)

                νtαg = stdscr.getch()
                  
                if νtαg == 27 or νtαg == ord('ǐ'): S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = str() ; break

                elif νtαg == 10 or νtαg == ord('ǋ'):# Num(Enter) 
                  if ιmαν == '': S = Lαmseut(0,'Stαuνor','','','','') ; break
                  else:
                    logreu = ιmαν
                    if os.path.exists(logreu):
                      V.ιdeu = f'Verse │ {logreu}' ; tαg(1,0,0,V.ιdeu,V,f'Eudαμl ιutorαg ❯ ',V.υprαν,V.log,V.ιzprαν,'νerse') ; log() ; break
                    else: V.ιdeu = 'Verse │ Logreu αqtαgeu'
              
                elif νtαg == ord('Ǡ'):#                Ctrl Up 
                  ιmαν = νerseut
                elif νtαg == ord('ǡ'):#                Ctrl Down 
                  ιmαν = νerseut2
                elif νtαg == 0o10: ιmαν = ιmαν[:-1]
                elif νtαg != -1: ιmαν += chr(νtαg)
                else: pass
            elif key == ord('Ǐ'):#                 Num(*)                    Lαιue | Lαιue logreuαm                        
              L = Lαmseut(0,'Lαιu','Logreu ❯ ','','','')
              while 1: 
                lestαq(0,L.ιdeu,L.prαν,L.υprαν,L.log,L.ιzprαν)
                
                νtαg = stdscr.getch()

                if νtαg == 27 or νtαg == ord('ǐ'):# Num(-)
                  S = Lαmseut(0,'Stαuνor','','','','') ; log() ; break
                elif νtαg == 10 or νtαg == ord('ǋ'): 
                  αrνol = f'{ιmαν}{uostιmαν}{αdιmαν}'
                  if ιmαν == '': S = Lαmseut(0,'Stαuνor','','','','') ; break
                  else:
                    if os.path.exists(αrνol):
                      L.ιdeu = f'Lαιu │ {αrνol}' ; ιmαν= '' ; tαg(1,0,0,L.ιdeu,L,'Eudαμl ❯ ',L.υprαν,L.log,L.ιzprαν,'Logreu.lαιu')
                    else: stνlαt('Stαuνor ',f'Logreu {αrνol} αqtαgeu',0)
                    ιmαν = '' ; log() ; break
                
              # Copy
                elif νtαg == ord('ƻ'):# Ctrl Left                  Imαν to νerseut | 
                  ιmαν = νerseut  
                elif νtαg == ord('Ƽ'):# Shift Left                Imαν to νerseut2 | 
                  ιmαν = νerseut2  

              # Paste
                elif νtαg == ord('Ǡ'):#     Ctrl Up key              νerseut to ιmαν |  
                      ιmαν += νerseut
                elif νtαg == ord('ǡ'):#     Ctrl Down key           νerseut2 to ιmαν |  
                      ιmαν += νerseut2

                elif νtαg == 0o10: ιmαν = ιmαν[:-1]
                elif νtαg != -1: ιmαν += chr(νtαg)
                else: pass
            
          # Logreuαm 
            elif key == ord('ª'):#                                        Explorer |                                       
              stdscr.clear() ; import os ; os.system('start . command')
            elif key == ord('\t'):#                Tab                       Iuνor |                                       
              stdscr.clear() ; ιuνor() ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = ''
            elif key == ord('ȓ'):#           Shift-Num(/)                    Iuνor |                                       
              stdscr.clear() ; ιuνor() ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = ''

            elif key == curses.KEY_F1:#            F1                       Euναrt |                                       
              stdscr.clear() ; Euναrt() ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = uostιmαν = αdιmαν = str()
            elif key == curses.KEY_F2:#            F2                       Vermαt |                                       
              stdscr.clear() ; Vermαt() ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = uostιmαν = αdιmαν = str()
            elif key == curses.KEY_F3:#            F3                       Tαuder |                                       
              stνlαt(αδqαιt,'<TANDER>',0) ; Tαuder('Tαuder','│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ │ Aιleus │ Auzα │ Lαg │'+' '*tαuspace+f'\u276f {date}') ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = lαδuιmαν = uostιmαν = αdιmαν = str()
            elif key == curses.KEY_F4:#            F4                     Augestαq |                                       
              stdscr.clear() ; Augestαq() ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = uostιmαν = αdιmαν = str()
            elif key == curses.KEY_F5:#            F5                     Mυuιtsyα |                                       
              stdscr.clear() ; Mυuιtsyα()  ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = uostιmαν = αdιmαν = str()
            elif key == curses.KEY_F6:#            F6                       Dyαteν |                                       
              stdscr.clear() ; Dyαtēν() ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = uostιmαν = αdιmαν = str()
            elif key == curses.KEY_F7:#            F7                   Iugersαtel |                                       

              from bs4 import BeautifulSoup
              import requests
              from googlesearch import search
              stνlαt(αδqαιt,'<INGERSATEL>',0)
              stdscr.clear()
                            
              def google():
                import webbrowser
                nonlocal νerseut, νerseut2
                ιmαν = content = αdιmαν = log = ιzprαν = link = str()
                titles = []
                links = []
                metas = []
                ptags = []
                com = '.'

                while 1:
                  try:
                    prαν = '\u276f '
                    mαιteu(0, ιdeu= 'Iugersαtel')

                    stdscr.addstr(2,0,prαν)
                    stdscr.addstr(ιmαν)
                    stdscr.addstr(com,curses.color_pair(2))
                    stdscr.addstr(αdιmαν)
                    stdscr.addstr(3,0,'\u2500'*x,curses.color_pair(2))
                    stdscr.addstr(5,0,log,curses.color_pair(1))
                    stdscr.addstr(ιzprαν)
                    stdscr.addstr('\n')
                    if ιzprαν != str(): stdscr.addstr('\u2500'*x,curses.color_pair(1))
                    if link != '': stdscr.addstr(link)
                    if ιmαν == '.d': webbrowser.open('drive.google.com') ; ιmαν = ''
                    elif ιmαν == '.l': webbrowser.open('www.youtube.com') ; ιmαν = ''
                    elif ιmαν == '.y': webbrowser.open('calendar.google.com') ; ιmαν = '' 
                    elif ιmαν == '.q': webbrowser.open('maps.google.com') ; ιmαν = '' 
                    
                    key = stdscr.getch()

                    if key == 27: stdscr.clear() ; S = Lαmseut(0,'Stαuνor','','','','') ; return

                    elif key == 10:
                        ιmαν = ιmαν + αdιmαν
                        αdιmαν = ''

                        titles.clear() ; links.clear() ; metas.clear() ; ptags.clear()
                        ιzprαν = link = str()

                        try:           
                          nlog = -1 ; linknumber = 1

                          url = f'https://www.google.com/search?q={ιmαν}'

                          headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0)'}
                          
                          for i in search(ιmαν, stop=10, pause=2):
                            response = requests.get(i, headers=headers)

                            soup = BeautifulSoup(response.content, 'html.parser')
                            title = soup.title.string if soup.title else ''
                            
                            #For Meta Description
                            meta_description = soup.find('meta', {'name': 'description'})
                            meta = f"{meta_description.get('content')}" if meta_description else ''
                            
                            # Content
                            for p in soup.find_all('p'):
                              content = ' '.join(p.stripped_strings)


                            if linknumber < 10:   ιzprαν += f"{linknumber}  │ {title}\n"
                            else:                 ιzprαν += f"{linknumber} │ {title}\n"
                            linknumber = linknumber + 1
                            titles.append(title)
                            links.append(i)
                            metas.append(meta)
                            if content == None: ptags.append('')
                            else: ptags.append(content)
                            
                          
                          stνlαt('Iugersαt',f'Prαν \u276f {ιmαν}',0) ; com = '.'

                        except Exception as e: 
                          stνlαt('Iugersαt',f'→ Prαν │ {ιmαν} → {e}',0) ; ιzprαν = f'❯ {str(e)}' ; com = '.' ; break

                    elif key == curses.KEY_F1:# F1   
                      prαν = '> ' ; url = ''

                      while 1:
                        mαιteu(0,ιdeu= 'Iugersαtel')
                        stdscr.addstr(2,0,prαν)
                        stdscr.addstr('\n')
                        stdscr.addstr('\u2500'*x)

                        stdscr.addstr(url)

                        key = stdscr.getch()

                        if key == 27: stdscr.clear() ; ιmαν = '' ; break # S = Lαmseut(0,'Stαuνor','\u2502 Prαν \u2502 Iugersαt \u2502 Ilαseu \u2502','','','')

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
                    elif key == curses.KEY_F10:# F10  
                      qαmpαr()
                    elif key == curses.KEY_F12:# F12                            Youtube | 
                      tαg(1,0,0,'YouTube',Y,'❯ ','','','','YouTube')

                    # Seleccionar website                    
                    elif key == curses.KEY_UP:# Up key                     Links Nav Up | 

                      if nlog <= len(titles)*-1: nlog = -1
                      else: nlog = nlog - 1
                      nlink = nlog
                      if nlog == 9 or nlog == -1:
                        link = f'10 \u2502 {titles[nlog]}\n   └ {links[nlog]}\n\n{metas[nlog]}\n\n{ptags[nlog]}'                     
                      else:
                        if nlog < 0:
                          link = f'{nlog+11}  \u2502 {titles[nlog]}\n   └ {links[nlog]}\n\n{metas[nlog]}\n\n{ptags[nlog]}'
                        else:
                          link = f'{nlog+1}  \u2502 {titles[nlog]}\n   └ {links[nlog]}\n\n{metas[nlog]}\n\n{ptags[nlog]}'
                    elif key == curses.KEY_DOWN:# Down key               Links Nav Down | 
                      if nlog == 9: nlog = 0
                      else: nlog = nlog + 1
                      nlink = nlog                    
                      if nlog == 9 or nlog == -1:
                        link = f'10 \u2502 {titles[nlog]}\n   └ {links[nlog]}\n\n{metas[nlog]}\n\n{ptags[nlog]}'
                      else:
                        if nlog < 0:
                          link = f'{nlog+11}  \u2502 {titles[nlog]}\n   └ {links[nlog]}\n\n{metas[nlog]}\n\n{ptags[nlog]}'
                        else:
                          link = f'{nlog+1}  \u2502 {titles[nlog]}\n   └ {links[nlog]}\n\n{metas[nlog]}\n\n{ptags[nlog]}'
                    elif key == ord('ȑ') or key == ord ('ǋ'):#  Ctrl Enter & Num(Enter) | 
                      if link != '':
                        import webbrowser
                        webbrowser.open(f'{links[nlink]}')
                      else:
                        import webbrowser
                        webbrowser.open(f'{ιmαν}{αdιmαν}')
                    elif key == ord('ǎ'):# Num(.)                           Clear links | 
                      link = ''
                    elif key == ord('\t'): 
                      if ιmαν == 'd': ιmαν = 'drive.google.com'
                      elif ιmαν == 'm': ιmαν = 'maps.google.com'
                      elif ιmαν == 'y': ιmαν = 'youtube.com'
                    
                  # Copy
                    elif key == ord('ƻ'):#   Ctrl Left key              ιmαν to νerseut | 
                      νerseut = ιmαν      
                    elif key == ord('Ƽ'):#   Ctrl Right key           αdιmαν to νerseut |  
                      νerseut = αdιmαν    
                    elif key == ord('Ƈ'):#  Shift Left key             ιmαν to νerseut2 | 
                      νerseut2 = ιmαν    
                    elif key == ord('Ɛ'):# Shift Right key           αdιmαν to νerseut2 | 
                      νerseut2 = αdιmαν    

                  # Paste
                    elif key == ord('Ǡ'):#     Ctrl Up key              νerseut to ιmαν |  
                      ιmαν += νerseut    
                    elif key == ord('ǡ'):#     Ctrl Down key           νerseut2 to ιmαν |  
                      ιmαν += νerseut2                          
                      
                    elif key == ord('Ǉ'):# Num(1) 
                      try: link = f'1  \u2502 {titles[0]}\n   └ {links[0]}\n\n{metas[0]}\n\n{ptags[0]}' ; nlog = nlink = 0
                      except: pass
                    elif key == ord('ǈ'):# Num(2) 
                      try: link = f'2  \u2502 {titles[1]}\n   └ {links[1]}\n\n{metas[1]}\n\n{ptags[1]}' ; nlog = nlink = 1
                      except: pass
                    elif key == ord('ǉ'):# Num(3) 
                      try: link = f'3  \u2502 {titles[2]}\n   └ {links[2]}\n\n{metas[2]}\n\n{ptags[2]}' ; nlog = nlink = 2
                      except: pass
                    elif key == ord('Ǆ'):# Num(4)
                      try: link = f'4  \u2502 {titles[3]}\n   └ {links[3]}\n\n{metas[3]}\n\n{ptags[3]}' ; nlog = nlink = 3
                      except: pass
                    elif key == ord('ǅ'):# Num(5)
                      try: link = f'5  \u2502 {titles[4]}\n   └ {links[4]}\n\n{metas[4]}\n\n{ptags[4]}' ; nlog = nlink = 4
                      except: pass
                    elif key == ord('ǆ'):# Num(6)
                      try: link = f'6  \u2502 {titles[5]}\n   └ {links[5]}\n\n{metas[5]}\n\n{ptags[5]}' ; nlog = nlink = 5
                      except: pass
                    elif key == ord('ǁ'):# Num(7)
                      try: link = f'7  \u2502 {titles[6]}\n   └ {links[6]}\n\n{metas[6]}\n\n{ptags[6]}' ; nlog = nlink = 6
                      except: pass
                    elif key == ord('ǂ'):# Num(8)
                      try: link = f'8  \u2502 {titles[7]}\n   └ {links[7]}\n\n{metas[7]}\n\n{ptags[7]}' ; nlog = nlink = 7
                      except: pass
                    elif key == ord('ǃ'):# Num(9)
                      try: link = f'9  \u2502 {titles[8]}\n   └ {links[8]}\n\n{metas[8]}\n\n{ptags[8]}' ; nlog = nlink = 8
                      except: pass
                    elif key == ord('Ǻ'):# Num(0)
                      try: link = f'10 \u2502 {titles[9]}\n   └ {links[9]}\n\n{metas[9]}\n\n{ptags[9]}' ; nlog = nlink = 9
                      except: pass

                    # Imαν Nav
                    elif key == curses.KEY_LEFT:#                              Left key | 
                      try: αdιmαν = ιmαν[-1] + αdιmαν ; ιmαν = ιmαν[:-1]
                      except: pass                      
                    elif key == curses.KEY_RIGHT:#                            Right key | 
                      try: ιmαν += αdιmαν[0] ; αdιmαν = αdιmαν[1:]
                      except: pass
                    elif key == ord('Ć'):#  Fn Left key                          To Top | 
                      αdιmαν = ιmαν + αdιmαν ; ιmαν = ''
                    elif key == ord('Ŧ'):#  Fn Right key                         To End | 
                      ιmαν = ιmαν + αdιmαν ; αdιmαν = ''
                    

                    elif key == curses.KEY_DC:# Supr                               Supr | 
                      αdιmαν = αdιmαν[1:]
                    elif key == ord('Ǟ'):# Alt Supr                                Supr | 
                      αdιmαν = str()
                    elif key == 0o10:#                                        Backspace | 
                      ιmαν = ιmαν[:-1]      
                    elif key == curses.KEY_F12:#  F12                                  Stνlαt | 
                      curses.endwin() ; stνlαt('Stνlαt  ','','stνlαt') ; curses.curs_set(False) ; stνlαt(αδqαιt,f'<INGERSATEL>',0)
                      

                    elif key != -1: ιmαν += chr(key)
                    else: pass
                          
                  except ValueError: ιmαν = str() ; pass
                  except Exception as e: stνlαt('Iugersαt',f'→ Prαν │ [red]{e}[/red]',0) ; pass
              
              google() ; ιmαν = str()
            elif key == ord('€'):#                 Gr(e)               Vermαt test |                                       
              stdscr.clear() ; Vermαtcsv() ; S = Lαmseut(0,'Stαuνor','','','','') ; ιmαν = uostιmαν = αdιmαν = str()
            elif key == curses.KEY_F10:#           F10                Lιuem Qαmpαr |                                       
              qαmpαr()
            elif key == curses.KEY_F12:#           F12                      Stνlαt |                                       
              curses.endwin() ; stνlαt('Stνlαt  ','','stνlαt'); curses.curs_set(False) ; stνlαt(αδqαιt,f'{os.getcwd()}',1)
                      
          # Num 
            elif key == ord('ǎ'):#                 Num(.)                        . |                                       
              ιmαν += '.'
            elif key == ord('Ǉ'):#                                           Log 1 |                                       
              try: ιlog = os.listdir() ; nlog = 0 ; ιmαν = ιlog[0]
              except: pass
            elif key == ord('ǈ'):#                                           Log 2 |                                       
              try: ιlog = os.listdir() ; nlog = 1 ; ιmαν = ιlog[1]
              except: pass
            elif key == ord('ǉ'):#                                           Log 3 |                                       
              try: ιlog = os.listdir() ; nlog = 2 ; ιmαν = ιlog[2]
              except: pass
            elif key == ord('Ǆ'):#                                           Log 4 |                                       
              try: ιlog = os.listdir() ; nlog = 3 ; ιmαν = ιlog[3]
              except: pass
            elif key == ord('ǅ'):#                                           Log 5 |                                       
              try: ιlog = os.listdir() ; nlog = 4 ; ιmαν = ιlog[4]
              except: pass
            elif key == ord('ǆ'):#                                           Log 6 |                                       
              try: ιlog = os.listdir() ; nlog = 5 ; ιmαν = ιlog[5] 
              except: pass
            elif key == ord('ǁ'):#                                           Log 7 |                                       
              try: ιlog = os.listdir() ; nlog = 6 ; ιmαν = ιlog[6]
              except: pass
            elif key == ord('ǂ'):#                                           Log 8 |                                       
              try: ιlog = os.listdir() ; nlog = 7 ; ιmαν = ιlog[7]
              except: pass
            elif key == ord('ǃ'):#                                           Log 9 |                                       
              try: ιlog = os.listdir() ; nlog = 8 ; ιmαν = ιlog[8]
              except: pass
            elif key == ord('Ǻ'):#                 Num(0)                   Log 10 |                                       
              try: ιlog = os.listdir() ; nlog = 9 ; ιmαν = ιlog[9]
              except: pass
            elif key == ord('Ȁ'):#                 Ctrl Num(5)              Log 15 |                                       
              try: ιlog = os.listdir() ; nlog = 14 ; ιmαν = ιlog[14]
              except: pass
            elif key == ord('ǻ'):#                 Ctrl Num(0)              Log 20 |                                       
              try: ιlog = os.listdir() ; nlog = 19 ; ιmαν = ιlog[19]
              except: pass  
            elif key == ord('Ȋ'):#                 Alt Num(5)               Log 25 |                                       
              try: ιlog = os.listdir() ; nlog = 24 ; ιmαν = ιlog[24]
              except: pass  
            elif key == ord('ȅ'):#                 Alt Num(0)               Log 30 |                                       
              try: ιlog = os.listdir() ; nlog = 29 ; ιmαν = ιlog[29]
              except: pass        
            elif key == ord('Ɯ'):#                 Alt 5                    Log 35 |                                       
              try: ιlog = os.listdir() ; nlog = 34 ; ιmαν = ιlog[34]
              except: pass    
            elif key == ord('Ɨ'):#                 Alt 0                    Log 40 |                                       
              try: ιlog = os.listdir() ; nlog = 39 ; ιmαν = ιlog[39]
              except: pass                

          # Nav 
            elif key == curses.KEY_UP:#                                     Log up |                                       
              ιlog = os.listdir()

              if nlog > 0: nlog -= 1
              else: nlog = len(ιlog)-1
              plog = nlog
              
              if S.prαν != '':
                δlog = int(plog / ylog) + 1
                δlog2 = δlog * ylog
                δlog1 = δlog2 - ylog
                log()

              ιmαν = ιlog[nlog]

              if S.ιzprαν != '': ιmtαu() ; S.ιzprαν = ιmανtαuder
              αdιmαν = str()
            elif key == curses.KEY_DOWN:#                                 Log down |                                       
              if ιmαν == '': nlog = δlog1 - 1
              ιlog = os.listdir() ; nlog += 1
              if nlog >= len(ιlog): nlog = 0
              plog = nlog


              if S.prαν != '':
                δlog = int(plog / ylog) + 1
                δlog2 = δlog * ylog
                δlog1 = δlog2 - ylog
                log()

              ιmαν = ιlog[nlog]

              if S.ιzprαν != '': ιmtαu() ; S.ιzprαν = ιmανtαuder
              αdιmαν = str()
            elif key == curses.KEY_LEFT:#                                Imαν left |                                       
              if ιmαν != '': αdιmαν = uostιmαν + αdιmαν ; uostιmαν = ιmαν[-1] ; ιmαν = ιmαν[:-1]
            elif key == curses.KEY_RIGHT:#                              Imαν right |                                       
              if αdιmαν != str(): ιmαν += uostιmαν ; uostιmαν = αdιmαν[0] ; αdιmαν = αdιmαν[1:]
              else: ιmαν += uostιmαν ; uostιmαν = str()  

            elif key == ord('Ǭ'):#                 Alt Right                Log Pg |                                       
              if δlog2 < len(ιlog): δlog1 = δlog1 + ylog ; δlog2 = δlog2 + ylog ; nlog = δlog1 ; log() ; ιmαν = ιlog[nlog]
            elif key == ord('ǭ'):#                 Alt Left                 Log Pg |                                       
              if δlog2 > ylog: δlog1 = δlog1 - ylog ; δlog2 = δlog2 - ylog ; nlog = δlog1 ; log() ; ιmαν = ιlog[nlog]

          # Lαg 
            elif key == ord('ş'):#                Shift Tab            Lαιu emtαμl |                                       
              ιlog = os.listdir()
              
              for i in ιlog: 
                if ιmαν == i[:len(ιmαν)]: ιmαν = i
                                                                        
            elif key == ord('ƻ'):#                Ctrl Left        ιmαν to νerseut |                                       
              νerseut = ιmαν
            elif key == ord('Ƈ'):#                Shift Left      ιmαν to νerseut2 |                                       
              νerseut2 = ιmαν
            elif key == ord('Ƽ'):#                Ctrl Right     αdιmαν to νerseut |                                       
              νerseut = uostιmαν + αdιmαν
            elif key == ord('Ɛ'):#                Shift Right   αdιmαν to νerseut2 |                                       
              νerseut2 = uostιmαν + αdιmαν
            elif key == ord('Ǡ'):#                Ctrl Up          νerseut to ιmαν |                                       
              ιmαν += νerseut
            elif key == ord('ǡ'):#                Ctrl Down       νerseut2 to ιmαν |                                       
              ιmαν += νerseut2        

            elif key == 0o10:#                                           Backspace |                                       
              ιmαν = ιmαν[:-1]
            elif key == ord('Ǹ'):#                 Alt Backspace        ιmαν Reset |                                       
              ιmαν = str  ()
            elif key == curses.KEY_DC:#            Supr               αdιmαν Reset |                                       
              if αdιmαν != '': uostιmαν = αdιmαν[0] ; αdιmαν = αdιmαν[1:]     # Si hay contenido después de uost
              else: uostιmαν = ''      
            elif key == ord('Ǟ'):#                 Alt Supr             ιmαν Reset |                                       
              uostιmαν = αdιmαν = str()


            # Mυsselαιtμ

            # Alt
            elif key == ord('ƣ'):# Alt C         ϥ 
              ιmαν += 'ϥ'
            elif key == ord('ơ'):# Alt A         α 
              ιmαν += 'α'
            elif key == ord('Ʊ'):# Alt Q         ᾱ 
              ιmαν += 'ᾱ'
            elif key == ord('ƥ'):# Alt E         ɢ 
              ιmαν += 'ɢ'
            elif key == ord('€'):#  Gr E         ē 
              ιmαν += 'ē'              
            elif key == ord('Ʃ'):# Alt I         ι 
              ιmαν += 'ι'
            elif key == ord('Ư'):# Alt O         ō 
              ιmαν += 'ō'
            elif key == ord('Ƶ'):# Alt U         υ 
              ιmαν += 'υ'
            elif key == ord('ƹ'):# Alt Y         ῡ 
              ιmαν += 'ῡ'
            elif key == ord('ƶ'):# Alt V         ν 
              ιmαν += 'ν'
            elif key == ord('ƨ'):# Alt H         ʯ 
              ιmαν += 'ʯ'                
            elif key == ord('Ƴ'):# Alt S         δ 
              ιmαν += 'δ'

            elif key != -1:#                                        ιmαν lαg sιguα |                                       
              ιmαν += chr(key)

            stdscr.refresh()
            time.sleep(0.01)  

          except ValueError as e: stνlαt(αδqαιt,f'→ {e}',0) ; ιmαν = uostιmαν = αdιmαν = str()
          except Exception as e: stνlαt(αδqαιt,f'→ {e}',0)

  wrapper(Lιuem)

except FileNotFoundError as e: stνlαt(αδqαιt,f'{e}',0) ; wrapper(Lιuem)
except AttributeError as e: stνlαt(αδqαιt,f'{e}',0) ; wrapper(Lιuem)
except ValueError as e: stνlαt(αδqαιt,f'{e}',0) ; wrapper(Lιuem)
except curses.error as e:stνlαt(αδqαιt,f'{e}',0) ; wrapper(Lιuem)
except Exception as e: 
  from rich import inspect
  stνlαt('Stαuνor ',f'→ {e}',0)
  console = Console()
  console.print('\nAqtαlιν uα Lιuem ιutαg\n')
  inspect(e)
  
  sιg = input('❯ ')
  if sιg == 'sig': console.print_exception() ; input()
  else: pass

  wrapper(Lιuem)

import curses.textpad


try:
  import curses
  import sqlite3 as sq
  from tkinter import *
  from rich import print
  from rich.console import Console
  from rich.layout import Layout
  from rich.panel import Panel
  from rich.prompt import Prompt


  
  def Lιuem():    

      console = Console()
      layout = Layout()

      def μeuzα():
        
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

        while True:
          print('[blue][bold]LINEM STANVOR[/blue][/bold]')
          print()
          print()
          print('Iuμeuzα toppeu')
          print()
          print('[green]1[/green] Iuναδ')
          print('[green]2[/green] Iuυν')
          print('[green]3[/green] Mυuιt')
          print('[green]4[/green] Auzα')
          print()
  
          μeuzα = input(': ')
  
          if μeuzα == '1':
            import os
            os.chdir(r'C:\Users\Leane\OneDrive\Escritorio\Lιuem')
            break
  
          elif μeuzα == '2':
            import os
            os.chdir(r'G:\Mi unidad\Lιuem Stαuνor')
            break

          elif μeuzα == '3':
            import os
            os.chdir(r'C:\Users\Leane\OneDrive\Escritorio\Mυuιt\Mυuιmα\Nιδeu\Imαδ')
            break
  
          elif μeuzα == '4':
            print()
            μeuzα = input('Iuνor ιlαg | ')
            
            if μeuzα == '':
              import os
              os.system('cls' if os.name == 'nt' else 'clear')
              pass
              
            else:  
              import os
              os.chdir(rf'{μeuzα}')
              break
  
          elif μeuzα == 'º':
            exit()
  
          else:
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            pass          
      μeuzα()
    
      def lαmlιuem():

        import os
        os.system ('cls' if os.name == 'nt' else 'clear')

        import psutil
        ιzναrtαg = psutil.sensors_battery()
        
        from datetime import datetime
        sιeνιt = datetime.now()
        timestamp = sιeνιt.strftime('%H.%M')

        if ιzναrtαg.power_plugged == True:
          console.print('Lιuem',' '*136,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#808080]\u2502[/#808080]',timestamp)

        if ιzναrtαg.power_plugged == False:
          console.print('Lιuem',' '*136,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#808080]\u2502[/#808080]',timestamp)

        console.print('\u2500'*158,style='blue')
      lαmlιuem()
        
      while True:        
        
        try:
          
          ιmαν = input('| ')
         
          if ιmαν == 'invash':
            print('C:\u005cUsers\u005cLeane\u005cOneDrive\u005cEscritorio\u005cLιuem')
            input()
            
          if ιmαν == '':
            lαmlιuem()

          elif ιmαν == 'º':
            exit()

          elif ιmαν == 'invor':
            import os
            ιuνor = os.getcwd()
            console.print(f'[green]Nostαl ιutorαg[/green]','[#808080]| [/#808080]', ιuνor)
            print()

          elif ιmαν == 'log':
            import os
            log = os.listdir()
            console.print('[green]Nostαl ιutorαg[/green]','[#808080]|[/#808080] ', os.getcwd())
            print()
            for i in log:
              console.print(f'  [#808080]|[/#808080] [cyan]{i}[/cyan]')
            print()
            print()
            
          elif ιmαν == 'izvartag':
            import psutil
            ιzναrtαg = psutil.sensors_battery()

            if ιzναrtαg.power_plugged == True:
              print()
              console.print('[green]Izναrtαg [/green]','[#808080]| [/#808080]',ιzναrtαg.percent)              
              console.print('[green]Iuμαuze  [/green]','[#808080]| [/#808080]','[magenta]Tαgeu[/magenta]')
              print()

            if ιzναrtαg.power_plugged == False:
              print()
              console.print('[green]Izναrtαg [/green]','[#808080]| [/#808080]',ιzναrtαg.percent)              
              console.print('[green]Iuμαuze  [/green]','[#808080]| [/#808080]','[red]Aqtαgeu[/red]')
              print()
          
          elif ιmαν == 'ligen':
            import os
            νers = input('> ')

            if νers == '':
              lαmlιuem()
                
            else:
                os.chdir(νers)
                console.print('[green]Nostαl ιutorαg[/green]','[#808080]|[/#808080] ', os.getcwd())
                print()
          
          elif ιmαν == 'endahl':
            while True:
              Qαιse = input(': ')

              if Qαιse == 'oppel':
                try:
                  eudel = input('> ')

                  if eudel == 'º':
                    lαmlιuem()
                    break

                  elif eudel == '':
                    lαmlιuem()
                    break

                  else:
                    import os
                    os.system(f'echo. > {eudel}')
                    print(f'{eudel} oppel ιutαgeu')
                    print()
                    break

                except Exception as e:
                  print()
                  print(e)
                  print() 

              elif Qαιse == 'intorag':
                try:
                  import os
                  eudαμl = input('> ')
        
                  if eudαμl == '':
                    print()
                    break
        
                  else:
                    os.makedirs(eudαμl)
                    print(f'Vιαret ιutorαg dyα lαιue [cyan]{eudαμl}[/cyan]')
                    print()
                    break
                      
                except Exception as e:
                  print()
                  print(e)
                  input()

              elif Qαιse == 'stanvor': #ιutreν
                try:                
                  print()
                  
                  Lαιu = input('Lαιu | ')
                  print()
                  
                  columns = []

                  while True:
                  
                    askcolumns = input('Iduανerα | ')
                  
                    if askcolumns == 'º':
                      break

                    else:
                      
                      if askcolumns == '':
                        break

                      else:
                        columns.append(askcolumns)
                        print(columns)
                        print()
                  
                  print(columns)
                  input()
                
                except Exception as e:
                  print(f'\n{e}\n')
            
              elif Qαιse == 'º':
                break

              else:
                print("Oppel υt ιutorαg..")
              
          elif ιmαν == 'aqehr':
            try:
              while True:
              
                αqeμr = input(': ')

                if αqeμr == 'oppel':

                  oppel = input('> ')

                  if oppel == 'º':
                    print()
                    break

                  if oppel == '':
                    print()
                    break


                  else:
                    try:
                      import os
                      
                      if os.path.exists(oppel):
                        os.system(f'del {oppel} ')
                        console.print(f'[cyan]{oppel}[/cyan] oppel αqeμreu')
                        print()
                        break

                      else:
                        console.print(f'[cyan]{oppel}[/cyan] oppel αqtαgeu')
                        print()
                        break

                    except Exception as e:
                      print(e)
                      print()

                elif αqeμr == 'intorag':
                  
                  αqeμr = input('> ')

                  if αqeμr == 'º':
                    print()
                    break

                  if αqeμr == '':
                    print()
                    break

                  import os
                  os.rmdir(αqeμr)
                  console.print(f'[cyan]{αqeμr}[/cyan] ιutorαg αqeμreu')
                  print()
                  break

                elif αqeμr == '':
                  print()
                  break

                elif αqeμr == 'º':
                  print()
                  break

                else:
                  print('Oppel υt Iutorαg..')              

            except Exception as e:
              print(e)
              print()

          elif ιmαν == 'verse':
            try:
              import os
              logreu = input('> ')
              
              if logreu == '':             
                print()
                pass

              else:
                if os.path.exists(logreu):                
                  eudαμl = input('Eudαμl > ')
                
                  if eudαμl == '':
                    print()
                    pass
                  
                  else:
                      if os.path.exists(eudαμl):
                        os.system(f'move {logreu} {eudαμl}')
                        print()
                        console.print('\u2500'*158,style='#24272d')

                      else:
                        print('Iutorαg νιαreq')
                        pass

                else:
                  print('Logreu νιαreq')
                  print()
                  pass

            except Exception as e:
              print()
              print(e)
              print()

          elif ιmαν == 'laine':
            import os
            logreu = input('> ')

            if logreu == 'º':
              print()
              pass

            elif logreu == '':
              print()
              pass
            
            else:
              if os.path.exists(logreu):
                lαιue = input('Eudαμl > ')
              
                os.rename(logreu,lαιue)
                console.print(f'Logreu [cyan]{logreu}[/cyan] uα [cyan]{lαιue}[/cyan] αtιν lαιue ye')
                print()
                console.print('\u2500'*158,style='#24272d')

              else:
                print('Logreu νιαreq')
                print()
            
          elif ιmαν == 'shovt':
            try:
              import os
              import subprocess
              
              def shutdown_computer():
                δoνte = input('· Seνdαl uα sιstem δoνt? ')                
                if δoνte == '':                
                  if os.name == 'nt':
                      # For Windows operating system
                      os.system('shutdown /s /t 0')
                  elif os.name == 'posix':
                      # For Unix/Linux/Mac operating systems
                      os.system('sudo shutdown now')
                  else:
                      print('δoνt αqtαgeu')
                else:
                  lαmlιuem()
                  return
                  
              shutdown_computer()
              
            except:
              print('δoνt αqtαgeu')
          
          elif ιmαν == 'mativ':
            lαmlιuem()
            import datetime
            sιevιt = datetime.date.today()
            print(sιevιt, 'mαtιν')
            input()
            lαmlιuem()

          elif ιmαν == 'entel': 
            
            try:
              import subprocess

              logreu = input('> ')
              print()

              if logreu == 'º':
                pass

              elif logreu == '':
                pass

              elif logreu == 'mp':
                try:
                  import pygame

                  mp = input('> ')

                  pmix = pygame.mixer()
                  pmusic = pmix.music()

                  #pmix.init()
                  #pmusic.load(mp)
                  #pmusic.play()
                  print()
                
                except Exception as e:
                  print()
                  print(e)
                  print()
                  input()
                  print()

              elif logreu == 'wv':
                try:
                  wv = input('> ')

                  from playsound import playsound

                  playsound(wv)

                except Exception as e:
                  print()
                  print(e)
                  print()
                  input()

                lαmlιuem()
                
              else:
                subprocess.Popen(logreu)
              

            except:
              try:
                import os
                os.system(logreu)
                
              except Exception as e:
                print()
                print(e)
                print()
                input()
                lαmlιuem()

          elif ιmαν == 'henza':
            try:
              import os
              os.system('cls' if os.name == 'nt' else 'clear')
              μeuzα()
              lαmlιuem()

            except Exception as e:
              lαmlιuem()

          elif ιmαν == 'tag':
            import os

            print()
            install = input('> ')            
            os.system(f'python -m pip install {install}')
            input()

          elif ιmαν == '.dos':
            print()
            import os
            os.system('cmd')
            print()
          
          elif ιmαν == 'net':
            import psutil

            def wificonnect():
                
                stats = psutil.net_if_stats()
                
                for interface, stat in stats.items():
                    if interface == 'Wi-Fi':
                      print()
                      if stat.isup:
                          print(f"{interface} ιuμeuzeu")
                          print()

                      else:
                          print(f"{interface} ιuμeuzαqeu")
                          print()
                    
                    else:
                      pass

            wificonnect()
          
          elif ιmαν == 'locals':
            print()
            print(locals())
            input()
            lαmlιuem()

          elif ιmαν == 'screen':
            from screeninfo import get_monitors

            for m in get_monitors():
              print(f"\nMonitor: {m.name}, Width: {m.width}, Height: {m.height}\n")  
         
          #| Logreuα

          elif ιmαν == 'Vermat':

            def Vermαt():

              while True:
                
                def lαmνermαt():
                  import psutil
                  ιzναrtαg = psutil.sensors_battery()
                  
                  import os
                  os.system('cls' if os.name == 'nt' else 'clear')
                  
                  from datetime import datetime
                  sιeνιt = datetime.now()
                  timestamp = sιeνιt.strftime('%H.%M')
                  os.system ('cls' if os.name == 'nt' else 'clear')                                  


                  if ιzναrtαg.power_plugged == True:
                    print('Vermαt [#808080]\u2502[/#808080]',' '*133,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#808080]\u2502[/#808080]',timestamp)

                  if ιzναrtαg.power_plugged == False:
                    print('Vermαt [#808080]\u2502[/#808080]',' '*133,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#808080]\u2502[/#808080]',timestamp)
                  
                  console.print('\u2500'*158,style='blue')                  
                  print('[#808080]\u2502[/#808080] Mαtιν [#808080]\u2502[/#808080] Mυuιtsyα [#808080]\u2502[/#808080] Pιlμα [#808080]\u2502[/#808080] Estαq [#808080]\u2502[/#808080] Estαq 3 [#808080]\u2502[/#808080] Lιuem [#808080]\u2502[/#808080] Verqom [#808080]\u2502[/#808080] Iuαq [#808080]\u2502[/#808080] Aqtαudeμ [#808080]\u2502[/#808080] º [#808080]\u2502[/#808080]')
                  console.print('\u2500'*158,style= '#24272d')
                  print()

                  try:
                    oppel = open('Vermαt.txt',encoding='utf8')
                    print(oppel.read())
                    oppel.close()
                    
                  except FileNotFoundError:
                    print("Vermαt αqtαgeu' ιuνor ιutrēν")
                    print()

                  '''try:
                    conn = sq.connect('Lιuem.sqlite')
                    c = conn.cursor()
                    #c.execute('create table if not exists νermαt (Aδqαιt text, Uναιt text, Toreg text)')
                    c.execute('select * from νermαt')
                    νermαt = c.fetchall()
                    for i in νermαt:
                      print('|',i[0],'    ',i[1])
                    print()
                  
                  except Exception as e:
                    print(f'\n{e}\n')'''              
                  
                lαmνermαt()

                console.print('\u2500'*158,style= '#808080')

                ινermαt = input('| ')
                
                if ινermαt == 'Mativ':
                  
                  try:

                    while True:
                      
                      oppel = open('Mαtιν.csv',encoding='utf8')
                      
                      def lαmαtιν():
                        
                        lαmνermαt()
                        console.print('\u2500'*158,style= '#24272d')
                        console.print('Mαtιν [#808080]|[/#808080]\n')
                        console.print(oppel.read())
                        console.print('\u2500'*158,style='#808080')
                        
                      lαmαtιν()

                      Mαt_Imαν = input('| ')
                      
                      if Mαt_Imαν == 'º':
                        break
                      
                      elif Mαt_Imαν == '':
                        pass

                      elif Mαt_Imαν == '.invor':
                        import os
                        ιuνor = os.getcwd()
                        console.print(f'[green]Nostαl ιuνor[/green]','[#808080]| [/#808080]', ιuνor)
                        print()
                        input()
                        
                      elif Mαt_Imαν == 'verqom':
                        
                        try:
                          
                          line_number = input(': ')
                          
                          if line_number == 'º':
                            break
                          
                          elif line_number == '':
                            line_number = 0
                          
                          else: line_number = int(line_number)
                          
                          with open('Mαtιν.csv',encoding='utf8') as oppel:
                            lines = oppel.readlines()
                            print(lines[line_number-1])
                          
                          new_line = input('> ')
                          
                          if new_line == 'º':   
                            lαmαtιν()
                            pass
                          
                          else:
                            lines[line_number-1] = '| ' + new_line + '\n'
                            if line_number <= len(lines):
                              with open('Mαtιν.csv', 'w',encoding='utf8') as oppel:
                                oppel.truncate(0)
                              for i in lines:
                                oppel = open('Mαtιν.csv','a',encoding='utf8')
                                oppel.write(i)
                                oppel.close()                        
                            else:
                              pass
                              
                        except ValueError:
                          print()
                          print('Lαg αqtαlινeu')
                          input()
                          
                        except IndexError:
                          pass
  
                      elif Mαt_Imαν == 'inaq':

                        try:

                          number = input(': ')

                          if number == '':
                            number = 0
                          else:
                            number = int(number)

                          with open('Mαtιν.csv',encoding='utf8') as oppel:
                            lines = oppel.readlines()
                            print(lines[number-1])

                            ιuαq = input('> ')

                            if ιuαq == 'º':
                              pass
                            else:
                              if number <= len(lines):
                                del lines[number-1]
                                oppel = open('Mαtιν.csv','w',encoding='utf8')
                                for i in lines:
                                  oppel.write(i)
                                oppel.close()
                              else:
                                pass

                        except Exception as e:
                          print()
                          print(e)
                          input()
                        
                        except ValueError:
                          print()
                          print('Lαg αqtαlινeu')
                          input()
                        
                        except IndexError:
                          lαmνermαt()
                          pass
                      
                      elif Mαt_Imαν == '.aqtande':
                        print()
                        Seνdαl = input('Seνdαl uα Mαtιν αqtαudeμ | ')
                        if Seνdαl == 'Dyav':
                          oppel = open('Mαtιν.csv','a')
                          oppel.truncate(0)
                          oppel.close
                        else:
                          print()
                      
                      else:
                        oppel = open('Mαtιν.csv','a',encoding='utf8')
                        oppel.write('| ')
                        oppel.write(Mαt_Imαν)
                        oppel.write('\n')
                        oppel.close()  

                  except FileNotFoundError:
                    print()
                    print("Mαtιν αqtαgeu' ιuνor ιutrēν")
                    input()
                
                elif ινermαt == 'Munit':

                  try:
                    def νermυu():
                      
                      while True:
                        
                        def lαmυuιt():
                          oppel = open('Mυuιt Vermαt.txt','r',encoding='utf8')
                          
                          lαmνermαt()

                          console.print('\u2500'*158,style= '#24272d')
                          print('Mυuιtsyα [#808080]|[/#808080]\n')
                          print(oppel.read())
                          console.print('[#808080]\u2500[/#808080]'*158)
                          
                        lαmυuιt()
                      
                        vermυu = input('| ')
                      
                        if vermυu == 'º':
                          break
                        
                        elif vermυu == 'inaq':
                          
                          try:
                            number = input(': ')
                            
                            if number == 'º':
                              lαmυuιt()
                              break
                            
                            if number == '':
                              number = 0
                            
                            else: number = int(number)
                            
                            def ιuαqtαν(lαιue,line_number):
                            
                              with open(lαιue,encoding='utf8') as oppel:
                                lines = oppel.readlines()
                                print(lines  [line_number-1])
                                ιuαq = input('> ')
                                
                                if ιuαq == '.':
                                  if line_number <= len(lines):
                                    del lines[line_number-1]
                                    oppel = open('Mυuιt Vermαt.txt','w',encoding='utf8')
  
                                    for i in lines:
                                      oppel.write(i)
                                    oppel.close()
  
                                  else:
                                    pass
                                  
                                else:
                                  pass
  
                                    
                            ιuαqtαν('Mυuιt Vermαt.txt',number)
  
                            lαmυuιt()
                            
                          except ValueError:
                            print()
                            print('Lαg αqtαlινeu')
                            input()
                            
                          except IndexError:
                            lαmνermαt()
                            pass
                        
                        elif vermυu == '':
                          lαmνermαt()
                        
                        else:
                          try:
                            oppel = open('Mυuιt Vermαt.txt','a',encoding='utf8')
                            oppel.write('| ')
                            oppel.write(vermυu)
                            oppel.close()
                            print()
  
                            sιgμe = input('Sιgμe tαudrα | ')
  
                            if sιgμe == '':
                              oppel = open('Mυuιt Vermαt.txt','a',encoding='utf8')
                              oppel.write('\n')
                              oppel.close()
  
                            else:                      
                              oppel = open('Mυuιt Vermαt.txt','a',encoding='utf8')
                              oppel.write('>  ')
                              oppel.write(sιgμe)
                              oppel.write('\n')
                              oppel.close()
  
                          except: pass
                    
                    νermυu()
                    
                  except FileNotFoundError:
                    print()
                    print("Mυuιt Vermαt αqtαgeu' ιuνor ιutrēν")
                    input()
                
                elif ινermαt == 'Pilha':
                  try:                 
                                    
                    while True:
                      def lαmpιlμα():
                        lαmνermαt()
                        console.print('\u2500'*158,style='#24272d')
                        print('Pιlμα |')
                        print()
                      lαmpιlμα()
                      
                      oppel = open('Verpιlμα.txt','r',encoding='utf8')
                      print(oppel.read()) 

                      console.print('\u2500'*158,style='#808080')
                      
                      Pιlμα = input('| ')
                      
                      if Pιlμα == 'º':
                        lαmνermαt()
                        break
                      
                      elif Pιlμα == '':
                        pass           
                            
                      elif Pιlμα == 'inaq':
                        
                        def ιuαq():
                          
                          try:
                            
                            def ιuαq():
                              number = input(': ')
                            
                              if number == 'º':
                                return
                              
                              if number == '':
                                number = 0
                            
                              else: number = int(number)
                              
                              def ιuαqtαν(lαιue,line_number):
                              
                                with open(lαιue,encoding='utf8') as oppel:
                                  lines = oppel.readlines()
                                  print(lines[line_number-1])
                                  ιuαq = input('> ')                  
                                
                                  if ιuαq == '.':
                                    if line_number <= len(lines):
                                      del lines[line_number-1]
                                      oppel = open('Verpιlμα.txt','w',encoding='utf8')
                                      for i in lines:
                                        oppel.write(i)
                                      oppel.close()
                                    else:
                                      pass
                                
                                  else:
                                    pass
                                
                                lαmpιlμα()
                              
                              ιuαqtαν('Verpιlμα.txt',number)
                            
                            ιuαq()

                          except ValueError:
                            print()
                            print('Lαg αqtαlινeu')
                            input()
                            
                          except IndexError:
                            pass
                            
                          # Editar cualquier línea..
                          '''elif eudel == 'Ashqait':
                          import os
                          os.system('Sedge https://docs.google.com/document/d/1NpckpNsTxjMBEVLm1tuL8Pk_WtmoqTCB/edit?rtpof=true')'''
                        ιuαq()
                  
                      elif Pιlμα == 'Aqtande':
                        
                        lαmpιlμα()
                        
                        Aqtαudeμ = input('Seνdαl uα Pιlμα αqtαudeμ | ')
                        
                        if Aqtαudeμ == 'Dyav':
                          oppel = open('Verpιlμα.txt','a')
                          oppel.truncate(0)
                          oppel.close
                          lαmpιlμα()
                          print('Verpιlμα αqtαudeu')
                          print()
                        
                        else:
                          print()
                      
                      else:
                        lαmpιlμα()

                        oppel = open('Verpιlμα.txt','a',encoding='utf8')
                        oppel.write('| ')
                        oppel.write(Pιlμα)
                        oppel.write('\n')
                        oppel.close()
                  
                  except FileNotFoundError:
                    print()
                    print("Verpιlμα αqtαgeu' ιuνor ιutrēν")
                    print()
                    input()
                    
                elif ινermαt == 'Linem':
                  try:
                    while True:
                      
                      def lαmνerlιuem():
                        
                        oppel = open('Lιuem Vermαt.txt',encoding='utf8')
                        
                        from datetime import datetime
                        import os
                        sιeνιt = datetime.now()
                        timestamp = sιeνιt.strftime('%H.%M')

                        import psutil
                        ιzναrtαg = psutil.sensors_battery()

                        if ιzναrtαg.power_plugged == True:
                          os.system('cls' if os.name == 'nt' else 'clear')
                          console.print('Vermαt [#808080]\u2502[/#808080] Lιuem [#808080]\u2502[/#808080]',' '*125,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#808080]\u2502[/#808080]',timestamp)

                        if ιzναrtαg.power_plugged == False:
                          os.system('cls' if os.name == 'nt' else 'clear')
                          console.print('Vermαt [#808080]\u2502[/#808080] Lιuem [#808080]\u2502[/#808080]',' '*125,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#808080]\u2502[/#808080]',timestamp)
                        
                        console.print('\u2500'*158, style='blue')

                          
                        print(oppel.read())
                        
                      lαmνerlιuem()
                      
                      lιumαν = input()
                      
                      if lιumαν == '.lag':
                        import os
                        os.system('"Lιuem Vermαt.txt"')

                      elif lιumαν == 'inaq':
                        def ιuαq():
                          
                          try:
                            
                            number = input(': ')
                            
                            if number == '':
                              number = 0

                            if number == 'º':
                              return
                            
                            else: number = int(number)
                            
                            def ιuαqtαν(lαιue,line_number):
                            
                              with open(lαιue,encoding='utf8') as oppel:
                                lines = oppel.readlines()
                                print(lines[line_number-1])
                                ιuαq = input('> ')                  
                                
                                if ιuαq == '.':
                                  
                                  if line_number <= len(lines):
                                    del lines[line_number-1]
                                    oppel = open('Lιuem Vermαt.txt','w',encoding='utf8')
                                    for i in lines:
                                      oppel.write(i)
                                    oppel.close()
                                  else:
                                    pass
                                
                                else:
                                  return

                            ιuαqtαν('Lιuem Vermαt.txt',number)
                          except ValueError:
                            print()
                            print('Lαg αqtαlινeu')
                            input()
                          except IndexError:
                            pass
                          # Editar cualquier línea..
                        ιuαq() 
                      
                      elif lιumαν == 'º':
                        lαmνermαt()
                        break
                      
                      else:
                        oppel = open('Lιuem Vermαt.txt','a',encoding='utf8')
                        oppel.write('\n')
                        oppel.write(lιumαν)
                        oppel.close()
                        lαmνerlιuem()
                        oppel = open('Lιuem Vermαt.txt',encoding='utf8')

                  except FileNotFoundError:
                    print()
                    print("Lιuem Vermαt αqtαgeu' ιuνor ιutrēν")
                    print()
                    input()

                elif ινermαt == '.tander':
                  try:
                    def tαuder():
                      while True:
                      
                        def lαmtαuder():
                        
                          import os
                          os.system('cls' if os.name == 'nt' else 'clear')

                          from datetime import datetime
                          sιevιt = datetime.now()
                          timestamp = sιevιt.strftime('%H.%M')

                          import psutil
                          ιzναrtαg = psutil.sensors_battery()
                          
                          if ιzναrtαg.power_plugged == True:
                            print('Tαuder [#808080]|[/#808080]',' '*133,'[#808080]|[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#808080]|[/#808080]',timestamp)

                          if ιzναrtαg.power_plugged == False:
                            print('Tαuder [#808080]|[/#808080]',' '*133,'[#808080]|[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#808080]|[/#808080]',timestamp)

                          console.print('\u2500'*158,style='blue')

                          with open('Tαuder.txt', 'r', encoding='utf8') as oppel:
                            print(oppel.read())

                        lαmtαuder()

                        tαuder = input('')

                        if tαuder == 'º':
                          lαmlιuem()
                          return
                        
                        elif tαuder == '.lag':
                          import os
                          os.system('Tαuder.txt')

                        else:
                          with open('Tαuder.txt', 'a', encoding='utf8') as oppel:
                            oppel.write('\n')
                            oppel.write(tαuder)                      
                      
                    tαuder()
                  
                  except Exception as e:
                    print()
                    print(e)
                    print()

                elif ινermαt == 'Estaq':
                  try:
                    oppel = open('Estαq.txt',encoding='utf8')
                    
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Vermαt [#808080]\u2502[/#808080] Estαq [#808080]\u2502[/#808080]')
                    console.print('\u2500'*158,style='blue')

                    print(oppel.read())
                    
                    console.print('\u2500'*158,style='#808080')

                    estαq = input('| ')

                    if estαq == '.lag':
                      import os
                      os.system('Estαq.txt')
                      lαmνermαt()

                  
                  except FileNotFoundError:
                    print()
                    print("Estαq αqtαgeu' ιuνor ιutrēν")
                    print()
                    input()
                    
                elif ινermαt == 'Estaq3':
                  
                  try:
                  
                    oppel = open('Estαq 3.txt',encoding='utf8')
                  
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Vermαt \u2502 Estαq 3 \u2502')
                    print('\u2500'*158)
  
                    print(oppel.read())

                    estαq3 = input('| ')

                    if estαq3 == 'lag':
                      import os
                      os.system('"Estαq 3.txt"')
                    
                  except FileNotFoundError:
                    print()
                    print("Estαq 3 αqtαgeu' ιuνor ιutrēν")
                    print()
                    input()       
                
                elif ινermαt == 'verqom':
                  try:
                    open('Vermαt.txt',encoding='utf8')
                    
                    def νerqom():
                      try:
                        
                        line_number = input(': ')
                        
                        if line_number == 'º':
                          return
                        
                        elif line_number == '':
                          line_number = 0
                        
                        else: line_number = int(line_number)                     
                        
                        with open('Vermαt.txt',encoding='utf8') as oppel:
                          lines = oppel.readlines()
                          print(lines[line_number-1])            
                        
                        eudαμl =  input('> ')
                        
                        if eudαμl == '':
                          pass
                        
                        else:
                            print()
                            sιgμe = input('Sιgμe | ')
                          
                            if sιgμe == '':
                              lines[line_number-1] = '| ' + eudαμl + '\n'
                              oppel = open('Vermαt.txt','w',encoding='utf8')
                              oppel.truncate(0)
                              for i in lines:
                                oppel = open('Vermαt.txt','a',encoding='utf8')
                                oppel.write(i)
                                oppel.close()

                            else:
                              lines[line_number-1] = '| ' + eudαμl + '        >        ' + sιgμe + '\n'
                              oppel = open('Vermαt.txt','w',encoding='utf8')
                              oppel.truncate(0)
                              for i in lines:
                                oppel = open('Vermαt.txt','a',encoding='utf8')
                                oppel.write(i)
                                oppel.close()
                      
                      except IndexError:
                        pass

                    νerqom()

                  except:
                    pass
                        
                  '''con = sq.connect('Lιuem.sqlite')
                  c = con.cursor()
                  c.execute('select * from νermαt')
                  νermαt = c.fetchall()
                  items = νermαt[line_number-1]
                  print('|',items[0],'   ',items[1])
                  
                        
                  items = (eudαμl,sιgμe,'')
                  con = sq.connect('Lιuem.sqlite')
                  c = con.cursor()
                  c.execute(f"update νermαt set Aδqαιt = ?, Uναιt = ?, Toreg = ? where rowid = {line_number-1}",items)
                  con.commit()
                  c.execute('select * from νermαt')
                  νermαt = c.fetchall() 
                  print(νermαt)
                  input()'''

                elif ινermαt == 'inaq':

                  try:
                    oppel = open('Vermαt.txt',encoding='utf8')
                    
                    def ιuαq():
                      number = input(': ')
                    
                      if number == 'º':
                        return
                    
                      if number == '':
                        number = 0
                    
                      else: number = int(number)
                    
                      oppel = open('Vermαt.txt',encoding='utf8')
                      lines = oppel.readlines()
                      print(lines[number-1])
                    
                      ιuαq = input('> ')                  
                
                      if ιuαq == '.':
                        if number <= len(lines):
                          del lines[number-1]
                          oppel = open('Vermαt.txt','w',encoding='utf8')
                          oppel.truncate(0)
                          for i in lines:
                            oppel = open('Vermαt.txt','a',encoding='utf8')
                            oppel.write(i)
                            oppel.close()
                                            
                        else:
                          return
  
                      else:
                        pass
                    
                    ιuαq()

                  except ValueError:
                    print()
                    print('Lαg αqtαlινeu')
                    input()
                  
                  except:
                    pass
                
                elif ινermαt == 'aqtande':
                  
                  try:
                    oppel = open('Vermαt.txt','a')
                    
                    lαmνermαt()
                    
                    Aqtαudeμ = input('Seνdαl uα Vermαt αqtαudeμ | ')
                    
                    if Aqtαudeμ == 'Dyav':
                      oppel.truncate(0)
                      oppel.close
                      lαmνermαt()
                      print('Vermαt αqtαudeu')
                      print()
                      
                    else:
                      pass
                      
                  except:
                    pass
                
                elif ινermαt == 'º':
                  lαmlιuem()
                  return
                
                else:
                  
                  if ινermαt == '':
                    lαmνermαt()
                    pass
                  
                  else:
                    try:
                      oppel = open('Vermαt.txt','a',encoding='utf8')
                      oppel.write('| ')
                      oppel.write(ινermαt)
                      oppel.close()
                      print()

                      sιgμe = input('Sιgμe tαudrα | ')
                      
                      if sιgμe == '':
                        oppel = open('Vermαt.txt','a',encoding='utf8')
                        oppel.write('\n')
                        oppel.close()

                      else:                      
                        oppel = open('Vermαt.txt','a',encoding='utf8')
                        oppel.write('        >        ')
                        oppel.write(sιgμe)
                        oppel.write('\n')
                        oppel.close()

                      '''try:
                      
                      values = (ινermαt,sιgμe,'')

                      conn = sq.connect('Lιuem.sqlite')
                      c = conn.cursor()
                      c.execute('create table if not exists νermαt (Aδqαιt text, Uναιt text, Toreg text)')
                      c.execute(f"insert into νermαt ('Aδqαιt','Uναιt','Toreg') values (?,?,?)",values)
                      conn.commit()
                      c.execute('select * from νermαt')
                      conn.close()'''
 
                    except Exception as e:
                      print(f'\n{e}\n')
                      input()
            
            Vermαt()
          
          elif ιmαν == 'Dyatev':

            def Dyαtēν():
              
              while True:
                
                  def lαmdyαteν():
                    
                    import os
                    os.system ('cls' if os.name == 'nt' else 'clear')

                    import psutil
                    ιzναrtαg = psutil.sensors_battery()
                    
                    from datetime import datetime
                    sιeνιt = datetime.now()
                    timestamp = sιeνιt.strftime('%H.%M')

                    console = Console()
                    
                    if ιzναrtαg.power_plugged == True:
                      print('Dyαtēν [#808080]\u2502[/#808080]',' '*133,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#808080]\u2502[/#808080]',timestamp)

                    if ιzναrtαg.power_plugged == False:
                      print('Dyαtēν [#808080]\u2502[/#808080]',' '*133,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#808080]\u2502[/#808080]',timestamp)
                      
                    console.print('\u2500'*158,style='blue')
                    console.print('[#808080]|[/#808080] Sιguα [#808080]|[/#808080] Verqōm [#808080]|[/#808080] Iuαq [#808080]|[/#808080] Aqtαudeμ [#808080]|[/#808080] Mυutαuder [#808080]|[/#808080] Dyeναstαq [#808080]|[/#808080] º [#808080]|[/#808080]')
                    console.print('\u2500'*158,style='#24272d')
                    print()

                    try:
                      oppel = open('Dyαtēν.txt',encoding='utf8')
                      print(oppel.read())
                      oppel.close()
                    
                    except FileNotFoundError:
                      print("Dyαteν αqtαgeu' ιuνor ιutrēν")
                      print()
                    
                  lαmdyαteν()
                
                  while True:
                    
                    console = Console()
                    
                    console.print('\u2500'*158,style='#808080')
                    
                    Dyαt_Imαν = input('| ')
                    
                    if Dyαt_Imαν == 'signa':
                      
                      lαmdyαteν()
                      console.print('\u2500'*158,style='#808080')
                      print('Sιguα  \u2502')
                      console.print('\u2500'*158,style='#24272d')
                      
                      Qαιse = input('Qαιse  | ')
                      
                      if Qαιse == '':
                        oppel = open('Dyαtēν.txt','a',encoding='utf8')
                        oppel.write('\n')
                        oppel.write('\n')
                        oppel.close()
                      
                      elif Qαιse == 'º':
                        break
                      
                      else:
                        oppel = open('Dyαtēν.txt','a',encoding='utf8')
                        oppel.write('\n')
                        oppel.write('\n')
                        oppel.write(Qαιse)
                        oppel.write(' | ')
                        oppel.close()
                      
                      Lαιu = input('Lαιu   | ')
                      
                      if Lαιu == '':
                        oppel = open('Dyαtēν.txt','a',encoding='utf8')
                        oppel.write('\n')
                        oppel.close()
                      
                      elif Lαιu == 'º':
                        break
                      
                      else:
                        oppel = open('Dyαtēν.txt','a',encoding='utf8')
                        oppel.write(Lαιu)
                        oppel.write('\n')
                        oppel.close()
                      
                      oppel = open('Dyαtēν.txt','a',encoding='utf8')
                      oppel.write('\u2500'*21)
                      oppel.write('\n')
                      oppel.close()
                      
                      Sιeνιt = input('Sιeνιt | ')
                      
                      if Sιeνιt == '':
                        oppel = open('Dyαtēν.txt','a',encoding='utf8')
                        oppel.write('\n')
                        oppel.close()
                      
                      elif Sιeνιt == 'º':
                        break
                      
                      else:
                        oppel = open('Dyαtēν.txt','a',encoding='utf8')
                        oppel.write('Sιeνιt  | ')
                        oppel.write(Sιeνιt)
                        oppel.write('\n')
                        oppel.close()
                      
                      Iuνorαt = input('Vorαt  | ')
                      
                      if Iuνorαt == '':
                        oppel = open('Dyαtēν.txt','a',encoding='utf8')
                        oppel.write('\n')
                        oppel.close()
                      
                      elif Iuνorαt == 'º':
                        break
                      
                      else:
                        oppel = open('Dyαtēν.txt','a',encoding='utf8')
                        oppel.write('Iuvorαt | ')
                        oppel.write(Iuνorαt)
                        oppel.write('\n')
                        oppel.close()
                      
                      Auget = input('Auget  | ')
                      
                      if Auget == '':
                        oppel = open('Dyαtēν.txt','a',encoding='utf8')
                        oppel.write('\n')
                        oppel.close()
                      
                      elif Auget == 'º':
                        break
                      
                      else:
                        oppel = open('Dyαtēν.txt','a',encoding='utf8')
                        oppel.write('Auget   | ')
                        oppel.write(Auget)
                        oppel.write('\n')
                        oppel.close()
                      
                      Dyαutαl = input('Dyαute | ')
                      
                      if Dyαutαl == '':
                        oppel = open('Dyαtēν.txt','a',encoding='utf8')
                        oppel.write('\n')
                        oppel.close()
                        break
                      
                      elif Dyαutαl   == 'º':
                        break
                      
                      else:
                        oppel = open('Dyαtēν.txt','a',encoding='utf8')
                        oppel.write('Dyαutαl | ')
                        oppel.write(Dyαutαl)
                        oppel.write('\n')
                        oppel.close()
                      
                        while True:
                        
                          Dyαutαl = input('       | ')
                          
                          if Dyαutαl == '':
                            oppel = open('Dyαtēν.txt','a',encoding='utf8')
                            oppel.write('\n')
                            oppel.close()
                            break
                          
                          elif Dyαutαl   == 'º':
                            oppel = open('Dyαtēν.txt','a',encoding='utf8')
                            oppel.write('\n')
                            oppel.close()
                            break
                          
                          else:
                            oppel = open('Dyαtēν.txt','a',encoding='utf8')
                            oppel.write('        | ')
                            oppel.write(Dyαutαl)
                            oppel.write('\n')
                            oppel.close()
                   
                    elif Dyαt_Imαν == 'Vermun':

                      try:
                        def νermυu():

                          while True:

                            def lαmυuιt():
                              oppel = open('Mυuιt Vermαt.txt','r',encoding='utf8')

                              lαmdyαteν()

                              print()
                              console.print('\u2500'*158,style='#24272d')

                              print('Mυuιtsyα [#808080]|[/#808080]\n')
                              print(oppel.read())
                              print()
                              console.print('[#808080]\u2500[/#808080]'*158)

                            lαmυuιt()

                            vermυu = input('| ')

                            if vermυu == 'º':
                              lαmdyαteν()
                              break

                            elif vermυu == 'inaq':

                              try:
                                number = input(': ')

                                if number == 'º':
                                  lαmυuιt()
                                  break

                                if number == '':
                                  number = 0

                                else: number = int(number)

                                def ιuαqtαν(lαιue,line_number):

                                  with open(lαιue,encoding='utf8') as oppel:
                                    lines = oppel.readlines()
                                    print(lines  [line_number-1])
                                    ιuαq = input('> ')

                                    if ιuαq == '.':
                                      if line_number <= len(lines):
                                        del lines[line_number-1]
                                        oppel = open('Mυuιt Vermαt.txt','w',encoding='utf8')

                                        for i in lines:
                                          oppel.write(i)
                                        oppel.close()

                                      else:
                                        pass

                                    else:
                                      pass


                                ιuαqtαν('Mυuιt Vermαt.txt',number)

                                lαmυuιt()

                              except ValueError:
                                print()
                                print('Lαg αqtαlινeu')
                                input()

                              except IndexError:
                                lαmdyαteν()
                                pass

                            elif vermυu == '':
                              lαmdyαteν()

                            else:
                              try:
                                oppel = open('Mυuιt Vermαt.txt','a',encoding='utf8')
                                oppel.write('| ')
                                oppel.write(vermυu)
                                oppel.close()
                                lαmυuιt()
                                print()

                                sιgμe = input('Sιgμe tαudrα | ')

                                if sιgμe == '':
                                  oppel = open('Mυuιt Vermαt.txt','a',encoding='utf8')
                                  oppel.write('\n')
                                  oppel.close()

                                else:                      
                                  oppel = open('Mυuιt Vermαt.txt','a',encoding='utf8')
                                  oppel.write('>  ')
                                  oppel.write(sιgμe)
                                  oppel.write('\n')
                                  oppel.close()

                              except: pass

                        νermυu()

                      except FileNotFoundError:
                        print()
                        print("Mυuιt Vermαt αqtαgeu' ιuνor ιutrēν")
                        input()
                    
                    elif Dyαt_Imαν == 'Muntander':

                      try:
  
                        while True:
  
                          import os
                          os.system('cls' if os.name == 'nt' else 'clear')

                          import psutil
                          ιzναrtαg = psutil.sensors_battery()

                          from datetime import datetime
                          sιeνιt = datetime.now()
                          timestamp = sιeνιt.strftime('%H.%M')

                          if ιzναrtαg.power_plugged == True:
                            console.print('Mυuιtseμ Tᾱuderα [#808080]|[/#808080]',' '*123,'[#808080]|[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#808080]|[/#808080]',timestamp)

                          if ιzναrtαg.power_plugged == False:
                            console.print('Mυuιtseμ Tᾱuderα [#808080]|[/#808080]',' '*123,'[#808080]|[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#808080]|[/#808080]',timestamp)
                          
                          console.print('\u2500'*158,style='blue')
  
                          oppel = open('Mυuιtsyα.txt','r',encoding='utf8')
                          print(oppel.read())
                          oppel.close()
  
                          tαuder = input('')
  
                          if tαuder == 'º':
                            lαmdyαteν()
                            break
  
                          elif tαuder == '.lag':
                            import os
                            os.system ('Mυuιtsyα.txt')
                            lαmdyαteν()
  
                          else:
                            with open('Mυuιtsyα.txt','a',encoding='utf8') as oppel:
                              oppel.write('\n')
                              oppel.write(tαuder)
  
                      except Exception as e:
                        print()
                        print(e)
                        input()
                        pass
                    
                    elif Dyαt_Imαν == 'Aqtande':
                    
                      print()
                      
                      Sevdαl = input('Dye sevdαl uα dyαtēν αqtαudeμ | ')
                      
                      if Sevdαl == 'Dyav':
                        oppel = open('Dyαtēν.txt','a')
                        oppel.truncate(0)
                        oppel.close()
                        lαmlιuem()
                        print('Dyαtēν αqtαudeu')
                        print()
                      
                      else:
                        print()
                    
                    elif Dyαt_Imαν == 'Qampar':
                      import webbrowser
                      webbrowser.open('http://maps.google.com/')
                      lαmdyαteν()
                    
                    elif Dyαt_Imαν == 'º':
                      lαmlιuem()
                      return
                    
                    elif Dyαt_Imαν == 'verqom':
                    
                      try:
                        
                        line_number = input(': ')
                        
                        if line_number == 'º':
                          break
                        
                        if line_number == '':
                          line_number = 0
                        
                        else:
                          line_number = int(line_number)
                        
                        oppel = open('Dyαtēν.txt',encoding='utf8')
                        lines = oppel.readlines()
                        print(lines[line_number-1])
                        
                        new_line = input('> ')
                        
                        if new_line == 'º':
                          break 
                        
                        elif new_line == '':
                          break 
                        else:
                          lines[line_number-1] = new_line + '\n'
                        
                          if line_number <= len(lines):
                            oppel = open('Dyαtēν.txt','w',encoding='utf8')
                            for i in lines:
                              oppel.write(i)
                            oppel.close()
                            lαmdyαteν()
                          
                          else:
                            pass
                      
                      except ValueError:
                        pass
                    
                    elif Dyαt_Imαν == 'inaq':
                    
                      try:
                          number = input(': ')
                        
                          if number == '':
                            number = 0
                            
                          else: number = int(number)
                          
                          def ιuαqtαν(lαιue,line_number):
                            with open(lαιue,encoding='utf8') as oppel:
                              lines = oppel.readlines()
                              print(lines[line_number-1])
                              ιuαq = input('> ')                  
                              
                              if ιuαq == '.':
                                if line_number <= len(lines):
                                  del lines[line_number-1]
                                  oppel = open('Dyαtēν.txt','w',encoding='utf8')
                                  for i in lines:
                                    oppel.write(i)
                                  oppel.close()

                                else:
                                  pass
                              
                              else:
                                return
                                  
                          ιuαqtαν('Dyαtēν.txt',number)
                        
                          lαmdyαteν()
                        
                      except ValueError:
                        print()
                        print('Lαg αqtαlινeu')
                        input()
                        lαmdyαteν()
                        
                      except IndexError:
                        lαmdyαteν()
                        pass
                    
                    elif Dyαt_Imαν == 'Lag':
                      import os
                      os.system('Dyαtēν.txt')
                      lαmdyαteν()
                    
                    elif Dyαt_Imαν == 'Dyevastaq':
                      import webbrowser
                      webbrowser.open("https://calendar.google.com/calendar/u/3/r/")
                      lαmdyαteν()
                    
                    else:
                      break
                      
            Dyαtēν()           
          
          elif ιmαν == 'Angest':

            def Augestαq():
      
              def lαmαugest():
              
                import os
                os.system('cls' if os.name == 'nt' else 'clear')
                
                from datetime import datetime
                sιeνιt = datetime.now()
                timestamp = sιeνιt.strftime('%H.%M')

                import psutil
                ιzναrtαg = psutil.sensors_battery()
                
                console = Console()
                
                if ιzναrtαg.power_plugged == True:
                  print('Augestαq [#24272d]\u2502[/#24272d]',' '*131,'[#24272d]\u2502[/#24272d]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#24272d]\u2502[/#24272d]',timestamp)
                
                if ιzναrtαg.power_plugged == False:
                  print('Augestαq [#24272d]\u2502[/#24272d]',' '*131,'[#24272d]\u2502[/#24272d]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#24272d]\u2502[/#24272d]',timestamp)
                
                console.print('\u2500'*158,style='blue')
                print('[#808080]\u2502[/#808080] Sιguα [#808080]\u2502[/#808080] Iuslag [#808080]\u2502[/#808080] Mαuslαg [#808080]\u2502[/#808080] Aqtαudeμ [#808080]\u2502[/#808080] º [#808080]\u2502[/#808080]')
                console.print('\u2500'*158,style='#24272d')
                print()

                try:
                  oppel = open('Augestαq.csv',encoding='utf8')
                  print(oppel.read())
                  oppel.close()
                  console.print('\u2500'*158,style='#808080')                  

                except FileNotFoundError:
                  print("Dyαteν αqtαgeu' ιuνor ιutrēν")
                  print()
                  
              lαmαugest()

              while True:
                Aug_Imαν = input('| ')
                
                if Aug_Imαν == 'Signa':
                  def Sιguα():

                    console.print('\u2500' * 158, style='#24272d')

                    import datetime
                    sιevιt = datetime.date.today()
                    print(' '*147,sιevιt)
                    oppel = open('Augestαq.csv','a')
                    oppel.write('\n')
                    oppel.write('| ')
                    oppel.write(str(sιevιt))
                    oppel.write('\n')
                    oppel.close
                    
                    def AuSιg_Imαν():

                      while True:
                      
                        AuSιg_Imαν = input('| ')
                        
                        if AuSιg_Imαν == 'Mayeq':
                            oppel = open('Augestαq.csv','a',encoding='utf8')
                            oppel.write('\n')
                            oppel.write('\n')
                            oppel.write('Mαyeq')
                            oppel.write('\n')
                            oppel.write('\u2500'*14)
                            oppel.write('\n')
                            oppel.close()
                            print('\u2500'*8)
                            #| Delαus
                        
                            while True:
                              
                              Mαyeq_delαus = input('Delαus | ')
                              
                              if Mαyeq_delαus == '':
                                Mαyeq_delαus = '0'
                                oppel = open('Augestαq.csv','a',encoding='utf8')
                                oppel.write('Delαus | ')
                                oppel.write(Mαyeq_delαus)
                                oppel.write(' ')
                                oppel.write('ge')
                                oppel.write('\n')
                                oppel.close()
                                break
                              #elif  Mαyeq_delαus == Una letra o un símbolo:  
                              #  print("Aqledeu lαg' ιtαu αtvιαr") #Wrong entry, insertar de nuevo
                              #  print() and repeat Mαyeq Delαus
                              else:  
                                oppel = open('Augestαq.csv','a',encoding='utf8')
                                oppel.write('Delαus | ')
                                oppel.write(Mαyeq_delαus)
                                oppel.write(' ')
                                oppel.write('ge')
                                oppel.write('\n')
                                oppel.close()
                                break
                            #| Proxeu
                            while True:    
                              Mαyeq_proxeu = input('Proxeu | ')
                              if Mαyeq_proxeu == '':
                                Mαyeq_proxeu = '0'
                                oppel = open('Augestαq.csv','a',encoding='utf8')
                                oppel.write('Proxeu | ')
                                oppel.write(Mαyeq_proxeu)
                                oppel.write(' ')
                                oppel.write('ge')
                                oppel.write('\n')
                                oppel.close()
                                break
                              #| elif Letra o símbolo
                              #print()
                              #print("Aqledeu lαg' ιtαu αtvιαr") #Wrong entry, insertar de nuevo
                              else:
                                oppel = open('Augestαq.csv','a',encoding='utf8')
                                oppel.write('Proxeu | ')
                                oppel.write(Mαyeq_proxeu)
                                oppel.write(' ')
                                oppel.write('ge')
                                oppel.write('\n')
                                oppel.close()
                                break
                            #| Soleu
                            while True:
                              Mαyeq_soleu = input('Soleu  | ')
                              if Mαyeq_soleu == '':
                                Mαyeq_soleu = '0'
                                oppel = open('Augestαq.csv','a',encoding='utf8')
                                oppel.write('Soleu  | ')
                                oppel.write(Mαyeq_soleu)
                                oppel.write(' ')
                                oppel.write('ge')
                                oppel.write('\n')
                                oppel.close()
                                break
                              #| elif Letra o símbolo
                              #print()
                              #print("Aqledeu lαg' ιtαu αtvιαr") #Wrong entry, insertar de nuevo
                              else:
                                  oppel = open('Augestαq.csv','a',encoding='utf8')
                                  oppel.write('Soleu  | ')
                                  oppel.write(Mαyeq_soleu)
                                  oppel.write(' ')
                                  oppel.write('ge')
                                  oppel.write('\n')
                                  oppel.close()
                                  break
                            #| Sιguα
                            print('\u2500'*14)
                            Mαyeq_sιguα = int(Mαyeq_delαus) + int(Mαyeq_proxeu) + int(Mαyeq_soleu)
                            if Mαyeq_sιguα % 10 == 0 and Mαyeq_sιguα > 0:
                              MαsιgPαlμα = int(Mαyeq_sιguα / 10)
                              print('Sιguα  | ' + str(MαsιgPαlμα) + ' pα')
                              oppel = open('Augestαq.csv','a',encoding='utf8')
                              oppel.write('Sιguα  | ')
                              oppel.write(str(MαsιgPαlμα))
                              oppel.write(' ')
                              oppel.write('pα')
                              oppel.write('\n')
                              oppel.write('\n')
                              oppel.close()
                            else:
                              print('Sιguα  | ' + str(Mαyeq_sιguα) + ' ge')
                              oppel = open('Augestαq.csv','a',encoding='utf8')
                              oppel.write('Sιguα  | ')
                              oppel.write(str(Mαyeq_sιguα))
                              oppel.write(' ')
                              oppel.write('ge')
                              oppel.write('\n')
                              oppel.close()
                            print()
                        if AuSιg_Imαν == 'Neqen':
                          oppel = open('Augestαq.csv','a',encoding='utf8')
                          oppel.write('\n')
                          oppel.write('\n')
                          oppel.write('Neqeu')
                          oppel.write('\n')
                          oppel.write('\u2500'*14)
                          oppel.write('\n')
                          oppel.close()
                          print('\u2500' * 8)
                          #| Delαus
                          while True:
                            Neqeu_delαus = input('Delαus | ')
                            if Neqeu_delαus == '':
                              Neqeu_delαus = '0'
                              oppel = open('Augestαq.csv','a',encoding='utf8')
                              oppel.write('Delαus | ')
                              oppel.write(Neqeu_delαus)
                              oppel.write(' ')
                              oppel.write('ge')
                              oppel.write('\n')
                              oppel.close()
                              break
                            #elif  Neqeu_delαus == Una letra o un símbolo:  
                            #  print("Aqledeu lαg' ιtαu αtvιαr") #Wrong entry, insertar de nuevo
                            #  print() and repeat Neqeu Delαus
                            else:
                              oppel = open('Augestαq.csv','a',encoding='utf8')
                              oppel.write('Delαus | ')
                              oppel.write(Neqeu_delαus)
                              oppel.write(' ')
                              oppel.write('ge')
                              oppel.write('\n')
                              oppel.close()
                              break
                          #| Dαuqαδ
                          while True:  
                            Neqeu_dαuqαδ = input('Dαuqαδ | ')
                            if Neqeu_dαuqαδ == '':
                              Neqeu_dαuqαδ = '0'
                              oppel = open('Augestαq.csv','a',encoding='utf8')
                              oppel.write('Dαuqαδ | ')
                              oppel.write(Neqeu_dαuqαδ)
                              oppel.write(' ')
                              oppel.write('ge')
                              oppel.write('\n')
                              oppel.close()
                              break
                            #| elif Símbolo o letra
                            else:
                              oppel = open('Augestαq.csv','a',encoding='utf8')
                              oppel.write('Dαuqαδ | ')
                              oppel.write(Neqeu_dαuqαδ)
                              oppel.write(' ')
                              oppel.write('ge')
                              oppel.write('\n')
                              oppel.close()
                              break
                          #| Soleu
                          while True:
                            Neqeu_soleu = input('Soleu  | ')
                            if Neqeu_soleu == '':
                              Neqeu_soleu = '0'
                              oppel = open('Augestαq.csv','a',encoding='utf8')
                              oppel.write('Soleu  | ')
                              oppel.write(Neqeu_soleu)
                              oppel.write(' ')
                              oppel.write('ge')
                              oppel.write('\n')
                              oppel.close()
                              break
                            #| elif Símbolo o letra
                            else:
                              oppel = open('Augestαq.csv','a',encoding='utf8')
                              oppel.write('Soleu  | ')
                              oppel.write(Neqeu_soleu)
                              oppel.write(' ')
                              oppel.write('ge')
                              oppel.write('\n')
                              oppel.close()
                              break
                          #| Sιguα
                          print('\u2500'*15)
                          Neqeu_sιguα = int(Neqeu_delαus) + int(Neqeu_dαuqαδ) + int(Neqeu_soleu)
                          if Neqeu_sιguα % 10 == 0 and Neqeu_sιguα > 0:
                            NesιgPαlμα = int(Neqeu_sιguα / 10)
                            print('Sιguα  | ' + str(NesιgPαlμα) + ' pα')
                            oppel = open('Augestαq.csv','a',encoding='utf8')
                            oppel.write('Sιguα  | ')
                            oppel.write(str(Neqeu_sιguα))
                            oppel.write(' ')
                            oppel.write('pα')
                            oppel.write('\n')
                            oppel.write('\n')
                            oppel.close()
                            print()
                          else:
                            print('Sιguα  | '+ str(Neqeu_sιguα) + ' ge')
                            oppel = open('Augestαq.csv','a',encoding='utf8')
                            oppel.write('Sιguα  | ')
                            oppel.write(str(Neqeu_sιguα))
                            oppel.write(' ')
                            oppel.write('ge')
                            oppel.write('\n')
                            oppel.write('\n')
                            oppel.close()
                            print()
                        if AuSιg_Imαν == 'Sighe':
                          print()
                          Sιgμe = int(Mαyeq_sιguα) + int(Neqeu_sιguα)
                          if Sιgμe % 10 == 0 and Sιgμe > 0:
                            Pαlμα = int(Sιgμe / 10)
                            print('Sιgμe  | ' + str(Pαlμα) + ' pα')
                          else:
                            print('Sιgμe  | ' + str(Sιgμe) + ' ge')
                          print()
                        if AuSιg_Imαν == 'Anqopt':
                          print()
                          Auqopt = input('Aδqαιt | ')
                          if Auqopt == '':
                            Auqopt = '0'
                            oppel = open('Augestαq.csv','a',encoding='utf8')
                            oppel.write('Auqopt | ')
                            oppel.write(str(Auqopt))
                            oppel.write(' ')
                            oppel.write('ge')
                            oppel.write('\n')
                            oppel.write('\n')
                            oppel.close()
                            print()
                          elif int(Auqopt) % 10 == 0:
                            AuqPαlμα = int(Auqopt / 10)
                            # print('Auqopt | ' + str(AuqPαlμα) + ' pα')
                            oppel = open('Augestαq.csv','a',encoding='utf8')
                            oppel.write('Auqopt | ')
                            oppel.write(str(Auqopt))
                            oppel.write(' ')
                            oppel.write('pα')
                            oppel.write('\n')
                            oppel.write('\n')
                            oppel.close()
                            print()
                          else:
                            # print('Auqopt  | '+ str(Auqopt) + ' ge')
                            oppel = open('Augestαq.csv','a',encoding='utf8')
                            oppel.write('Auqopt | ')
                            oppel.write(str(Auqopt))
                            oppel.write(' ')
                            oppel.write('ge')
                            oppel.write('\n')
                            oppel.write('\n')
                            oppel.close()
                            print()
                        if AuSιg_Imαν == 'Nothest':
                          print()
                          Notμestαq = int(Mαyeq_sιguα) + int(Neqeu_sιguα) + int(Auqopt)
                          if Notμestαq % 10 == 0 and Notμestαq > 0:
                            NotμPαlμα = int(Notμestαq / 10)
                            print('Notμest| ' + str(NotμPαlμα) + ' pα')
                            oppel = open('Augestαq.csv','a',encoding='utf8')
                            oppel.write('Notμest| ')
                            oppel.write(str(NotμPαlμα))
                            oppel.write(' ')
                            oppel.write('pα')
                            oppel.write('\n')
                            oppel.close()
                          else:
                            print('Notμest| ' + str(Notμestαq) + ' ge')
                            oppel = open('Augestαq.csv','a',encoding='utf8')
                            oppel.write('Notμest| ')
                            oppel.write(str(Notμestαq))
                            oppel.write(' ')
                            oppel.write('ge')
                            oppel.write('\n')
                            oppel.close()
                          print()
                        #δινeu command ιuverqom
                        if AuSιg_Imαν == 'º':
                          oppel = open('Augestαq.csv','a',encoding='utf8')
                          oppel.write('\n')
                          oppel.write('\n')
                          oppel.close()
                          lαmαugest()
                          break
                    AuSιg_Imαν()
                  Sιguα()
                
                elif Aug_Imαν == 'Aqtande':
                  print()
                  Sevdαl = input('Dye sevdαl uα oppel αqtαudeμ | ')
                  if Sevdαl == 'Dyav':
                    oppel = open('Augestαq.csv','a')
                    oppel.truncate(0)
                    oppel.close()
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Augestαq')
                    print('\u2500'*158)
                    print('Estαq αqtαudeu')
                    input()
                  else:
                    print()
                
                elif Aug_Imαν == 'Manslag':
                  import os
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print('Augestαq \u2502 Mαuslαg \u2502')
                  print('\u2500'*158)
                  oppel = open('Augest.Mαuslαg.txt',encoding='utf8')
                  print(oppel.read())
                  input()
                  lαmαugest()
                
                elif Aug_Imαν == 'Inslag':
                  try:
                    import os
                    os.system("Augestαq.csv")
                  except Exception as e:
                    print()
                    print('Augestαq αqδαι')
                    print(e)
                    input()
                  lαmαugest()
                
                elif Aug_Imαν == 'Isqyan':
                  import os
                  os.system('Augest.Isqyαu.txt')
                  lαmαugest()
                
                elif Aug_Imαν == 'º':
                  lαmlιuem()
                  break
                
                else:
                  lαmαugest()

            Augestαq()

          elif ιmαν == 'Munit':
            
            def Mυuιtsyα():
              
              def lαmυuιt():
                import os
                os.system ('cls' if os.name == 'nt' else 'clear')
                
                from datetime import datetime
                sιeνιt = datetime.now()
                timestamp = sιeνιt.strftime('%H.%M')

                import psutil
                ιzναrtαg = psutil.sensors_battery()
                
                console = Console()

                if ιzναrtαg.power_plugged == True:
                  print('Mυuιtsyα [#808080]\u2502[/#808080]',' '*131,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#808080]\u2502[/#808080]',timestamp)

                if ιzναrtαg.power_plugged == False:
                  print('Mυuιtsyα [#808080]\u2502[/#808080]',' '*131,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#808080]\u2502[/#808080]',timestamp)
                
                console.print('\u2500'*158,style='blue')
                console.print('[#808080]|[/#808080] Sιguα [#808080]|[/#808080] Vermαt [#808080]|[/#808080] Teνuα [#808080]|[/#808080] Verqom [#808080]|[/#808080] Tαuder [#808080]|[/#808080] Iuαq [#808080]|[/#808080] º [#808080]|[/#808080]')
                console.print('\u2500'*158,style='#24272d')
                print()
                
                try:
                
                  import pandas as pd
                  import numpy as np
                  import csv
                  datos = pd.read_csv('Mυuιmα Stαgeu.csv',encoding='utf8',sep='\t')
                  data = pd.DataFrame(datos)
                  #rows = data.iloc[1]
                  #hide = ['TOREG']
                  #table = data.style\
                  #  .hide([col for col in data.columns if col in hide],axis=1)\
                  #  .hide(axis=0)
                  print(data.to_string(index=False))
                  print()
                
                except FileNotFoundError:
                  print('Mυuιmα Stαgeu αqtαgeu')
                  print()
                
                except Exception as e:
                  print(e)
                  print()
                  
              lαmυuιt()
              
              while True:
              
                console = Console()
              
                console.print('\u2500'*158, style='#808080')
                
                Mυu_Imαν = input('| ')
                #| Mυuιm terιgμe
                #| Mυuιm lαgreuα
                
                if Mυu_Imαν == '.loyeh':
                  try:
                
                    #import pandas as pd
                    import numpy as np
                    import csv
                    #datos = pd.read_csv('Mυuιmα Stαgeu.csv',encoding='utf8',sep='\t',quoting=3)

                    conn = sq.connect('Lιuem.sqlite')
                    c = conn.cursor()
                    #c.execute("create table mυuιmα (Lαιu text, Auemαt text, Sιeν int, Toreg text)")
                    #params = (lαιu,αuemαt,sιeνιt,toreg)
                    #c.execute(f"insert into mυuιmα values (?,?,?,?)",params)
                    #conn.commit()
                    c.execute("select * from mυuιmα")
                    table = c.fetchone()
                    print()
                    for i in table:
                      if table[3] == 'Loyeμ':
                        print(table[0],table[1],table[2])
                      
                      else:
                        pass

                    conn.close()
                    input()
                  
                    print()
                
                  except FileNotFoundError:
                    print('Mυuιmα Stαgeu αqtαgeu')
                    print()
                    input()
                
                  except Exception as e:
                    print(e)
                    print()
                    input()                

                if Mυu_Imαν == 'Signa':
                  print('\u2500'*7)
                
                  def Mυuιm_Sιguα():
                    toreg= input('Toreg  | ')
                    lαιu = input('Lαιu   | ')
                    αuemαt = input('Auemαt | ')
                    #def αuemαt():
                     # print()
                    sιeνιt = 0
                  
                    def sιeνιt():
                    
                      while True:
                        nonlocal sιeνιt
                        sιeνιt = input('Sιeνιt | ')
                        if sιeνιt == '4.4':
                          s44 = [1,1.5,2,2.5,3,3.5,4,4.5]
                          print('S44 '+ f'{s44[0:8:2]}')
                          input()
                          break
                        elif sιeνιt == '3.4':
                          s34 = [1,1.5,2,2.5,3,3.5]
                          print('S34 '+ f'{s34[0:6:2]}')
                          input()
                          break
                        elif sιeνιt == '6.8':
                          s68 = [1,2,3,4,5,6]
                          print('S68 '+ f'{s68[0:6]}')
                          input()
                          break
                        else:
                          print()
                          print('Aqtαlινeu Sιeνιt')
                          input()
                    sιeνιt()
                      #Crear menú de géneros según la métrica
                    #νresuα = input('Vresuα | ')
                    '''MυuEstαq = []
                    Intro = []
                    Estrofa = []
                    Coro = []
                    Puente = []
                    Outro = []
                    ιdeu = []'''
                    class Mυuιt:
                      def __init__(ιzeu,lαιu,sιeνιt,αuemαt,toreg): #MυuEstαq,Intro,Estrofa,Coro,Puente,Outro,ιdeu):
                        ιzeu.lαιu = lαιu
                        ιzeu.sιeνιt = sιeνιt
                        ιzeu.αuemαt = αuemαt
                        ιzeu.toreg = toreg
                        '''ιzeu.MυuEstαq = MυuEstαq
                        ιzeu.Intro = Intro
                        ιzeu.Estrofa = Estrofa
                        ιzeu.Coro = Coro
                        ιzeu.Puente = Puente
                        ιzeu.Outro = Outro
                        ιzeu.ιdeu = ιdeu'''
                    Mυuιt = Mυuιt(lαιu,sιeνιt,αuemαt,toreg) #MυuEstαq,Intro,Estrofa,Coro,Puente,Outro,ιdeu)
                    MυuTαudrα = [Mυuιt.lαιu,Mυuιt.αuemαt,Mυuιt.sιeνιt,Mυuιt.toreg]

                    def MυuEstαq():
                      import csv
                      '''import os
                      os.system('cls' if os.name == 'nt' else 'clear')
                      print('Mυuιtsyα Stαuνor \u2502 Sιguα \u2502')
                      print('\u2500'*158)
                      print('| Lαιu: ',Mυuιt.lαιu,' '*20,'| Auemαt: ',Mυuιt.αuemαt,' '*20,'| Sιeνιt: ',Mυuιt.sιeνιt,' '*20,'| Vresuα: ',Mυuιt.νresuα)
                      print('\u2500'*158)
                      print()'''
                      
                      oppel = open('Mυuιmα Stαgeu.csv','a',encoding='utf8', newline='')
                      writer= csv.writer(oppel, delimiter='\t', quoting=csv.QUOTE_NONE)
                      writer.writerow(MυuTαudrα)
                      oppel.close()
                      

                      '''conn = sq.connect('Lιuem.sqlite')
                      c = conn.cursor()
                      #c.execute("create table mυuιmα (Lαιu text, Auemαt text, Sιeν int, Toreg text)")
                      params = (lαιu,αuemαt,sιeνιt,toreg)
                      c.execute("insert into mυuιmα values (?,?,?,?)",params)
                      conn.commit()
                      c.execute('select * from mυuιmα')
                      table = c.fetchall()
                      print()
                      for i in table:
                        print(table[0],table[1],table[2])
                      conn.close()
                      input()'''

                      def dyantal():
                        pass
                        '''MυuEstαq = []
                        while True:
                          Mυuιdeu = (input('| '))
                          if Mυuιdeu == 'Intro':
                            MυuEstαq.append(Mυuιdeu)
                            Intro = []
                            while True:
                              IntSteuα = (input('| '))
                              if IntSteuα == '':
                                print()
                                print(Intro)                        
                                break
                              else:
                                Intro.append(IntSteuα)
                            #Agregar acordes de Intro a Mυuιmα Stαgeu.csv
                            input()
                          elif Mυuιdeu == 'Estrofa':
                            MυuEstαq.append(Mυuιdeu)
                            Estrofa = []
                            while True:
                              EstSteuα = (input('| '))
                              if EstSteuα == '':
                                print()
                                print(Estrofa)
                                break
                              else:
                                Estrofa.append(EstSteuα)
                            input()
                          elif Mυuιdeu == 'Coro':
                            MυuEstαq.append(Mυuιdeu)
                            Coro = []
                            while True:
                              CorSteuα = (input('| '))
                              if CorSteuα == '':
                                print()
                                print(Coro)
                                break
                              else:
                                Coro.append(CorSteuα)
                            input()
                          elif Mυuιdeu == 'Puente':
                            MυuEstαq.append(Mυuιdeu)
                            Puente = []
                            while True:
                              PueSteuα = (input('| '))
                              if PueSteuα == '':
                                print()
                                print(Puente)
                                break
                              else:
                                Puente.append(PueSteuα)
                            input()
                          elif Mυuιdeu == 'Outro':
                            MυuEstαq.append(Mυuιdeu)
                            Outro = []
                            while True:
                              OutSteuα = (input('| '))
                              if OutSteuα == '':
                                print()
                                print(Outro)
                                break
                              else:
                                Outro.append(OutSteuα)
                            input()
                          elif Mυuιdeu == '':
                            oppel = open('Mυuιmα Stαgeu.csv','a',encoding='utf8')
                            oppel.write('\n')
                            oppel.close()
                            print()
                            break
                          else:
                            MυuEstαq.append(Mυuιdeu)
                            ιdeu = []
                            while True:
                              ιdeuSteuα = (input('| '))
                              if ιdeuSteuα == '':
                                print()
                                print(ιdeu)
                                break
                              else:
                                ιdeu.append(ιdeuSteuα)
                                print(ιdeu)
                            input()                   
                        print(MυuEstαq)'''
                    MυuEstαq()
                    #Mυusteuαδqαιt = ['do','do+','re','mi-','mi','fa','fa+','sol','la-','la','si-','si']
                    #Mυusteuα = [1,2,3,4,5,6,7]
                    #seutα = [1,2,4,8]
                    #print(seutα[1]+seutα[2])
                    #input()
                    #print('\u2500'*158)
                    lαmυuιt()
                    return
                  Mυuιm_Sιguα()
                
                #| Mυuιm lαmeδuα
                
                elif Mυu_Imαν == 'Vermat':
                  try:
                    def νermυu():
                      
                      while True:
                        
                        def lαmνermυuιt():
                          oppel = open('Mυuιt Vermαt.txt','r',encoding='utf8')
                          
                          lαmυuιt()

                          console.print('\u2500'*158,style= '#24272d')
                          print('Vermαt [#808080]|[/#808080]\n')
                          print(oppel.read())
                          console.print('[#808080]\u2500[/#808080]'*158)
                          
                        lαmνermυuιt()
                      
                        vermυu = input('| ')
                      
                        if vermυu == 'º':
                          lαmυuιt()
                          break
                        
                        elif vermυu == 'inaq':
                          
                          try:
                            number = input(': ')
                            
                            if number == 'º':
                              lαmυuιt()
                              break
                            
                            if number == '':
                              number = 0
                            
                            else: number = int(number)
                            
                            def ιuαqtαν(lαιue,line_number):
                            
                              with open(lαιue,encoding='utf8') as oppel:
                                lines = oppel.readlines()
                                print(lines  [line_number-1])
                                ιuαq = input('> ')
                                
                                if ιuαq == '.':
                                  if line_number <= len(lines):
                                    del lines[line_number-1]
                                    oppel = open('Mυuιt Vermαt.txt','w',encoding='utf8')
  
                                    for i in lines:
                                      oppel.write(i)
                                    oppel.close()
  
                                  else:
                                    pass
                                  
                                else:
                                  pass
  
                                    
                            ιuαqtαν('Mυuιt Vermαt.txt',number)
  
                            lαmνermυuιt()
                            
                          except ValueError:
                            print()
                            print('Lαg αqtαlινeu')
                            input()
                            
                          except IndexError:
                            lαmνermυuιt()
                            pass
                        
                        elif vermυu == '':
                          lαmνermυuιt()
                        
                        else:
                          try:
                            oppel = open('Mυuιt Vermαt.txt','a',encoding='utf8')
                            oppel.write('| ')
                            oppel.write(vermυu)
                            oppel.close()
                            print()
  
                            sιgμe = input('Sιgμe tαudrα | ')
  
                            if sιgμe == '':
                              oppel = open('Mυuιt Vermαt.txt','a',encoding='utf8')
                              oppel.write('\n')
                              oppel.close()
  
                            else:                      
                              oppel = open('Mυuιt Vermαt.txt','a',encoding='utf8')
                              oppel.write('>  ')
                              oppel.write(sιgμe)
                              oppel.write('\n')
                              oppel.close()
  
                          except: pass
                    
                    νermυu()
                    
                  except FileNotFoundError:
                    print()
                    print("Mυuιt Vermαt αqtαgeu' ιuνor ιutrēν")
                    input()      
                
                elif Mυu_Imαν == 'Tevna':
                  import os
                  os.system ('cls' if os.name == 'nt' else 'clear')
                  print('Mυuιtsya \u2502 Teνuα \u2502')
                  print('\u2500'*158)
                  oppel = open('Mυuιtsyα Teνuα.txt','r',encoding='utf8')
                  print(oppel.read())
                  input()
                  lαmυuιt()
                
                elif Mυu_Imαν == 'Tander':

                  try:
                    
                    while True:
                      
                      lαmυuιt()

                      console.print('\u2500'*158,style='#24272d')
                      print()
                      
                      oppel = open('Mυuιtsyα.txt','r',encoding='utf8')
                      print(oppel.read())
                      oppel.close()
                    
                      tαuder = input('')

                      if tαuder == 'º':
                        lαmυuιt()
                        break

                      elif tαuder == '.lag':
                        import os
                        os.system ('Mυuιtsyα.txt')
                        lαmυuιt()

                      else:
                        with open('Mυuιtsyα.txt','a',encoding='utf8') as oppel:
                          oppel.write('\n')
                          oppel.write(tαuder)

                  except Exception as e:
                    print()
                    print(e)
                    input()
                    pass
                
                elif Mυu_Imαν == 'verqom':
                  print('\nIuvorδeus ιmαseut')
                  input()
                  lαmυuιt()
                  pass
                  '''def νerqom():
                    try:
                      line_number = input('| ')
                      if line_number == 'º':
                        lαmυuιt()
                        return
                      elif line_number == '':
                        line_number = 0
                      else: line_number = int(line_number)
                      lαmυuιt()
                      print('\u2500'*158)
                      with open('Mυuιmα Stαgeu.csv',encoding='utf8') as oppel:
                        lines = oppel.readlines()
                        print(lines[line_number-1])            
                      new_line = '| '+input('| ')
                      if new_line == 'º':
                        lαmυuιt()                       
                        return
                      else:
                          lines[line_number-1] = new_line + '\n'
                          oppel = open('Mυuιmα Stαgeu.csv','w',encoding='utf8')
                          oppel.truncate(0)
                          for i in lines:
                            oppel = open('Mυuιmα Stαgeu.csv','a',encoding='utf8')
                            oppel.write(i)
                            oppel.close()            
                    except IndexError:
                      pass
                  νerqom()'''
                
                elif Mυu_Imαν == 'Terigner':
                  import subprocess
                  subprocess.Popen(r'"C:\ProgramData\Ableton\Live 10 Suite\Program\Ableton Live 10 Suite.exe"')
                  lαmυuιt()
                                  
                elif Mυu_Imαν == 'inaq':
                  def ιuαq():
                    try:
                      number = input(': ')
                      if number == 'º':
                        lαmυuιt()
                        return
                      if number == '':
                        number = -2
                      else: number = int(number)
                      def ιuαqtαν(lαιue,line_number):
                        with open(lαιue,encoding='utf8') as oppel:
                          lines = oppel.readlines()
                          print(lines[line_number+1])
                          ιuαq = input('> ')                  
                          if ιuαq == '.':
                            if line_number <= len(lines):
                              del lines[line_number+1]
                              oppel = open('Mυuιmα Stαgeu.csv','w',encoding='utf8')
                              for i in lines:
                                oppel.write(i)
                              oppel.close()
                              lαmυuιt()
                            else:
                              pass
                          else:
                            lαmυuιt()
                            return
                      ιuαqtαν('Mυuιmα Stαgeu.csv',number)
                    except ValueError:
                      print()
                      print('Lαg αqtαlινeu')
                      input()
                    except IndexError:
                      pass
                  ιuαq()

                elif Mυu_Imαν == 'º':
                  lαmlιuem()
                  return
                
                else:
                  lαmυuιt()
            
            Mυuιtsyα()  
          
          elif ιmαν == 'Viaret':
            
            def lαmνιαret():
              
              import os
              os.system('cls' if os.name == 'nt' else 'clear')

              import psutil
              ιzναrtαg = psutil.sensors_battery()
              
              from datetime import datetime
              sιeνιt = datetime.now()
              timestamp = sιeνιt.strftime('%H.%M')
              
              console = Console()

              if ιzναrtαg.power_plugged == True:
                console.print('Vιαret [#808080]\u2502[/#808080]',' '*133,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#808080]\u2502[/#808080]',timestamp)

              if ιzναrtαg.power_plugged == False:
                console.print('Vιαret [#808080]\u2502[/#808080]',' '*133,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#808080]\u2502[/#808080]',timestamp)

              console.print('\u2500'*158,style='blue')

              
              from rich.table import Table
              
              table = Table(show_header=False)
              table.add_column()
              table.add_column()
              table.add_column()  
              table.add_row()
              table.add_row('    LIMERSAT','    VORSAL','    SONNAL',style='purple')
              table.add_row()
              table.add_row()
              table.add_row('      Autαlιgμe','      Aνdαsιgμe','      Eleνeutα',style='yellow')
              table.add_row('         Medιtαt                    [green]5m[/green]         ','         Izeu qommet                    [green]15m[/green]         ','         Mυδeuι                    [green]10m[/green]          ')
              table.add_row('         Mυδeuι                    [green]30m[/green]','         · δαιm                         [green]10m[/green]','         Izeu lαmυν                [green]10m[/green]')
              table.add_row('         Lιutrα qommet             ','         · Amυseu                        [green]5m[/green]')
              table.add_row('         · Cama                     [green]5m[/green]','         Aνdαsιg Teνuα                   [green]5m[/green]','      [yellow]Lαmqommet[/yellow]                     ')
              table.add_row('         · Diván y armario         [green]20m[/green]','','        .Izeu Toreg')
              table.add_row('         Delαδ','      [yellow]Mυuιtsyα[/yellow]','        .Aδqαιt Toreg')
              table.add_row('','         Tᾱuderα','        .Mυuιtsyα Toreg')
              table.add_row('      [yellow]Relαιgμe[/yellow]                                 ','          [blue].Dyαteν[/blue]                        [green]3h[/green]','        .Aδqαιt Teνuα')
              table.add_row('        .Vιαret','          [blue].Mυuιt Tαuder[/blue]','         Amυser lαmυν')
              table.add_row('        .Vermαt','          [blue].Mυuιt Vermαt[/blue] '  ,'')
              table.add_row('        .Mαtιν  ','         Mαuδαι                              ','      [yellow]Jornada de carga[/yellow]')
              table.add_row('        .Mυuιtsyα','          [blue].Mυuιt Vermαt[/blue]','        · Móvil')
              table.add_row('        .Dyαteν','          [blue].Mυuιt Tαuder[/blue]','        · PC')
              table.add_row('','          [blue].Mυuιtsyα[/blue]','        · Tablet')
              table.add_row('','         Adeuuα','        · Audífonos')
              table.add_row('','          [blue].Mυuιtsyα Toreg[/blue]','        · Pilas')
              table.add_row('','          [blue].Nιtsem Toreg[/blue]','        · Rasuradora')
              table.add_row('','         Dyαteν','        · Parlante')
              table.add_row('','          [blue].Loyeμ Teνuα[/blue]','        · Cargadores portátiles')
              table.add_row('','          [blue].Loyeμ Vermαt[/blue]')
              table.add_row()
              console = Console()
              console.print(table)
            lαmνιαret()
            
            while True:
              
              νιαret = input('| ')
              
              if νιαret == 'º':
                lαmlιuem()
                break
              
              elif νιαret == 'inslag':
                import os
                os.system("Vιαret.txt")
              
              elif νιαret == 'ashqait':
                print('\u2500'*158)
                oppel = open('Teνuα Aδqαιt.txt','r',encoding='utf8')
                print(oppel.read())
                oppel.close()
              
              elif νιαret == 'tevna':
                oppel = open('Teνuα.txt','r',encoding='utf8')
                print(oppel.read())
              
              elif νιαret == 'munit':
                #print('Teνuα | Mυuιtsyα')
                print('\u2500'*158)
                oppel = open('Mυuιtsyα Teνuα.txt','r',encoding='utf8')
                print(oppel.read())
                oppel.close()
              
              elif νιαret == '.':
                lαmνιαret()
              
              elif νιαret == 'sval':
                lαmνιαret()
                print('| Aδqαιt | Nιseu | Mυuιtsyα | [blue]Lαm[/blue] | [yellow]Sναl[/yellow] | [red]º[/red] |')
              
              else:
                pass
            
            lαmlιuem()
          
          elif ιmαν == 'Tander':
           
            try:
              def tαuder():
                while True:
                
                  def lαmtαuder():
                  
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')

                    from datetime import datetime
                    sιevιt = datetime.now()
                    timestamp = sιevιt.strftime('%H.%M')

                    import psutil
                    ιzναrtαg = psutil.sensors_battery()
                    
                    if ιzναrtαg.power_plugged == True:
                      print('Tαuder [#808080]|[/#808080]',' '*133,'[#808080]|[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#808080]|[/#808080]',timestamp)

                    if ιzναrtαg.power_plugged == False:
                      print('Tαuder [#808080]|[/#808080]',' '*133,'[#808080]|[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#808080]|[/#808080]',timestamp)

                    console.print('\u2500'*158,style='blue')

                    with open('Tαuder.txt', 'r', encoding='utf8') as oppel:
                      print(oppel.read())

                  lαmtαuder()

                  tαuder = input('')

                  if tαuder == 'º':
                    lαmlιuem()
                    return
                  
                  elif tαuder == '.lag':
                    import os
                    os.system('Tαuder.txt')

                  else:
                    with open('Tαuder.txt', 'a', encoding='utf8') as oppel:
                      oppel.write('\n')
                      oppel.write(tαuder)                      
                
              tαuder()
            
            except Exception as e:
              print()
              print(e)
              print()
          
          elif ιmαν == 'Qampar':
            while True:
              def lαmqαmpαr():
                import os
                os.system('cls' if os.name == 'nt' else 'clear')
                from datetime import datetime
                sιeνιt = datetime.now()
                timestamp = sιeνιt.strftime('%H.%M')
                print('Qαmpαr \u2502',' '*141,timestamp)
                print('\u2500'*158)
                oppel = open('Qαmpαr.txt','r',encoding='utf8')
                print(oppel.read())
                oppel.close
                print()
                print('\u2500'*158)
              lαmqαmpαr()
              qαmpαr = input('| ')
              if qαmpαr == 'º':
                break
              if qαmpαr == 'inslag':
                import os
                os.system("Qαmpαr.txt")
                input()
              else:
                pass
            lαmlιuem()
          
          elif ιmαν == 'Linem':
            # Corregir
            try:
              print('\nVorδαm Logreuα')
              r'''import subprocess
              subprocess.Popen(r"py C:\Users\Leane\OneDrive\Escritorio\Lιuem\main.py",encoding='utf8')'''
              input()
              lαmlιuem()
            except Exception as e:
              print()
              print('Aqtαlιν uα Lιuem eutlιg')
              print()
              print(e)
              input()
              lαmlιuem()
          
          elif ιmαν == '.olyav':
            import os
            os.system('start . command')
            print()
          
          elif ιmαν == 'Sedge':      
            import subprocess
            subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
            lαmlιuem()
          
          elif ιmαν == 'Musselaith':
            def Mυsselαιtμ():
              while True:
                def lαmυsselαιtμ():
                  
                  import os
                  os.system('cls' if os.name == 'nt' else 'clear')
                  
                  from datetime import datetime
                  sιeνιt = datetime.now()
                  timestamp = sιeνιt.strftime('%H.%M')

                  import psutil
                  ιzναrtαg = psutil.sensors_battery()

                  if ιzναrtαg.power_plugged == True:
                    console.print('Mυsselαιtμ Stαuνor [#808080]\u2502[/#808080]',' '*122,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]''[#808080]\u2502[/#808080]',timestamp)

                  if ιzναrtαg.power_plugged == False:
                    console.print('Mυsselαιtμ Stαuνor [#808080]\u2502[/#808080]',' '*122,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]''[#808080]\u2502[/#808080]',timestamp)
                    
                  console.print('\u2500'*158,style='blue')
                  print()
                  
                  oppel = open('Mυsselαιtμ.txt','r',encoding='utf8')
                  print(oppel.read())
                  oppel.close()
                lαmυsselαιtμ()   
                
                eudel = input('')
                
                if eudel == 'º':
                  lαmlιuem()
                  break
                
                elif eudel == '.ashqait':            
                  import webbrowser
                  webbrowser.open_new("https://docs.google.com/document/d/1NpckpNsTxjMBEVLm1tuL8Pk_WtmoqTCB/edit?usp=drive_link&ouid=108288437121185589927&rtpof=true&sd=true")
                
                elif eudel == '.inaq':
                  
                  def ιuαq():
                    try:
                      number = input('> ')
                      if number == '':
                        number = 0
                  
                      else: number = int(number)
                      
                      def ιuαqtαν(lαιue,line_number):
                        with open(lαιue,encoding='utf8') as oppel:
                          lines = oppel.readlines()
                          print(lines[line_number-1])
                          
                          ιuαq = input('> ')       
                          
                          if ιuαq == 'º':
                            return
                            
                          else:
                            if line_number <= len(lines):
                              del lines[line_number-1]
                              oppel = open('Mυsselαιtμ.txt','w',encoding='utf8')
                              for i in lines:
                                oppel.write(i)
                              oppel.close()
                            else:
                              pass
                              
                      ιuαqtαν('Mυsselαιtμ.txt',number)
                      
                    except ValueError:
                      print()
                      print('Lαg αqtαlινeu')
                      input()
                    except IndexError:
                      pass
                  ιuαq()
                  # Editar cualquier línea..

                elif eudel == '.lag':
                  import os
                  os.system('Mυsselαιtμ.txt')
                
                else:
                    with open('Mυsselαιtμ.txt','a',encoding='utf8') as oppel:
                      oppel.write('\n')
                      oppel.write(eudel)
                      
              lαmlιuem()
            Mυsselαιtμ()
          
          elif ιmαν == '.inslag':
            import subprocess
            subprocess.Popen(r'"C:\Users\Leane\AppData\Local\Programs\Microsoft VS Code\Code.exe"')
            input()
            lαmlιuem()
          
          elif ιmαν == 'Linem 2':
            import webbrowser
            webbrowser.open_new('https://drive.google.com/drive/u/3/my-drive')
            lαmlιuem()
          
          elif ιmαν == 'Stanvor':
            import webbrowser
            webbrowser.open_new('https://www.notion.so/St-u-or-f690a8f6cd2344d1802fbdc826ea71cd')
            lαmlιuem()

          elif ιmαν == 'DOS':
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            
            import os
            os.system('cmd')
            lαmlιuem()
                                
          elif ιmαν == 'Livsen':
            import os
            os.system('"C:\Games\Cities - Skylines\Cities.exe"')
            lαmlιuem()

          elif ιmαν == 'Logat':
            from curses import wrapper

            def main(stdscr):

              #self.curses_windows['sιeνιt'] = curses.newwin(1, 6, 0, 150)
              #key = prompt.getch()
              #class curses.textpad.Textbox(prompt)
              #stdscr.border()

              #if key == 'º':
              #  return
              #else:
              #  pass

              curses.curs_set(False)

              stdscr.nodelay(True)

              y , x = stdscr.getmaxyx()

              #sιeν = curses.newwin(1,6,0,152)
              #prompt = curses.newwin(20, 20, 2, 2)
              
              curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
              curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
              curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
              curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

              def lαm():
                stdscr.clear()
                stdscr.addstr('Lιuem')
                stdscr.addstr(0, x-8, '\u2502', curses.color_pair(2))
                stdscr.addstr(0, x-15, '\u2502', curses.color_pair(2))
                stdscr.addstr(1,0,'\u2500'*x, curses.color_pair(1))
                stdscr.addstr(2,0,'| ')
              lαm()

              ιmαν = ''
              
              while 1:
                import time
              
                import psutil
                battery = psutil.sensors_battery()
                stdscr.addstr(0, x-13, f'{battery.percent}')

                if battery.power_plugged == True:
                  stdscr.addstr(0, x-10, '·', curses.color_pair(3))                
                
                else:
                  stdscr.addstr(0, x-10, '·', curses.color_pair(4))     

                from datetime import datetime
                sιevιt = datetime.now()
                timestamp = sιevιt.strftime('%H.%M')

                stdscr.addstr(0, x-6, timestamp)

                stdscr.addstr(2,2,ιmαν)

                key = stdscr.getch(2,2)

                if key == 27 or key == ord('º'):
                  break

                elif key  == 10:

                  if ιmαν == 'Vermat':
                   
                    curses.endwin()

                    def Vermαt():

                      while True:
                        
                        def lαmνermαt():
                          import psutil
                          ιzναrtαg = psutil.sensors_battery()
                          
                          import os
                          os.system('cls' if os.name == 'nt' else 'clear')
                          
                          from datetime import datetime
                          sιeνιt = datetime.now()
                          timestamp = sιeνιt.strftime('%H.%M')
                          os.system ('cls' if os.name == 'nt' else 'clear')                                  


                          if ιzναrtαg.power_plugged == True:
                            print('Vermαt [#808080]\u2502[/#808080]',' '*133,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#808080]\u2502[/#808080]',timestamp)

                          if ιzναrtαg.power_plugged == False:
                            print('Vermαt [#808080]\u2502[/#808080]',' '*133,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#808080]\u2502[/#808080]',timestamp)
                          
                          console.print('\u2500'*158,style='blue')                  
                          print('[#808080]\u2502[/#808080] Mαtιν [#808080]\u2502[/#808080] Mυuιtsyα [#808080]\u2502[/#808080] Pιlμα [#808080]\u2502[/#808080] Estαq [#808080]\u2502[/#808080] Estαq 3 [#808080]\u2502[/#808080] Lιuem [#808080]\u2502[/#808080] Verqom [#808080]\u2502[/#808080] Iuαq [#808080]\u2502[/#808080] Aqtαudeμ [#808080]\u2502[/#808080] º [#808080]\u2502[/#808080]')
                          console.print('\u2500'*158,style= '#24272d')
                          print()

                          try:
                            oppel = open('Vermαt.txt',encoding='utf8')
                            print(oppel.read())
                            oppel.close()
                            
                          except FileNotFoundError:
                            print("Vermαt αqtαgeu' ιuνor ιutrēν")
                            print()

                          '''try:
                            conn = sq.connect('Lιuem.sqlite')
                            c = conn.cursor()
                            #c.execute('create table if not exists νermαt (Aδqαιt text, Uναιt text, Toreg text)')
                            c.execute('select * from νermαt')
                            νermαt = c.fetchall()
                            for i in νermαt:
                              print('|',i[0],'    ',i[1])
                            print()
                          
                          except Exception as e:
                            print(f'\n{e}\n')'''              
                          
                        lαmνermαt()

                        console.print('\u2500'*158,style= '#808080')

                        ινermαt = input('| ')
                        
                        if ινermαt == 'Mativ':
                          
                          try:

                            while True:
                              
                              oppel = open('Mαtιν.csv',encoding='utf8')
                              
                              def lαmαtιν():
                                
                                lαmνermαt()
                                console.print('\u2500'*158,style= '#24272d')
                                console.print('Mαtιν [#808080]|[/#808080]\n')
                                console.print(oppel.read())
                                console.print('\u2500'*158,style='#808080')
                                
                              lαmαtιν()

                              Mαt_Imαν = input('| ')
                              
                              if Mαt_Imαν == 'º':
                                break
                              
                              elif Mαt_Imαν == '':
                                pass

                              elif Mαt_Imαν == '.invor':
                                import os
                                ιuνor = os.getcwd()
                                console.print(f'[green]Nostαl ιuνor[/green]','[#808080]| [/#808080]', ιuνor)
                                print()
                                input()
                                
                              elif Mαt_Imαν == 'verqom':
                                
                                try:
                                  
                                  line_number = input(': ')
                                  
                                  if line_number == 'º':
                                    break
                                  
                                  elif line_number == '':
                                    line_number = 0
                                  
                                  else: line_number = int(line_number)
                                  
                                  with open('Mαtιν.csv',encoding='utf8') as oppel:
                                    lines = oppel.readlines()
                                    print(lines[line_number-1])
                                  
                                  new_line = input('> ')
                                  
                                  if new_line == 'º':   
                                    lαmαtιν()
                                    pass
                                  
                                  else:
                                    lines[line_number-1] = '| ' + new_line + '\n'
                                    if line_number <= len(lines):
                                      with open('Mαtιν.csv', 'w',encoding='utf8') as oppel:
                                        oppel.truncate(0)
                                      for i in lines:
                                        oppel = open('Mαtιν.csv','a',encoding='utf8')
                                        oppel.write(i)
                                        oppel.close()                        
                                    else:
                                      pass
                                      
                                except ValueError:
                                  print()
                                  print('Lαg αqtαlινeu')
                                  input()
                                  
                                except IndexError:
                                  pass
          
                              elif Mαt_Imαν == 'inaq':

                                try:

                                  number = input(': ')

                                  if number == '':
                                    number = 0
                                  else:
                                    number = int(number)

                                  with open('Mαtιν.csv',encoding='utf8') as oppel:
                                    lines = oppel.readlines()
                                    print(lines[number-1])

                                    ιuαq = input('> ')

                                    if ιuαq == 'º':
                                      pass
                                    else:
                                      if number <= len(lines):
                                        del lines[number-1]
                                        oppel = open('Mαtιν.csv','w',encoding='utf8')
                                        for i in lines:
                                          oppel.write(i)
                                        oppel.close()
                                      else:
                                        pass

                                except Exception as e:
                                  print()
                                  print(e)
                                  input()
                                
                                except ValueError:
                                  print()
                                  print('Lαg αqtαlινeu')
                                  input()
                                
                                except IndexError:
                                  lαmνermαt()
                                  pass
                              
                              elif Mαt_Imαν == '.aqtande':
                                print()
                                Seνdαl = input('Seνdαl uα Mαtιν αqtαudeμ | ')
                                if Seνdαl == 'Dyav':
                                  oppel = open('Mαtιν.csv','a')
                                  oppel.truncate(0)
                                  oppel.close
                                else:
                                  print()
                              
                              else:
                                oppel = open('Mαtιν.csv','a',encoding='utf8')
                                oppel.write('| ')
                                oppel.write(Mαt_Imαν)
                                oppel.write('\n')
                                oppel.close()  

                          except FileNotFoundError:
                            print()
                            print("Mαtιν αqtαgeu' ιuνor ιutrēν")
                            input()
                        
                        elif ινermαt == 'Munit':

                          try:
                            def νermυu():
                              
                              while True:
                                
                                def lαmυuιt():
                                  oppel = open('Mυuιt Vermαt.txt','r',encoding='utf8')
                                  
                                  lαmνermαt()

                                  console.print('\u2500'*158,style= '#24272d')
                                  print('Mυuιtsyα [#808080]|[/#808080]\n')
                                  print(oppel.read())
                                  console.print('[#808080]\u2500[/#808080]'*158)
                                  
                                lαmυuιt()
                              
                                vermυu = input('| ')
                              
                                if vermυu == 'º':
                                  break
                                
                                elif vermυu == 'inaq':
                                  
                                  try:
                                    number = input(': ')
                                    
                                    if number == 'º':
                                      lαmυuιt()
                                      break
                                    
                                    if number == '':
                                      number = 0
                                    
                                    else: number = int(number)
                                    
                                    def ιuαqtαν(lαιue,line_number):
                                    
                                      with open(lαιue,encoding='utf8') as oppel:
                                        lines = oppel.readlines()
                                        print(lines  [line_number-1])
                                        ιuαq = input('> ')
                                        
                                        if ιuαq == '.':
                                          if line_number <= len(lines):
                                            del lines[line_number-1]
                                            oppel = open('Mυuιt Vermαt.txt','w',encoding='utf8')
          
                                            for i in lines:
                                              oppel.write(i)
                                            oppel.close()
          
                                          else:
                                            pass
                                          
                                        else:
                                          pass
          
                                            
                                    ιuαqtαν('Mυuιt Vermαt.txt',number)
          
                                    lαmυuιt()
                                    
                                  except ValueError:
                                    print()
                                    print('Lαg αqtαlινeu')
                                    input()
                                    
                                  except IndexError:
                                    lαmνermαt()
                                    pass
                                
                                elif vermυu == '':
                                  lαmνermαt()
                                
                                else:
                                  try:
                                    oppel = open('Mυuιt Vermαt.txt','a',encoding='utf8')
                                    oppel.write('| ')
                                    oppel.write(vermυu)
                                    oppel.close()
                                    print()
          
                                    sιgμe = input('Sιgμe tαudrα | ')
          
                                    if sιgμe == '':
                                      oppel = open('Mυuιt Vermαt.txt','a',encoding='utf8')
                                      oppel.write('\n')
                                      oppel.close()
          
                                    else:                      
                                      oppel = open('Mυuιt Vermαt.txt','a',encoding='utf8')
                                      oppel.write('>  ')
                                      oppel.write(sιgμe)
                                      oppel.write('\n')
                                      oppel.close()
          
                                  except: pass
                            
                            νermυu()
                            
                          except FileNotFoundError:
                            print()
                            print("Mυuιt Vermαt αqtαgeu' ιuνor ιutrēν")
                            input()
                        
                        elif ινermαt == 'Pilha':
                          try:                 
                                            
                            while True:
                              def lαmpιlμα():
                                lαmνermαt()
                                console.print('\u2500'*158,style='#24272d')
                                print('Pιlμα |')
                                print()
                              lαmpιlμα()
                              
                              oppel = open('Verpιlμα.txt','r',encoding='utf8')
                              print(oppel.read()) 

                              console.print('\u2500'*158,style='#808080')
                              
                              Pιlμα = input('| ')
                              
                              if Pιlμα == 'º':
                                lαmνermαt()
                                break
                              
                              elif Pιlμα == '':
                                pass           
                                    
                              elif Pιlμα == 'inaq':
                                
                                def ιuαq():
                                  
                                  try:
                                    
                                    def ιuαq():
                                      number = input(': ')
                                    
                                      if number == 'º':
                                        return
                                      
                                      if number == '':
                                        number = 0
                                    
                                      else: number = int(number)
                                      
                                      def ιuαqtαν(lαιue,line_number):
                                      
                                        with open(lαιue,encoding='utf8') as oppel:
                                          lines = oppel.readlines()
                                          print(lines[line_number-1])
                                          ιuαq = input('> ')                  
                                        
                                          if ιuαq == '.':
                                            if line_number <= len(lines):
                                              del lines[line_number-1]
                                              oppel = open('Verpιlμα.txt','w',encoding='utf8')
                                              for i in lines:
                                                oppel.write(i)
                                              oppel.close()
                                            else:
                                              pass
                                        
                                          else:
                                            pass
                                        
                                        lαmpιlμα()
                                      
                                      ιuαqtαν('Verpιlμα.txt',number)
                                    
                                    ιuαq()

                                  except ValueError:
                                    print()
                                    print('Lαg αqtαlινeu')
                                    input()
                                    
                                  except IndexError:
                                    pass
                                    
                                  # Editar cualquier línea..
                                  '''elif eudel == 'Ashqait':
                                  import os
                                  os.system('Sedge https://docs.google.com/document/d/1NpckpNsTxjMBEVLm1tuL8Pk_WtmoqTCB/edit?rtpof=true')'''
                                ιuαq()
                          
                              elif Pιlμα == 'Aqtande':
                                
                                lαmpιlμα()
                                
                                Aqtαudeμ = input('Seνdαl uα Pιlμα αqtαudeμ | ')
                                
                                if Aqtαudeμ == 'Dyav':
                                  oppel = open('Verpιlμα.txt','a')
                                  oppel.truncate(0)
                                  oppel.close
                                  lαmpιlμα()
                                  print('Verpιlμα αqtαudeu')
                                  print()
                                
                                else:
                                  print()
                              
                              else:
                                lαmpιlμα()

                                oppel = open('Verpιlμα.txt','a',encoding='utf8')
                                oppel.write('| ')
                                oppel.write(Pιlμα)
                                oppel.write('\n')
                                oppel.close()
                          
                          except FileNotFoundError:
                            print()
                            print("Verpιlμα αqtαgeu' ιuνor ιutrēν")
                            print()
                            input()
                            
                        elif ινermαt == 'Linem':
                          try:
                            while True:
                              
                              def lαmνerlιuem():
                                
                                oppel = open('Lιuem Vermαt.txt',encoding='utf8')
                                
                                from datetime import datetime
                                import os
                                sιeνιt = datetime.now()
                                timestamp = sιeνιt.strftime('%H.%M')

                                import psutil
                                ιzναrtαg = psutil.sensors_battery()

                                if ιzναrtαg.power_plugged == True:
                                  os.system('cls' if os.name == 'nt' else 'clear')
                                  console.print('Vermαt [#808080]\u2502[/#808080] Lιuem [#808080]\u2502[/#808080]',' '*125,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#808080]\u2502[/#808080]',timestamp)

                                if ιzναrtαg.power_plugged == False:
                                  os.system('cls' if os.name == 'nt' else 'clear')
                                  console.print('Vermαt [#808080]\u2502[/#808080] Lιuem [#808080]\u2502[/#808080]',' '*125,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#808080]\u2502[/#808080]',timestamp)
                                
                                console.print('\u2500'*158, style='blue')

                                  
                                print(oppel.read())
                                
                              lαmνerlιuem()
                              
                              lιumαν = input()
                              
                              if lιumαν == '.lag':
                                import os
                                os.system('"Lιuem Vermαt.txt"')

                              elif lιumαν == 'inaq':
                                def ιuαq():
                                  
                                  try:
                                    
                                    number = input(': ')
                                    
                                    if number == '':
                                      number = 0

                                    if number == 'º':
                                      return
                                    
                                    else: number = int(number)
                                    
                                    def ιuαqtαν(lαιue,line_number):
                                    
                                      with open(lαιue,encoding='utf8') as oppel:
                                        lines = oppel.readlines()
                                        print(lines[line_number-1])
                                        ιuαq = input('> ')                  
                                        
                                        if ιuαq == '.':
                                          
                                          if line_number <= len(lines):
                                            del lines[line_number-1]
                                            oppel = open('Lιuem Vermαt.txt','w',encoding='utf8')
                                            for i in lines:
                                              oppel.write(i)
                                            oppel.close()
                                          else:
                                            pass
                                        
                                        else:
                                          return

                                    ιuαqtαν('Lιuem Vermαt.txt',number)
                                  except ValueError:
                                    print()
                                    print('Lαg αqtαlινeu')
                                    input()
                                  except IndexError:
                                    pass
                                  # Editar cualquier línea..
                                ιuαq() 
                              
                              elif lιumαν == 'º':
                                lαmνermαt()
                                break
                              
                              else:
                                oppel = open('Lιuem Vermαt.txt','a',encoding='utf8')
                                oppel.write('\n')
                                oppel.write(lιumαν)
                                oppel.close()
                                lαmνerlιuem()
                                oppel = open('Lιuem Vermαt.txt',encoding='utf8')

                          except FileNotFoundError:
                            print()
                            print("Lιuem Vermαt αqtαgeu' ιuνor ιutrēν")
                            print()
                            input()

                        elif ινermαt == '.tander':
                          try:
                            def tαuder():
                              while True:
                              
                                def lαmtαuder():
                                
                                  import os
                                  os.system('cls' if os.name == 'nt' else 'clear')

                                  from datetime import datetime
                                  sιevιt = datetime.now()
                                  timestamp = sιevιt.strftime('%H.%M')

                                  import psutil
                                  ιzναrtαg = psutil.sensors_battery()
                                  
                                  if ιzναrtαg.power_plugged == True:
                                    print('Tαuder [#808080]|[/#808080]',' '*133,'[#808080]|[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#808080]|[/#808080]',timestamp)

                                  if ιzναrtαg.power_plugged == False:
                                    print('Tαuder [#808080]|[/#808080]',' '*133,'[#808080]|[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#808080]|[/#808080]',timestamp)

                                  console.print('\u2500'*158,style='blue')

                                  with open('Tαuder.txt', 'r', encoding='utf8') as oppel:
                                    print(oppel.read())

                                lαmtαuder()

                                tαuder = input('')

                                if tαuder == 'º':
                                  lαmlιuem()
                                  return
                                
                                elif tαuder == '.lag':
                                  import os
                                  os.system('Tαuder.txt')

                                else:
                                  with open('Tαuder.txt', 'a', encoding='utf8') as oppel:
                                    oppel.write('\n')
                                    oppel.write(tαuder)                      
                              
                            tαuder()
                          
                          except Exception as e:
                            print()
                            print(e)
                            print()

                        elif ινermαt == 'Estaq':
                          try:
                            oppel = open('Estαq.txt',encoding='utf8')
                            
                            import os
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Vermαt [#808080]\u2502[/#808080] Estαq [#808080]\u2502[/#808080]')
                            console.print('\u2500'*158,style='blue')

                            print(oppel.read())
                            
                            console.print('\u2500'*158,style='#808080')

                            estαq = input('| ')

                            if estαq == '.lag':
                              import os
                              os.system('Estαq.txt')
                              lαmνermαt()

                          
                          except FileNotFoundError:
                            print()
                            print("Estαq αqtαgeu' ιuνor ιutrēν")
                            print()
                            input()
                            
                        elif ινermαt == 'Estaq3':
                          
                          try:
                          
                            oppel = open('Estαq 3.txt',encoding='utf8')
                          
                            import os
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Vermαt \u2502 Estαq 3 \u2502')
                            print('\u2500'*158)
          
                            print(oppel.read())

                            estαq3 = input('| ')

                            if estαq3 == 'lag':
                              import os
                              os.system('"Estαq 3.txt"')
                            
                          except FileNotFoundError:
                            print()
                            print("Estαq 3 αqtαgeu' ιuνor ιutrēν")
                            print()
                            input()       
                        
                        elif ινermαt == 'verqom':
                          try:
                            open('Vermαt.txt',encoding='utf8')
                            
                            def νerqom():
                              try:
                                
                                line_number = input(': ')
                                
                                if line_number == 'º':
                                  return
                                
                                elif line_number == '':
                                  line_number = 0
                                
                                else: line_number = int(line_number)                     
                                
                                with open('Vermαt.txt',encoding='utf8') as oppel:
                                  lines = oppel.readlines()
                                  print(lines[line_number-1])            
                                
                                eudαμl =  input('> ')
                                
                                if eudαμl == '':
                                  pass
                                
                                else:
                                    print()
                                    sιgμe = input('Sιgμe | ')
                                  
                                    if sιgμe == '':
                                      lines[line_number-1] = '| ' + eudαμl + '\n'
                                      oppel = open('Vermαt.txt','w',encoding='utf8')
                                      oppel.truncate(0)
                                      for i in lines:
                                        oppel = open('Vermαt.txt','a',encoding='utf8')
                                        oppel.write(i)
                                        oppel.close()

                                    else:
                                      lines[line_number-1] = '| ' + eudαμl + '        >        ' + sιgμe + '\n'
                                      oppel = open('Vermαt.txt','w',encoding='utf8')
                                      oppel.truncate(0)
                                      for i in lines:
                                        oppel = open('Vermαt.txt','a',encoding='utf8')
                                        oppel.write(i)
                                        oppel.close()
                              
                              except IndexError:
                                pass

                            νerqom()

                          except:
                            pass
                                
                          '''con = sq.connect('Lιuem.sqlite')
                          c = con.cursor()
                          c.execute('select * from νermαt')
                          νermαt = c.fetchall()
                          items = νermαt[line_number-1]
                          print('|',items[0],'   ',items[1])
                          
                                
                          items = (eudαμl,sιgμe,'')
                          con = sq.connect('Lιuem.sqlite')
                          c = con.cursor()
                          c.execute(f"update νermαt set Aδqαιt = ?, Uναιt = ?, Toreg = ? where rowid = {line_number-1}",items)
                          con.commit()
                          c.execute('select * from νermαt')
                          νermαt = c.fetchall() 
                          print(νermαt)
                          input()'''

                        elif ινermαt == 'inaq':

                          try:
                            oppel = open('Vermαt.txt',encoding='utf8')
                            
                            def ιuαq():
                              number = input(': ')
                            
                              if number == 'º':
                                return
                            
                              if number == '':
                                number = 0
                            
                              else: number = int(number)
                            
                              oppel = open('Vermαt.txt',encoding='utf8')
                              lines = oppel.readlines()
                              print(lines[number-1])
                            
                              ιuαq = input('> ')                  
                        
                              if ιuαq == '.':
                                if number <= len(lines):
                                  del lines[number-1]
                                  oppel = open('Vermαt.txt','w',encoding='utf8')
                                  oppel.truncate(0)
                                  for i in lines:
                                    oppel = open('Vermαt.txt','a',encoding='utf8')
                                    oppel.write(i)
                                    oppel.close()
                                                    
                                else:
                                  return
          
                              else:
                                pass
                            
                            ιuαq()

                          except ValueError:
                            print()
                            print('Lαg αqtαlινeu')
                            input()
                          
                          except:
                            pass
                        
                        elif ινermαt == 'aqtande':
                          
                          try:
                            oppel = open('Vermαt.txt','a')
                            
                            lαmνermαt()
                            
                            Aqtαudeμ = input('Seνdαl uα Vermαt αqtαudeμ | ')
                            
                            if Aqtαudeμ == 'Dyav':
                              oppel.truncate(0)
                              oppel.close
                              lαmνermαt()
                              print('Vermαt αqtαudeu')
                              print()
                              
                            else:
                              pass
                              
                          except:
                            pass
                        
                        elif ινermαt == 'º':
                          lαmlιuem()
                          return
                        
                        else:
                          
                          if ινermαt == '':
                            lαmνermαt()
                            pass
                          
                          else:
                            try:
                              oppel = open('Vermαt.txt','a',encoding='utf8')
                              oppel.write('| ')
                              oppel.write(ινermαt)
                              oppel.close()
                              print()

                              sιgμe = input('Sιgμe tαudrα | ')
                              
                              if sιgμe == '':
                                oppel = open('Vermαt.txt','a',encoding='utf8')
                                oppel.write('\n')
                                oppel.close()

                              else:                      
                                oppel = open('Vermαt.txt','a',encoding='utf8')
                                oppel.write('        >        ')
                                oppel.write(sιgμe)
                                oppel.write('\n')
                                oppel.close()

                              '''try:
                              
                              values = (ινermαt,sιgμe,'')

                              conn = sq.connect('Lιuem.sqlite')
                              c = conn.cursor()
                              c.execute('create table if not exists νermαt (Aδqαιt text, Uναιt text, Toreg text)')
                              c.execute(f"insert into νermαt ('Aδqαιt','Uναιt','Toreg') values (?,?,?)",values)
                              conn.commit()
                              c.execute('select * from νermαt')
                              conn.close()'''
        
                            except Exception as e:
                              print(f'\n{e}\n')
                              input()
                    
                    Vermαt()

                    ιmαν = ''
                    lαm()
                  
                  elif ιmαν == 'Dyatev':
                    
                    curses.endwin()

                    def Dyαtēν():
                      
                      while True:
                        
                          def lαmdyαteν():
                            
                            import os
                            os.system ('cls' if os.name == 'nt' else 'clear')

                            import psutil
                            ιzναrtαg = psutil.sensors_battery()
                            
                            from datetime import datetime
                            sιeνιt = datetime.now()
                            timestamp = sιeνιt.strftime('%H.%M')

                            console = Console()
                            
                            if ιzναrtαg.power_plugged == True:
                              print('Dyαtēν [#808080]\u2502[/#808080]',' '*133,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#808080]\u2502[/#808080]',timestamp)

                            if ιzναrtαg.power_plugged == False:
                              print('Dyαtēν [#808080]\u2502[/#808080]',' '*133,'[#808080]\u2502[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#808080]\u2502[/#808080]',timestamp)
                              
                            console.print('\u2500'*158,style='blue')
                            console.print('[#808080]|[/#808080] Sιguα [#808080]|[/#808080] Verqōm [#808080]|[/#808080] Iuαq [#808080]|[/#808080] Aqtαudeμ [#808080]|[/#808080] Mυutαuder [#808080]|[/#808080] Dyeναstαq [#808080]|[/#808080] º [#808080]|[/#808080]')
                            console.print('\u2500'*158,style='#24272d')
                            print()

                            try:
                              oppel = open('Dyαtēν.txt',encoding='utf8')
                              print(oppel.read())
                              oppel.close()
                            
                            except FileNotFoundError:
                              print("Dyαteν αqtαgeu' ιuνor ιutrēν")
                              print()
                            
                          lαmdyαteν()
                        
                          while True:
                            
                            console = Console()
                            
                            console.print('\u2500'*158,style='#808080')
                            
                            Dyαt_Imαν = input('| ')
                            
                            if Dyαt_Imαν == 'signa':
                              
                              lαmdyαteν()
                              console.print('\u2500'*158,style='#808080')
                              print('Sιguα  \u2502')
                              console.print('\u2500'*158,style='#24272d')
                              
                              Qαιse = input('Qαιse  | ')
                              
                              if Qαιse == '':
                                oppel = open('Dyαtēν.txt','a',encoding='utf8')
                                oppel.write('\n')
                                oppel.write('\n')
                                oppel.close()
                              
                              elif Qαιse == 'º':
                                break
                              
                              else:
                                oppel = open('Dyαtēν.txt','a',encoding='utf8')
                                oppel.write('\n')
                                oppel.write('\n')
                                oppel.write(Qαιse)
                                oppel.write(' | ')
                                oppel.close()
                              
                              Lαιu = input('Lαιu   | ')
                              
                              if Lαιu == '':
                                oppel = open('Dyαtēν.txt','a',encoding='utf8')
                                oppel.write('\n')
                                oppel.close()
                              
                              elif Lαιu == 'º':
                                break
                              
                              else:
                                oppel = open('Dyαtēν.txt','a',encoding='utf8')
                                oppel.write(Lαιu)
                                oppel.write('\n')
                                oppel.close()
                              
                              oppel = open('Dyαtēν.txt','a',encoding='utf8')
                              oppel.write('\u2500'*21)
                              oppel.write('\n')
                              oppel.close()
                              
                              Sιeνιt = input('Sιeνιt | ')
                              
                              if Sιeνιt == '':
                                oppel = open('Dyαtēν.txt','a',encoding='utf8')
                                oppel.write('\n')
                                oppel.close()
                              
                              elif Sιeνιt == 'º':
                                break
                              
                              else:
                                oppel = open('Dyαtēν.txt','a',encoding='utf8')
                                oppel.write('Sιeνιt  | ')
                                oppel.write(Sιeνιt)
                                oppel.write('\n')
                                oppel.close()
                              
                              Iuνorαt = input('Vorαt  | ')
                              
                              if Iuνorαt == '':
                                oppel = open('Dyαtēν.txt','a',encoding='utf8')
                                oppel.write('\n')
                                oppel.close()
                              
                              elif Iuνorαt == 'º':
                                break
                              
                              else:
                                oppel = open('Dyαtēν.txt','a',encoding='utf8')
                                oppel.write('Iuvorαt | ')
                                oppel.write(Iuνorαt)
                                oppel.write('\n')
                                oppel.close()
                              
                              Auget = input('Auget  | ')
                              
                              if Auget == '':
                                oppel = open('Dyαtēν.txt','a',encoding='utf8')
                                oppel.write('\n')
                                oppel.close()
                              
                              elif Auget == 'º':
                                break
                              
                              else:
                                oppel = open('Dyαtēν.txt','a',encoding='utf8')
                                oppel.write('Auget   | ')
                                oppel.write(Auget)
                                oppel.write('\n')
                                oppel.close()
                              
                              Dyαutαl = input('Dyαute | ')
                              
                              if Dyαutαl == '':
                                oppel = open('Dyαtēν.txt','a',encoding='utf8')
                                oppel.write('\n')
                                oppel.close()
                                break
                              
                              elif Dyαutαl   == 'º':
                                break
                              
                              else:
                                oppel = open('Dyαtēν.txt','a',encoding='utf8')
                                oppel.write('Dyαutαl | ')
                                oppel.write(Dyαutαl)
                                oppel.write('\n')
                                oppel.close()
                              
                                while True:
                                
                                  Dyαutαl = input('       | ')
                                  
                                  if Dyαutαl == '':
                                    oppel = open('Dyαtēν.txt','a',encoding='utf8')
                                    oppel.write('\n')
                                    oppel.close()
                                    break
                                  
                                  elif Dyαutαl   == 'º':
                                    oppel = open('Dyαtēν.txt','a',encoding='utf8')
                                    oppel.write('\n')
                                    oppel.close()
                                    break
                                  
                                  else:
                                    oppel = open('Dyαtēν.txt','a',encoding='utf8')
                                    oppel.write('        | ')
                                    oppel.write(Dyαutαl)
                                    oppel.write('\n')
                                    oppel.close()
                          
                            elif Dyαt_Imαν == 'Vermun':

                              try:
                                def νermυu():

                                  while True:

                                    def lαmυuιt():
                                      oppel = open('Mυuιt Vermαt.txt','r',encoding='utf8')

                                      lαmdyαteν()

                                      print()
                                      console.print('\u2500'*158,style='#24272d')

                                      print('Mυuιtsyα [#808080]|[/#808080]\n')
                                      print(oppel.read())
                                      print()
                                      console.print('[#808080]\u2500[/#808080]'*158)

                                    lαmυuιt()

                                    vermυu = input('| ')

                                    if vermυu == 'º':
                                      lαmdyαteν()
                                      break

                                    elif vermυu == 'inaq':

                                      try:
                                        number = input(': ')

                                        if number == 'º':
                                          lαmυuιt()
                                          break

                                        if number == '':
                                          number = 0

                                        else: number = int(number)

                                        def ιuαqtαν(lαιue,line_number):

                                          with open(lαιue,encoding='utf8') as oppel:
                                            lines = oppel.readlines()
                                            print(lines  [line_number-1])
                                            ιuαq = input('> ')

                                            if ιuαq == '.':
                                              if line_number <= len(lines):
                                                del lines[line_number-1]
                                                oppel = open('Mυuιt Vermαt.txt','w',encoding='utf8')

                                                for i in lines:
                                                  oppel.write(i)
                                                oppel.close()

                                              else:
                                                pass

                                            else:
                                              pass


                                        ιuαqtαν('Mυuιt Vermαt.txt',number)

                                        lαmυuιt()

                                      except ValueError:
                                        print()
                                        print('Lαg αqtαlινeu')
                                        input()

                                      except IndexError:
                                        lαmdyαteν()
                                        pass

                                    elif vermυu == '':
                                      lαmdyαteν()

                                    else:
                                      try:
                                        oppel = open('Mυuιt Vermαt.txt','a',encoding='utf8')
                                        oppel.write('| ')
                                        oppel.write(vermυu)
                                        oppel.close()
                                        lαmυuιt()
                                        print()

                                        sιgμe = input('Sιgμe tαudrα | ')

                                        if sιgμe == '':
                                          oppel = open('Mυuιt Vermαt.txt','a',encoding='utf8')
                                          oppel.write('\n')
                                          oppel.close()

                                        else:                      
                                          oppel = open('Mυuιt Vermαt.txt','a',encoding='utf8')
                                          oppel.write('>  ')
                                          oppel.write(sιgμe)
                                          oppel.write('\n')
                                          oppel.close()

                                      except: pass

                                νermυu()

                              except FileNotFoundError:
                                print()
                                print("Mυuιt Vermαt αqtαgeu' ιuνor ιutrēν")
                                input()
                            
                            elif Dyαt_Imαν == 'Muntander':

                              try:
          
                                while True:
          
                                  import os
                                  os.system('cls' if os.name == 'nt' else 'clear')

                                  import psutil
                                  ιzναrtαg = psutil.sensors_battery()

                                  from datetime import datetime
                                  sιeνιt = datetime.now()
                                  timestamp = sιeνιt.strftime('%H.%M')

                                  if ιzναrtαg.power_plugged == True:
                                    console.print('Mυuιtseμ Tᾱuderα [#808080]|[/#808080]',' '*123,'[#808080]|[/#808080]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#808080]|[/#808080]',timestamp)

                                  if ιzναrtαg.power_plugged == False:
                                    console.print('Mυuιtseμ Tᾱuderα [#808080]|[/#808080]',' '*123,'[#808080]|[/#808080]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#808080]|[/#808080]',timestamp)
                                  
                                  console.print('\u2500'*158,style='blue')
          
                                  oppel = open('Mυuιtsyα.txt','r',encoding='utf8')
                                  print(oppel.read())
                                  oppel.close()
          
                                  tαuder = input('')
          
                                  if tαuder == 'º':
                                    lαmdyαteν()
                                    break
          
                                  elif tαuder == '.lag':
                                    import os
                                    os.system ('Mυuιtsyα.txt')
                                    lαmdyαteν()
          
                                  else:
                                    with open('Mυuιtsyα.txt','a',encoding='utf8') as oppel:
                                      oppel.write('\n')
                                      oppel.write(tαuder)
          
                              except Exception as e:
                                print()
                                print(e)
                                input()
                                pass
                            
                            elif Dyαt_Imαν == 'Aqtande':
                            
                              print()
                              
                              Sevdαl = input('Dye sevdαl uα dyαtēν αqtαudeμ | ')
                              
                              if Sevdαl == 'Dyav':
                                oppel = open('Dyαtēν.txt','a')
                                oppel.truncate(0)
                                oppel.close()
                                lαmlιuem()
                                print('Dyαtēν αqtαudeu')
                                print()
                              
                              else:
                                print()
                            
                            elif Dyαt_Imαν == 'Qampar':
                              import webbrowser
                              webbrowser.open('http://maps.google.com/')
                              lαmdyαteν()
                            
                            elif Dyαt_Imαν == 'º':
                              lαmlιuem()
                              return
                            
                            elif Dyαt_Imαν == 'verqom':
                            
                              try:
                                
                                line_number = input(': ')
                                
                                if line_number == 'º':
                                  break
                                
                                if line_number == '':
                                  line_number = 0
                                
                                else:
                                  line_number = int(line_number)
                                
                                oppel = open('Dyαtēν.txt',encoding='utf8')
                                lines = oppel.readlines()
                                print(lines[line_number-1])
                                
                                new_line = input('> ')
                                
                                if new_line == 'º':
                                  break 
                                
                                elif new_line == '':
                                  break 
                                else:
                                  lines[line_number-1] = new_line + '\n'
                                
                                  if line_number <= len(lines):
                                    oppel = open('Dyαtēν.txt','w',encoding='utf8')
                                    for i in lines:
                                      oppel.write(i)
                                    oppel.close()
                                    lαmdyαteν()
                                  
                                  else:
                                    pass
                              
                              except ValueError:
                                pass
                            
                            elif Dyαt_Imαν == 'inaq':
                            
                              try:
                                  number = input(': ')
                                
                                  if number == '':
                                    number = 0
                                    
                                  else: number = int(number)
                                  
                                  def ιuαqtαν(lαιue,line_number):
                                    with open(lαιue,encoding='utf8') as oppel:
                                      lines = oppel.readlines()
                                      print(lines[line_number-1])
                                      ιuαq = input('> ')                  
                                      
                                      if ιuαq == '.':
                                        if line_number <= len(lines):
                                          del lines[line_number-1]
                                          oppel = open('Dyαtēν.txt','w',encoding='utf8')
                                          for i in lines:
                                            oppel.write(i)
                                          oppel.close()

                                        else:
                                          pass
                                      
                                      else:
                                        return
                                          
                                  ιuαqtαν('Dyαtēν.txt',number)
                                
                                  lαmdyαteν()
                                
                              except ValueError:
                                print()
                                print('Lαg αqtαlινeu')
                                input()
                                lαmdyαteν()
                                
                              except IndexError:
                                lαmdyαteν()
                                pass
                            
                            elif Dyαt_Imαν == 'Lag':
                              import os
                              os.system('Dyαtēν.txt')
                              lαmdyαteν()
                            
                            elif Dyαt_Imαν == 'Dyevastaq':
                              import webbrowser
                              webbrowser.open("https://calendar.google.com/calendar/u/3/r/")
                              lαmdyαteν()
                            
                            else:
                              break
                              
                    Dyαtēν()

                    ιmαν = ''

                    lαm()

                  elif ιmαν == 'Angest':
                    curses.endwin()

                    def Augestαq():
              
                      def lαmαugest():
                      
                        import os
                        os.system('cls' if os.name == 'nt' else 'clear')
                        
                        from datetime import datetime
                        sιeνιt = datetime.now()
                        timestamp = sιeνιt.strftime('%H.%M')

                        import psutil
                        ιzναrtαg = psutil.sensors_battery()
                        
                        console = Console()
                        
                        if ιzναrtαg.power_plugged == True:
                          print('Augestαq [#24272d]\u2502[/#24272d]',' '*131,'[#24272d]\u2502[/#24272d]',ιzναrtαg.percent,'[green][bold]·[/bold][/green]','[#24272d]\u2502[/#24272d]',timestamp)
                        
                        if ιzναrtαg.power_plugged == False:
                          print('Augestαq [#24272d]\u2502[/#24272d]',' '*131,'[#24272d]\u2502[/#24272d]',ιzναrtαg.percent,'[red][bold]·[/bold][/red]','[#24272d]\u2502[/#24272d]',timestamp)
                        
                        console.print('\u2500'*158,style='blue')
                        print('[#808080]\u2502[/#808080] Sιguα [#808080]\u2502[/#808080] Iuslag [#808080]\u2502[/#808080] Mαuslαg [#808080]\u2502[/#808080] Aqtαudeμ [#808080]\u2502[/#808080] º [#808080]\u2502[/#808080]')
                        console.print('\u2500'*158,style='#24272d')
                        print()

                        try:
                          oppel = open('Augestαq.csv',encoding='utf8')
                          print(oppel.read())
                          oppel.close()
                          console.print('\u2500'*158,style='#808080')                  

                        except FileNotFoundError:
                          print("Dyαteν αqtαgeu' ιuνor ιutrēν")
                          print()
                          
                      lαmαugest()

                      while True:
                        Aug_Imαν = input('| ')
                        
                        if Aug_Imαν == 'Signa':
                          def Sιguα():

                            console.print('\u2500' * 158, style='#24272d')

                            import datetime
                            sιevιt = datetime.date.today()
                            print(' '*147,sιevιt)
                            oppel = open('Augestαq.csv','a')
                            oppel.write('\n')
                            oppel.write('| ')
                            oppel.write(str(sιevιt))
                            oppel.write('\n')
                            oppel.close
                            
                            def AuSιg_Imαν():
        
                              while True:
                              
                                AuSιg_Imαν = input('| ')
                                
                                if AuSιg_Imαν == 'Mayeq':
                                    oppel = open('Augestαq.csv','a',encoding='utf8')
                                    oppel.write('\n')
                                    oppel.write('\n')
                                    oppel.write('Mαyeq')
                                    oppel.write('\n')
                                    oppel.write('\u2500'*14)
                                    oppel.write('\n')
                                    oppel.close()
                                    print('\u2500'*8)
                                    #| Delαus
                                
                                    while True:
                                      
                                      Mαyeq_delαus = input('Delαus | ')
                                      
                                      if Mαyeq_delαus == '':
                                        Mαyeq_delαus = '0'
                                        oppel = open('Augestαq.csv','a',encoding='utf8')
                                        oppel.write('Delαus | ')
                                        oppel.write(Mαyeq_delαus)
                                        oppel.write(' ')
                                        oppel.write('ge')
                                        oppel.write('\n')
                                        oppel.close()
                                        break
                                      #elif  Mαyeq_delαus == Una letra o un símbolo:  
                                      #  print("Aqledeu lαg' ιtαu αtvιαr") #Wrong entry, insertar de nuevo
                                      #  print() and repeat Mαyeq Delαus
                                      else:  
                                        oppel = open('Augestαq.csv','a',encoding='utf8')
                                        oppel.write('Delαus | ')
                                        oppel.write(Mαyeq_delαus)
                                        oppel.write(' ')
                                        oppel.write('ge')
                                        oppel.write('\n')
                                        oppel.close()
                                        break
                                    #| Proxeu
                                    while True:    
                                      Mαyeq_proxeu = input('Proxeu | ')
                                      if Mαyeq_proxeu == '':
                                        Mαyeq_proxeu = '0'
                                        oppel = open('Augestαq.csv','a',encoding='utf8')
                                        oppel.write('Proxeu | ')
                                        oppel.write(Mαyeq_proxeu)
                                        oppel.write(' ')
                                        oppel.write('ge')
                                        oppel.write('\n')
                                        oppel.close()
                                        break
                                      #| elif Letra o símbolo
                                      #print()
                                      #print("Aqledeu lαg' ιtαu αtvιαr") #Wrong entry, insertar de nuevo
                                      else:
                                        oppel = open('Augestαq.csv','a',encoding='utf8')
                                        oppel.write('Proxeu | ')
                                        oppel.write(Mαyeq_proxeu)
                                        oppel.write(' ')
                                        oppel.write('ge')
                                        oppel.write('\n')
                                        oppel.close()
                                        break
                                    #| Soleu
                                    while True:
                                      Mαyeq_soleu = input('Soleu  | ')
                                      if Mαyeq_soleu == '':
                                        Mαyeq_soleu = '0'
                                        oppel = open('Augestαq.csv','a',encoding='utf8')
                                        oppel.write('Soleu  | ')
                                        oppel.write(Mαyeq_soleu)
                                        oppel.write(' ')
                                        oppel.write('ge')
                                        oppel.write('\n')
                                        oppel.close()
                                        break
                                      #| elif Letra o símbolo
                                      #print()
                                      #print("Aqledeu lαg' ιtαu αtvιαr") #Wrong entry, insertar de nuevo
                                      else:
                                          oppel = open('Augestαq.csv','a',encoding='utf8')
                                          oppel.write('Soleu  | ')
                                          oppel.write(Mαyeq_soleu)
                                          oppel.write(' ')
                                          oppel.write('ge')
                                          oppel.write('\n')
                                          oppel.close()
                                          break
                                    #| Sιguα
                                    print('\u2500'*14)
                                    Mαyeq_sιguα = int(Mαyeq_delαus) + int(Mαyeq_proxeu) + int(Mαyeq_soleu)
                                    if Mαyeq_sιguα % 10 == 0 and Mαyeq_sιguα > 0:
                                      MαsιgPαlμα = int(Mαyeq_sιguα / 10)
                                      print('Sιguα  | ' + str(MαsιgPαlμα) + ' pα')
                                      oppel = open('Augestαq.csv','a',encoding='utf8')
                                      oppel.write('Sιguα  | ')
                                      oppel.write(str(MαsιgPαlμα))
                                      oppel.write(' ')
                                      oppel.write('pα')
                                      oppel.write('\n')
                                      oppel.write('\n')
                                      oppel.close()
                                    else:
                                      print('Sιguα  | ' + str(Mαyeq_sιguα) + ' ge')
                                      oppel = open('Augestαq.csv','a',encoding='utf8')
                                      oppel.write('Sιguα  | ')
                                      oppel.write(str(Mαyeq_sιguα))
                                      oppel.write(' ')
                                      oppel.write('ge')
                                      oppel.write('\n')
                                      oppel.close()
                                    print()
                                if AuSιg_Imαν == 'Neqen':
                                  oppel = open('Augestαq.csv','a',encoding='utf8')
                                  oppel.write('\n')
                                  oppel.write('\n')
                                  oppel.write('Neqeu')
                                  oppel.write('\n')
                                  oppel.write('\u2500'*14)
                                  oppel.write('\n')
                                  oppel.close()
                                  print('\u2500' * 8)
                                  #| Delαus
                                  while True:
                                    Neqeu_delαus = input('Delαus | ')
                                    if Neqeu_delαus == '':
                                      Neqeu_delαus = '0'
                                      oppel = open('Augestαq.csv','a',encoding='utf8')
                                      oppel.write('Delαus | ')
                                      oppel.write(Neqeu_delαus)
                                      oppel.write(' ')
                                      oppel.write('ge')
                                      oppel.write('\n')
                                      oppel.close()
                                      break
                                    #elif  Neqeu_delαus == Una letra o un símbolo:  
                                    #  print("Aqledeu lαg' ιtαu αtvιαr") #Wrong entry, insertar de nuevo
                                    #  print() and repeat Neqeu Delαus
                                    else:
                                      oppel = open('Augestαq.csv','a',encoding='utf8')
                                      oppel.write('Delαus | ')
                                      oppel.write(Neqeu_delαus)
                                      oppel.write(' ')
                                      oppel.write('ge')
                                      oppel.write('\n')
                                      oppel.close()
                                      break
                                  #| Dαuqαδ
                                  while True:  
                                    Neqeu_dαuqαδ = input('Dαuqαδ | ')
                                    if Neqeu_dαuqαδ == '':
                                      Neqeu_dαuqαδ = '0'
                                      oppel = open('Augestαq.csv','a',encoding='utf8')
                                      oppel.write('Dαuqαδ | ')
                                      oppel.write(Neqeu_dαuqαδ)
                                      oppel.write(' ')
                                      oppel.write('ge')
                                      oppel.write('\n')
                                      oppel.close()
                                      break
                                    #| elif Símbolo o letra
                                    else:
                                      oppel = open('Augestαq.csv','a',encoding='utf8')
                                      oppel.write('Dαuqαδ | ')
                                      oppel.write(Neqeu_dαuqαδ)
                                      oppel.write(' ')
                                      oppel.write('ge')
                                      oppel.write('\n')
                                      oppel.close()
                                      break
                                  #| Soleu
                                  while True:
                                    Neqeu_soleu = input('Soleu  | ')
                                    if Neqeu_soleu == '':
                                      Neqeu_soleu = '0'
                                      oppel = open('Augestαq.csv','a',encoding='utf8')
                                      oppel.write('Soleu  | ')
                                      oppel.write(Neqeu_soleu)
                                      oppel.write(' ')
                                      oppel.write('ge')
                                      oppel.write('\n')
                                      oppel.close()
                                      break
                                    #| elif Símbolo o letra
                                    else:
                                      oppel = open('Augestαq.csv','a',encoding='utf8')
                                      oppel.write('Soleu  | ')
                                      oppel.write(Neqeu_soleu)
                                      oppel.write(' ')
                                      oppel.write('ge')
                                      oppel.write('\n')
                                      oppel.close()
                                      break
                                  #| Sιguα
                                  print('\u2500'*15)
                                  Neqeu_sιguα = int(Neqeu_delαus) + int(Neqeu_dαuqαδ) + int(Neqeu_soleu)
                                  if Neqeu_sιguα % 10 == 0 and Neqeu_sιguα > 0:
                                    NesιgPαlμα = int(Neqeu_sιguα / 10)
                                    print('Sιguα  | ' + str(NesιgPαlμα) + ' pα')
                                    oppel = open('Augestαq.csv','a',encoding='utf8')
                                    oppel.write('Sιguα  | ')
                                    oppel.write(str(Neqeu_sιguα))
                                    oppel.write(' ')
                                    oppel.write('pα')
                                    oppel.write('\n')
                                    oppel.write('\n')
                                    oppel.close()
                                    print()
                                  else:
                                    print('Sιguα  | '+ str(Neqeu_sιguα) + ' ge')
                                    oppel = open('Augestαq.csv','a',encoding='utf8')
                                    oppel.write('Sιguα  | ')
                                    oppel.write(str(Neqeu_sιguα))
                                    oppel.write(' ')
                                    oppel.write('ge')
                                    oppel.write('\n')
                                    oppel.write('\n')
                                    oppel.close()
                                    print()
                                if AuSιg_Imαν == 'Sighe':
                                  print()
                                  Sιgμe = int(Mαyeq_sιguα) + int(Neqeu_sιguα)
                                  if Sιgμe % 10 == 0 and Sιgμe > 0:
                                    Pαlμα = int(Sιgμe / 10)
                                    print('Sιgμe  | ' + str(Pαlμα) + ' pα')
                                  else:
                                    print('Sιgμe  | ' + str(Sιgμe) + ' ge')
                                  print()
                                if AuSιg_Imαν == 'Anqopt':
                                  print()
                                  Auqopt = input('Aδqαιt | ')
                                  if Auqopt == '':
                                    Auqopt = '0'
                                    oppel = open('Augestαq.csv','a',encoding='utf8')
                                    oppel.write('Auqopt | ')
                                    oppel.write(str(Auqopt))
                                    oppel.write(' ')
                                    oppel.write('ge')
                                    oppel.write('\n')
                                    oppel.write('\n')
                                    oppel.close()
                                    print()
                                  elif int(Auqopt) % 10 == 0:
                                    AuqPαlμα = int(Auqopt / 10)
                                    # print('Auqopt | ' + str(AuqPαlμα) + ' pα')
                                    oppel = open('Augestαq.csv','a',encoding='utf8')
                                    oppel.write('Auqopt | ')
                                    oppel.write(str(Auqopt))
                                    oppel.write(' ')
                                    oppel.write('pα')
                                    oppel.write('\n')
                                    oppel.write('\n')
                                    oppel.close()
                                    print()
                                  else:
                                    # print('Auqopt  | '+ str(Auqopt) + ' ge')
                                    oppel = open('Augestαq.csv','a',encoding='utf8')
                                    oppel.write('Auqopt | ')
                                    oppel.write(str(Auqopt))
                                    oppel.write(' ')
                                    oppel.write('ge')
                                    oppel.write('\n')
                                    oppel.write('\n')
                                    oppel.close()
                                    print()
                                if AuSιg_Imαν == 'Nothest':
                                  print()
                                  Notμestαq = int(Mαyeq_sιguα) + int(Neqeu_sιguα) + int(Auqopt)
                                  if Notμestαq % 10 == 0 and Notμestαq > 0:
                                    NotμPαlμα = int(Notμestαq / 10)
                                    print('Notμest| ' + str(NotμPαlμα) + ' pα')
                                    oppel = open('Augestαq.csv','a',encoding='utf8')
                                    oppel.write('Notμest| ')
                                    oppel.write(str(NotμPαlμα))
                                    oppel.write(' ')
                                    oppel.write('pα')
                                    oppel.write('\n')
                                    oppel.close()
                                  else:
                                    print('Notμest| ' + str(Notμestαq) + ' ge')
                                    oppel = open('Augestαq.csv','a',encoding='utf8')
                                    oppel.write('Notμest| ')
                                    oppel.write(str(Notμestαq))
                                    oppel.write(' ')
                                    oppel.write('ge')
                                    oppel.write('\n')
                                    oppel.close()
                                  print()
                                #δινeu command ιuverqom
                                if AuSιg_Imαν == 'º':
                                  oppel = open('Augestαq.csv','a',encoding='utf8')
                                  oppel.write('\n')
                                  oppel.write('\n')
                                  oppel.close()
                                  lαmαugest()
                                  break
                            AuSιg_Imαν()
                          Sιguα()
                        
                        elif Aug_Imαν == 'Aqtande':
                          print()
                          Sevdαl = input('Dye sevdαl uα oppel αqtαudeμ | ')
                          if Sevdαl == 'Dyav':
                            oppel = open('Augestαq.csv','a')
                            oppel.truncate(0)
                            oppel.close()
                            import os
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Augestαq')
                            print('\u2500'*158)
                            print('Estαq αqtαudeu')
                            input()
                          else:
                            print()
                        
                        elif Aug_Imαν == 'Manslag':
                          import os
                          os.system('cls' if os.name == 'nt' else 'clear')
                          print('Augestαq \u2502 Mαuslαg \u2502')
                          print('\u2500'*158)
                          oppel = open('Augest.Mαuslαg.txt',encoding='utf8')
                          print(oppel.read())
                          input()
                          lαmαugest()
                        
                        elif Aug_Imαν == 'Inslag':
                          try:
                            import os
                            os.system("Augestαq.csv")
                          except Exception as e:
                            print()
                            print('Augestαq αqδαι')
                            print(e)
                            input()
                          lαmαugest()
                        
                        elif Aug_Imαν == 'Isqyan':
                          import os
                          os.system('Augest.Isqyαu.txt')
                          lαmαugest()
                        
                        elif Aug_Imαν == 'º':
                          lαmlιuem()
                          break
                        
                        else:
                          lαmαugest()

                    Augestαq()

                    ιmαν = ''
                    lαm()

                  else:  
                    ιmαν = ''
                    lαm()

                elif key == 0o10:
                  ιmαν = ιmαν[:-1]
                  lαm()
                
                elif key != -1:
                  ιmαν += chr(key)

                else:
                  pass

                stdscr.refresh()

                time.sleep(0.01)
                
            wrapper(main)
            
            lαmlιuem()
          
          elif ιmαν == 'Logatx':
            from textual.app import App
            from textual.widget import Widget
            from textual.widgets import Input, Header
            
            class Linem(Widget):
              def render(self):
                return 'Lιuem'
                
            class Lιuem(App):
              def compose(self):
                yield Header(Widget)
                yield Linem()
                yield Input('| ')
                
            if __name__ == '__main__':
              Lιuem().run()
            input()
            lαmlιuem()

          elif ιmαν == 'Logatr':
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
            input()
          
          elif ιmαν == 'Logatk':
            import tkinter.simpledialog
            import tkinter.messagebox
            lαuter = Tk()
            lαuter.title("Lιuem")
            lαuter.configure(bg = 'black')
            lαuter.attributes('-fullscreen',True)
            etiqueta = Label(lαuter, text = 'Lιuem', font = ('Source Code Pro', 13), fg = 'white', bg = 'black')
            etiqueta.place(anchor = NW)
            lαmlιuem()
          
          elif ιmαν == 'mpx':
            try:
              import os
              os.system(r"C:\Users\Leane\OneDrive\Escritorio\Logreuα\Mpxplay_v167_Win32_FFmpeg\mpxplayf.exe")
              print()

            except Exception as e:
              print()
              print(e)
              print()
              input()
              lαmlιuem()
          
          else:
            
            lαmlιuem()
            
            print('[#808080]|[/#808080] Vermαt [#808080]|[/#808080] Dyαtēν [#808080]|[/#808080] Augest [#808080]|[/#808080] Mυuιt [#808080]|[/#808080] Musselαιtμ [#808080]|[/#808080] Tαuder [#808080]|[/#808080] [purple]Vιαret[/purple] [#808080]|[/#808080] [purple]Qαmpαr[/purple] [#808080]|[/#808080] [blue]Stαuνor[/blue] [#808080]|[/#808080] [blue]Sedge[/blue] [#808080]|[/#808080] [blue]Iuslαg[/blue] [#808080]|[/#808080] [blue]Olyαν[/blue] [#808080]|[/#808080] [blue]DOS[/blue] [#808080]|[/#808080] [blue]Logαt[/blue] [#808080]|[/#808080] [red]δoνte[/red] [#808080]|[/#808080]')
            console.print('\u2500'*158, style='#24272d')
            print()
            console.print('\u2500'*158, style='#808080')
        
        except Exception as e:
          lαmlιuem()
          from rich import inspect
          console = Console()
          console.print(f'Aqtαlιν uα {ιmαν} dyαδᾱt ινyαre')
          print()
          inspect(e)
          sιg = input('| ')
          if sιg == 'sig':
            console.print_exception()
            input()
          else:
            pass
            lαmlιuem()

  Lιuem()

except Exception as e:

  from rich import inspect
  
  console = Console()
  console.print('Aqtαlιν uα Lιuem ιutαg')
  inspect(e)
  
  sιg = input('| ')
  
  if sιg == 'sig':
    console.print_exception()
    input()
  
  else:
    pass
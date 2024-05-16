#!/bin/bash

if [ $1 = "--help" ] || [ $1 = "-h" ]
then
    echo "katalogHTML.sh --help, katalogHTML.sh -h : Wywołanie pomocy"
    echo "katalogHTML.sh <-s|-r|-u> KATALOG [-c LISTA ROZSZERZEŃ]"
    echo
    echo "Pierwszy argument - wybór sortowania:"
    echo "  -s - sortowanie alfabetyczne;"
    echo "  -r - sortowanie odwrotne;"
    echo "  -u - brak sortowania."
    echo
    echo "Drugi argument - katalog, który ma zostać przetworzony."
    echo
    echo "Argument opcjonalny - dodatkowe rozszerzenia:"
    echo "  -c - utwórz dodatkową sekcję zawierającą pliki o podanych rozszerzeniach;"
    echo "  LISTA ROZSZERZEŃ - lista dodatkowych rozszerzeń, które mają zostać przetworzone."
else
    if [ $1 = "-s" ] || [ $1 = "-r" ] || [ $1 = "-u" ]
    then
        if [ -d $2 ]
        then
            graphics=(".png", ".gif", ".jpg", ".svg")
            music=(".mp3", ".ogg", ".flac")
            documents=(".pdf", ".odt", ".txt", ".docx", ".csv")
            for graphic_ext in ${graphics[@]}; do
                for file in $(find ${2} -name "*${graphic_ext}"); do
                    echo $file
                done
            done

            for music_ext in ${music[@]}; do
                for file in $(find ${2} -name "*${music_ext}"); do
                    echo $file
                done
            done

            for document_ext in ${documents[@]}; do
                for file in $(find ${2} -name "*${document_ext}"); do
                    echo $file
                done
            done

            if [ $3 = "-c" ]
            then
                directory=$2
                i=4
                j=$#
                shift 3
                while [ $i -le $j ] 
                do
                    echo "Ext: $1"
                    ext=$1
                    for file in $(find ${directory} -name "*${ext}"); do
                        echo $file
                    done
                    i=$((i + 1))
                    shift 1
                done
            fi

        else
            echo "Aby wywołać pomoc, uruchom używając składni katalogHTML.sh --help lub katalogHTML.sh -h"
        fi
    else
        echo "Aby wywołać pomoc, uruchom używając składni katalogHTML.sh --help lub katalogHTML.sh -h"
    fi
fi

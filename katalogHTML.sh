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
        sort=$1
        if [ -d $2 ]
        then
            graphics=(".png", ".gif", ".jpg", ".svg")
            music=(".mp3", ".ogg", ".flac")
            documents=(".pdf", ".odt", ".txt", ".docx", ".csv")
            echo -e "Name\tPath\tLast modified" > tmpimg.txt
            for graphic_ext in ${graphics[@]}; do
                for file in $(find ${2} -name "*${graphic_ext}"); do
                    for x in $(echo ${file} | tr "/" " "); do
                        name=$x
                    done
                    lastModified=$(ls -l "${file}" | tr -s " " | cut -d " " -f 6-8 | cat)
                    echo -e "${name}\t${file}\t${lastModified}" >> tmpimg.txt
                done
            done

            echo -e "Name\tPath\tLast modified" > tmpmusic.txt
            for music_ext in ${music[@]}; do
                for file in $(find ${2} -name "*${music_ext}"); do
                    for x in $(echo ${file} | tr "/" " "); do
                        name=$x
                    done
                    lastModified=$(ls -l "${file}" | tr -s " " | cut -d " " -f 6-8 | cat)
                    echo -e "${name}\t${file}\t${lastModified}" >> tmpmusic.txt
                done
            done

            echo -e "Name\tPath\tLast modified" > tmpdoc.txt
            for document_ext in ${documents[@]}; do
                for file in $(find ${2} -name "*${document_ext}"); do
                    for x in $(echo ${file} | tr "/" " "); do
                        name=$x
                    done
                    lastModified=$(ls -l "${file}" | tr -s " " | cut -d " " -f 6-8 | cat)
                    echo -e "${name}\t${file}\t${lastModified}" >> tmpdoc.txt
                done
            done

            customExts=()
            if [ $# -gt 2 ] && [ $3 = "-c" ]
            then
                directory=$2
                i=4
                j=$#
                shift 3
                while [ $i -le $j ] 
                do
                    customExts+=($1)
                    i=$((i + 1))
                    shift 1
                done
                for ext in ${customExts[@]};do
                    echo -e "Name\tPath\tLast modified" > "tmp${ext}.txt"
                    for file in $(find ${directory} -name "*${ext}"); do
                        for x in $(echo ${file} | tr "/" " "); do
                            name=$x
                        done
                        lastModified=$(ls -l "${file}" | tr -s " " | cut -d " " -f 6-8 | cat)
                        echo -e "${name}\t${file}\t${lastModified}" >> "tmp${ext}.txt"
                    done
                done
            fi

        if [ $sort = "-u" ]
        then
            cat tmpimg.txt | tail -n +2 | cat > img.txt
            cat tmpmusic.txt | tail -n +2 | cat > music.txt
            cat tmpdoc.txt | tail -n +2 | cat > doc.txt
            rm tmpimg.txt
            rm tmpmusic.txt
            rm tmpdoc.txt
            for ext in ${customExts[@]};do
                cat "tmp${ext}.txt" | tail -n +2 | cat > "${ext}.txt"
                rm "tmp${ext}.txt"
            done
        fi

        if [ $sort = "-s" ]
        then
            cat tmpimg.txt | tail -n +2 | sort -f -k 1 | cat > img.txt
            cat tmpmusic.txt | tail -n +2 | sort -f -k 1 | cat > music.txt
            cat tmpdoc.txt | tail -n +2 | sort -f -k 1 | cat > doc.txt
            rm tmpimg.txt
            rm tmpmusic.txt
            rm tmpdoc.txt
            for ext in ${customExts[@]};do
                cat "tmp${ext}.txt" | tail -n +2 | sort -f -k 1 | cat > "${ext}.txt"
                rm "tmp${ext}.txt"
            done
        fi

        if [ $sort = "-r" ]
        then
            cat tmpimg.txt | tail -n +2 | sort -f -r -k 1 | cat > img.txt
            cat tmpmusic.txt | tail -n +2 | sort -f -r -k 1 | cat > music.txt
            cat tmpdoc.txt | tail -n +2 | sort -f -r -k 1 | cat > doc.txt
            rm tmpimg.txt
            rm tmpmusic.txt
            rm tmpdoc.txt
            for ext in ${customExts[@]};do
                cat "tmp${ext}.txt" | tail -n +2 | sort -f -r -k 1 | cat > "${ext}.txt"
                rm "tmp${ext}.txt"
            done
        fi


        #tu zrób wypisywanie do hatemenela, najlepiej samo echo (będzie się można pochwalić że wypisuje do STDouta mmmmmm przekierowanie)


        rm img.txt
        rm music.txt
        rm doc.txt
        for ext in ${customExts[@]};do
            rm "${ext}.txt"
        done

        else
            echo "Aby wywołać pomoc, uruchom używając składni katalogHTML.sh --help lub katalogHTML.sh -h"
        fi
    else
        echo "Aby wywołać pomoc, uruchom używając składni katalogHTML.sh --help lub katalogHTML.sh -h"
    fi
fi

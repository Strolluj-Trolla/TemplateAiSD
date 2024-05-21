#!/bin/bash

if [ $# -eq 0 ] || [ $1 = "--help" ] || [ $1 = "-h" ];
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
    if [ $1 = "-s" ] || [ $1 = "-r" ] || [ $1 = "-u" ];
    then
        sort=$1
        if [ -d $2 ];
        then
            graphics=(".png" ".gif" ".jpg" ".svg")
            music=(".mp3" ".ogg" ".flac" ".wav")
            documents=(".pdf" ".odt" ".txt" ".docx" ".csv")
            echo -e "Name\tPath\tLast modified" > tmpimg.txt
            for graphic_ext in ${graphics[@]}; do
                find ${2} -name "*${graphic_ext}" > tmp.txt
                while read file; do #for file in $(find ${2} -name "*${graphic_ext}"); do
                    name=$(echo ${file} | tr "/" "\n" | tail -n 1)
                    lastModified=$(ls -l "${file}" | tr -s " " | cut -d " " -f 6-8 | cat)
                    echo -e "${name}\t${file}\t${lastModified}" >> tmpimg.txt
                done < "tmp.txt"
            done

            echo -e "Name\tPath\tLast modified" > tmpmusic.txt
            for music_ext in ${music[@]}; do
                find ${2} -name "*${music_ext}" > tmp.txt
                while read file; do #for file in $(find ${2} -name "*${music_ext}"); do
                    name=$(echo ${file} | tr "/" "\n" | tail -n 1)
                    lastModified=$(ls -l "${file}" | tr -s " " | cut -d " " -f 6-8 | cat)
                    echo -e "${name}\t${file}\t${lastModified}" >> tmpmusic.txt
                done < "tmp.txt"
            done

            echo -e "Name\tPath\tLast modified" > tmpdoc.txt
            for document_ext in ${documents[@]}; do
                find ${2} -name "*${document_ext}" > tmp.txt
                while read file; do #for file in $(find ${2} -name "*${document_ext}"); do
                    name=$(echo ${file} | tr "/" "\n" | tail -n 1)
                    lastModified=$(ls -l "${file}" | tr -s " " | cut -d " " -f 6-8 | cat)
                    echo -e "${name}\t${file}\t${lastModified}" >> tmpdoc.txt
                done < "tmp.txt"
            done

            customExts=()
            if [ $# -gt 2 ] && [ $3 = "-c" ];
            then
                directory=$2
                i=4
                j=$#
                shift 3
                while [ $i -le $j ];
                do
                    customExts+=($1)
                    i=$((i + 1))
                    shift 1
                done
                for ext in ${customExts[@]};do
                    echo -e "Name\tPath\tLast modified" > "tmp${ext}.txt"
                    find ${directory} -name "*${ext}" > tmp.txt
                    while read file;do #for file in $(find ${directory} -name "*${ext}"); do
                        name=$(echo ${file} | tr "/" "\n" | tail -n 1)
                        lastModified=$(ls -l "${file}" | tr -s " " | cut -d " " -f 6-8 | cat)
                        echo -e "${name}\t${file}\t${lastModified}" >> "tmp${ext}.txt"
                    done < "tmp.txt"
                done
            fi

        if [ $sort = "-u" ];
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

        if [ $sort = "-s" ];
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

        if [ $sort = "-r" ];
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
        
        #------
        
        echo "<!DOCTYPE html><html lang='pl'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>Katalog HTML</title><style>body {background-color: #151515;}header {text-align: center;}.block {width: 100%;border-radius: 40px;background-color: #A91D3A; text-align: center; display: flex; margin: 20px; justify-content: center; flex-wrap: wrap;} .item {margin: 10px; width: 20%; text-align: center; border-radius: 20px;background-color: #C7B7A3; }</style></head><body><header><h1 style='color: #C7B7A3;'>Katalog HTML</h1></header><main>"
        if [ ${#customExts[@]} -ne 0 ]
        then
            for ext in ${customExts[@]};do
                echo " <div class='block'>"
                echo " <div style='width: 100%'><h1>Pliki $ext </h1><br></div>"

                length=$(cat "${ext}.txt" | wc -l)
                i=1
                while [ $i -le $length ]; do
                    name=$(cat "${ext}.txt" | tail -n+${i} | head -n 1 | cut -f 1)
                    file=$(cat "${ext}.txt" | tail -n+${i} | head -n 1 | cut -f 2)
                    date=$(cat "${ext}.txt" | tail -n+${i} | head -n 1 | cut -f 3)
                    i=$(($i+1))
                    echo "<div class='item'>"
                    echo "<h2> ${name} </h2><a href='${file}'>${file} </a><p> ${date}</p></div>"
                done
                echo "</div>"
            done
        fi
        

        echo " <div class='block'>"
        echo " <div style='width: 100%'><h1>Pliki tekstowe</h1><br></div> "
        length=$(cat doc.txt | wc -l)
        i=1
        while [ $i -le $length ]; do
            name=$(cat doc.txt | tail -n+${i} | head -n 1 | cut -f 1)
            file=$(cat doc.txt | tail -n+${i} | head -n 1 | cut -f 2)
            date=$(cat doc.txt | tail -n+${i} | head -n 1 | cut -f 3)
            i=$(($i+1))
            echo "<div class='item'>"
            echo "<h2> ${name} </h2><a href='${file}'>${file} </a><p> ${date}</p></div>"
        done
        echo "</div>"


        echo " <div class='block'>"
        echo " <div style='width: 100%'><h1>Pliki dźwiękowe</h1><br></div> "
        length=$(cat music.txt | wc -l)
        i=1
        while [ $i -le $length ]; do
            name=$(cat music.txt | tail -n+${i} | head -n 1 | cut -f 1)
            file=$(cat music.txt | tail -n+${i} | head -n 1 | cut -f 2)
            date=$(cat music.txt | tail -n+${i} | head -n 1 | cut -f 3)
            i=$(($i+1))
            echo "<div class='item'>"
            echo "<h2> ${name} </h2><a href='${file}'>${file} </a><p> ${date}</p></div>"
        done
        echo "</div>"


        echo " <div class='block'>"
        echo " <div style='width: 100%'><h1>Pliki graficzne</h1><br></div> "
        length=$(cat img.txt | wc -l)
        i=1
        while [ $i -le $length ]; do
            name=$(cat img.txt | tail -n+${i} | head -n 1 | cut -f 1)
            file=$(cat img.txt | tail -n+${i} | head -n 1 | cut -f 2)
            date=$(cat img.txt | tail -n+${i} | head -n 1 | cut -f 3)
            i=$(($i+1))
            echo "<div class='item'>"
            echo "<h2> ${name} </h2><a href='${file}'>${file} </a><p> ${date}</p>"
            echo "<img src='${file}' width="200"></img></div>"
        done
        echo "</div>"

        echo " </main></body></html> "
        
        #------
        rm tmp.txt
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

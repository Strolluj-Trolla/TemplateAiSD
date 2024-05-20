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
                    for file in $(find ${directory} -name "*${ext}"); do
                        for x in $(echo ${file} | tr "/" " "); do
                            name=$x
                        done
                        lastModified=$(ls -l "${file}" | tr -s " " | cut -d " " -f 6-8 | cat)
                        echo -e "${name}\t${file}\t${lastModified}" >> "tmp${ext}.txt"
                    done
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
            
                while read p; do
                    sp=($p)
                    echo "<div class='item'>"
                    echo "<h2> ${sp[0]} </h2><a href='${sp[1]}'>${sp[1]} </a><p> ${sp[2]} ${sp[3]} ${sp[4]}</p></div>"
                done < "${ext}.txt"
                echo "</div>"
            done
        fi
        

        echo " <div class='block'>"
        echo " <div style='width: 100%'><h1>Pliki tekstowe</h1><br></div> "
        while read p; do
            sp=($p)
            echo "<div class='item'>"
            echo "<h2> ${sp[0]} </h2><a href='${sp[1]}'>${sp[1]} </a><p> ${sp[2]} ${sp[3]} ${sp[4]}</p></div>"
        done < doc.txt
        echo "</div>"


        echo " <div class='block'>"
        echo " <div style='width: 100%'><h1>Pliki dźwiękowe</h1><br></div> "
        while read p; do
            sp=($p)
            echo "<div class='item'>"
            echo "<h2> ${sp[0]} </h2><a href='${sp[1]}'>${sp[1]} </a><p> ${sp[2]} ${sp[3]} ${sp[4]}</p></div>"
        done < music.txt
        echo "</div>"


        echo " <div class='block'>"
        echo " <div style='width: 100%'><h1>Pliki graficzne</h1><br></div> "
        while read p; do
            sp=($p)
            echo "<div class='item'>"
            echo "<h2> ${sp[0]} </h2><a href='${sp[1]}'>${sp[1]} </a><p> ${sp[2]} ${sp[3]} ${sp[4]}</p>"
            echo "<img src='${sp[1]}' width="200"></img></div>"
        done < img.txt
        echo "</div>"

        echo " </main></body></html> "
        
        #------
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

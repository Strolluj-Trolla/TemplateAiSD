def insertionSort(tab):

    n=len(tab)-1

    for j in range(n-1, -1, -1):
        x=tab[j]
        i=j+1
        while (i<len(tab)) and (x>tab[i]):
            tab[i-1]=tab[i]
            i+=1

        tab[i-1]=x
    return
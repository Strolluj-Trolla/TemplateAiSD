from random import randint;

def quickSortRand(tab, start, end):

    pivot=tab[randint(start, end)]
    i=start
    j=end

    while i<=j:
        while(tab[i]>pivot):
            i+=1
        while(tab[j]<pivot):
            j-=1

        if(i<=j):
            tab[i], tab[j]= tab[j], tab[i]
            i+=1
            j-=1

    if i<end:
        quickSortRand(tab, i, end)
    if j>start:
        quickSortRand(tab, start, j)
    return

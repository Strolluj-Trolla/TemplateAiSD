def quickSortLeft(tab, start, end):

    pivot=tab[start]
    
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
        quickSortLeft(tab, i, end)
    if j>start:
        quickSortLeft(tab, start, j)
    return
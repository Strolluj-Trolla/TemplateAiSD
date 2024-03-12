def shellSort(tab):

    n=len(tab)-1
    sedge=[1]
    l=0
    i=0;
    while i<n:
        i=4**(l+1)+3*2**l+1
        sedge.append(i)
        l+=1
    sedge.pop(l)
    l-=1

    while l>=0:
        for j in range(n-1, -1, -sedge[l]):
            x=tab[j]
            i=j+sedge[l]
            while (i<len(tab)) and (x>tab[i]):
                tab[i-sedge[l]]=tab[i]
                i+=sedge[l]

            tab[i-sedge[l]]=x
        l-=1
    return

import random
import time
from plecak import plecak

'''while(True):
    print("Wybier sposób wprowadzenia plecaka:")
    print("0 - z klawiatury")
    print("1 - z pliku")
    print("2 - wyjdź")
    x=input()
    try:
        x=int(x)
        if(x>=0 and x<=2):
            break
        else:
            print("Należy wpisać 0, 1 lub 2.")
    except ValueError:
        print("Należy wpisać 0, 1 lub 2.")
(bp,n,b)=(0,0,0)
if(x==0):
    (bp,n,b)=from_input()
elif(x==1):
    (bp,n,b)=from_file("bp.txt")
if(x!=2):
    solutions=[]
    names=["programowania dynamicznego","zachłanny","siłowy"]
    solutions.append(dynamic(bp,n,b))
    solutions.append(greedy(bp.copy(),n,b))
    solutions.append(brute(bp,n,b))
    for i in range(3):
        print(f"*** Algorytm {names[i]} ***")
        print("    Elementy wybrane:")
        for item in solutions[i][0]:
            print(f"        Rozmiar: {item[1]}, Wartość: {item[0]}")
        print(f"    Sumaryczny rozmiar: {solutions[i][1]}")
        print(f"    Wartość funkcji celu: {solutions[i][2]}")'''
#(bp,n,b)=gen(10,10)
#(bp,n,b)=([[3, 6], [9, 2], [4, 7], [2, 5], [4, 4], [3, 3], [8, 4], [4, 2], [8, 4], [3, 4]], 10, 10)
backpack=plecak([[5, 9], [10, 1], [10, 5], [10, 10], [4, 9], [4, 7], [6, 4], [5, 1], [6, 4], [1, 6]], 10 ,10)
print(backpack.dynamic())
print(backpack.greedy())
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:28:53 2021

@author: Mehmet Öztürk
"""
import itertools
import random

giris=""
while(len(giris)<5):
    giris=input("Lütfen en az 5 karakterlik bir değer giriniz: ")

palindromlar=[]

for i in range(5,len(giris)+1):
    kelime=[]
    kelimeler=[]

    for j in giris:
        kelime.append(j)
    kelimeler=list(itertools.permutations(kelime,i))
    for k in kelimeler:
        if(k==k[::-1]):
            if(k not in palindromlar):
                palindromlar.append(k)
            
palindromKelimeler=[]
for i in palindromlar:
    pal=""
    for j in i:
        pal+=j
    palindromKelimeler.append(pal)
    print(pal)    


if(len(palindromKelimeler)==0):
    print("Girilen değerden palindrom kelime üretilemedi.")
    
    
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:05:46 2018

@author: ozgenurc
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)

#Kısıt fonksiyonlarımızın tanımlanması.
y1 = 4 - 2*x
y2 = 3 - 0.5*x
y3 = 1 -x

#2 fonksiyon arasındaki en düşük nokta--altını çizdirmek için kullandığımız metod.
y4 = np.minimum(y1, y2)

#y eksenine limit koyuyoruz--eksili değerler çıkmasın--1. bölgede işlemleri yapabilmek için.
plt.ylim(0, 5)

#Fonksiyonlarımızı çizdiriyoruz.
plt.plot(x, y1,
         x, y2,
         x, y3)

#3 kısıt fonksiyonu arasında tarama işlemi
plt.fill_between(x, y3, y4, color='grey', alpha='0.5')

#Amaç fonksiyonumuzunsonucunu bulan metod 
def amac(x,y):
    z=7*x+6*y
    return z

print ("Amaç Fonksiyonumuz:" , "Z=(6x+7y)max")
print ("Kısıt Denklemlerimiz:" , "y<=4-2x" 
                               , "y<=3-0.5x" 
                               , "y>=1-x")
plt.show()
print ("ÇözümKümesi={(2,0),(0,3),(0,1),(0.6,2.6),(1,0)}" )
print ("Z(2,0):", amac(2,0))
print ("Z(0,3):", amac(0,3))
print ("Z(0,1):", amac(0,1))
print ("Z(1,0):", amac(1,0))
print ("Z(0.6,2.6):", amac(0.6,2.6))
list =[14,16,6,7,19.8]
print( "Maximum Değer=" , max(list))
print( "Minimum Değer=" , min(list))
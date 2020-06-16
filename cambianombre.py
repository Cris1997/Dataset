#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 13:54:05 2019

@author: cristianrosales
"""

import os

def list_files(dir):
    fnames = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            fnames.append(os.path.join(name))
    return fnames



dir='/Users/cristianrosales/Desktop/Recuperados/REs'
fnames=list_files(dir)
#print(len(fnames))
numero = 1
for item in fnames:
    ruta = dir + '/' + item
    rutanuevo = dir +'/10_' + str(numero) + '.JPG'
    os.rename(ruta, rutanuevo)
    #print(ruta)
    #print(rutanuevo)
    numero = numero +1
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:02:37 2023

@author: GTong
"""
import secrets


path = 'random_plaintext.txt'
f = open(path, 'w')

nb = 5000 # Number of random plaintext you need

pt = secrets.token_hex(16)

pt = secrets.token_hex(16)

for i in range (0,nb):
    pt = secrets.token_hex(16)
    f.write(pt)
    if(i < nb-1):
        f.write('\n')
f.close()
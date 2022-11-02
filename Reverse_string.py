# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 23:18:58 2021

@author: DELL
"""

def reverse_string(a):
    words = a.split(' ')
    
    print("words:", words)
    
    reverse_str = ' '.join(reversed(words))
    
    print("Reversed String:", reverse_str)


orig_string = "Rabin is good in Go-Lang and Python"
reverse_string(orig_string)
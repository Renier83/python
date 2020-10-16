# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 06:54:47 2020

@author: renie
"""

user_play = "y"

start_number = 0


while user_play == "y":

    user_number = int(input(" How many numbers?"))
    
    for x in range(start_number, int(user_number) + start_number):
    
        print(x)
        
    start_number = start_number + int(user_number)
    
        
    user_play = input(" Continue : (y)es or (n)o? ")
    
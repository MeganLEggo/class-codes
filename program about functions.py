#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:01:25 2024

@author: lanem3406
"""

def main():
    print('program greets user then gets numbers')
    
    #call greeting function
    greeting()
    
    n1, n2 = get_nums()
    
    #gadd nums
    total = n1 + n2
    print(total)

def greeting():
    '''
    no arg should be passed
    asks for name and greets user
    

    Returns
    -------
    None.

    '''   
    name = input("name? ")
    print("hello", name)

def get_nums():
    '''
    gets 2 nums
    
    Returns
    -------
    num1 : TYPE INT
        DESCRIPTION.
    num2 : TYPE INT
        DESCRIPTION.

    '''
    
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    
    return num1, num2
    
main()    
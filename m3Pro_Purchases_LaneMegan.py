#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:06:07 2024

@author: lanem3406
"""

# This project lists books authors prices and publishing dates.
# 9/25/2024
#CSC-121 m3Pro - Purchases
# Megan Lane


# The import of the defined functions for this program
# Makes it look well organized
import def_m3Pro_Purchases_LaneMegan as df

# four lists that are associated with real like book info
authors = ["William Shakespeare", "Charles Dickens", "James Joyce", "Earnest Hemingway", "J.K. Rowling"]
books = ["Hamlet", "A Tale of Two Cities", "Ulysses", "The Old Man and the Sea", "Harry Potter and the Philosopher's Stone"]
published = [1601, 1859, 1922, 1952, 1997]
prices  = [14.52, 9.56, 19.97, 10.35, 16.62]
# list for multiple selections
book_nums = []

# The main to run the program
def main():
    # run the display for all the lists
    df.book_display(books, authors, published, prices)
    
    # start the program
    choice = "y"

    # Give the user the option to choose multiple books with a loop
    while choice != "n":
        book_num = int(input("Enter the Num of the book you want to buy: "))
        
        book_nums.append(book_num-1)
        choice = input("Would you like to purchase another book? (y/n): ")
       
    #Shows the selected books info
    df.show_purchase(book_nums, books, authors, published, prices)
       
    #Calculates the total and the taxed total of selected books
    df.total(book_nums, prices)
    
# If This program is modularized, or imported, will allow specific 
# functions to be ran instead of just main :D
if __name__ == '__main__':
    main()
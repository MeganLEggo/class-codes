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
#

authors = ["William Shakespeare", "Charles Dickens", "James Joyce", "Earnest Hemingway", "J.K. Rowling"]
books = ["Hamlet", "A Tale of Two Cities", "Ulysses", "The Old Man and the Sea", "Harry Potter and the Philosopher's Stone"]
published = [1601, 1859, 1922, 1952, 1997]
prices  = [14.52, 9.56, 19.97, 10.35, 16.62]

book_nums = []


def main():
    book_display()

    choice = "y"

    while choice != "n":
        book_num = int(input("Enter the Num of the book you want to buy: "))
        
        book_nums.append(book_num-1)
        choice = input("Would you like to purchase another book? (y/n): ")
        
    show_purchase(book_nums)
        
    total(book_nums)
    
def book_display():
    print(f'{"Num":<15}{"Books":<45}{"Authors":<30}{"Published":<15}{"Prices":<15}')
    print('-'*115)
    for i in range(len(books)):
        print(f'{i+1:<15}{books[i]:<45}{authors[i]:<30}{published[i]:<15}{prices[i]}')
    print('-'*115)

    

def show_purchase(book_nums):
    print(f'\n{"Books":<45}{"Authors":<30}{"Published":<15}{"Prices":<15}')
    print('-'*115)
    for i in book_nums:
        print(f'{books[i]:<45}{authors[i]:<30}{published[i]:<15}{prices[i]}')
        
def total(book_nums):
    for i in book_nums:
        prices[i]
        total = prices[i] + 0
        

    print("Total price (cost of books(s) + 5% tax): ")    
    print(total)


if __name__ == '__main__':
    main()
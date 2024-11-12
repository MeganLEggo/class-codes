# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:12:53 2024

@author: megan
"""

def book_display(books, authors, published, prices):
    '''
    #Function that displays the following lists

    Parameters
    ----------
    books : LIST
        List of book titles
    authors : LIST
        List of authors assoc with book titles
    published : LIST
        List of the year the books were published in assoc with book titles
    prices : LIST
        List of prices assoc with book titles

    Returns
    -------
    None.

    '''
    print(f'{"Num":<15}{"Books":<45}{"Authors":<30}{"Published":<15}{"Prices":<15}')
    print('-'*115)
    for i in range(len(books)):
        print(f'{i+1:<15}{books[i]:<45}{authors[i]:<30}{published[i]:<15}{prices[i]}')
    print('-'*115)

    

def show_purchase(book_nums, books, authors, published, prices):
    '''
    #Function that displays the following info for selected books

    Parameters
    ----------
    books : LIST
        List of book titles
    authors : LIST
        List of authors assoc with book titles
    published : LIST
        List of the year the books were published in assoc with book titles
    prices : LIST
        List of prices assoc with book titles

    Returns
    -------
    None.

    '''
    # well spaced list header
    print(f'\n{"Books":<45}{"Authors":<30}{"Published":<15}{"Prices":<15}')
    #underline
    print('-'*115)
    # displays all inside the list, equally well spaced
    for i in book_nums:
        print(f'{books[i]:<45}{authors[i]:<30}{published[i]:<15}{prices[i]}')
        
def total(book_nums, prices):
    '''
    #Function that determines the total price and total taxed price for selected books

    Parameters
    ----------
    books : LIST
        List of book titles
    authors : LIST
        List of authors assoc with book titles
    published : LIST
        List of the year the books were published in assoc with book titles
    prices : LIST
        List of prices assoc with book titles

    Returns
    -------
    None.

    '''
    # A running total
    
    totals = 0 #counter
    for i in book_nums: #adds all the selected prices together
        totals += prices[i]
        
    # Determines tax based on total amount
    tax = 0.05 * totals
    # Adds tax to total
    tax_and_totals = tax + totals
        

    print("\n\nTotal price (cost of books(s) + 5% tax): ")    
    print(f"Book(s) cost Before Tax ${totals:.2f}")
    print(f"Tax ${tax:.2f}")
    print(f"Total After Tax ${tax_and_totals:.2f}")
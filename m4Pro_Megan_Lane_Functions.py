# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:41:41 2024

@author: megan
"""
def menu():
    '''
    Displays a menu for the while loop to start the program
    and reference the other functions that analyze the 
    nested dict

    Returns
    -------
    None.

    '''
    print('\n',"----------MENU----------")
    print("1) Display Book Inventory and Calculate Total")
    print("2) Lookup by Author and Get Total")
    print("3) Lookup by Book Name and Get Total")
    print("4) Lookup By Price Range")
    print("5) Exit", '\n')
    
    
    
def first(book_inventory):
    '''
    Makes the nested dic a table/graph

    Parameters
    ----------
    book_inventory : DICT
        A nested dictonary: {x:[{}]} format

    Returns
    -------
    None.

    '''
    # header
    print(f"{'Author':<30}{'Book':<45}{'Year':<10}{'Price':<10}{'Quantity'}")
    print("-"*110)
    total = 0 # counter
    # unpacks the nested dict
    for authors, books in book_inventory.items():
       for book in books:
           print(f"{authors:<30}{book['book_name']:<45}{book['year_pub']:<10}{book['price']:<10}{book['quantity']}", end='\n')
           # accounts for the total cost value of all books on file
           total =+ book['price']*book['quantity']
    print("-"*110)
    #calc the total after counting
    print(f'{"Overall Total":<95}${total:.2f}')
    
    
    
def second(book_inventory):
    '''
    User can specify author
    Then creates a table of all books by that author

    Parameters
    ----------
    book_inventory : DICT
        A nested dictonary: {x:[{}]} format

    Returns
    -------
    None.

    '''
    #user input
    authors = input('Enter author name: ')
    print(' ')
      # if author is found unpack the books
    if authors in book_inventory:
        print(f"{'Book':<45}{'Year':<10}{'Price':<10}{'Quantity'}")
        print('-'*75)
        total = 0
        for book in book_inventory[authors]:
            print(f"{book['book_name']:<45}{book['year_pub']:<10}{book['price']:<10}{book['quantity']}", end='\n')
            total += book['price']*book['quantity']
        print('-'*75)
        print(f'{"Total":<65}${total:.2f}\n')
        # A nested if statement if author is not found
        if authors not in book_inventory:
            print("No books for author mentioned")
            authors = input('Enter another author name: ')
        
        
        
def third(book_inventory):
    '''
    Looks for the specific book taken from input from a user

    Parameters
    ----------
    book_inventory : DICT
        A nested dictonary: {x:[{}]} format

    Returns
    -------
    None.

    '''
    #input from the user for a specific book name
    book_title = input('Enter the book name: ')
    print(' ')
      
    # Makes a new list via a list comphrehension to use to unpackage the code
    # Avoids running into the issue of the code iterating over the entire book_inventory
    book_info = [
    {**book, "author": author} 
    for author, books in book_inventory.items() 
    for book in books 
    ]
    
#Unpacking the information if the book exists
    if book_info:
        info = book_info[0]
        # A nested if statement if the input is invalid
        if info["book_name"] != book_title:
            print("Book not found.")
            book_title = input('Enter a book name again: ')# Get the first match
        #header
        print(f"{'Author':<30}{'Book':<45}{'Year':<10}{'Price':<10}{'Quantity'}")
        print("-"*110)
        total = 0 #initilized  the var
        # pasting info copied to the list
        print(f"{info['author']:<30}{info['book_name']:<45}{info['year_pub']:<10}{info['price']:<10}{info['quantity']}", end='\n')
        total += info['price']*info['quantity']
        print('-'*110)
        print(f'{"Total":<95}${total:.2f}')

       
def fourth(book_inventory):
    '''
    Evalues books in price range suggested by the user

    Parameters
    ----------
    book_inventory : DICT
        A nested dictonary: {x:[{}]} format

    Returns
    -------
    None.

    '''
    # 2 inputs from user to identify the price range
    start_range = float(input("Enter Starting Range: "))
    print(' ')
    end_range = float(input("Enter last number in lookup range: "))
    print(' ')
    # header
    print(f"{'Author':<30}{'Book':<45}{'Year':<10}{'Price':<10}{'Quantity'}")
    print('-'*110)
    
    count = 0 # counter
    # unpacks all the books in the price range
    for author, books in book_inventory.items():
        for book in books:
            # only display books on the price range
            if start_range <= book["price"] <= end_range:
                count += 1
                print(f"{author:<30}{book['book_name']:<45}{book['year_pub']:<10}{book['price']:<10}{book['quantity']}", end='\n')
                
                if count == 0:
                    print('No books in price range found.')
                    start_range = float(input("Enter a new Starting Range: "))
                    print(' ')
                    end_range = float(input("Enter the new last number in lookup range: "))
                    print(' ') 
    # get the total counted from displayed books, does not include quantity
    print('-'*110) 
    print(f"\nNumber of books priced between {start_range} and {end_range} is {count}")
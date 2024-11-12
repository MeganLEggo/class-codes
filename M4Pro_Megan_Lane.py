# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 17:05:21 2024

@author: megan
"""
#importing 
import m4Pro_Megan_Lane_Functions as F
# The main function
def main():
    # The nested dictionary: dict containing a key and a value of a list containing several dict
    book_inventory = {"William Shakespear": [
        {"book_name": "Hamlet", "year_pub": 1601, "price":14.52, "quantity":43},
        {"book_name": "Macbeth", "year_pub": 1606, "price":13.45, "quantity":50},
        {"book_name": "Othello", "year_pub": 1604, "price":15.30, "quantity":37},
        {"book_name": "Romeo and Juliet", "year_pub": 1597, "price":12.99, "quantity":60}
        ],
        
        "Charles Dickens": [
        {"book_name": "A tale of Two Cites", "year_pub": 1859, "price":9.56, "quantity":75},
        {"book_name": "Great Expectations", "year_pub": 1861, "price":12.50, "quantity":60},
        {"book_name": "Oliver Twist", "year_pub": 1837, "price":9.75, "quantity":50},
        {"book_name": "David Copperfield", "year_pub": 1850, "price":12.25, "quantity":40}
        ],
        
        "James Joyce": [
        {"book_name": "Ulysses", "year_pub": 1922, "price":19.99, "quantity":30},
        {"book_name": "A Portrait of the Artust as a Young Man", "year_pub": 1916, "price":13.50, "quantity":25},
        {"book_name": "Dubliners", "year_pub": 1914, "price":12.00, "quantity":35},
        {"book_name": "Finnegans Wake", "year_pub": 1939, "price":16.50, "quantity":20}
        ],
        
        "Ernest Hemingway": [
            {"book_name": "The Old Man and the Sea", "year_pub": 1952, "price":10.35, "quantity":80},
            {"book_name": "A Farewell to Arms", "year_pub": 1929, "price": 14.75, "quantity": 45},
            {"book_name": "For Whom the Bell Tolls", "year_pub": 1940, "price":13.50, "quantity":50},
            {"book_name": "The Sun Also Rises", "year_pub": 1926, "price":12.99, "quantity":55}
        ],
        
        "J.K. Rowling": [
            {"book_name": "Harry Potter and the Philosopher's Stone", "year_pub": 1997, "price":16.62, "quantity":100},
            {"book_name": "Harry Patter and the Chamber of Secrets", "year_pub": 1998, "price":22.99, "quantity":90},
            {"book_name": "Harry Potter and the Prisone rof Azkaban", "year_pub": 1999, "price":23.99, "quantity":85},
            {"book_name": "Harry Potter and the Goblet of Fire", "year_pub": 2000, "price":25.99, "quantity":80}
        ]
    }
    # value to initalize the while loop
    choice = 0
    while choice != 5:
        # runs the menu
        F.menu()
        # ask for the menu option
        choice = int(input("What is your choice? "))
        print('\n\n')
        # evaluates the choice choosen above
        if choice == 1:
            F.first(book_inventory)
        elif choice == 2:
            F.second(book_inventory)
        elif choice == 3:
            F.third(book_inventory)
        elif choice == 4:
            F.fourth(book_inventory)
        elif choice == 5:
            print('bye')
        else: 
            # if there is an invalid choice asks for the user to re-enter choice
            print("invalid")
            choice = int(input("What is your choice? "))
            

            
          
if __name__ == "__main__":
    main()

import csv

#lists
authors = ["William Shakespeare","Charles Dickens","James Joyce","Earnest Hemingway","J.K. Rowling"]

books = ["Hamlet","A Tale of Two Cities","Ulysses","The Old Man and the Sea","Harry Potter and the Philosopher’s Stone"]

published = [1601, 1859, 1922, 1952, 1997]
#list of book names

#list referencing book prices
prices =[14.52, 9.56, 19.97, 10.35, 16.62]
    
def menu():
    '''
    Displays a menu for the user to choose from (could identify as a var...)

    Returns
    -------
    None.

    '''
    print('-'*14,'Menu','-'*20)
    print('1)Display Book Enventory (Create Reports)')
    print('2)Purchase Book(s)')
    print('3)Display list of purchases, Total Cost & Write Report')
    print('4)Exit')
    print('-'*40)

def one():
    '''
    converts the book display to a txt file manually...

    Returns
    -------
    None.

    '''
    #open the txt file to write in
    enventory_t = open('enventory.txt','w')
    #display to indicate success
    print(f'{"Num":<5}{"Book":<60}{"Author":<30}{"Year":<8}{"Price"}')
    print('-'*120)
    #iterates the lists
    for i in range(len(authors)):
            print(f'{i+1:<5}{books[i]:<60}{authors[i]:<30}{published[i]:<8}${prices[i]}')
    print('-'*120,'\n')
    
    
    #write to the file finally... 
    enventory_t.write(f'{"Num":<5}{"Book":<60}{"Author":<30}{"Year":<8}{"Price"}\n')
    enventory_t.write('-'*120+'\n')
    #iterates the lists
    for i in range(len(authors)):
            enventory_t.write(f'{i+1:<5}{books[i]:<60}{authors[i]:<30}{published[i]:<8}${prices[i]}\n')
    enventory_t.write('-'*120+'\n')
    
    #opens the csv file to write in
    enventory_c = open('enventory.csv','w',newline='')
    # uses the csv writer
    active = csv.writer(enventory_c)
    # write
    active.writerow(["Num", "Books", "Author", "Year", "Price"])
    #iterates the lists
    for i in range(len(authors)):
        active.writerow([i+1, books[i], authors[i], published[i], prices[i]])
    
    # close the files
    enventory_t.close()
    enventory_c.close()
    
def two(book_nums):
    again = 'y'
        #ask user to enter book num
    while again == 'y':
        book_num = int(input("\nEnter number of book you want to buy: "))
            # append to book_nums after subtracting 1 (to get accurate index num)
    
        
    
            # find book info (in all lists)
    
        book_num -= 1
    
        book_nums.append(book_num)
    
        again = input("\nWould you like to purchase another book? (y for yes) :")
    
        #pass to show_purchase function
    
    show_purchase(book_nums)
    cost, tax, total = totals(book_nums)

    
    report(cost, tax, total)
    
def three(book_nums, cost, total, tax):
    '''
    Takes the conclusion of the two() function and transverse the purchase a csv

    Parameters
    ----------
    book_nums : list
        Contains the copied books, can duplicate books! :D
    cost : var
        after iterating the books and adding the price, overall cost
    total : var
        The total is the valueof the cost and the tax
    tax : var
        tax calculated by multiplying the cost by 0.05 (5%)

    Returns
    -------
    None.

    '''
    # two is required for three to work
    
    # identify the variables from the total function
    cost, tax, total = totals(book_nums)
    # run the report for display for the user
    report()
    # open the csv files
    purchased_c = open('purchased.csv','w', newline='')
    # use the csv writer
    purch_rep = csv.writer(purchased_c)
    # header written
    # iterate the options
    purch_rep.writerow(["Num", "Books", "Author", "Year", "Price"])
    for i in book_nums:
        purch_rep.writerow([i+1, books[i], authors[i], published[i], prices[i]])
    # the conclusion, it actually worked to add the blanks to skip the square :D
    purch_rep.writerow(["Cost:", " ", " ", " ", cost])
    purch_rep.writerow(["Tax:", " ", " ", " ", tax])
    purch_rep.writerow(["Cost:", " ", " ", " ", total])
    
def book_display():
    '''
    function displays book information. Information retrieved from 4 different lists

    Returns
    -------
    None.

    '''


    print(f'{"Num":<5}{"Book":<60}{"Author":<30}{"Year":<8}{"Price"}')
    print('-'*120)

    for i in range(len(authors)):
            print(f'{i+1:<5}{books[i]:<60}{authors[i]:<30}{published[i]:<8}${prices[i]}')
    print('-'*120,'\n')

def show_purchase(book_nums):
    '''

    Parameters
    ----------
    book_nums : list , references index number for books user wants to purchase
    
    function displays information on the books selected

    Returns
    -------
    None.

    '''

    # create
    print()

    print(f'{"Book":<60}{"Author":<30}{"Year":<8}{"Price"}')
    print('-'*115)

    for i in book_nums:

        print(f'{books[i]:<60}{authors[i]:<30}{published[i]:<8}${prices[i]}')

def totals(book_nums):
    '''
    

    Parameters
    ----------
    book_nums : list , references index number for books user wants to purchase

    Returns
    -------
    cost : price total for books chosen
    tax : 5% tax on total price
    total : cost + tax

    '''

    pur_prices = []

    for i in book_nums:
        # get prices
        price = prices[i]

        pur_prices.append(price)

    # add cost of both books

    cost = sum(pur_prices)
    cost = round(cost, 2)
    tax = cost * 0.05
    tax = round(tax, 2)
    total = cost + tax

    return cost, tax, total

def report(cost,tax,total):
    '''
    the report display calcuated and displayed for the user
   

    Parameters
    ----------
    cost : var
        after iterating the books and adding the price, overall cost
    total : var
        The total is the valueof the cost and the tax
    tax : var
        tax calculated by multiplying the cost by 0.05 (5%)

    Returns
    -------
    None.

    '''
   
    print("\nTotal price (cost of book(s) + 5% tax):")
    print(f'Book(s) cost Before Tax ${cost:,.2f}')
    print( f'Tax ${tax:,.2f}')
    print(f'Total After Tax ${total:,.2f}\n')
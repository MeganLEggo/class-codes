ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5

import csv
import M5Pro_Functions as fn

def main():
    
    


    #display book list

    fn.book_display()

    book_nums = []
    
    cost, tax, total = fn.totals(book_nums)
    totally = fn.report(cost, tax, total)

    run_again = 0


    while run_again != 4:
        try:   
            fn.menu()
    
            run_again = int(input("Which menu item did you want (1,2,3,4): "))
        except:
            print("Input must be a number!!")
            run_again = input("Which menu item did you want (1,2,3,4): ")
        
        if run_again == ONE:
            fn.one()
            
        elif run_again == TWO:
            fn.two(book_nums)
            
        elif run_again == THREE:
            fn.three(book_nums, cost, total, tax, totally)
            
        elif run_again == FOUR:
            print('Terminating...')
        else:
            try:
                print("Invalid input!!")
                run_again = input("Which menu item did you want (1,2,3,4): ")
            except:
                print("Input must be a number!!")
                run_again = input("Which menu item did you want (1,2,3,4): ")
        

            


# Call the main function.
if __name__ == "__main__":
    main()


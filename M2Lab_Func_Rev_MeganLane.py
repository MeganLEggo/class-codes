# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:16:36 2024

@author: megan
"""

# description
# 9/14/2024
# CSC121 M2LAB_Func_Rev_MeganLane.py
# Megan Lane

# import the other functions
import def_file_M2Lab as df

# This is the main function

def main():
    # the while loop variable is starts on, or 1
    menu = 1
    # as long as the loop is not 2, it will run
    while menu != 2:
        print("\nMENU ----------------------")
        print("1) Calculate Parking Fee")
        print("2) Exit")
        print("     ----------------------")
    
    # ask for input to keep the loop running, conditional
        menu = int(input("Enter which option you would like ( 1 or 2 ): "))
        
    # if the loop does not end do the if statement
        if menu == 1: 
            hours_parked = df.getParkingHours()
            df.calcParkingFee(hours_parked)
    # if the loop ends say bye
        elif menu == 2:
            print("bye!")
    # will tell the user invalid unless 1 or 2 and reprompt the input from user
        else: 
            print("invalid!")
        
            menu = int(input("Enter which option you would like ( 1 or 2 ): "))    
    
# Call the main function.
if __name__ == "__main__":
    main()
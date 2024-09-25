# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:09:07 2024

@author: megan
"""

def getParkingHours():
    '''
    get the input from the user for the number of hours they parked

    Returns 
    -------
    hours_parked

    '''
# get the input from the user for the number of hours they parked
    hours_parked = int(input("How many hours were you parked? "))
    print("You were parked for", hours_parked, "hours")
    return hours_parked
    
def calcParkingFee(hours_parked):
    '''
    

    Parameters
    ----------
    hours_parked : INT
        A number recieved from the user used in the formula. Then
        will determine the amount owed by the user.

    Returns
    -------
    None.

    '''
# Do the math: it is 2.50 an hour 
    calc_hours = hours_parked * 2.5


# The minimum is $6, the max is $20

# if the total is below $6 print $6
    if calc_hours < 6:
        print("you owe $6")
# if the total is above $20 print $20
    elif calc_hours > 20:
        print("you owe $20")
# if the total is above $6 print calc_hours
    elif calc_hours > 6:
        print("You owe $"+str(calc_hours))
# should not need else, just for testing
    else:
        print("err")
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:07:17 2024

@author: lanem3406
"""

# This is an in book assignment, exercise 2,
# 8/28/2024
#CSC121 M1LAB1 - Review
# Megan Lane


# first ask to run the program
want = input("Would you like to run the BMI Calculator Program? \n")

# As long as the value of want does not equal "no" the program will run
while want != "no":
    # getting values for height and weightno
  he = float(input("what is your height in inches?\n"))
  we = float(input("what is your weight in pounds?\n"))  
  
  # standards for BMI
  min_bmi = 18.5
  max_bmi = 24
  
  #bmi formula to calculate
  bmi = (we/(he**2)*703)
  
  #I round the bmi vlaue to 2 decimal places
  bmi = round(bmi, 2)
  
  # if bmi is outside the heathly bmi range... if  bmi is greater than
  # max bmi or is less than min bmi
  
  if bmi >= max_bmi or bmi <= min_bmi:
      print("Your BMI is  UN- HEALTHY!\n")
      
      #directly specify after realizing the bmi is unhealthy
      # overweight
      if bmi >= max_bmi:
          #Tell them their current bmi
          print("Your BMI is", bmi, "\n")
          print("You are overweight!\n")
          over_bmi = bmi - max_bmi
          
          # I round the over_bmi value to 2 decimal places
          over_bmi = round(over_bmi, 2)
          # over max bmi by how much ...
          print("You are", over_bmi, "over the max standard BMI of", max_bmi, "\n")
          
     #underweight
      elif bmi <= min_bmi:
          print("Your BMI is", bmi, "\n")
          print("You are underweight!\n")
          under_bmi = min_bmi - bmi
          
          #I round the over_bmi vlaue to 2 decimal places
          under_bmi = round(under_bmi, 2)
          # underweight by how much ...
          print("You are", under_bmi, "under the min standard BMI of", min_bmi, "\n")
      else:
          #otherwise you are healthy. If error
          print("You are healthy.")
# if an unhealthy weight is not detected then,
# this individual is considered healthy
  else:
# Tell them their current bmi
      print("You are healthy.\n")
      print("Your BMI is", bmi, "\n")
#Tell them the standard range of bmi
      print("This is within the standard range of", min_bmi, "and", max_bmi, "\n")
      
# Ask if they want to run the program again
  want = input("Would you like to run this program again? (yes/no)")
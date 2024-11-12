# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv

def main():
    # open the file 
    rep = open("file.txt", "r")
    #bypass the header
    aline = rep.readline()
    print(aline)

    #create the txt file to write to
    bmi_txt = open("bmi.txt", "w")
    #header
    bmi_txt.write(f"{'bmi':<15}{'Patient ID'}\n")

    #create the csv file to write to
    bmi_csv = open("bmi.csv", "w",newline='')
    active = csv.writer(bmi_csv)
    #header
    active.writerow(['BMI','Patient ID','Height', 'Weight'])
    


    
    # identify each item on each line as a var
    # then calc the bmi while on each line
    # then write the bmi to the bmi_txt.txt
    # then write the bmi to the bmi_csv.csv
    for line in rep:
        patient_id, height, weight = line.split(',')
        try: 
            weight.isnumeric()
            height.isnumeric()
            
        except: 
            print(patient_id, "data must be a number\n")
            
        finally:
            bmi = int(weight)/int(height)**2 * 703
            bmi = round(bmi, 2)
            bmi_txt.write(f'{bmi:<15}{patient_id}\n')
            active.writerow([bmi, patient_id, height, weight])
        
    
    
    bmi_txt.close()
    bmi_csv.close()
    rep.close()

if __name__ == "__main__":
    main()

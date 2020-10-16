# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:03:43 2020

@author: renie
"""
import os
import csv


# Load data in files and output
data_file = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

total_months = 0
net_total = 0
change_net = 0
prev_net = 0
avg_change = []
month_change = []
biggest_inc = ["",0]
biggest_dec = ["",999999999999999]

with open(data_file, "r") as record:
    new_record = csv.reader(record)
    
    
    header = next(new_record)

    for row in new_record:
   
        total_months += 1 
        net_total += int(row[1])
        change_net = int(row[1]) - prev_net
        
        prev_net = int(row[1]) 
        avg_change += [change_net]
        month_change = row[0]
        if change_net > biggest_inc[1]:
            biggest_inc[0] = row[0]
            biggest_inc[1] = change_net
        
        if change_net < biggest_dec[1]:
            biggest_dec[0] = row[0]
            biggest_dec[1] = change_net
        
            
        
    print(f'Your total months are {total_months}')
    
    print(f'Your total Profit/Losses are {net_total}')
    
    print(f'Your avarage change in Profit/Losses is {sum(avg_change) / len(avg_change)}')
    
    print(f' Biggest increase in profit is {biggest_inc[0]}')
    print(f'Your Biggest Decrease was {biggest_dec[0]}')
    
    output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    # f"Average  Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {biggest_inc[0]} (${biggest_inc[1]})\n"
    f"Greatest Decrease in Profits: {biggest_dec[0]} (${biggest_dec[1]})\n")
    
    
    
print(output)
# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
    
 
    
          
          



# The average of the changes in "Profit/Losses" over the entire period


# The greatest increase in profits (date and amount) over the entire period




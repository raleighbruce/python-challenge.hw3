
#Import Modules
import os
import csv

#Define path to csv file
budget_data = os.path.join("..","PyBank", "Resources", "budget_data.csv")

#Set Variables
rowcount = 0
total = 0
currentValue = 0
lastValue = 0
valueChanges = 0
monthlyValueChange = []
monthOfChange = []

#Open csv file
with open(budget_data, encoding= 'utf-8') as budget_file:

#Define reader and skip headers
    csvreader = csv.reader(budget_file, delimiter=',')
    csvheader = next(csvreader)

#Start Counter 
    for row in csvreader:
#Count Total Rows
        rowcount += 1
#Count Sum of Profits/Losses
        total += int(row[1])
#Assign current value before looping through rows
        currentValue = int(row[1])
#Start loop
        if rowcount == 1:
#Set last Value at start of loop
            lastValue = currentValue
#Set value change per month and update lists
        else:
        
            valueChanges = currentValue - lastValue

            monthOfChange.append(row[0])

            monthlyValueChange.append(valueChanges)

            lastValue = currentValue
#Get Average of profit/losses
    averageValue = sum(monthlyValueChange)/len(monthOfChange)
#Get Min and Max of monthly profit/loss
    greatestIncrease = max(monthlyValueChange)
    greatestDecrease = min(monthlyValueChange)
#Set the Min and Max in the list
    greatestMonthIncrease = monthlyValueChange.index(greatestIncrease)
    greatestMonthDecrease = monthlyValueChange.index(greatestDecrease)
#Get the month associated with the min and max from the list
    highestMonth = monthOfChange[greatestMonthIncrease]
    lowestMonth = monthOfChange[greatestMonthDecrease]

#Print to terminal to double check work
print(f'Financial Analysis')
print('--------------------------')
print(f'Total Months: {rowcount}')
print(f'Total: {total}')
print(f'Average Change: {"%.2f" % averageValue}')
print(f'Greatest Increase In Profits {highestMonth} {greatestIncrease}')
print(f'Greatest Decrease In Profits {lowestMonth} {greatestDecrease}')


#Export data to .txt file
analysis_data = os.path.join("..","PyBank", "Analysis", "analysis_data.txt")
with open(analysis_data, 'w') as analysis_out:
    analysis_out.write(f'Financial Analysis\n')
    analysis_out.write('--------------------------\n')
    analysis_out.write(f'Total Months: {rowcount}\n')
    analysis_out.write(f'Total: ${total}\n')
    analysis_out.write(f'Average Change: ${"%.2f" % averageValue}\n')
    analysis_out.write(f'Greatest Increase In Profits {highestMonth} (${greatestIncrease})\n')
    analysis_out.write(f'Greatest Decrease In Profits {lowestMonth} (${greatestDecrease})\n')


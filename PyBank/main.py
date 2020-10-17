
# import the file
import csv
import os

# set the path
filepath = os.path.join("PyBank","Resources","PyBank.csv")
print(filepath)

def PyBank(file):
    # Define variables
    months = []                  
    TotalMonth = 0              
    total_profit = 0            
    monthly_change = []         
    total_profit_change = 0     
    previous_month_profit = 0   
    current_month_profit = 0
    monthly_change_profits = 0

    # Calculations
    for column in csvreader:
        
        # Append the date 
        months.append(column[0])
        TotalMonth = len(months)
        
        # Append the profit and calculate the profits
        current_month_profit = int(column[1])
        total_profit = total_profit + current_month_profit
        
        if TotalMonth == 1:
        # Calculate the monthly change
            previous_month_profit = current_month_profit
                  
        else:
            monthly_change_profits = current_month_profit - previous_month_profit
            monthly_change.append(monthly_change_profits)
            previous_month_profit = current_month_profit
        
        
        total_profit_change = sum(monthly_change)
        
        # Average profit
      
    average_change_profits = round(total_profit_change/(len(monthly_change)),2)

    #Find the max and min change in profits and the corresponding dates these changes were obeserved
    greatest_increase_profits = max(monthly_change)
    greatest_decrease_profits = min(monthly_change)
        
    increase_date = months[monthly_change.index(greatest_increase_profits)]
    decrease_date = months[monthly_change.index(greatest_decrease_profits)]



    print("PyBank Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(TotalMonth))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

    with open('PyBank.txt', 'w') as text:
        text.write("  Financial Analysis"+ "\n")
        text.write("----------------------------------------------------------\n\n")
        text.write("    Total Months: " + str(TotalMonth) + "\n")
        text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
        text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
        text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
        text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
        text.write("----------------------------------------------------------\n")


# Open the CSV
with open(filepath, "r", newline='') as file:
    csvreader = csv.reader(file)
    csv_header = next(csvreader)
    PyBank(csvreader)

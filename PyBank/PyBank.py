import os
import csv

# PyBank variables
months = []
profit_loss_change_list = []
total_months = 0
net_profit_loss = 0
current_profit_loss = 0
previous_profit_loss = 0
profit_loss_change = 0

csvpath = os.path.join('Resources/budget_data.csv')

with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the header
    csv_header = next(csv_file)
    print(f'CSV Header: {csv_header}')

    # Read the rows after header
    for row in csv_reader:

        #find how many months
        total_months += 1

        # Total amount over the period
        current_profit_loss = int(row[1])
        net_profit_loss += current_profit_loss

        if(total_months == 1):
            previous_profit_loss = current_profit_loss

        else:
            # Compute profit change
            profit_loss_change = current_profit_loss - previous_profit_loss
            months.append(row[0])
            profit_loss_change_list.append(profit_loss_change)
            previous_profit_loss = current_profit_loss

    # Find the changes of the Profit/Losses over the period
    sum_profit_loss = sum(profit_loss_change_list)
    average_profit_loss = round(sum_profit_loss/(total_months - 1), 2)

    # Find the Greatest Increase in profits
    greatest_increase = max(profit_loss_change_list)
    highest_month = profit_loss_change_list.index(greatest_increase)

    # Find the Greatest Decrease in profits
    greatest_decrease = min(profit_loss_change_list)
    lowest_month = profit_loss_change_list.index(greatest_decrease)

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {months[highest_month]} (${greatest_increase}")
print(f"Greatest Decrease in Losses:  {months[lowest_month]} (${greatest_decrease}")

# Export results text file to Analysis folder
budget_file = os.path.join("Analysis", "budget_data.txt")
with open(budget_file, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {total_months}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {months[highest_month]} (${greatest_increase}\n")
    outfile.write(f"Greatest Decrease in Losses:  {months[lowest_month]} (${greatest_decrease}\n")

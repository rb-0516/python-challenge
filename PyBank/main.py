# Import module
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_total = 0
previous_profit = 0
profit_changes = []
dates = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        # Count total months
        total_months += 1
        
        # Calculate net total
        current_profit = int(row[1])
        net_total += current_profit
        
        # Calculate profit changes
        if total_months > 1:
            change = current_profit - previous_profit
            profit_changes.append(change)
            dates.append(row[0])
            
            # Check for greatest increase
            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = row[0]
            
            # Check for greatest decrease
            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = row[0]
        
        previous_profit = current_profit

# Calculate average change
average_change = sum(profit_changes) / len(profit_changes)

# Prepare the analysis results
analysis = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})
Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})
"""

# Print to terminal
print(analysis)

# Export to text file
output_path = os.path.join("PyBank", "analysis", "financial_analysis.txt")

# Ensure the directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Write to text file
with open(output_path, "w") as txt_file:
    txt_file.write(analysis)

print(f"Analysis has been exported to {output_path}")
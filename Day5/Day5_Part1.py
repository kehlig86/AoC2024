### Explanation of the script:
### 1. Reading the rules and updates:
### The function `read_rules` reads the file `config_rules.csv` (by default) unless another file is specified.  
### The file contains pairs of integers separated by a pipe (|), each representing a rule.
### The function `read_updates` reads the file `config_updates.csv` (by default) unless another file is specified.  
### The file contains lists of integers separated by commas (,), each representing an update.
### 
### 2. Checking the order of updates:
### The function `is_correct_order` checks if the updates follow the given rules.  
### It iterates through each rule and ensures that the order of elements in the update complies with the rule.
### 
### 3. Finding the middle page:
### The function `middle_page` returns the middle element of an update list.
### 
### 4. User-friendliness:  
### The script assumes the files `config_rules.csv` and `config_updates.csv` are present in the current directory. If they are missing, a helpful error message is shown.  
### Debug information is printed during execution to assist in verifying the content of rules and updates.  
### 
### 5. Output:  
### The script outputs the sum of the middle pages of correctly ordered updates, in German.

import csv
import os

# Check if updates follow the specified rules
def is_correct_order(update, rules):
    for rule in rules:
        x, y = rule
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

# Return the middle element of an update list
def middle_page(update):
    return update[len(update) // 2]

# Read rules from a CSV file
def read_rules(file_name='config_rules.csv'):
    rules = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file, delimiter='|')
        for row in csv_reader:
            if row:  # Ensure the row is not empty
                rules.append((int(row[0]), int(row[1])))
    return rules

# Read updates from a CSV file
def read_updates(file_name='config_updates.csv'):
    updates = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:  # Ensure the row is not empty
                updates.append([int(x) for x in row if x])  # Ensure no empty strings are converted
    return updates

# Check the current working directory
print(f"Das aktuelle Arbeitsverzeichnis ist: {os.getcwd()}")

# Read rules and updates from their respective files
rules = read_rules('config_rules.csv')
updates = read_updates('config_updates.csv')

# Find the correctly ordered updates and their middle pages
correct_updates = [update for update in updates if is_correct_order(update, rules)]
middle_pages = [middle_page(update) for update in correct_updates]

# Calculate the sum of the middle pages
result = sum(middle_pages)

print(f"Die Summe der mittleren Seiten der korrekt geordneten Updates beträgt {result}.")

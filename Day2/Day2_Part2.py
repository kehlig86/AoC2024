# Explanation of the script:
# 1. Reading the file:
# The function `read_config_file` reads the file `config.csv` (by default) unless another file is specified.
# The file contains lines with numbers separated by spaces. Each line represents a report.
#
# 2. Report validation:
# Each report is checked to determine if it is safe. A safe report satisfies the following criteria:
# - All numbers are either strictly increasing or strictly decreasing.
# - The differences between adjacent numbers are between 1 and 3.
# If a report does not meet these rules, the **Problem Dampener** checks whether removing a single number can make the report safe.
#
# 3. Calculation of the number of safe reports:
# Reports that are either directly safe or can be made safe using the **Problem Dampener** are counted.
#
# 4. User-friendliness:
# If the file `config.csv` does not exist or is empty, an error message is displayed.
#
# 5. Output:
# The script outputs the number of safe reports, including those that can be made safe by the **Problem Dampener**.

import os

def read_config_file(filepath="config.csv"):
    """
    Reads the file and returns the data as a list of lists.
    Each inner list represents a report containing numbers.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Die Datei '{filepath}' wurde nicht gefunden.")
    
    with open(filepath, "r") as file:
        data = file.readlines()
    
    reports = [list(map(int, line.split())) for line in data if line.strip()]
    return reports

def is_safe_report(report):
    """
    Checks if a report is safe:
    - Numbers must be either strictly increasing or strictly decreasing.
    - Differences between adjacent numbers must be between 1 and 3.
    """
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)
    
    return is_increasing or is_decreasing

def can_be_safe_with_dampener(report):
    """
    Checks if a report can become safe by removing a single number.
    """
    for i in range(len(report)):
        # Create a new report without the current number
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    return False

def count_safe_reports_with_dampener(reports):
    """
    Counts the number of safe reports, including those that can be made safe using the Problem Dampener.
    """
    safe_count = 0
    for report in reports:
        if is_safe_report(report) or can_be_safe_with_dampener(report):
            safe_count += 1
    return safe_count

def main():
    try:
        # Read the file
        reports = read_config_file()
        
        # Count safe reports (including the Problem Dampener logic)
        safe_count = count_safe_reports_with_dampener(reports)
        
        # Output the result in German
        print(f"Anzahl sicherer Berichte (inkl. Problem Dampener): {safe_count}")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    main()

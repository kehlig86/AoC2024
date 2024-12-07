### Explanation of the script:
### 1. Reading the file:
### The function `read_config_file` reads the file `config.csv` (by default) unless another file is specified.  
### The file contains lines with numbers separated by spaces. Each line represents a report.
### 
### 2. Validating the reports:
### Each report is checked to ensure the numbers form a valid, safe sequence.  
### The criteria are:  
### - All numbers must either be strictly increasing or decreasing.  
### - The difference between two adjacent numbers must be between 1 and 3.
###
### 3. Calculating the number of safe reports:
### Reports that meet the criteria above are counted as safe.  
### 
### 4. User-friendliness:  
### The default file is `config.csv`. If it doesn't exist or is empty, an error message is displayed.
###
### 5. Output:
### The script outputs the number of safe reports in the file.

import os

def read_config_file(filepath="config.csv"):
    """
    Reads the file and returns the data as a list of lists.  
    Each inner list represents a report with numbers.
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
    - Numbers must either be increasing or decreasing.  
    - Differences between adjacent numbers must be between 1 and 3.
    """
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)
    
    return is_increasing or is_decreasing

def count_safe_reports(reports):
    """
    Counts the number of safe reports in the given list.
    """
    return sum(1 for report in reports if is_safe_report(report))

def main():
    try:
        # Read the file
        reports = read_config_file()
        
        # Count safe reports
        safe_count = count_safe_reports(reports)
        
        # Output the result
        print(f"Anzahl sicherer Berichte: {safe_count}")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    main()

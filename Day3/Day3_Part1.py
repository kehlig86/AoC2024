### Explanation of the script:
###
#### 1. Reading the file:  
###   - The function `read_config_file(filepath="config.csv")` reads the file `config.csv` by default unless another file is specified.  
###   - It ensures that the file exists. If not, a `FileNotFoundError` is raised.  
###   - It reads all lines, removes empty ones, and returns them as a list of strings.
###
### 2. Validating and extracting `mul(X, Y)` instructions:  
###  - The function `extract_mul_instructions(text)` uses regular expressions to find patterns like `mul(X, Y)` in each line.  
###  - The numbers `X` and `Y` must be between 1 and 3 digits.  
###  - This function calculates the product of all valid instructions in a given line.
###
### 3. Processing the data:  
###   - The script reads all lines from the file using `read_config_file`.  
###   - It processes each line by calling `extract_mul_instructions` to parse and compute their products.  
###
#### 4. Error handling for robustness:  
###   - The script checks if the file exists. If not, it handles this gracefully with a `FileNotFoundError`.  
###   - Any other unexpected errors are caught to avoid crashes.
###
### 5. **User-friendly default behavior**:  
###   - The script defaults to using `config.csv`. If this file doesn't exist, or if it's empty, the user receives a clear error message.
###
### 6. **Output**:  
###   - The script computes the sum of all calculated products from all lines and prints it in German: `Gesamtsumme der Ergebnisse: {total_sum}`.

# Reads the file and extracts the data as a list of lines.  
# Each line represents a section of the corrupted memory.

import os
import re


def read_config_file(filepath="config.csv"):
    """
    Reads the configuration file and processes the data into a list of strings.  
    This method uses the default value 'config.csv' if no other path is specified.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file '{filepath}' was not found.")
    
    with open(filepath, "r") as file:
        # Read all lines and remove spaces or empty lines
        data = file.readlines()
    
    # Convert each line into a clean string
    return [line.strip() for line in data if line.strip()]



# Extracts valid mul(X,Y) instructions from a given text and calculates their products.  
# mul(X,Y) is only valid if X and Y are numbers between 1 and 3 digits.  
# Uses regular expressions for extraction.
def extract_mul_instructions(text):
    # Regular expression to find valid mul(X,Y) instructions
    pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
    matches = re.findall(pattern, text)  # Search for all valid mul(X,Y) instructions

    # Calculate the sum of the products of found numbers
    return sum(int(x) * int(y) for x, y in matches)


def main():
    try:
        # Read input data from the file
        reports = read_config_file()
        
        # Extract and calculate all mul(X,Y) instructions from all lines
        total_sum = sum(extract_mul_instructions(report) for report in reports)
        
        # Output the result
        print(f"Gesamtsumme der Ergebnisse: {total_sum}")
    except FileNotFoundError as e:
        # Handle missing file error
        print(e)
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Ein Fehler ist aufgetreten: {e}")


if __name__ == "__main__":
    main()

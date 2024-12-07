### Explanation of the script:
### 1. Reading the file:
### The function `read_grid_from_csv` reads the file `config.csv` (by default) unless another file is specified.  
### The file contains rows of characters, each representing a line in a word search puzzle.  
### Each cell in the grid is treated as a single character.
### 
### 2. Searching for the word "XMAS":
### The function `count_xmas_occurrences` counts how many times the word "XMAS" appears in the grid.  
### The word can appear in any direction: horizontal, vertical, diagonal, or reversed.
### 
### 3. User-friendliness:  
### The script assumes the file `config.csv` is present in the current directory. If it is missing, a helpful error message is shown.  
### Debug information is printed during execution to assist in verifying the grid content.  
### 
### 4. Output:  
### The script outputs the total number of occurrences of the word "XMAS" in the grid, in German.

import csv
import os

# Define the function to count occurrences of the word XMAS
# Words can be found in all directions: horizontal, vertical, diagonal, and reversed
def count_xmas_occurrences(grid):
    # Get dimensions of the grid
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Define the target word
    target = "XMAS"
    target_len = len(target)

    # Initialize count
    count = 0

    # Helper function to check a direction
    def check_direction(start_row, start_col, delta_row, delta_col):
        for i in range(target_len):
            r = start_row + i * delta_row
            c = start_col + i * delta_col
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != target[i]:
                return False
        return True

    # Iterate over each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Check all 8 directions
            directions = [
                (0, 1),  # Right
                (1, 0),  # Down
                (0, -1), # Left
                (-1, 0), # Up
                (1, 1),  # Down-Right
                (1, -1), # Down-Left
                (-1, 1), # Up-Right
                (-1, -1) # Up-Left
            ]
            for dr, dc in directions:
                if check_direction(row, col, dr, dc):
                    count += 1

    return count

# Read the grid from the config.csv file
def read_grid_from_csv(file_path):
    grid = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Ensure each row is split into individual characters
                grid.append([char for char in row[0]])
        print("Grid erfolgreich aus der Datei gelesen.")
    except FileNotFoundError:
        print("Fehler: Datei nicht gefunden. Bitte überprüfen Sie den Dateinamen.")
    except IndexError:
        print("Fehler: Die CSV-Datei scheint nicht im erwarteten Format zu sein.")
    return grid

# Main script
if __name__ == "__main__":
    # Default file path
    default_file_path = "config.csv"

    # Use the default file path for now
    file_path = default_file_path

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Fehler: Die Datei {file_path} wurde nicht gefunden.")
    else:
        # Read the grid from the file
        grid = read_grid_from_csv(file_path)

        if grid:
            # Count the occurrences of XMAS
            occurrences = count_xmas_occurrences(grid)

            # Print the result
            print(f"Das Wort 'XMAS' erscheint insgesamt {occurrences} Mal im Suchrätsel.")

### Script Explanation:
### 1. Reading the file:
### The function read_config_file reads a configuration file containing two columns of numbers (left_list and right_list). These numbers are split into two separate lists.
### 
### 2. Sorting and pairing:
### The numbers in both lists are sorted in ascending order. Then, they are compared pairwise based on their respective positions after sorting.
### 
### 3. Calculating the total distance:
### For each pair of numbers, the absolute difference is calculated. These differences are summed to obtain the total distance between the two lists.
### 
### 4. User-friendliness:
### If no file path is provided, the default file config.csv is used. The script checks whether the file exists before starting processing to minimize error messages.
### 
### 5. Output:
### The script outputs the calculated total distance, allowing the user to easily understand the differences between the number pairs in the two lists.

# Import necessary libraries
import os  # For file checking (optional)

# Function to read the configuration file
def read_config_file(file_path):
    """
    Reads the configuration file containing two columns:
    The left list and the right list.

    Args:
        file_path (str): The path to the configuration file

    Returns:
        list, list: Two lists with numbers from the file
    """
    try:
        left_list = []
        right_list = []
        with open(file_path, 'r') as file:
            for line in file:
                left, right = map(int, line.strip().split(','))
                left_list.append(left)
                right_list.append(right)
        return left_list, right_list
    except Exception as e:
        print(f"Fehler beim Einlesen der Datei: {e}")
        return [], []

# Function to calculate the total distance
def calculate_total_distance(left_list, right_list):
    """
    Calculates the total distance between two lists by
    comparing numbers pairwise after sorting.

    Args:
        left_list (list): List of numbers from the left column
        right_list (list): List of numbers from the right column

    Returns:
        int: The total distance between the two lists
    """
    # Sort both lists
    left_list_sorted = sorted(left_list)
    right_list_sorted = sorted(right_list)
    
    # Calculate the distances between paired numbers
    distances = []
    for left, right in zip(left_list_sorted, right_list_sorted):
        distance = abs(left - right)  # Absolute difference
        distances.append(distance)
    
    # Sum up the distances
    total_distance = sum(distances)
    return total_distance

# Main program
if __name__ == "__main__":
    print("Willkommen beim Paarweise-Distanzrechner!")
    
    # Default file name
    default_file = "config.csv"
    
    # Prompt the user to input the file name
    file_path = input(f"Bitte geben Sie den Pfad zur Konfigurationsdatei ein (oder drücken Sie Enter für '{default_file}'): ").strip()
    
    # Use the default file if no input is provided
    if not file_path:
        file_path = default_file

    # Check if the file exists (optional, for user-friendliness)
    if not os.path.isfile(file_path):
        print(f"Die Datei '{file_path}' wurde nicht gefunden. Bitte überprüfen Sie den Pfad.")
    else:
        # Read the lists from the file
        left_list, right_list = read_config_file(file_path)
        
        if not left_list or not right_list:
            print("Die Listen konnten nicht eingelesen werden. Bitte prüfen Sie die Datei.")
        else:
            # Calculate the total distance
            total_distance = calculate_total_distance(left_list, right_list)
            
            # Output the result
            print(f"Die Gesamtdistanz zwischen den beiden Listen beträgt: {total_distance}")

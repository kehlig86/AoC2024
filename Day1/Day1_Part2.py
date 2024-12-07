#### Script Explanation:
### 1. Reading the file:
### The function read_config_file reads the two lists (left_list and right_list) from the config.csv file.
###
### 2. Counting frequency:
### The numbers in the right list are counted in a dictionary (right_count), where the key is the number and the value is its frequency.
###
### 3. Calculating the similarity score:
### For each number in the left list, the frequency in the right list is retrieved, and the calculation is performed using the formula: 
### similarity_score += number_in_left × frequency_in_right
###
### 4. User-friendliness:
### By default, config.csv is used if no other file path is provided.
### The script checks whether the file exists before processing begins.
###
### 5. Output:
### The script calculates the similarity score between two lists of numbers read from a CSV file. 
### The similarity score is the sum of the product of each number in the left list with its frequency in the right list.

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

# Function to calculate the similarity score
def calculate_similarity_score(left_list, right_list):
    """
    Calculates the similarity score by determining how often
    each number in the left list appears in the right list.
    
    Args:
        left_list (list): List of numbers from the left column
        right_list (list): List of numbers from the right column

    Returns:
        int: The similarity score
    """
    # Dictionary to count the frequency of numbers in the right list
    right_count = {}
    for number in right_list:
        right_count[number] = right_count.get(number, 0) + 1

    # Calculate the similarity score
    similarity_score = 0
    for number in left_list:
        # Retrieve the frequency of the current number in the right list (or 0 if not present)
        count_in_right = right_count.get(number, 0)
        # Add to the similarity score: number * frequency
        similarity_score += number * count_in_right

    return similarity_score

# Main program
if __name__ == "__main__":
    print("Willkommen beim Ähnlichkeitswert-Rechner!")
    
    # Default file name
    default_file = "config.csv"
    
    # Prompt the user to input the file name
    file_path = input(f"Bitte geben Sie den Pfad zur Konfigurationsdatei ein (oder drücken Sie Enter für '{default_file}'): ").strip()
    
    # Use the default file if no input is provided
    if not file_path:
        file_path = default_file

    # Check if the file exists
    import os
    if not os.path.isfile(file_path):
        print(f"Die Datei '{file_path}' wurde nicht gefunden. Bitte überprüfen Sie den Pfad.")
    else:
        # Read the lists from the file
        left_list, right_list = read_config_file(file_path)
        
        if not left_list or not right_list:
            print("Die Listen konnten nicht eingelesen werden. Bitte prüfen Sie die Datei.")
        else:
            # Calculate the similarity score
            similarity_score = calculate_similarity_score(left_list, right_list)
            
            # Output the result
            print(f"Der Ähnlichkeitswert zwischen den beiden Listen beträgt: {similarity_score}")

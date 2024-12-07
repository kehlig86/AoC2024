### Explanation of the script:
### 1. Reading the file:
### The function `load_matrix` reads the file `config.csv` (by default) unless another file is specified.  
### The file contains rows of characters, each representing a line in a word search puzzle.  
### Each cell in the matrix is treated as a single character.
### 
### 2. Searching for the word "XMAS":
### The function `count_patterns` counts how many times the word "XMAS" appears in the matrix.  
### The word can appear in any direction: horizontal, vertical, diagonal, or reversed.
### 
### 3. Extracting diagonal patterns:
### The function `diagonals` extracts diagonals from the matrix in multiple directions for analysis.
### 
### 4. Analyzing patterns:
### The function `count_mas_patterns` counts occurrences of specific patterns based on predefined conditions in the matrix.
### 
### 5. Output:
### The script computes the total counts of "XMAS" occurrences and other pattern counts, then prints the results.

def load_matrix(filename):
    """
    Reads the matrix from a file and returns it as a list of lists.
    Each line in the file is treated as a row in the matrix, with each character treated as a cell.
    """
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]


def transpose(matrix):
    """
    Transposes a given 2D matrix (swap rows and columns).
    Used to facilitate vertical pattern analysis.
    """
    return [list(row) for row in zip(*matrix)]


def diagonals(matrix):
    """
    Extracts diagonals from the given matrix in four diagonal directions.
    These diagonals are analyzed for patterns later in the script.
    """
    diags = []
    for i in range(len(matrix)):
        # Extract diagonal patterns in four directions
        diag1 = [matrix[x][x+i] for x in range(len(matrix)-i)]
        diag2 = [matrix[x+i][x] for x in range(len(matrix)-i)]
        diag3 = [matrix[x][len(matrix)-1-x-i] for x in range(len(matrix)-i)]
        diag4 = [matrix[x+i][len(matrix)-1-x] for x in range(len(matrix)-i)]
        diags.extend([diag1, diag2, diag3, diag4])
    return diags


def count_patterns(lines, pattern):
    """
    Counts occurrences of a given pattern (e.g., 'XMAS') in horizontal, vertical, diagonal,
    and reversed directions across the provided matrix lines.
    """
    count = 0
    for line in lines:
        # Count pattern in forward and reversed order
        count += ''.join(line).count(pattern)
        count += ''.join(line)[::-1].count(pattern)
    return count


def count_mas_patterns(matrix):
    """
    Counts specific patterns based on a series of conditions in the provided matrix.
    These patterns are combinations of characters (M, S, A) in specific formations.
    """
    count = 0
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            # Look for specific configurations of patterns
            if matrix[i][j] == 'A':
                if matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S' and matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S':
                    count += 1
                elif matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S' and matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M':
                    count += 1
                elif matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M' and matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S':
                    count += 1
                elif matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M' and matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M':
                    count += 1
    return count


# Main execution:
# Load the matrix from the file and prepare for analysis
matrix = load_matrix("config.csv")  # Load matrix from the file
horiz = matrix  # Horizontal analysis uses the original matrix
vert = transpose(matrix)  # Transpose matrix for vertical analysis
diag = diagonals(matrix)  # Extract diagonals for diagonal analysis

# Count occurrences of the pattern "XMAS" horizontally, vertically, and diagonally
xmas_count = count_patterns(horiz, "XMAS") + count_patterns(vert, "XMAS") + count_patterns(diag, "XMAS")

# Count occurrences of specific pattern formations based on defined conditions
mas_count = count_mas_patterns(matrix)

# Output the results
print(mas_count)

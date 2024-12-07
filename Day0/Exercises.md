
# Introduction to Python for Beginners: A List of 10 Exercises  

## Basics: Setting Up and Using Python  
**Installation:**  
Download and install Python from [python.org](https://www.python.org/downloads/).  

**Recommended Editors:**  
Use VS Code (lightweight, versatile, with plugins available) or IDLE (simple for beginners).  

Advantages of VS Code: Extensible, syntax highlighting, debugging capabilities.  
Disadvantages of VS Code: Requires more setup.  

IDLE: Easy to use and ready to go, but has fewer features for larger projects.  

**Online Option:**
Try [online-python.com](https://www.online-python.com/)  

Advantages: No installation required, ready to use immediately.  
Disadvantages: Dependent on an internet connection.



# Useful Links  
[w3schools](https://www.w3schools.com/python/default.asp)  
[Offical Python Tutorial](https://docs.python.org/3/tutorial/)  
[freecodecamp](https://www.freecodecamp.org/)


## Exercise Series: 10 Tasks  
**Goal: Build understanding of basic Python concepts and prepare for challenges similar to Advent of Code.**  

### Getting Started
**Time Investment:** Each exercise should take about 20–60 minutes, depending on your skill level.  
**Seek Help:** Use Google or docs.python.org for specific questions.  
**Debugging:** Test your scripts step-by-step to find errors. Sometimes it helps to test individual functions in isolation.  

### Exercise 1: "Hello, World!" and First Steps
Write a script that prints "Hello, World!"  
Let the user enter their name and greet them with a personalized message.  
*Learning Objective: Basic syntax, print and input.*  

```
# Example  
name = input("Wie heißt du? ")  
print(f"Hallo, {name}! Willkommen in Python!")
```

### Exercise 2: Simple Math  
Write a script that asks the user for two numbers and calculates their sum, difference, product, and quotient.  
*Learning Objective: Working with variables and mathematical operations.*

```
# Example
zahl1 = int(input("Gib die erste Zahl ein: "))
zahl2 = int(input("Gib die zweite Zahl ein: "))
print("Summe:", zahl1 + zahl2)
```

### Exercise 3: Decision Making with if  
Write a script that checks if a given number is even or odd.  
*Learning Objective: Conditional statements and the modulo operator (%).*

## Exercise 4: Lists and Loops  
Write a script that stores the numbers from 1 to 10 in a list and prints each value.  
*Learning Objective: Introduction to loops (for) and lists.*

## Exercise 5: Custom Functions  
Write a function that checks if a number is prime.  
*Learning Objective: Writing and understanding functions.*

## Exercise 6: Working with Strings
Write a script that asks for a sentence and counts the number of words.  
*Learning Objective: Using string methods like split and len.*

## Exercise 7: Dictionaries and Basic Data Processing
Create a script that counts the frequency of each letter in a given text.  
*Learning Objective: Introduction to dictionaries.*

## Exercise 8: Reading and Writing Files
Write a script that reads a file and writes its content to a new file.  
*Learning Objective: Working with files (open, read, write).*

## Exercise 9: Error Handling
Write a script that asks the user for a number and calculates its square root. Learning Objective: Working with files (open, read, write).  Handle cases where the user doesn't enter a valid number.Learning Objective: Working with files (open, read, write).  
*Learning Objective: Introduction to try and except.*

## Exercise 10: Advent-of-Code-like Challenge
Write a script that takes a list of numbers and checks if two numbers exist whose sum equals a given target value.  
*Learning Objective: Problem-solving strategies and preparation for AoC tasks.*

```
# Example
zahlen = [10, 15, 3, 7]
ziel = 17
for i in zahlen:
    for j in zahlen:
        if i + j == ziel:
            print(f"Gefunden: {i} + {j} = {ziel}")
```

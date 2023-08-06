Valid Integer Checker
This Python script contains two functions: valid_int() and get_int(). The valid_int() function takes a string as input and checks to see if it is a valid integer. The get_int() function prompts the user for input, and only accepts valid integers as input.

Functionality
The valid_int() function first checks to see if the input string is empty. If it is, the function returns False. Otherwise, the function checks to see if the first character is a negative sign. If it is, the negative sign is removed and the rest of the string is checked for validity.

The get_int() function prompts the user for input and uses the valid_int() function to check the input for validity. If the input is not a valid integer, the user is prompted to try again. Once a valid integer is entered, it is returned as an int type.

Usage
To use these functions in your own code, simply import them using the following statement:




from main.py import valid_int, get_int
Then, you can use the valid_int() and get_int() functions as needed. For example:

x = get_int("Enter a valid integer: ")
print(f"You entered: {x}")

# Comprehension is the consize way to create lists, sets, or dictionaries in Python.


# Que : Where they are used?# Ans : They are used to make code more readable and concise. They can replace the need for loops in many cases.
# # Example 1: List Comprehension
# syntax: [expression for item in iterable if condition]# Create a list of squares of even numbers from 0 to 9
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("List of even squares from 0 to 9:", even_squares)


squares = [x**2 for x in range(10)]
print("List of squares from 0 to 9:", squares) 

menu=['pizza', 'pasta', 'salad', 'soup', 'burger', 'iced-tea', 'iced-peached tea']
upper_menu = [item.upper() for item in menu]
print("Menu in uppercase:", upper_menu)

check_iced = [item for item in menu if 'iced' in item]
print("Menu items containing 'iced':", check_iced)

# Example 2: Set Comprehension
# syntax: {expression for item in iterable if condition}# Create a set of unique vowels     
vowels = 'aeiou'
unique_vowels = {char for char in 'hello world' if char in vowels}
print("Unique vowels in 'hello world':", unique_vowels)

# Example 3: Dictionary Comprehension
# syntax: {key_expression: value_expression for item in iterable if condition}# Create a dictionary mapping numbers to their squares
num_square_dict = {x: x**2 for x in range(5)}
print("Dictionary of numbers and their squares:", num_square_dict)

# Create a dictionary from two lists
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
info_dict = {keys[i]: values[i] for i in range(len(keys))}
print("Dictionary from two lists:", info_dict)



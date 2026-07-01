#String Manipulation 
#1. Write a program to create a new string made of an input string’s first, middle, and last character. 
# Input a string
text = input("Enter a string: ")

# Find the middle index
middle = len(text)//2

# Create the new string
new_string = text[0] + text[middle] + text[-1]

# Display the result
print("New string:", new_string)


#2. Write a program to count occurrences of all characters within a string Given. 

# Input a string
text = input("Enter a string: ")

# Count occurrences of each character
count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

# Display the result
print("Character occurrences:")
for char, freq in count.items():
    print(char, ":", freq)

 
#3. Reverse a given string 

# Input a string
N= input("Enter a string: ")

# Reverse the string
reverse_N = N[::-1]

# Display the result
print("Reversed string:", reverse_N)

#4. Split a string on hyphens

# Input a string
leo = input("Enter a hyphen-separated string: ")

# Split the string on hyphens
result = leo.split("-")

# Display the result
print("After splitting:")
for word in result:
    print(word)


#5. Remove special symbols / punctuation from a string 
import string

# Input a string
text = input("Enter a string: ")

# Remove punctuation
clean_text = ""

for char in text:
    if char not in string.punctuation:
        clean_text += char

# Display the result
print("String after removing special symbols:")
print(clean_text)

#List Manipulation
#1.  Reverse a list in Python 

# Input a list of numbers
numbers = input("Enter numbers separated by spaces: ").split()

# Reverse the list
numbers.reverse()

# Display the reversed list
print("Reversed List:", numbers)

#2.  Turn every item of a list into its square
# Input a list of numbers
x = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Square each number
squares = []

for num in x:
    squares.append(num ** 2)

# Display the result
print("Squared List:", squares)

#3.  Remove empty strings from the list of strings 
# List of strings
strings = ["Ali", "", "Sara", "", "shahzain", "Python", ""]

# Remove empty strings
result = []

for item in strings:
    if item != "":
        result.append(item)

# Display the result
print("Original List:", strings)
print("List after removing empty strings:", result)

#4. Add new item to list after a specified item 
# Original list
fruits = ["Apple", "Banana", "Mango", "Orange"]

# Item after which to insert
specified_item = "Banana"
new_item = "Grapes"

# Find the position and insert the new item
index = fruits.index(specified_item)
fruits.insert(index + 1, new_item)

# Display the updated list
print("Updated List:", fruits)

#5.  Replace list’s item with new value if found
# Original list
fruits = ["Apple", "Banana", "Mango", "Orange"]

# Item to replace and new value
old_item = "Mango"
new_item = "Grapes"

# Replace the item if found
if old_item in fruits:
    index = fruits.index(old_item)
    fruits[index] = new_item

# Display the updated list
print("Updated List:", fruits)

#Dictionary Manipulation
#1.Check if a value exists in a dictionary 
# Dictionary
student = {
    "name": "shahzain",
    "age": 24,
    "city": "Lahore"
}

# Input the value to search
value = input("Enter a value to search: ")

# Check if the value exists
if value in student.values():
    print("Value exists in the dictionary.")
else:
    print("Value does not exist in the dictionary.")

#2 Get the key of a minimum value from the following dictionary 
# Dictionary
marks = {
    "shahzain": 85,
    "Sara": 92,
    "babul": 78,
    "Ayesha": 88
}

# Find the key with the minimum value
min_key = min(marks, key=marks.get)

# Display the result
print("Key with minimum value:", min_key)
print("Minimum value:", marks[min_key])


#3.  Delete a list of keys from a dictionary
# Dictionary
student = {
    "name": "shahzain",
    "age": 20,
    "city": "Lahore",
    "grade": "A",
    "marks": 85
}

# Keys to delete
keys_to_remove = ["age", "grade"]

# Delete the keys
for key in keys_to_remove:
    if key in student:
        del student[key]

# Display the updated dictionary
print("Updated Dictionary:")
print(student)

#Tuple Manipulation
#1. Reverse the tuple 
# Original tuple
numbers = (10, 20, 30, 40, 50)

# Reverse the tuple
reversed_tuple = numbers[::-1]

# Display the result
print("Original Tuple:", numbers)
print("Reversed Tuple:", reversed_tuple)

#2.  Access value 20 from the tuple 
# Tuple
numbers = (10, 20, 30, 40, 50)

# Access the value 20
print("Value:", numbers[1])

#3. Swap two tuples in Python
# Tuple 1
tuple1 = (10, 20, 30)

# Tuple 2
tuple2 = (40, 50, 60)

# Display original tuples
print("Before Swapping:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# Swap the tuples
tuple1, tuple2 = tuple2, tuple1

# Display swapped tuples
print("\nAfter Swapping:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

#Loop Manipulation
#1.Print first 10 natural numbers using while
# Initialize the counter
i = 1

# Print the first 10 natural numbers
while i <= 10:
    print(i)
    i += 1

#2.Take Input from user , and print even number till that input number 

# Input from the user
num = int(input("Enter a number: "))

# Start from 2
i = 2

# Print even numbers up to the input number
while i <= num:
    print(i)
    i += 2

#3.Take Input from user , and print odd number till that input number 

# Input from the user
num = int(input("Enter a number: "))

# Start from 1
i = 1

# Print odd numbers up to the input number
while i <= num:
    print(i)
    i += 2

#4.Take Input from user , and print prime number till that input number

# Input from the user
num = int(input("Enter a number: "))

# Print prime numbers up to the input number
for i in range(2, num + 1):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i)

#5 Print multiplication table of a given number 
# Input from the user
num = int(input("Enter a number: "))

# Print multiplication table
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


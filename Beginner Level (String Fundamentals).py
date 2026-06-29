#Beginner Level (Strings Fundamentals) 
#1. Length of a String 
#Write a program that reads a string and prints its length. 
# Input: "hello world" → Output: 11 
#Hint: Use len(s). 

# Input a string
s = input("Enter a string: ")

# Find and print the length
print("Length of the string:", len(s))

#2. Uppercase & Lowercase 
#Convert the input string to uppercase and lowercase. 
# Input: "Python3" → Output: "PYTHON3", "python3" 
#Hint: Methods: s.upper(), s.lower().

# Input a string
s = input("Enter a string: ")

# Convert to uppercase and lowercase
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

#3.Count a Character 
#Count how many times a given character appears in a string (case-sensitive). 
# Input: "banana", "a" → Output: 3 
#Hint: Use s.count(ch). 

# Input a string
s = input("Enter a string: ")

# Input the character to count
ch = input("Enter a character: ")

# Count occurrences
count = s.count(ch)

# Display the result
print("Number of occurrences:", count)

#4.First & Last Character 
#Print the first and last character of a string; handle empty input. 
#Input: "drawer" → Output: First: d, Last: r 
#Hint: Check empty with if not s; index via s[0] and s[-1].

# Input a string
s = input("Enter a string: ")

# Check if the string is empty
if not s:
    print("The string is empty.")
else:
    print("First:", s[0])
    print("Last:", s[-1])

#5.Check Substring Presence 
#Check if a substring exists in a string. 
#Input: "data science", "science" → Output: True 
#Hint: Use the in operator: sub in s. 
# Input the main string
s = input("Enter a string: ")

# Input the substring
sub = input("Enter a substring: ")

# Check if the substring exists
if sub in s:
    print(True)
else:
    print(False)

#6.Slice a String 
#Print a substring from index start to end (exclusive). 
# Input: "programming", 3, 8 → Output: "gramm" 
#Hint: Use slicing: s[start:end].
# Input the string
s = input("Enter a string: ")

# Input start and end indexes
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))

# Slice the string
result = s[start:end]

# Display the result
print("Substring:", result)

#7. Reverse a String 
#Reverse the string. 
# Input: "Python" → Output: "nohtyP" 
#Hint: Slicing trick: s[::-1].
# Input a string
s = input("Enter a string: ")

# Reverse the string
reverse = s[::-1]

# Display the result
print("Reversed string:", reverse)

#8. Replace Substring 
#Replace all occurrences of a word with another (case-sensitive). 
# Input: "I love apples. Apples are great!", "apples", "oranges" 
# Output: "I love oranges. Apples are great!" 
#Hint: s.replace(old, new) replaces exactly matching cases. 

# Input the string
s = input("Enter a string: ")

# Input the word to replace and the new word
old = input("Enter the word to replace: ")
new = input("Enter the new word: ")

# Replace the word
result = s.replace(old, new)

# Display the result
print("Updated string:", result)

#9. Split and Join 
#Split a sentence on spaces and join with -. 
# Input: "split this sentence" → Output: "split-this-sentence" 
#Hint: s.split() then "-".join(words).

# Input a sentence
s = input("Enter a sentence: ")

# Split the sentence into words
words = s.split()

# Join the words with hyphens
result = "-".join(words)

# Display the result
print("Output:", result)

#10. Strip Whitespace 
#Remove leading and trailing spaces. 
# Input: "   padded text  " → Output: "padded text" 
#Hint: Use s.strip().

# Input a string
s = input("Enter a string: ")

# Remove leading and trailing spaces
result = s.strip()

# Display the result
print("Output:", result)



#Intermediate Level (More Involved String Tasks) 


#1. Count Vowels & Consonants 
#Count vowels and consonants (letters only; ignore digits/punctuation). 
#Input: "Hello, World! 123" → Output: Vowels: 3, Consonants: 7 
#Hint: Iterate characters; check ch.isalpha(); membership test like ch.lower() in 
#"aeiou". 

# Input a string
s = input("Enter a string: ")

# Initialize counters
vowels = 0
consonants = 0

# Count vowels and consonants
for ch in s:
    if ch.isalpha():          # Check if the character is a letter
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Display the result
print("Vowels:", vowels)
print("Consonants:", consonants)


#2. Palindrome Check (Ignore Case & Non-alphanumerics) 
#Determine if a string is a palindrome ignoring case and non-alphanumeric characters. 
# Input: "A man, a plan, a canal: Panama!" → Output: True 
#Hint: Normalize with ''.join(ch.lower() for ch in s if ch.isalnum()); compare to 
#its reverse.

# Input a string
s = input("Enter a string: ")

# Remove non-alphanumeric characters and convert to lowercase
cleaned = "".join(ch.lower() for ch in s if ch.isalnum())

# Check if it is a palindrome
if cleaned == cleaned[::-1]:
    print(True)
else:
    print(False)

#3. Title Case (Manual) 
#Convert a sentence to title case without using .title(). 
# Input: "hELLO wORLD from PYTHON" → Output: "Hello World From Python" 
#Hint: Split into words; for each word: word[0].upper() + word[1:].lower() 
#(guard empty words). 

# Input a sentence
s = input("Enter a sentence: ")

# Split the sentence into words
words = s.split()

# Convert each word to title case manually
title_words = []

for word in words:
    if word:  # Check if the word is not empty
        title_words.append(word[0].upper() + word[1:].lower())

# Join the words back into a sentence
result = " ".join(title_words)

# Display the result
print("Title Case:", result)

#4. Find All Indices of a Substring (Allow Overlaps) 
#Return a list of starting indices where a substring occurs. 
# Input: s="aaaa", sub="aa" → Output: [0, 1, 2] 
#Hint: Loop i from 0 to len(s) - len(sub); compare slices s[i:i+len(sub)]. 

# Input the main string
s = input("Enter the string: ")

# Input the substring
sub = input("Enter the substring: ")

# List to store starting indices
indices = []

# Find all occurrences (including overlaps)
for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        indices.append(i)

# Display the result
print("Starting indices:", indices)

#5. Character Frequency Dictionary 
#Build a frequency dictionary for characters (case-insensitive, skip spaces). 
# Input: "Baa Baa Black Sheep" 
# Output (order may vary): {'b':3,'a':5,'l':1,'c':1,'k':1,'s':1,'h':1,'e':3,'p':1} 
#Hint: Iterate for ch in s.lower(): and if ch != ' ': then count with a dict; 
#dict.get(ch, 0)+=1. 

# Input a string
s = input("Enter a string: ")

# Create an empty dictionary
freq = {}

# Count character frequencies
for ch in s.lower():
    if ch != " ":      # Skip spaces
        freq[ch] = freq.get(ch, 0) + 1

# Display the result
print("Character Frequency Dictionary:")
print(freq)


#6. Anagram Checker 
#Check if two strings are anagrams (ignore spaces, punctuation, and case). 
# Input: "Listen", "Silent" → Output: True 
#Hint: Normalize to letters with ch.isalpha() and lower(), then compare 
#sorted(s1) vs sorted(s2) or frequency dicts.

# Input two strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Normalize the strings (keep only letters and convert to lowercase)
str1 = "".join(ch.lower() for ch in s1 if ch.isalpha())
str2 = "".join(ch.lower() for ch in s2 if ch.isalpha())

# Check if they are anagrams
if sorted(str1) == sorted(str2):
    print(True)
else:
    print(False)

#7. Compress Repeated Characters (RLE-lite) 
#Compress runs of the same character as <char><count>. 
# Input: "aaabbcaaaa" → Output: "a3b2c1a4" 
#Hint: Track current char and run length; flush when char changes or at the 
#end. 
# Input a string
s = input("Enter a string: ")

# Check if the string is empty
if not s:
    print("")
else:
    result = ""
    count = 1

    # Count repeated characters
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1

    # Add the last character and its count
    result += s[-1] + str(count)

    # Display the compressed string
    print("Compressed string:", result)

#8. Longest Word in a Sentence 
#Find the longest word; if multiple, return the first. Consider words as alphabetic sequences. 
# Input: "Find the longest_word here!" → Output: "longest" 
#Hint: Filter to letters using ''.join(ch for ch in token if ch.isalpha()); track max by length.

# Input a sentence
s = input("Enter a sentence: ")

# Split the sentence into tokens
tokens = s.split()

# Variables to store the longest word
longest = ""

# Check each token
for token in tokens:
    # Keep only alphabetic characters
    word = "".join(ch for ch in token if ch.isalpha())

    # Update the longest word
    if len(word) > len(longest):
        longest = word

# Display the result
print("Longest word:", longest)

#9. Remove Duplicate Characters but Keep Order 
#Remove duplicates while preserving the first occurrence order. 
#Input: "banana" → Output: "ban" 
#Hint: Maintain a seen set; build result by adding chars not in seen. 

# Input a string
s = input("Enter a string: ")

# Set to keep track of seen characters
seen = set()

# String to store the result
result = ""

# Remove duplicate characters while keeping order
for ch in s:
    if ch not in seen:
        seen.add(ch)
        result += ch

# Display the result
print("Result:", result)

#10. Mask Email Username 
#Mask all but the first and last character of the username with *; keep domain intact. 
#Input: "john.doe@example.com" → Output: "j******e@example.com" 
#Hint: Split on '@'; for the left part, if length ≥ 2, keep first and last and 
#replace middle with '*' * (len-2); if shorter, handle edge cases.

# Input email
email = input("Enter an email: ")

# Split username and domain
username, domain = email.split("@")

# Mask the username
if len(username) >= 2:
    masked = username[0] + "*" * (len(username) - 2) + username[-1]
else:
    masked = username

# Display the masked email
print("Masked Email:", masked + "@" + domain)
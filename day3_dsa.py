#str funcrion using dsa
# -------------------------------
# STRING OPERATIONS IN PYTHON
# -------------------------------

print("----- STRING OPERATIONS -----")

# Create strings
s1 = "Hello"
s2 = 'World'
s3 = """This is
multi-line string"""

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)

# Access characters
print("First character:", s1[0])
print("Last character:", s1[-1])

# String slicing
print("Slice [0:4]:", s1[0:4])
print("Slice [1:]:", s1[1:])
print("Reverse string:", s1[::-1])

# String concatenation
s = s1 + " " + s2
print("Concatenation:", s)

# String repetition
print("Repeat:", s1 * 3)

# Length of string
print("Length:", len(s1))

# Convert case
print("Upper:", s1.upper())
print("Lower:", s1.lower())

# Remove spaces
s4 = "  hello  "
print("Strip:", s4.strip())

# Replace
print("Replace:", s.replace("Hello", "Hi"))

# Split string
text = "apple,banana,grape"
print("Split:", text.split(","))

# Join string
words = ["Python", "is", "easy"]
print("Join:", " ".join(words))

# Find and index
print("Find 'lo':", s1.find("lo"))
print("Index 'H':", s1.index("H"))

# Count occurrences
print("Count 'l':", s1.count("l"))

# Check functions
print("Is alphabet:", s1.isalpha())
print("Is digit:", "123".isdigit())
print("Is alphanumeric:", "abc123".isalnum())

# Startswith and endswith
print("Starts with He:", s1.startswith("He"))
print("Ends with lo:", s1.endswith("lo"))

# Loop through string
print("Characters in string:")
for ch in s1:
    print(ch)

# Check substring
if "ell" in s1:
    print("'ell' is present in string")


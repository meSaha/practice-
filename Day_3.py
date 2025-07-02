# String in Python
# A string is a sequence of characters enclosed in either single ('')
# or double (" ") quotes.

# String Assignment
my_string_part1 = "This is my part-1"
my_string_part2 = "This is my part-2"
print(my_string_part1, '\n', my_string_part2)

# String Concatenation :
print("Welcome to" + " "+ "Rajdeep dar pathshala")

# String Repetition:
print("Rajdeep dar pathshala\n"*4)

# String Indexing:

print("Rajdeep Dar Pathshala"[0])
print("Rajdeep Dar Pathshala"[1])
print("Rajdeep Dar Pathshala"[2])
print("Rajdeep Dar Pathshala"[3])
print("Rajdeep Dar Pathshala"[4])
print("Rajdeep Dar Pathshala"[5])
print("Rajdeep Dar Pathshala"[6])
print("Rajdeep Dar Pathshala"[7])
print("Rajdeep Dar Pathshala"[8])
print("Rajdeep Dar Pathshala"[9])
print("Rajdeep Dar Pathshala"[10])
print("Rajdeep Dar Pathshala"[11])
print("Rajdeep Dar Pathshala"[12])
print("Rajdeep Dar Pathshala"[13])
print("Rajdeep Dar Pathshala"[14])
print("Rajdeep Dar Pathshala"[15])
print("Rajdeep Dar Pathshala"[16])
print("Rajdeep Dar Pathshala"[17])
print("Rajdeep Dar Pathshala"[18])
print("Rajdeep Dar Pathshala"[19])
print("Rajdeep Dar Pathshala"[20])

# indexing:
print("Rajdeep Dar Pathshala"[0])
print("Rajdeep Dar Pathshala"[3])
print("Rajdeep Dar Pathshala"[5])
print("Rajdeep Dar Pathshala"[7])
print("Rajdeep Dar Pathshala"[-1]) # last letter a
print("Rajdeep Dar Pathshala"[-5])
print("Rajdeep Dar Pathshala"[-4])

# String Slicing:
# substrings can be extracted using slicing the format [start:end]
# The start index is included, while the index is excluded.
print("Rajdeep Dar Pathshala"[0:5])
print("Rajdeep Dar Pathshala"[3:7])
print("Rajdeep Dar Pathshala"[2:5])

# String Methods:
print("python".upper())
print("PYTHON".lower())
print("  rajdeep da  ".strip())
print("rajdeep".replace("rajdeep","Raja"))
print("rajdeep da".count("e"))
print("rajdeep da".find("ee"))
print("rajdeep da".split()) # each work in a list

# String Formatting:
print("welcome to - {}".format("Rajdeep Dar Pathshala"))

# Escape Characters:
print("ami amar moto \n tai ei bhabe porai")

# String Comparison:
print("ami" == "ami")
print("ami"!="amar moto")
print("ami boro"<"na ami")

# String Methods for checking content:
# find()
# index()
print("rajdeep dar pathshala".find("ee"))
print("rajdeep dar pathshala".index("ee"))

# replace()
print("rajdeep dar pathshala".replace("ee","aa"))

# String Conversion :
# int()
# float ()
# str()

print(int(45.89))
print(float("67.9"))
print(str(56))

# string splitting and joining:
print("Hello ami python sikhi".split(" "))
print("-".join(["rajdeep","dar","pathshala"]))

# string case conversion:
print("rajdeep dar pathshala".title())

# string stripping
print("   rajdeep dar pathshala   ".strip())
print("  rajdeep dar pathshala  ".lstrip())

# startswith() , endswith()
print("Hello".startswith("Hel"))
print("Rajdeep dar pathshala". endswith("pathshala"))

# String Searching and Replacement:
print("rajdeep dar pathshala".find("ee"))
print("rajdeep dar pathshala".index("ee"))

#replace() method replaces occurrences of a substring with another substring.
print("rajdeep dar pathshala".replace("ee","aa"))

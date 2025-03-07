# SFS Lab 3 - Python Regex Questions
# EC May, 2022
# Add your answer to each of the questions
import re


# Q1 Import the apache log and print out the contents
import re 

access_log = "apache_log"

text = "192"

with open(access_log) as f:
    for line in f:
        if text in line:
            print(line)

# once you have answer for Q1 comment out the print statement to keep things tidy


# Q2 Use regex to find any instance of the word notice?
# your code here

with open("apache_log") as f:
    file = f.read()
    x = re.findall("notice",file)
    print(len(x))

# Q3 Use regex to find any instance of the word error?
# your code here

file = open("apache_log", "r")
data = file.read()

occurrences = data.count("error")
print("Number of occurrences of the word: ", occurrences)
    
# Q4 Use regex to count any instance of the word notice?
# your code here

with open("apache_log") as f:
    file = f.read()
    x = re.findall("notice",file)
    print(len(x))

# Q5 Use regex to count any instance of the word error?
# your code here

with open("apache_log") as f:
    file = f.read()
    x = re.findall("error",file)
    print(len(x))
    
# Q6 Use regex to count any instance of the letter p?
# your code here

with open("apache_log") as f:
    file = f.read()
    x = re.findall("p",file)
    print(len(x))


# Q7 Use regex to find any instance of the string jk2_init?
# your code here

file = open("apache_log", "r")
data = file.read()

occurrences = data.count("jk2_init")
print("Number of occurrences of the word: ", occurrences)
    

# Q8 Use regex to find any appearance of the number 6754?
# your code here

access_log = "apache_log"

text = "6754"

with open(access_log) as f:
    for line in f:
        if text in line:
            print(line)

# Q9 Use regex to find any appearance of the number 6?
# your code here

access_log = "apache_log"

text = "6"

with open(access_log) as f:
    for line in f:
        if text in line:
            print(line)

# Q10 Use regex to find any ip addresses?
# your code here

access_log = "apache_log"

text = "192"

with open(access_log) as f:
    for line in f:
        if text in line:
            print(line)


# Q11 Create a script that will ask for user input, ask the user to enter a letter, then use regex to return any matches of that letter in the file?
# your code here
import re 

access_log = "apache_log"

text = input("Enter a letter")

with open(access_log) as f:
    for line in f:
        if re.search(text,line):
            print(line.strip())


# Q12 adapt your answer from Q11, to use a function to search the file, the function should take one parameter - the letter you are searching for?
# your code here

import re

access_log = "apache_log"
text = input("Enter a letter")

def search(access_log, text):
    with open(access_log, "r") as f:
        for line in f:
            if re.search(text,line):
                print(line.strip())
                
search(access_log, text)



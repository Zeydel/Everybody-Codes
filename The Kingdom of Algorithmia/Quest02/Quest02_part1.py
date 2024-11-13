import re

#Open file and read as list of strings
inputfile = open('input_part1.txt', 'r')
lines = inputfile.readlines()

# Seperate into words and inscription
words = lines[0].strip().split(':')[1].split(',')
inscription = lines[2].strip()

# Init var for the number of words
runic_words = 0

# For every word, count the number of occurrences and add to total
for word in words:
    runic_words += len(re.findall(word, inscription))
    

print(f'{runic_words} runic words appear on the inscription')

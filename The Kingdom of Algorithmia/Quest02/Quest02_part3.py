# Get the indices of characters from a word in a line
def get_indices_of_word(line, word):
    
    # Init empty set
    indices = set()
    
    # For the length of the word
    for i in range(len(line)):
        
        # If the remainder starts with the word or its inverse
        if line[i:].startswith(word) or line[i:].startswith(word[::-1]):
            
            # Add the indices of the word to the set
            indices = indices.union(range(i, i+len(word)))
            
    return indices

# Open file and read as list of strings
inputfile = open('input_part3.txt', 'r')
lines = inputfile.readlines()

# Seperate into words and inscription
words = lines[0].strip().split(':')[1].split(',')
inscription = [line.strip() for line in lines[2:]]

# Init empty set of runic character coordinate
indices = set()

# For every line
for y, line in enumerate(inscription):

    # Double it, to catch wrapping words
    doubleLine = line * 2
        
    # For every word
    for word in words:
    
        # Get the list of indices and add to set
        for i in get_indices_of_word(doubleLine, word):
            indices.add((i % len(line), y))
                    
# For every character in first line
for x in range(len(inscription[0])):
    
    # Build column
    column = ''
    for line in inscription:
        column += line[x]
        
    # For every word
    for word in words:
        
        # Get the list of indices and add to set
        for i in get_indices_of_word(column, word):
            indices.add((x, i))
    
print(f'{len(indices)} Runic characters appear on the scale armour')
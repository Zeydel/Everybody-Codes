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
inputfile = open('input_part2.txt', 'r')
lines = inputfile.readlines()

# Split input into words and inscription
words = lines[0].strip().split(':')[1].split(',')
inscription = [line.strip() for line in lines[2:]]

# Init var for the number of runic symbols
runic_symbols = 0

# Go through every line
for line in inscription:
        
    # Init an empty set of indices of runic symbols
    indices = set()
    
    # Go throug every word
    for word in words:
        indices.update(get_indices_of_word(line, word))
        
    # Add the number of indices to the total
    runic_symbols += len(indices)
    
# Print the results
print(f'{runic_symbols} runic symbols appear on the shield')
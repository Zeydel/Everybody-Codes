# Parse the input into a list of names and a dictionary of next possible letters
def parse(lines):
    
    names = lines[0].strip().split(',')
    
    mappings = dict()
    
    for line in lines[2:]:
        
        letter, next_letters = line.split(' > ')
        
        mappings[letter] = set(next_letters.strip().split(','))
        
    return names, mappings

# Find out if a name is possible
def is_name_possible(name, mappings):
    
    # For every pair of letters in the name
    for i in range(len(name)-1):
        
        # If the latter letter is not in the set of possible
        # letters, return false
        if name[i+1] not in mappings[name[i]]:
            return False
    
    # Otherwise return true
    return True

# Read the input as a string
lines = open('input_part2.txt', 'r').readlines()

# Parse the input
names, mappings = parse(lines)

# Init empty result
name_index_sum = 0

# For every name
for i in range(len(names)):
    
    # Check if it is possible
    if is_name_possible(names[i], mappings):
        name_index_sum += (1 + i)
        
# Print the result
print(f'The sum of indices of possible names is {name_index_sum}')
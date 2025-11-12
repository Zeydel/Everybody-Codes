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

# Get the shortest version of each name. E.g. if we have 'Jim', we don't
# also want 'Jimx"
def get_shortest_names(names):
    
    names = set(names)
    
    to_remove = set()
    
    for n1 in names:
        for n2 in names:
            
            if n1 == n2:
                continue
            
            if n1 in n2:
                to_remove.add(n2)
                
    return names - to_remove

# Recursive memoization method for finding the number of possible names
def get_postfix_count(last_letter, mappings, min_length, max_length, length, memo_dict):
    
    # If the length is at max, there is one possible name. Add that to the dict
    if length == max_length:
        memo_dict[(last_letter, length)] = 1
    
    # If we already know the answer for this letter and depth, return it
    if (last_letter, length) in memo_dict:
        return memo_dict[(last_letter, length)]
    
    # Init count as zero
    count = 0
    
    # If length is bigger than the minimum for a name, add 1
    if length >= min_length:
        count += 1
        
    # For every possible subsequent letter
    for l in mappings[last_letter]:
        
        # Add the count of names
        count += get_postfix_count(l, mappings, min_length, max_length, length + 1, memo_dict)
        
    # Add the count to the dictionary
    memo_dict[(last_letter, length)] = count
    
    # Return the answer
    return memo_dict[(last_letter, length)]

# Read the input as a string
lines = open('input_part3.txt', 'r').readlines()

# Parse the input
names, mappings = parse(lines)

# Remove the names that are just longer versions of other names
names = get_shortest_names(names)

# Init problem variables
min_length = 7
max_length = 11

# Init empty result
possible_names = 0

# Init dict for memoization
memo_dict = dict()

# For every name
for name in names:
    
    # Check if it is possible
    if is_name_possible(name, mappings):

        # Add number of postfixes to the result
        possible_names += get_postfix_count(name[-1], mappings, min_length, max_length, len(name), memo_dict)
        
# Print the result
print(f'The number of possible names is {possible_names}')
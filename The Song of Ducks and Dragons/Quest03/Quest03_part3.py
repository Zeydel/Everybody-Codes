# Parse the input into a list of integers
def parse(line):    
  
    return [int(n) for n in line.split(',')]

# Get minimum number of sets. The minimum number of sets is equal to the
# maximum count of any one crate size
def get_min_sets(crates):
    
    # Get the set of crate sizes
    crate_sizes = set(crates)
    
    # Init max occurenses 
    max_occurences = 0
    
    # for every size
    for cs in crate_sizes:
        
        # Count how many crates there are of that size
        size_count = 0
        
        for crate in crates:
            
            if crate == cs:
                size_count += 1
        
        # If there are more than the previous max, save new max
        if size_count > max_occurences:
            max_occurences = size_count
    
    return max_occurences

# Read the input as a string
line = open('input_part3.txt', 'r').readlines()[0]

# Parse the input
crates = parse(line)

# Get minimum number of sets
min_sets = get_min_sets(crates)

# Print the result
print(f'The minumum number of sets is {min_sets}')
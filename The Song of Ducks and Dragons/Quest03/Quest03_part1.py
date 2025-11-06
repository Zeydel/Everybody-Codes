# Parse the input into a list of integers
def parse(line):    
  
    return [int(n) for n in line.split(',')]

# Get maximum set size
def get_max_set_size(crates):
    
    # Sorte the crates by decending size
    crates = sorted(crates)[::-1]
    
    # Init size as zero
    size = 0
    
    # Init current crate size as infinity
    cur_crate_size = float('inf')
    
    # Go trough the crates
    for crate in crates:
        
        # If the crate can fit into the current
        if crate < cur_crate_size:
            
            # Add the crate to the size
            size += crate
            
            # Set the current crate size
            cur_crate_size = crate
            
    # Return the size
    return size

# Read the input as a string
line = open('input_part1.txt', 'r').readlines()[0]

# Parse the input
crates = parse(line)

# Get max set size
max_set_size = get_max_set_size(crates)

# Print the result
print(f'The maximum set size is {max_set_size}')
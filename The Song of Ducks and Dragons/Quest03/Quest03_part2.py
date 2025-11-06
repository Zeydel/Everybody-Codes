# Parse the input into a list of integers
def parse(line):    
  
    return [int(n) for n in line.split(',')]

# Get maximum set size
def get_min_set_size(crates):
    
    # Sorte the crates by ascending
    crates = sorted(crates)
    
    # Init size as zero
    size = 0
    
    # Init crate count
    crate_count = 0
    
    # Init current crate size
    cur_crate_size = 0
    
    # Go trough the crates
    for crate in crates:
        
        # If the crate is bigger than the current
        if crate > cur_crate_size:
            
            # Add the crate to the size
            size += crate
            
            # Add crate to count
            crate_count += 1
            
            # Set the current crate size
            cur_crate_size = crate
            
            # If we have found 20 crates return the size
            if crate_count == 20:
                return size
            
            
    # Return -1 if no set of 20 can be made
    return -1

# Read the input as a string
line = open('input_part2.txt', 'r').readlines()[0]

# Parse the input
crates = parse(line)

# Get max set size
max_set_size = get_min_set_size(crates)

# Print the result
print(f'The maximum set size is {max_set_size}')
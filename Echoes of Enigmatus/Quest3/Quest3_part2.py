from math import lcm

def parse(notes):
    
    snails = []
    
    for line in notes:
        
        x, y = line.split(' ')
        
        snails.append((int(x.split('=')[1]), int(y.split('=')[1])))
        
    return snails
        
def get_position_after_days(snail, days):
        
    # Get snail coordinates
    x, y = snail
    
    # Get the length of the loop
    loop_length = y + (x-1)
    
    # zero index coordinate system
    x -= 1
    y -= 1
        
    # Compute new position, add one to one-index system
    n_x = ((x + days) % loop_length) + 1
    n_y = ((y - days) % loop_length) + 1
    
    return n_x, n_y
    
# Get the time to align all snails
def get_alignment_time(snails):
    
    # Init step count as one
    step = 1
    
    # Current day
    current = 0

    # Empty list of cylinder lengths
    lengths = []
    
    # Set of already aligned snails
    snails_aligned = set()
    
    # As long as we havent aligned all snails
    while len(snails_aligned) < len(snails):
        
        # Increment days
        current += step
        
        # For every snail
        for snail in snails:
            
            # Skip if already aligned
            if snail in snails_aligned:
                continue
            
            # Get position after days
            x, y = get_position_after_days(snail, current)
        
            # If aligned
            if y == 1:
            
                # Add length to lengths
                lengths.append(x)
                
                # Get the new step as lcm of all previous
                step = lcm(*lengths)
                
                # Add snail to aligned snails
                snails_aligned.add(snail)
            
    # Return the current day
    return current

# Open and parse input
file = open('input_part2.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the input
snails = parse(notes)

# Init score
total_score = 0
  
# Get time until all snails are aligned on the x axist
days_to_alignment = get_alignment_time(snails)

# Print the results
print(f'It takes {days_to_alignment} days for the snails to align')
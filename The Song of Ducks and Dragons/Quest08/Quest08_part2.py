# Parse input into list of numbers
def parse(line):
    
    return [int(n) for n in line.split(',')]

# Determine if two threads cross
def threads_cross(t1, t2, nails):
    
    # If the two threads have the same start or end, they do not cross
    if t1[0] in t2 or t1[1] in t2:
        return False
    
    # Offset, every number, so that the start of t1 is at zero
    offset = t1[0]
    
    t1 = ((t1[0] - offset) % nails, (t1[1] - offset) % nails)
    t2 = ((t2[0] - offset) % nails, (t2[1] - offset) % nails)
    
    # Assume that both start and end are between the start and end of t1
    t2_start_side = -1
    t2_end_side = -1
    
    # If the start of t2 is outside the bounds of t1, switch its side
    if t2[0] > t1[1]:
        t2_start_side = 1
        
    # Likewise with the end of t2
    if t2[1] > t1[1]:
        t2_end_side = 1
        
    # If the siders are different, return true. Otherwise return false
    return t2_start_side != t2_end_side

# Get the number of knots
def get_knots(numbers, nails):
    
    # Init set of previous threads
    previous_threads = set()
    
    # Init number of knots
    knots = 0
    
    # For every pair of numbers
    for i in range(len(numbers) - 1):
        
        # For every previous thread
        for pt in previous_threads:
            
            # If the threads cross, add 1
            if threads_cross((numbers[i], numbers[i+1]), pt, nails):
                knots += 1
                
        # Add the threads to the previous
        previous_threads.add((numbers[i], numbers[i+1]))
            
    return knots

# Read the input as a string
line = open('input_part2.txt', 'r').readline()

# Parse input
numbers = parse(line)

# Init problem vars
nails = 256

# Get the number of knots
center_passes = get_knots(numbers, nails)

# Print the results
print(f'The string makes {center_passes} knots')
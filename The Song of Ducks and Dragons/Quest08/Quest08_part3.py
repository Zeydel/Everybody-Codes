# Parse input into list of numbers
def parse(line):
    
    return [int(n) for n in line.split(',')]

# Determine if two threads cross
def threads_cross(t1, t2, nails):
    
    if t1[0] in t2 and t1[1] in t2:
        return True
    
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
def get_best_cut(numbers, nails):
    
    # Init var for best cut
    best_cut = 0
    
    # For every combination of nails 
    for i in range(1, nails+1):
        
        for j in range(i+1, nails+1):
        
            # Init cut counter
            cut = 0
            
            # Check every string
            for n in range(len(numbers)-1):
    
                # Count cuts
                if threads_cross((i, j), (numbers[n], numbers[n+1]), nails):
                   cut += 1 
                   
            # If we have beat previous best, overwrite best
            if cut > best_cut:
                best_cut = cut
            
    # Return best
    return best_cut

# Read the input as a string
line = open('input_part3.txt', 'r').readline()

# Parse input
numbers = parse(line)

# Init problem vars
nails = 256

# Get the number of knots
best_cut = get_best_cut(numbers, nails)

# Print the results
print(f'The best cut cuts {best_cut} strings')
# Parse the input into a list of numbers
def parse(lines):
    
    return [int(n) for n in lines]
 
# Figure out if any ducks can move forwards
def can_move_forwards(columns):
    
    for i in range(len(columns)-1):
        
        if columns[i] > columns[i+1]:
            return True
        
    return False

# Perform one round of moving ducks forwards
def move_fowards(columns):
    
    for i in range(len(columns) - 1):
        
        if columns[i] > columns[i+1]:
            columns[i] -= 1
            columns[i+1] += 1
            
    return columns

# Perform one round of moving the ducks backwards
def move_backwards(columns):
    
    for i in range(len(columns) - 1):
        
        if columns[i] < columns[i+1]:
            columns[i] += 1
            columns[i+1] -= 1
            
    return columns

# Do a given number of rounds
def do_rounds(columns, rounds):
    
    # Starts by going forwards
    go_forwards = True
    
    # For every rounds
    for i in range(rounds):
        
        # Figure out if we are going forward or backwards
        go_forwards = go_forwards and can_move_forwards(columns)
        
        # Do either a forwards or backwards round
        if go_forwards:
            columns = move_fowards(columns)
        else:
            columns = move_backwards(columns)
            
    return columns

# Get the checksum
def get_checksum(columns):
    
    # Init as zero
    checksum = 0
    
    # For every column
    for i in range(len(columns)):
        
        # Add its value to the checksum
        checksum += ((i + 1) * columns[i])
        
    # Return the checksum
    return checksum
   
# Read the input as a string
lines = open('input_part1.txt', 'r').readlines()

# Parse the input
columns = parse(lines)

# Init problem variable
rounds = 10

# Do the given number of rounds
columns = do_rounds(columns, rounds)

# Get the checksum
checksum = get_checksum(columns)

# Print the results
print(f'The checksum after {rounds} rounds is {checksum}')
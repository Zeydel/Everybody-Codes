# Parse the input as a list of numbers
def parse(lines):
    
    numbers = []

    for line in lines:
        
        start, end = line.split('-')
        
        numbers.append((int(start), int(end)))
        
    return numbers

# Build the lock from the instructions
def build_lock(numbers):
    
    # Init lock with zero as start
    lock = [1]
    
    # Maintain two arrays for the first and second hald of the lock
    first_half = []
    second_half = []
    
    # For every number
    for i, num_range in enumerate(numbers):
        
        # Get start and end of range
        start, end = num_range
        
        # Create the range
        n = [num for num in range(start, end+1)]
        
        # If even index, add to first half
        if i % 2 == 0:
            first_half += n
            
        # Else add to second half in opposite order
        else:
            second_half += n
            
    # Put the arrays together
    return lock + first_half + second_half[::-1]

# Get the position after a given number of turns
def get_position_after_turns(lock, turns):
    
    return lock[turns % len(lock)]

# Read the input as a string
lines = open('input_part3.txt', 'r').readlines()

# Parse the unput
numbers = parse(lines)

# Init problem variable
turns = 202520252025

# Build the lock
lock = build_lock(numbers)

# Get position after the given number of turns
position = get_position_after_turns(lock, turns)

# Print the results
print(f'The position after {turns} turns is {position}')
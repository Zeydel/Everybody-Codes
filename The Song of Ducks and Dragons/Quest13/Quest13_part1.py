# Parse the input as a list of numbers
def parse(lines):
    
    return [int(n) for n in lines]

# Build the lock from the instructions
def build_lock(numbers):
    
    # Init lock with zero as start
    lock = [1]
    
    # Maintain two arrays for the first and second hald of the lock
    first_half = []
    second_half = []
    
    # For every number
    for i, n in enumerate(numbers):
        
        # If even index, add to first half
        if i % 2 == 0:
            first_half.append(n)
            
        # Else add to second hald
        else:
            second_half.append(n)
            
    # Put the arrays together
    return lock + first_half + second_half[::-1]

# Get the position after a given number of turns
def get_position_after_turns(lock, turns):
    
    return lock[turns % len(lock)]

# Read the input as a string
lines = open('input_part1.txt', 'r').readlines()

# Parse the unput
numbers = parse(lines)

# Init problem variable
turns = 2025

# Build the lock
lock = build_lock(numbers)

# Get position after the given number of turns
position = get_position_after_turns(lock, turns)

# Print the results
print(f'The position after {turns} turns is {position}')
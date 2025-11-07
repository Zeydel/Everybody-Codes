# Parse the input into a list of integers
def parse(lines):
    
    return [int(n) for n in lines]

# Get the number of rotations of the last cog, given a number
# of turns of the first cog
def get_rotations(cogs, turns):
    
    # The first cog makes one rotation per turn
    rotations = [1]
    
    # For every other cog, calculate the number of rotations per
    # turn of the first cog
    for i in range(1, len(cogs)):
        
        # The number of rotations is the relationship with the previous
        # cog, multiplied by the number of rotations of that cog
        rotations.append((cogs[i-1]/cogs[i]) * rotations[i-1])
    
    # We only care about whole rotations, so turn the result into an integer
    return int(rotations[-1] * turns)
    

# Read the input as a string
lines = open('input_part1.txt', 'r').readlines()

# Parse the result
cogs = parse(lines)

# Init number of turns of the first cog
turns = 2025

# Get the number of rotations of the last cog
rotations = get_rotations(cogs, turns)

# Print the results
print(f'The last cog rotates {rotations} times after {turns} turns of the first cog')
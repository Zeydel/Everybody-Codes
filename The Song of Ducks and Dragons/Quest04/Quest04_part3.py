# Parse the input into a mixed list tuples
def parse(lines):
    
    # Init empty list of cogs
    cogs = []
    
    # For every line
    for line in lines:
        
        # If the cog is a pair, parse as a tuple of the two values
        if '|' in line:
            size1, size2 = line.split('|')
            cogs.append((int(size1), int(size2)))
            
        # Else, parse as a tuple of the same value twice
        else:
            cogs.append((int(line), int(line)))
    
    # Return the list of cogs
    return cogs
    

# Get the number of rotations of the final cog, given a number of rotations
# of the first cog
def get_reotations(cogs, turns):
        
    # The first cog makes one rotation per turn
    rotations = [1]
    
    # For every cog in the list
    for i in range(1, len(cogs)):
        
        # The number of rotations is the relationship with the previous
        # cog, multiplied by the number of rotations of that cog
        rotations.append((cogs[i-1][1]/cogs[i][0]) * rotations[i-1])
        
    # We only care about whole rotations, so turn the result into an integer
    return int(rotations[-1] * turns)

    

# Read the input as a string
lines = open('input_part3.txt', 'r').readlines()

# Parse the result
cogs = parse(lines)

# Init number of turns of the first cog
turns = 100

# Get the number of rotations of the final cog
rotations = get_reotations(cogs, turns)

# Print the results
print(f'The last cog rotates {rotations} times after {turns} turns of the first cog')
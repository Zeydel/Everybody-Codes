import math

# Parse the input into a list of integers
def parse(lines):
    
    return [int(n) for n in lines]

# Get the required number of turns of the first cog, given a target number
# of rotations of the final cog
def get_required_turns(cogs, rotations):
    
    # Reverse the list of cogs. We are working backwards
    cogs = cogs[::-1]
    
    # The final cog will make the target number of rotations
    rotations = [rotations]
    
    # For every cog in the list
    for i in range(1, len(cogs)):
        
        # Find the number of rotations the cog will need to make
        # in order for the final cog to rotate the target
        # number of times
        rotations.append(rotations[i-1] / (cogs[i]/cogs[i-1]))
        
    # We are interested in while rotations, so round up the final
    # result
    return math.ceil(rotations[-1])
    

# Read the input as a string
lines = open('input_part2.txt', 'r').readlines()

# Parse the result
cogs = parse(lines)

# Init target number of rotations for the last wheel
target_rotations = 10000000000000

# Get the number of required turns
turns = get_required_turns(cogs, target_rotations)

# Print the results
print(f'{turns} of the first cog is required to make the final cog turn {target_rotations} times')
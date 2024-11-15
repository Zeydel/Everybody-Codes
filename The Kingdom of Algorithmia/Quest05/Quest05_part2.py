# Convert lines to columns
def convert_lines_to_columns(lines):
    
    # Initialise the columns we need
    columns = [[] for l in lines[0].split()]
    
    # For every line
    for line in lines:
        
        # Convert each element to int and place in the correct column
        for i, n in enumerate(line.split()):
            columns[i].append(int(n))
            
    # Return the columns
    return columns

# Do one round of the dance
def do_round(columns, index):
    
    # Get the current clapper
    clapper = columns[index].pop(0)
    
    # Get the index of the colum that they will dance down
    ci = (index + 1) % len(columns)
    
    # Initialize the number of steps they have left to take
    steps_left = clapper
            
    # If we have more steps left than double the number of the column, we can skip it entirely and move to the next one
    steps_left %= (2 * len(columns[ci]))
            
    # Init var to figure out where to place the clapper
    idx = -1
    
    # Edgecase: If there is 0 steps left, it coresponds to having gone around the column
    # n times. Place clapper behind he first person
    if steps_left == 0:
        idx = 1
        
    # If clapper is absorbed going down the column, put them in before the place where they will end
    elif steps_left <= len(columns[ci]):
        idx = steps_left-1
                
    # If the clapper is absorbed goind up the colum, put them in before
    else:
        steps_left %= len(columns[ci])
        steps_left = len(columns[ci]) - (steps_left - 1)
        idx = steps_left - 1
        
    # Make the new column, including the clapper
    columns[ci] = columns[ci][:idx] + [clapper] + columns[ci][idx:]
        
    return columns
            
# Get the number shoutet
def get_number(columns):
    
    # Initialise the number
    number = ''
    
    # Append the number of everyone who is first in their colum
    for column in columns:
        number += str(column[0])
        
    return number
        
# Open input and read as strings
file = open('input_part2.txt', 'r')
lines = [line.strip() for line in file]

# Convert to columns
columns = convert_lines_to_columns(lines)

# Init dictionary to count number of each shouts
shouts = dict()

# Var for current round number
current_round = 0

target_number = 2024

# Perform rounds
while True:
    
    # Do a round
    do_round(columns, current_round % len(columns))
    
    # Get the current shout
    shout = get_number(columns)
    
    # If we have not seen that shout yet, add it to the dict
    if shout not in shouts:
        shouts[shout] = 0
    
    # Increment the number of times we have seen that shout
    shouts[shout] += 1
    
    # Increment the number of shouts
    current_round += 1
    
    # If we have reached the target number of shouts, break
    if shouts[shout] == target_number:
        break
    
# Print the result
print(f'The {target_number}th shout of {shout} appears after round {current_round}, resulting in {current_round * int(shout)}')
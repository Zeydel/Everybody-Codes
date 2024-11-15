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
        steps_left = (len(columns[ci]) + 2) - steps_left
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
file = open('input_part1.txt', 'r')
lines = [line.strip() for line in file]

# Convert to columns
columns = convert_lines_to_columns(lines)

# Init the number of rounds
number_of_rounds = 10

# Do the required number of rounds
for current_round in range(number_of_rounds):
    do_round(columns, current_round % len(columns))
    
    
# Print the result
print(f'{get_number(columns)} is the shout after {number_of_rounds} rounds')
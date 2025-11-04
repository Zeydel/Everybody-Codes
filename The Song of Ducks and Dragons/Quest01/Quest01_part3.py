# Turn the commands into tuples of direction and count
def parse_commands(commands):
    
    parsed = []
    
    for command in commands.split(','):
        
        direction = command[0]
        count = int(command[1:])
        
        parsed.append((direction, count))
        
    return parsed

# Read the input as a string
lines = open('input_part3.txt', 'r').readlines()

# Parse input into names and commnads
names = lines[0].split(',')
commands = parse_commands(lines[2])

# Init current name index
current_name_index = 0

# Go though commands and swap names
for direction, count in commands:
    
    index_to_swap = -1
    
    if direction == 'R':
        index_to_swap = count % len(names)
    else:
        index_to_swap = (-count) % len(names)
        
    names[0], names[index_to_swap] = names[index_to_swap], names[0]
    
# Print the result
print(f'My second parents name is {names[0]}')
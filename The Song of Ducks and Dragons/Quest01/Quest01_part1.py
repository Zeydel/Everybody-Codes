# Turn the commands into tuples of direction and count
def parse_commands(commands):
    
    parsed = []
    
    for command in commands.split(','):
        
        direction = command[0]
        count = int(command[1:])
        
        parsed.append((direction, count))
        
    return parsed

# Read the input as a string
lines = open('input_part1.txt', 'r').readlines()

# Split input into names and commands
names = lines[0].split(',')
commands = parse_commands(lines[2])

# Init index of current name
current_name_index = 0

# Go through command list find new name
for direction, count in commands:
    
    if direction == 'R':
        current_name_index = min(len(names)-1, current_name_index + count)
    else:
        current_name_index = max(0, current_name_index - count)
        
# Print the resuluts
print(f'My name is {names[current_name_index]}')
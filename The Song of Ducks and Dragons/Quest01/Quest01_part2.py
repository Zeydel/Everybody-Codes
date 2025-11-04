# Turn the commands into tuples of direction and count
def parse_commands(commands):
    
    parsed = []
    
    for command in commands.split(','):
        
        direction = command[0]
        count = int(command[1:])
        
        parsed.append((direction, count))
        
    return parsed

# Read the input as a string
lines = open('input_part2.txt', 'r').readlines()

# Parse input into names and commands
names = lines[0].split(',')
commands = parse_commands(lines[2])

# Init current name index
current_name_index = 0

# Go through directions and find new index
for direction, count in commands:
    
    if direction == 'R':
        current_name_index += count
    else:
        current_name_index -= count
        
    current_name_index %= len(names)
        
# Print the result
print(f'My first parents name is {names[current_name_index]}')
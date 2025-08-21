def parse(notes):
    
    snails = []
    
    for line in notes:
        
        x, y = line.split(' ')
        
        snails.append((int(x.split('=')[1]), int(y.split('=')[1])))
        
    return snails
        
def get_position_after_days(snail, days):
        
    # Get snail coordinates
    x, y = snail
    
    # Get the length of the loop
    loop_length = y + (x-1)
    
    # zero index coordinate system
    x -= 1
    y -= 1
        
    # Compute new position, add one to one-index system
    n_x = ((x + days) % loop_length) + 1
    n_y = ((y - days) % loop_length) + 1
    
    return n_x, n_y
    
# Get the score for the position of a snail
def get_snail_score(snail):
    
    x, y = snail
    
    return x + (100 * y)

# Open and parse input
file = open('input_part1.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the input
snails = parse(notes)

# Init number of days
days = 100

# Init score
total_score = 0

# For every snail, get the new position and add value to total
for snail in snails:
    
    new_pos = get_position_after_days(snail, days)
    total_score += get_snail_score(new_pos)
    
# Print the result
print(f'The total value of the snails after {days} is {total_score}')
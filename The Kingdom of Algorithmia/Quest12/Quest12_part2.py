# Get location of every target and catapult as coordinate.
def parse(notes):
    
    catapults = []
    targets = []
    
    for i in range(len(notes)):
        for j in range(len(notes[i])):
            if notes[i][j] in ['A', 'B', 'C']:
                catapults.append((notes[i][j],(i,j)))
            
            if notes[i][j] in ['T', 'H']:
                targets.append((notes[i][j],(i,j)))
                
    return (catapults, targets)

# Get the segment number of a catapult from its letter
def get_segment_number(catapult):
    
    if catapult == 'A':
        return 1
    if catapult == 'B':
        return 2
    if catapult == 'C':
        return 3

# Get hits to destroy a block
def get_hits(block):
    
    if block == 'T':
        return 1
    if block == 'H':
        return 2

# Compute location of a target, as if it was on level with the catapult
# This enables us to easier identify the speed needed to hit it, without
# altering the result
def get_aligned_position(catapult_location, target):
    
    height_dif = catapult_location[0] - target[0]
    
    return (target[0] + height_dif, target[1] + height_dif)

# Given a target and every catapult, get the ranking
def get_ranking(target, catapults):
    
    target_name, target_pos = target
    
    # For every catapult
    for name, location in catapults:
        
        # Compute the position of the target, as if it was on level
        # with the target
        aligned_pos = get_aligned_position(location, target_pos)
        
        # If the distance between catapult and target is a multiple of 3, we can hit it
        if (aligned_pos[1] - location[1]) % 3 == 0:
            
            # Compute the ranking value and return it
            return ((aligned_pos[1] - location[1]) // 3) * get_segment_number(name) * get_hits(target_name)
            
        


# Open and parse input
file = open('input_part2.txt','r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
catapults, targets = parse(lines)

# Init value to be outputted
ranking_sum = 0

# Compute and add together ranking of every target
for target in targets:
    
    ranking_sum += get_ranking(target, catapults)

# Print the result
print(f'The ranking value of destroying the targets is {ranking_sum}')
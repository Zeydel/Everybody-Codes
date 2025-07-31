# Parse initial coordinates as coordinates
def parse(notes):
    
    meteors = []
    
    for line in notes:
        
        length, height = line.split()
        
        meteors.append((int(length), int(height)))
        
    return meteors

# Init the catapults
def init_catapults():
    
    catapults = []
    catapults.append(('A', (0,0)))
    catapults.append(('B', (0,1)))
    catapults.append(('C', (0,2)))
    
    return catapults
    
# Get segment number from name of the catapult
def get_segment_number(catapult):
    
    if catapult == 'A':
        return 1
    if catapult == 'B':
        return 2
    if catapult == 'C':
        return 3

# Get the earliest position in which we can hit the meteor
def get_earliest_hit_pos(meteor):
    
    hit_length = meteor[0] // 2
    
    dif = meteor[0] - hit_length
    
    return (hit_length, meteor[1] - dif)
    
# Compute location of a target, as if it was on level with the catapult
# This enables us to easier identify the speed needed to hit it, without
# altering the result
def get_aligned_position(catapult_location, target):
    
    height_dif = catapult_location[1] - target[1]
    
    return (target[0] - height_dif, target[1] + height_dif)

# If the meteor flies over the catapult, we will not be able to hit it
def can_hit(catapult_pos, meteor_pos):
    
    if meteor_pos[1] - meteor_pos[0] <= catapult_pos[1]:
        return True
    
    return False

# Compute the rank of hitting a meteor at a specific position
def compute_rank(meteor_pos, catapult):
    
    # Seperate catapult into name and position
    catapult_name, catapult_pos = catapult
    
    # Get the segment number
    segment_number = get_segment_number(catapult_name)
    
    # Exit early if the meteor flies over the catapult
    if not can_hit(catapult_pos, meteor_pos):
        return float('inf')
    
    # Case 1, we can hit the meteor on the way up
    if meteor_pos[0] - catapult_pos[0] == meteor_pos[1] - catapult_pos[1]:
        return meteor_pos[0] * segment_number
    
    # Case 2, we can hit the meteor on the horizontal stretch
    power = meteor_pos[1] - catapult_pos[1]
    if meteor_pos[0] > power and meteor_pos[0] <= 2*power and power > 0:
        return power * segment_number
    
    # Case 3, we can hit the meteor on the way down
    aligned_pos = get_aligned_position(catapult_pos, meteor_pos)
    
    if (aligned_pos[0] - catapult_pos[0]) % 3 == 0:
        return ((aligned_pos[0] - catapult_pos[0]) // 3) * segment_number
    
    # If no case has hit, return infinity
    return float('inf')
    
# Get the minimum ranking of hitting a meteor at the highest possible place 
def get_ranking(meteor, catapults):
    
    # Get the earlist position we can hit the meteor
    meteor_pos = get_earliest_hit_pos(meteor)
    
    # Init rank as infinity
    best_rank = float('inf')
    
    # While the meteor has not yet hit the ground
    while meteor_pos[1] > -1:
        
        # For every catapult
        for catapult in catapults:
            
            # Compute the rank
            rank = compute_rank(meteor_pos, catapult)
            
            # If we have beaten the best rank, update it
            if rank < best_rank:
                best_rank = rank
                    
        # If we can hit the meteor at the current place, return the rank
        if best_rank != float('inf'):
            return best_rank
        
        # Update meteor position by one tick
        meteor_pos = (meteor_pos[0] - 1, meteor_pos[1] - 1)

    
# Open and parse input
file = open('input_part3.txt','r')
lines = [line.strip() for line in file.readlines()]

# parse the input into meteors and init the catapults
meteors = parse(lines)
catapults = init_catapults()

# Init value to be outputted
ranking_sum = 0

# For every meteor
for meteor in meteors:
    
    # Compute ranking and add to running total
    ranking_sum += get_ranking(meteor, catapults)
    
# Print the result
print(f'The ranking value of destroying the meteors is {ranking_sum}')
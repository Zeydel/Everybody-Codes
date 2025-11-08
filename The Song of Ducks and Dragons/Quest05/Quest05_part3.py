from functools import cmp_to_key

# Parse the input into a list of lists of integers
def parse(lines):
    
    swords = []
    
    for line in lines:
        
        sword_id = int(line.split(':')[0])
        sword_numbers = [int(n) for n in line.split(':')[1].split(',')]
        
        swords.append((sword_id, sword_numbers))
    
    return swords

# Build the fishbone from the numbers
def build_fishbone(sword):
    
    # Start with an empty fishbone
    fishbone = []
    
    # For every number
    for n in sword[1]:
        
        # Go through the fishbone from the top
        i  = 0
        
        while i <= len(fishbone):
            
            # If we are at the end, add the number to the end and break
            if i == len(fishbone):
                fishbone.append([-1, n, -1])
                break
            
            # If it is smaller than the current number and the left spot is
            # free, put it there
            if n < fishbone[i][1] and fishbone[i][0] == -1:
                fishbone[i][0] = n
                break
            
            # If it is bigger than the current number and the right spot is
            # free, put it there
            elif n > fishbone[i][1] and fishbone[i][2] == -1:
                fishbone[i][2] = n
                break
            
            i += 1
            
    # Return the fishbone
    return (sword[0], fishbone)

# Get the quality of a fishbone
def get_quality(fishbone):
    
    # Start with an empty string
    quality = ''
    
    # Go down the fishbone and add the middle number to the string
    for n in fishbone:
        quality += str(n[1])
        
    # Return the quality as an integer
    return int(quality)

# Get the score of a level of a sword
def get_level_score(sword, level):
    
    # Init empty string
    level_score = ''
    
    # For every number on the level
    for n in sword[level]:
        
        # If id has a value, add it to the strng
        if n != -1:
            level_score += str(n)
            
    # Return score as integer
    return int(level_score)

# Compare two fishbones
def compare_fishbones(s1, s2):
    
    # Get the two qualities
    q1 = get_quality(s1[1])
    q2 = get_quality(s2[1])
    
    # If they are not equal, return the difference
    if q1 != q2:
        return q2 - q1
    
    # Go through every level
    for i in range(len(s1[1])):
        
        # Get the two level scores
        ls1 = get_level_score(s1[1], i)
        ls2 = get_level_score(s2[1], i)
        
        # If they are not equal, return the difference
        if ls1 != ls2:
            return ls2 - ls1
        
    # If all else fails, return the difference of ids
    return s2[0] - s1[0]
  
# Calculate the checksum
def calculate_checksum(fishbones):
    
    # Init checksum as zero
    checksum = 0
    
    # Init position
    i = 1
    
    # For every fishbone
    for f in fishbones:
        
        # Add the id multiplied by its position
        checksum += (i * f[0])
        i += 1
        
    # Return the checksum
    return checksum
    
  
# Read the input as a string
lines = open('input_part3.txt', 'r').readlines()

# Parse the input
swords = parse(lines)

# Compute every fishbone
fishbones = []

for s in swords:
    fishbones.append(build_fishbone(s))
    
# Sort the fishbones by the custom sorting function
fishbones = sorted(fishbones, key= cmp_to_key(compare_fishbones))

# Compute the checksum
checksum = calculate_checksum(fishbones)

# Print the result
print(f'TThe checksum is {checksum}')
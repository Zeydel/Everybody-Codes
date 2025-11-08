# Parse the input into a list of lists of integers
def parse(lines):
    
    swords = []
    
    for line in lines:
        swords.append([int(n) for n in line.split(':')[1].split(',')])
    
    return swords

# Build the fishbone from the numbers
def build_fishbone(numbers):
    
    # Start with an empty fishbone
    fishbone = []
    
    # For every number
    for n in numbers:
        
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
    return fishbone

# Get the quality of a fishbone
def get_quality(fishbone):
    
    # Start with an empty string
    quality = ''
    
    # Go down the fishbone and add the middle number to the string
    for n in fishbone:
        quality += str(n[1])
        
    # Return the quality as an integer
    return int(quality)

# Read the input as a string
lines = open('input_part2.txt', 'r').readlines()

# Parse the input
swords = parse(lines)

# Init vars for max and min quality
min_quality, max_quality = float('inf'), float('-inf')

for sword in swords:
    # Build the fishbone
    fishbone = build_fishbone(sword)

    # Read its quality
    quality = get_quality(fishbone)
    
    # Overwrite current bests if applicable
    if quality < min_quality:
        min_quality = quality
    if quality > max_quality:
        max_quality = quality

# Compute the difference in quality
quality_difference = max_quality - min_quality

# Print the result
print(f'The difference in quality between the best and worst sword is {quality_difference}')
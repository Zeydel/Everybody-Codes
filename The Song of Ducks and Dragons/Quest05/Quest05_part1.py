# Parse the input into a list of integers
def parse(line):
    
    return [int(n) for n in line.split(':')[1].split(',')]

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
line = open('input_part1.txt', 'r').readline()

# Parse the input
numbers = parse(line)

# Build the fishbone
fishbone = build_fishbone(numbers)

# Read its quality
quality = get_quality(fishbone)

# Print the result
print(f'The quality of the sword is {quality}')
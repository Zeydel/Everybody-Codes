# Get tje number of beetles needed for a ball, given a list of stamps.
# For this specific list of stamps, it is enough to simply apply the biggest stamp first, as many times
# as needed and then move on in the same way down the list
# This is not the case in the more general problem
def get_beetles_for_ball(ball, stamps):
    
    # Init number of beetles needed
    beetles_needed = 0
    
    # For every stamp in descending size
    for stamp in stamps[::-1]:
        
        # Add the number of beetles we can stamp with it
        beetles_needed += ball // stamp
        
        # Decrease the number of needed spots
        ball -= (ball // stamp) * stamp
        
    # Return the beetles needed
    return beetles_needed

# Open the file and read each line a an int
file = open("input_part1.txt", 'r')
balls = [int(line) for line in file.readlines()]

# Init list of stamp
stamps = [1, 3, 5, 10]

# Init total number of needed beetles
total_beetles_needed = 0

# For every ball in the list
for ball in balls:
    
    # Add the number of needed beetles
    total_beetles_needed += get_beetles_for_ball(ball, stamps)

# Print the results
print(f'{total_beetles_needed} is the number of beetles needed')
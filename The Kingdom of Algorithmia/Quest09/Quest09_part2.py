# Recursive functio to get the number of beetles needed for a ball
def get_beetles_for_ball(ball, stamps, optimal_dict):
    
    # If we already know the anser, return it
    if ball in optimal_dict:
        return optimal_dict[ball]
    
    # If we are below zero, return infinity
    if ball < 0:
        return float('inf')
    
    # If we dont have to do anythin, return 0
    if ball == 0:
        return 0
          
    # Otherwise start searching for the best number
    best = float('inf')
        
    # For every stamp
    for stamp in stamps:

        # Get the best number of beetles needed if we use the stamp        
        beetles = 1 + get_beetles_for_ball(ball - stamp, stamps, optimal_dict)
        
        # If that is better than the best so far, save it
        if beetles < best:
            best = beetles
            
    # Save the result and return it
    optimal_dict[ball] = best
    return best
        
        

# Open the file and read each line a an int
file = open("input_part2.txt", 'r')
balls = [int(line) for line in file.readlines()]

# Init stamps
stamps = [30, 25, 24, 20, 16, 15, 10, 5, 3, 1]

# Init total number of needed beetles
total_beetles_needed = 0

# Init dict to save optimal values
optimal_dict = dict()

# For every ball
for ball in balls:
    
    # Add the optimal number of beetles
    total_beetles_needed += get_beetles_for_ball(ball, stamps, optimal_dict)
    
# Print the results
print(f'{total_beetles_needed} is the number of beetles needed')
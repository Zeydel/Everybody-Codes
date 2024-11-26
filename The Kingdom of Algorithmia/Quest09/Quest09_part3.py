import math

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
file = open("input_part3.txt", 'r')
balls = [int(line) for line in file.readlines()]

# Init the stamps
stamps = [101, 100, 75, 74, 50, 49, 38, 37, 30, 25, 24, 20, 16, 15, 10, 5, 3, 1]

# Init total number of needed beetles
total_beetles_needed = 0

optimal_dict = dict()

# For every ball
for ball in balls:
    
    # Init a value for the optimal number of beetles
    optimal_split_beetles = float('inf')
    
    # For every difference
    for i in range(0, 51):
        
        # Init the targets
        target_1 = math.ceil(ball / 2) - i
        target_2 = math.floor(ball / 2) + i
        
        # Get the beetles for each ball
        beetles_ball_1 = get_beetles_for_ball(target_1, stamps, optimal_dict)
        beetles_ball_2 = get_beetles_for_ball(target_2, stamps, optimal_dict)
        
        # If the result it better than the one we have so far, save it
        if beetles_ball_1 + beetles_ball_2 < optimal_split_beetles:
            optimal_split_beetles = beetles_ball_1 + beetles_ball_2
    
    # Add to total
    total_beetles_needed += optimal_split_beetles
    
# Print the results
print(f'{total_beetles_needed} is the number of beetles needed')
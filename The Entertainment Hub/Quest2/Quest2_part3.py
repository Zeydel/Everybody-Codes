# Get the number of arrows needed to pop every baloon
def get_arrows_to_pop_balloons(balloons):

    # Init shot order
    shots = ['R', 'G', 'B']
    
    # Shot index
    shot_idx = 0    

    # While there is more than one balloon
    while len(balloons) > 1:
                
        # Compute middle
        mid = len(balloons) // 2
        
        # Determine if there is an even number of balloons
        even = len(balloons) % 2 == 0

        # Split into top and bottom ballons
        top_balloons = balloons[:mid]
        bottom_balloons = balloons[mid:]
        
        # Init bottoms remaining for next iterations
        new_bottom = ""
        
        # Set some vars depending on if there is even or odd balloons
        if even:
            bottom_idx = 0
        else:
            bottom_idx = 1
            new_bottom = bottom_balloons[0]
        
        # Go through top balloons
        for balloon in top_balloons:
            
            # Determine the shot to take
            shot = shots[shot_idx % 3]
            
            # If the number of ballons is even, and the shot doesn't match
            # the color of the balloon, save the opposite balloon for next
            # iteration and increment bottom index. There is now
            # an odd number of balloons
            if even and balloon != shot:
                new_bottom += bottom_balloons[bottom_idx]
                bottom_idx += 1
                even = False
            # If the number of balloons is even and the shot matches the ballon
            # increment the bottom index, to signal that the opposite ballon has
            # been popped
            elif even:
                bottom_idx += 1
            # If the number of ballons is odd, we only pop the topmost ballon
            # there is now an even number of ballons
            else:
                even = True
            
            # Increment shot index
            shot_idx += 1
            
        # Compute remaining balloons
        balloons = new_bottom + bottom_balloons[bottom_idx:]
        
    # Return the number of shots taken, plus 0 or 1 depending on if there
    # are any balloons left
    return shot_idx + len(balloons)

# Open and parse input
file = open('input_part3.txt','r')
balloons = file.read().strip()

# Number of repeats
repeats = 100000
    
# Compute baloon sequence
balloons = balloons * repeats
    
# Compute the result
arrows = get_arrows_to_pop_balloons(balloons)

# Print the result
print(f'{arrows} arrows are needed to pop the balloons')
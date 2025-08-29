# Get the number of arrows needed to pop every baloon
def get_arrows_to_pop_balloons(balloons):

    # Init shot order
    shots = ['R', 'G', 'B']
    
    # Shot index
    shot_idx = 0    

    while len(balloons) > 0:
        
        # Get the currect shot
        shot = shots[shot_idx % 3]

        first_balloon = balloons[0]

        # Shoot the first balloon
        balloons = balloons[1:]
        
        # If the we can hit another balloon through the circle, and the shot
        # matches the first ballon, shoot the next one too
        if len(balloons) % 2 == 1 and shot == first_balloon:
            mid_idx = len(balloons) // 2
            
            balloons = balloons[:mid_idx] + balloons[mid_idx+1:]
            
        # Increment shot index
        shot_idx += 1
        
    return shot_idx

# Open and parse input
file = open('input_part2.txt','r')
balloons = file.read().strip()

# Init the number of repeats
repeats = 100

# Repeat the balloons
balloons = balloons * repeats

# Compute the number of arrows
arrows = get_arrows_to_pop_balloons(balloons)

# Print the results
print(f'{arrows} arrows are needed to pop the balloons')
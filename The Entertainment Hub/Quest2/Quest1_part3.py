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
            
            if even and balloon != shot:
                new_bottom += bottom_balloons[bottom_idx]
                bottom_idx += 1
                even = False
            elif even:
                bottom_idx += 1
            else:
                even = True
            
            shot_idx += 1
            
        balloons = new_bottom + bottom_balloons[bottom_idx:]
        
    return shot_idx + len(balloons)

# Open and parse input
file = open('input_part3.txt','r')
balloons = file.read().strip()

repeats = 100000
    
balloons = balloons * repeats
    
arrows = get_arrows_to_pop_balloons(balloons)

print(f'{arrows} arrows are needed to pop the balloons')
# Get the number of arrows needed to pop every baloon
def get_arrows_to_pop_balloons(balloons):
    
    # Init shot order
    shots = ['R', 'G', 'B']
    
    # Shot index
    shot_idx = 0
        
    # While there are still balloons left
    while len(balloons) > 0:
        
        # Get the currect shot
        shot = shots[shot_idx % 3]
        
        # Find the first balloon that is a different color
        balloon_idx = 0
        
        while balloon_idx < len(balloons) and balloons[balloon_idx] == shot:
            balloon_idx += 1
            
        # Remove the frontmost balloons
        balloons = balloons[balloon_idx+1:]
        
        # Add one to shot index
        shot_idx += 1
                
    # Return shot index
    return shot_idx
        
    

# Open and parse input
file = open('input_part1.txt','r')
balloons = file.read().strip()

# Get the number of arrows
arrows = get_arrows_to_pop_balloons(balloons)

print(f'{arrows} arrows are needed to pop the balloons')
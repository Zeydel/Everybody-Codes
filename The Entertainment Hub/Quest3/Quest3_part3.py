# Parse notes into list of dice and racetrack
def parse(notes):

    dice = dict()
    
    split_idx = 0

    for line in notes:
        
        split_idx += 1
        
        if len(line) == 0:
            break
        
        die_id, numbers, seed = line.split(' ')
        
        numbers = numbers.split('[')[1].split(']')[0]
        seed = int(seed.split('=')[1])
        
        faces = [int(n) for n in numbers.split(',')]
                
        die = Die(faces, seed)
        dice[int(die_id[:-1])] = die        
        
        
    track = notes[split_idx:]
        
    return dice, track
    
# Class for a die
class Die:
    
    def __init__(self, faces, seed):
        self.faces = faces
        self.seed = seed
        self.pulse = seed
        self.rolls = 0
        self.face_index = 0
        
        
    def roll(self):
        
        self.rolls += 1
        
        spin = self.rolls * self.pulse
        
        self.pulse += spin
        
        self.pulse %= self.seed
        
        self.pulse += 1 + self.rolls + self.seed
        
        self.face_index += spin
        self.face_index %= len(self.faces)
        
        return self.faces[self.face_index]
           
# Get places that players can start along with the dice
# that they use         
def get_starts(dice, track):
    
    starts = []
    
    rolls = dict()
    
    for die in dice:
        
        rolls[(die, 0)] = dice[die].roll()
        
    for y in range(len(track)):
        for x in range(len(track[y])):
            
            for roll in rolls:
                
                if rolls[roll] == int(track[y][x]):
                    starts.append((x, y, roll[0], 0))
                    
    return starts, rolls
   
# Get places we can go, after a sucessful roll
def get_neighbors(x, y):
    
    return [(x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1),
            (x, y)]

# Get the max coins that can be won in the game
def get_max_coins(dice, track):
    
    # Get starts and first rolls
    queue, rolls = get_starts(dice, track)
        
    # Init empty set of states that has been explored
    explored = set()
    
    # Init empty set of positions where coins has been taken
    coins_taken = set()
    
    # While there are states left to explore
    while len(queue) > 0:
        
        # Pop the first element
        x, y, die_id, length = queue.pop(0)
        
        # If it has already been explored, continue
        if (x, y, die_id, length) in explored:
            continue
        
        # Add state to explored
        explored.add((x, y, die_id, length))
        
        # Add position to coins taken
        coins_taken.add((x, y))
        
        # If we don't know what the next target is, roll the die
        if (die_id, length + 1) not in rolls:
            rolls[(die_id, length+1)] = dice[die_id].roll()
        
        # Get target
        target = rolls[(die_id, length+1)]
            
        # For every next position
        for nx, ny in get_neighbors(x, y):
            
            # Check if we are within bounds
            if ny >= len(track) or ny < 0:
                continue
            
            if nx >= len(track[ny]) or nx < 0:
                continue

            # If it is not the correct number, continue            
            if track[ny][nx] != str(target):
                continue
            
            # Append next state to queue
            queue.append((nx, ny, die_id, length+1))
            
    # Return size of explored set
    return len(set(coins_taken))        
        
    
# Open and parse input
file = open('input_part3.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse input
dice, track = parse(notes)

# Get the maximum number of coins
max_coins = get_max_coins(dice, track)

# Print the results
print(f'The maximum number of coins obtainable is {max_coins}')
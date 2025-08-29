# Parse notes into list of dice and racetrack
def parse(notes):

    dice = []
    
    track = notes[-1]
    notes = notes[:-2]

    for line in notes:
        die_id, numbers, seed = line.split(' ')
        
        numbers = numbers.split('[')[1].split(']')[0]
        seed = int(seed.split('=')[1])
        
        faces = [int(n) for n in numbers.split(',')]
                
        die = Die(int(die_id[:-1]), faces, seed)
        dice.append(die)
        
    return dice, track
    
# Class for a die
class Die:
    
    def __init__(self, die_id, faces, seed):
        self.die_id = die_id
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
    
# Function to perform race
def race(dice, track):
    
    # init dict for each dies position on the track
    pos = dict()
    
    # Init set of dice that are still playing
    playing = set()
    
    # Init finishing order
    order = []
    
    # For every die, set them on the start of the track and
    # add to pool of still playing dice
    for die in dice:
        pos[die.die_id] = 0
        playing.add(die.die_id)
        
    # While there is still at least two dice playing
    while len(playing) > 1:
        
        # For every dice
        for die in dice:
            
            # If it is still playing
            if die.die_id not in playing:
                continue
            
            # Find target
            target = int(track[pos[die.die_id]])
            
            # Roll dice
            roll = die.roll()
            
            # If they match, move forward
            if roll == target:
                
                # Increment position
                pos[die.die_id] += 1
                
                # If we have finished, remove dice from playing pool
                # and append to finishers
                if pos[die.die_id] == len(track):
                    playing.remove(die.die_id)
                    order.append(die.die_id)
                    
    # Append the last dice to the order
    order.append(playing.pop())
    
    # Return the order
    return order
                    
# Open and parse input
file = open('input_part2.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse input
dice, track = parse(notes)

# Find the order of finishes
order = race(dice, track)

# Get string representation
order_string = ','.join([str(o) for o in order])

# Print the results
print(f'The order of finishes is {order_string}')
# Parse notes into list of dice
def parse(notes):

    dice = []    

    for line in notes:
        die_id, numbers, seed = line.split(' ')
        
        numbers = numbers.split('[')[1].split(']')[0]
        seed = int(seed.split('=')[1])
        
        faces = [int(n) for n in numbers.split(',')]
                
        die = Die(int(die_id[:-1]), faces, seed)
        dice.append(die)
        
    return dice
    
# Class for a dice
class Die:
    
    def __init__(self, die_id, faces, seed):
        self.die_id = die_id
        self.faces = faces
        self.seed = seed
        self.pulse = seed
        self.rolls = 0
        self.face_index = 0
        
        
    # Definition of a roll
    def roll(self):
        
        self.rolls += 1
        
        spin = self.rolls * self.pulse
        
        self.pulse += spin
        
        self.pulse %= self.seed
        
        self.pulse += 1 + self.rolls + self.seed
        
        self.face_index += spin
        self.face_index %= len(self.faces)
        
        return self.faces[self.face_index]
        

# Open and parse input
file = open('input_part1.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse notes into dice
dice = parse(notes)

# Init loop variables
dice_sum = 0
rolls = 0

# While the sum is under the target
while dice_sum < 10000:
    
    # Roll every dice and add value to total
    for die in dice:
        dice_sum += die.roll()
        
    # Increment roll counter
    rolls += 1
    
# Print the results
print(f'The number of points to reach the target is {rolls}')
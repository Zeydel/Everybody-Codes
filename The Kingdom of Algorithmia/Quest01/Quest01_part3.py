# Get the number of potions needed to defeat a single creature
def get_potions_needed(creature):
    if creature == 'B':
        return 1
    elif creature == 'C':
        return 3
    elif creature == 'D':
        return 5
    else: return 0

# Get the number of potions needed to defeat three creatures
def get_potions_needed_tripe(creatues):
    
    potions_needed = 0
    
    # Find out how many empty slots there are
    empty_slots = sum([1 if c == 'x' else 0 for c in creatues])
    
    # Find out how many extra potions are needed because there are multiple creatures
    if empty_slots == 0:
        potions_needed = 6
    elif empty_slots == 1:
        potions_needed = 2
        
    # Add the individual potions needed
    for c in creatues:
        potions_needed += get_potions_needed(c)
        
    return potions_needed

# Open file and read input as a string
inputfile3 = open('input_part3.txt', 'r')
creatures = inputfile3.readline()

# Init var for number of potions needed
potions_needed = 0

# Iterate through groups of creatures and sum potions
for i in range(0, len(creatures), 3):
    potions_needed += get_potions_needed_tripe(creatures[i:i+3])

# Print the results
print(f'{potions_needed} Potions are needed to defeat the monsters when they attack in triples')
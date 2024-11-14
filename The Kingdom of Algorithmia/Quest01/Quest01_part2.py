# Get the number of potions needed to defeat a single creature
def get_potions_needed(creature):
    if creature == 'B':
        return 1
    elif creature == 'C':
        return 3
    elif creature == 'D':
        return 5
    else: return 0

# Get the number of potions needed to defeat a pair of creatures
def get_potions_needed_pair(creaturePair):
    
    potions_needed = 0

    # If the creatues are not alone, add two to the total    
    if 'x' not in creaturePair:
        potions_needed += 2
        
    # Add the potions needed for the individual numbers
    return potions_needed + get_potions_needed(creaturePair[0]) + get_potions_needed(creaturePair[1])

# Read the input as a string
inputfile2 = open('input_part2.txt', 'r')
creaturePairs = inputfile2.readline()

# Initialise var for the number of potions needed
potions_needed = 0

# Iterate throgh the pairs and sum
for i in range(0, len(creaturePairs), 2):
    potions_needed += get_potions_needed_pair(creaturePairs[i:i+2])

# Print the results
print(f'{potions_needed} Potions are needed to defeat the monsters when they attack in pairs')


# Get the number of potions needed to defeat a single creature
def get_potions_needed(creature):
    if creature == 'B':
        return 1
    elif creature == 'C':
        return 3
    else: return 0    

# Read the input as a string
inputfile1 = open('input_part1.txt', 'r')
creatures = inputfile1.readline()

# Init variable for number of potions nedded
potions_needed = 0

# Iterate through cratures and sum number of potions needed
for c in creatures:
    potions_needed += get_potions_needed(c)
    
# Print the results
print(f'{potions_needed} Potions are needed to defeat the monsters')

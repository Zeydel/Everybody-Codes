def get_potions_needed(creature):
    if creature == 'B':
        return 1
    elif creature == 'C':
        return 3
    elif creature == 'D':
        return 5
    else: return 0

def get_potions_needed_pair(creaturePair):
    
    potions_needed = 0
    
    if 'x' not in creaturePair:
        potions_needed += 2
        
    return potions_needed + get_potions_needed(creaturePair[0]) + get_potions_needed(creaturePair[1])

def get_potions_needed_tripe(creatues):
    
    potions_needed = 0
    
    empty_slots = sum([1 if c == 'x' else 0 for c in creatues])
    
    if empty_slots == 0:
        potions_needed = 6
    elif empty_slots == 1:
        potions_needed = 2
        
    for c in creatues:
        potions_needed += get_potions_needed(c)
        
    return potions_needed
    

inputfile1 = open('input_part1.txt', 'r')
creatures = inputfile1.readline()

inputfile2 = open('input_part2.txt', 'r')
creaturePairs = inputfile2.readline()

inputfile3 = open('input_part3.txt', 'r')
creatureTriples = inputfile3.readline()

potions_needed = 0
potions_needed_pair = 0
potions_needed_triples = 0


for c in creatures:
    potions_needed += get_potions_needed(c)
    
for i in range(0, len(creaturePairs), 2):
    potions_needed_pair += get_potions_needed_pair(creaturePairs[i:i+2])
    
for i in range(0, len(creatureTriples), 3):
    potions_needed_triples += get_potions_needed_tripe(creatureTriples[i:i+3])
    
print(f'{potions_needed} Potions are needed to defeat the monsters')
print(f'{potions_needed_pair} Potions are needed to defeat the monsters when they attack in pairs')
print(f'{potions_needed_triples} Potions are needed to defeat the monsters when they attack in triples')
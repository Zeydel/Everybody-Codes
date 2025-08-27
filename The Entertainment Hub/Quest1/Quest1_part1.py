# Parse the notes into set of nails and list of tokens
def parse(notes):
    
    split = notes.index("")
    
    machine = notes[:split]
    tokens = notes[split+1:]
    
    nails = set()
    
    max_x = -1
    max_y = -1
    
    for y in range(len(machine)):
        for x in range(len(machine[y])):
            if machine[y][x] == '*':
                nails.add((x,y))
            max_x = x
                
        max_y = y
    
    return nails, tokens, max_x, max_y
    
# Fro every nail, get the landing position for going left or right
def get_drops(nails, max_x, max_y):
    
    drops = dict()
    
    for nail in nails:
        
        x, y = nail
        
        for direction, offset in [('L', -1), ('R', 1)]:
            
            nx = x+ offset
            
            if nx == -1:
                nx = 1
            
            if nx == max_x + 1:
                nx = max_x - 1
            
            ny = y + 1
            
            while (nx, ny) not in nails and ny <= max_y:
                ny += 1
                
            drops[(nail, direction)] = (nx, ny)
            
    return drops
                
# Given a start position, get the number of coins won by a token        
def get_coins(drops, token, start_x, max_y):
    
    x = start_x
    y = 0
    
    token_idx = 0
    
    while y <= max_y:
        
        token_dir = token[token_idx]
        
        x, y = drops[((x, y), token_dir)]
        token_idx += 1
        
    start_slot_no = (start_x // 2) + 1
    final_slot_no = (x // 2) + 1
        
    return max((final_slot_no * 2) - start_slot_no, 0)
    
    

# Open and parse input
file = open('input_part1.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the input
nails, tokens, max_x, max_y = parse(notes)

# Compute the drops
drops = get_drops(nails, max_x, max_y)

# Init loop values
total_coins = 0
start_x = 0

# For every token, compute the number of coins won and add to total
for token in tokens:
    total_coins += get_coins(drops, token, start_x, max_y)
    
    start_x += 2
    
# Print the results
print(f'The total number of coins won is {total_coins}')
    
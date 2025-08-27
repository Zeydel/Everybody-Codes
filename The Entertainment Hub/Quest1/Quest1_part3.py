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

# For every combination of token and start position, get the coins it would give
def get_drop_coins(drops, tokens, max_x, max_y):
    
    drop_coins = dict()

    for token in tokens:
        
        start_x = 0
        
        while start_x <= max_x:
            
            drop_coins[(token, start_x)] = get_coins(drops, token, start_x, max_y)
            
            start_x += 2
            
    return drop_coins
                
# Recursive function to get minumum and maximum number of coins
def get_min_and_max_coins(drop_coins, start_x, tokens):
        
    if len(tokens) == 0:
        return 0, 0
    
    min_coins = float('inf')
    max_coins = 0
    
    token = tokens[0]
    
    for x in start_x:
                
        token_x_coins = drop_coins[(token, x)]
        
        drop_min, drop_max = get_min_and_max_coins(drop_coins, start_x - {x}, tokens[1:])
    
        min_coins = min(min_coins, drop_min + token_x_coins)
    
        max_coins = max(max_coins, drop_max + token_x_coins)
        
    return min_coins, max_coins

# Open and parse input
file = open('input_part3.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the input
nails, tokens, max_x, max_y = parse(notes)

# Compute the drops
drops = get_drops(nails, max_x, max_y)

# Get coins for all dombinations of tokens and positions
drop_coins = get_drop_coins(drops, tokens, max_x, max_y)
    
# Ge all starting positions
start_x = {x for x in range(0, max_x+1, 2)}

# Get minimum and maximum coins
min_coins, max_coins = get_min_and_max_coins(drop_coins, start_x, tokens)

# Print the results
print(f'The minimun and maximum coins obtainable are {min_coins} {max_coins}')
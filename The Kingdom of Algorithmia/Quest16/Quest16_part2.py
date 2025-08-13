# Split the input into movements and columns of cats
def parse(notes):
    
    movements = [int(n) for n in notes[0].split(',')]
    
    column_count = len(movements)
    
    columns = []
    
    for i in range(column_count):
        columns.append([])
    
    for i in range(2, len(notes)):
        for j in range(0, len(notes[i]), 4):
            
            if notes[i][j] == ' ':
                continue
            
            columns[j // 4].append(notes[i][j:j+3])
            
    return movements, columns

# Gets the score in number of coins, given a list of cats
def get_coins(cats):
    
    symbols = dict()
    
    # For every cat
    for cat in cats:
        
        # For both eyes
        for char in [cat[0], cat[-1]]:
            
            # If symbol is not in dict, add it
            if char not in symbols:
                symbols[char] = 0
                
            # Increment its counter
            symbols[char] += 1
            
    # Init coins as zero
    coins = 0
            
    # For evey symbol, add its score to the coinss
    for symbol in symbols:
        coins += max(0, symbols[symbol] - 2)
        
    return coins
       
# Get the position at an iteration
def get_positions_at_iteration(columns, movements, iteration):
    
    positions = []
    
    for i in range(len(columns)):
        
        column = columns[i]
        movement = movements[i]
        
        positions.append((movement * iteration) % len(column))
        
    return positions



# Get the cats at a specific iteration
def get_cats_at_iteration(columns, movements, iteration):
    
    cats = []
    
    positions = get_positions_at_iteration(columns, movements, iteration)
    
    for i in range(len(columns)):
                
        column = columns[i]
        
        cats.append(column[positions[i]])
        
    return cats, positions

# Get the coins at after iteration
def get_coins_after_iteration(columns, movements, final_iteration):
        
    # Start at iteration 1
    iteration = 1
    
    # Init coin counter
    total_coins = 0
    
    while iteration <= final_iteration:
        
        # Get cat at iteration
        cats, position = get_cats_at_iteration(columns, movements, iteration)
        
        # Add coins
        total_coins += get_coins(cats)
        
        # If we have reset the columns
        if position == [0] * len(columns):
            
            # Identify the loop length
            loop_length = iteration
            
            # Add coins for every whole loop
            total_coins *= (final_iteration // loop_length)
                        
            # Skip forward until the end of the last whole loop
            iteration = (final_iteration // loop_length) * loop_length
            
        
        iteration += 1
                    
    # Return the total numbe of coins      
    return total_coins
    
# Open and parse input
file = open('input_part2.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the input
movements, columns = parse(notes)

# Print the result
print(f'After 202420242024 iterations, the number of coins is {get_coins_after_iteration(columns, movements, 202420242024)}')
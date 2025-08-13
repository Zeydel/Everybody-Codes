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
    
    for cat in cats:
        
        for char in [cat[0], cat[-1]]:
            
            if char not in symbols:
                symbols[char] = 0
                
            symbols[char] += 1
            
    coins = 0
            
    for symbol in symbols:
        coins += max(0, symbols[symbol] - 2)
        
    return coins
       
def get_next_positions(columns, positions, movements):
    
    new_positions = []
    
    for i in range(len(columns)):
        
        column = columns[i]
        movement = movements[i]
        position = positions[i]
        
        new_positions.append((position + movement) % len(column))
        
    return new_positions


# Get the cats at a specific iteration
def get_cats_at_positions(columns, positions):
    
    cats = []
        
    for i in range(len(columns)):
                
        column = columns[i]
        position = positions[i]
        
        cats.append(column[position])
        
    return cats

# Dynamic programming function to get max and min number of coins for a max iteration
def get_min_and_max_coins_after_iteration(columns, movements, max_iteration, positions, results = dict(), current_iteration = 0):
    
    # If the current iteration is the max, there are no more coins to obtain
    if current_iteration == max_iteration:
        return 0, 0
    
    # Check our result dict to see if we have been at this depth at the curent
    # iteration before
    if (current_iteration, tuple(positions)) in results:
        return results[current_iteration, tuple(positions)]
        
    # Compute the position after pulling and pushing the left lever
    pull_positions = [(positions[i] + 1) % len(columns[i]) for i in range(len(columns))]
    push_positions = [(positions[i] - 1) % len(columns[i]) for i in range(len(columns))]
    
    # Init max and min
    max_coins = float('-inf')
    min_coins = float('inf')
    
    # For every position
    for pos in [pull_positions, push_positions, positions]:
  
        # Compute the next position
        next_pos = get_next_positions(columns, pos, movements)
        
        # Get the cats
        cats = get_cats_at_positions(columns, next_pos)
        
        # Get the coins
        coins = get_coins(cats)
        
        # Recursively compute the max and min given the current state
        min_at_pos, max_at_pos = get_min_and_max_coins_after_iteration(columns, movements, max_iteration, next_pos, results, current_iteration + 1)
        
        # Update min and max if applicable
        min_coins = min(min_coins, min_at_pos + coins) 
        max_coins = max(max_coins, max_at_pos + coins)
        
    # Save the result
    results[current_iteration, tuple(positions)] = (min_coins, max_coins)
        
    # Return the result
    return min_coins, max_coins

    


    
# Open and parse input
file = open('input_part3.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the input
movements, columns = parse(notes)

# Init start position
starting_position = [0] * len(columns)

# Compute the result
min_coins, max_coins = get_min_and_max_coins_after_iteration(columns, movements, 256, starting_position)

# Print the results
print(f'The max and min coins obtainable is {max_coins} {min_coins}')
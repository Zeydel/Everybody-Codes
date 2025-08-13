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
        
        for char in cat:
            
            if char not in symbols:
                symbols[char] = 0
                
            symbols[char] += 1
            
    coins = 0
            
    for symbol in symbols:
        coins += max(0, symbols[symbol] - 2)
        
    return coins
       
# Get the cats at a specific iteration
def get_cats_at_iteration(columns, movements, iteration):
    
    cats = []
    
    for i in range(len(columns)):
        
        column = columns[i]
        movement = movements[i]
        
        cats.append(column[(movement * iteration) % len(column)])
        
    return cats
    
    
# Open and parse input
file = open('input_part1.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the input
movements, columns = parse(notes)

# Compute the result
cats_at_100 = ' '.join(get_cats_at_iteration(columns, movements, 100))

# Print the result
print(f'After 100 pulls, the sequence is {cats_at_100}')
# Parse the input into list of dictionaries
def parse(notes):
    
    letters = []
    
    for line in notes:
        
        row = dict()
        
        for pair in line.split(' '):
            
            letter, number = pair.split('=')
            
            row[letter] = int(number)
            
        letters.append(row)
            
    return letters

# Define the eni function
def eni(n, exp, mod):
    
    score = 1
    remainders = ''
    
    for i in range(exp):
        
        score = (score * n) % mod
        remainders = str(score) + remainders
        
    return int(remainders)
        

# Open and parse input
file = open('input_part1.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the input
letters = parse(notes)

# Init best
best = 0

# For every row, compute the value
for row in letters:
    
    value = eni(row['A'], row['X'], row['M'])
    
    value += eni(row['B'], row['Y'], row['M'])
    
    value += eni(row['C'], row['Z'], row['M'])
    
    # Override best if value is better
    if value > best:
        best = value
        
# Print the results
print(f'The best value is {best}')
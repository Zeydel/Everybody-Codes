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
def last_five_eni(n, exp, mod):
    
    # Init vars
    score = 1
    remainders = ''
    
    # We want to skip forward to the last five iterations
    skip = exp-5
    skip_n = n
    
    # Fast modular exponent
    while skip >= 1:
        
        if skip % 2 == 1:
            
            score = (score * skip_n) % mod
            
            skip -= 1
        
        else:
            skip_n = (skip_n * skip_n) % mod
            skip /= 2
    
        
    # Do the last five slowly
    for i in range(5):
        
        score = (score * n) % mod
        remainders = str(score) + remainders
        
    # Return the result as an int
    return int(remainders)
        

# Open and parse input
file = open('input_part2.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the input
letters = parse(notes)

# Init best
best = 0


# For every row, compute the value
for row in letters:
    
    value = last_five_eni(row['A'], row['X'], row['M'])
    
    value += last_five_eni(row['B'], row['Y'], row['M'])
    
    value += last_five_eni(row['C'], row['Z'], row['M'])
    
    # Override best if value is better
    if value > best:
        best = value
        
# Print the results
print(f'The best value is {best}')
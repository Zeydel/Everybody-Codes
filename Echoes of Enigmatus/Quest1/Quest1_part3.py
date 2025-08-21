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
    remainders = []
    
    # Do the score calculations manually
    for i in range(exp):
        
        score = (score * n) % mod
        
        # If we see a score that we have seen before, we know that we have made a loop
        if score in remainders:
            
            # Init sum
            remainder_sum = 0
            
            # Get first index of current score
            idx = remainders.index(score)
            
            # Add all the remainders up to that point
            remainder_sum += sum(remainders[:idx])
            
            # Subtract index from exp 
            exp -= idx
            
            # Get the length of the loop
            loop_length = len(remainders) - idx
                                    
            # Add sum of numbers in loop times loop iterations
            remainder_sum += sum(remainders[idx:]) * (exp // loop_length)
            
            # Get remaining length to add
            exp %= loop_length
            
            # Add the remaining numbers
            remainder_sum += sum(remainders[idx:idx+exp])
            
            # Return the sum
            return remainder_sum
        
        # Otherise just add to list
        remainders.append(score)
                
    # Return sum of remainders
    return int(remainders)
        

# Open and parse input
file = open('input_part3.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the input
letters = parse(notes)

# Init best
best = 0

eni(3,8,16)

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
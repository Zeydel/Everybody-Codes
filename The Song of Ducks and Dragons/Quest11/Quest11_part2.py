import math

# Parse the input into a list of numbers
def parse(lines):
    
    return [int(n) for n in lines]

# Get the number of rounds it takes for the ducks to move forwards
def do_forwards_rounds(columns):
    
    do_rounds = True

    # For each column, we count how many rounds they send one duck forwards
    forwards_rounds = [0 for i in range(len(columns))]

    # While we are doing rounds
    while do_rounds:
    
        # Assume no change
        do_rounds = False    
    
        # For every pair of columns
        for i in range(len(columns)-1):
            
            # Find the difference
            column_dif = columns[i] - columns[i+1]
            
            # If we do not have send any birds, continue
            if column_dif <= 0:
                continue
            
            # Find out how many birds we have to move
            moved_birds = math.ceil(column_dif / 2)
            
            # Add the moves birds to column total
            forwards_rounds[i] += moved_birds
            
            # Move the birds
            columns[i] -= moved_birds
            columns[i+1] += moved_birds
            
            # Mark that we will vontinue
            do_rounds = True
                        
    # Return the adjusted columns and the maximum number of moved birds
    return columns, max(forwards_rounds)

# The same as above, just for moving birds backwards
def do_backwards_rounds(columns):
    
    do_rounds = True

    backwards_rounds = [0 for i in range(len(columns))]

    while do_rounds:
    
        do_rounds = False    
    
        max_birds = 0
    
        for i in range(len(columns)-1):
            
            column_dif = columns[i+1] - columns[i]
            
            if column_dif <= 0:
                continue
            
            moved_birds = math.ceil(column_dif / 2)
            
            if moved_birds > max_birds:
                backwards_rounds[i] += moved_birds
            
            columns[i] += moved_birds
            columns[i+1] -= moved_birds
            
            do_rounds = True
             
    return max(backwards_rounds)

# Read the input as a string
lines = open('input_part2.txt', 'r').readlines()

# Parse the input
columns = parse(lines)

# Do the given number of rounds
columns, forwards_rounds = do_forwards_rounds(columns)
backwards_rounds = do_backwards_rounds(columns)

# Add forwards and backwards rounds
total_rounds = forwards_rounds + backwards_rounds

# Print the results
print(f'It takes {total_rounds} rounds for the ducks to be aligned')
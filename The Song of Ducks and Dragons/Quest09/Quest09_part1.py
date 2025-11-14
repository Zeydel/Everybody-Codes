# Parse the input into a list of dna sequences
def parse(lines):
    
    sequences = []
    
    for line in lines:
        
        sequences.append(line.split(':')[1].strip())
        
    return sequences

# Find out if a sequence is the child of two other sequnces
def is_child(child, parent1, parent2):
    
    # For the length of the sequences
    for i in range(len(child)):
        
        # Extract the character from each sequences
        c = child[i]
        p1 = parent1[i]
        p2 = parent2[i]
        
        # If the child character matches neither of the parent sequences
        # return false
        if c != p1 and c != p2:
            return False
        
    # Return true if we get through the whole sequence
    return True

# Get similarity of two sequences
def get_similarity(child, parent):

    # Init as zero
    similarity = 0

    # For the length of the sequences
    for i in range(len(child)):

        # Increment similarity of the characters match
        if child[i] == parent[i]:
            similarity += 1
            
    # Return the similarity
    return similarity


# Read the input as a string
lines = open('input_part1.txt', 'r').readlines()

# Parse the input
sequences = parse(lines)

# Init sequence vars
child = ''
parent1 = ''
parent2 = ''

# Go through the list of sequences
for i in range(len(sequences)):

    # Init potential parents
    p1 = sequences[(i+1) % len(sequences)]    
    p2 = sequences[(i+2) % len(sequences)]
    
    # If it is a child, overwrite sequence vars
    if is_child(sequences[i], p1, p2):
        child = sequences[i]
        parent1 = p1
        parent2 = p2
        
# Get similarity to both parents
p1_similarity = get_similarity(child, parent1)
p2_similarity = get_similarity(child, parent2)

# Calculate similarity degree
similarity_degree = p1_similarity * p2_similarity

# Print the result
print(f'The similarity degree is {similarity_degree}')    
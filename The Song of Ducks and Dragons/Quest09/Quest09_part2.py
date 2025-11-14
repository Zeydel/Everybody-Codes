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

# Get the parents of a child
def get_parents(child, sequences):
    
    # For every possible parent
    for i in range(len(sequences)):
        
        p1 = sequences[i]
        
        # The parent can not be the child
        if p1 == child:
            continue
        
        # For every possible other parent
        for j in range(i+1, len(sequences)):
            
            p2 = sequences[j]
            
            # The parent can still not be the child
            if p2 == child:
                continue
            
            # If we have found the parents, return them
            if is_child(child, p1, p2):
                return (p1, p2)

# Get the parents of all children
def get_all_parents(sequences):
    
    # Init empty dict
    parents = dict()
    
    # For every child
    for child in sequences:
        
        # Find its parents
        parents[child] = get_parents(child, sequences)
        
    # Return the dictionary of parents
    return parents

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

# Get similarity sum
def get_similarity_sum(parents):
    
    # Init as zero
    similarity_sum = 0
    
    # For every child
    for child in parents:
        
        # If it has parents
        if parents[child] == None:
            continue
        
        # Get similarity to both parents
        p1_similarity = get_similarity(child, parents[child][0])
        p2_similarity = get_similarity(child, parents[child][1])
        
        # Add their product to the sum
        similarity_sum += p1_similarity * p2_similarity
        
    # Return the sum
    return similarity_sum


# Read the input as a string
lines = open('input_part2.txt', 'r').readlines()

# Parse the input
sequences = parse(lines)

# Get all parents
parents = get_all_parents(sequences)

# Get the sum of similarites
similarity_sum = get_similarity_sum(parents)

# Print the result
print(f'The sum of similarites is {similarity_sum}')

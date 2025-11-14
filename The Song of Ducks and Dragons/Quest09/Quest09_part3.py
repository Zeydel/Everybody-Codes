# Parse the input into a list of dna sequences
def parse(lines):
    
    sequences = []
    
    for line in lines:
        
        sequences.append((int(line.split(':')[0]), line.split(':')[1].strip()))
        
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
            if is_child(child[1], p1[1], p2[1]):
                return (p1[0], p2[0])

    return (-1, -1)

# Get the parents of all children
def get_all_parents_and_children(sequences):
    
    # Init empty dict
    parents = dict()
    children = dict()
    
    # For every child
    for child in sequences:
        
        # Find its parents
        p1, p2 = get_parents(child, sequences)
        
        parents[child[0]] = (p1, p2)
        
        if p1 == -1:
            continue
        
        # Add child to both parents lists of children
        if p1 not in children:
            children[p1] = []
        if p2 not in children:
            children[p2] = []
            
        children[p1].append(child[0])
        children[p2].append(child[0])
        
    # Return the dictionary of parents
    return parents, children

# Given all parents and children, find the complete family of a duck
def get_family(duck, parents, children):
    
    # Init empty set
    family = set()
    
    # Init queue
    queue = [duck]
    
    # Whilere there is something left to explore
    while len(queue) > 0:
        
        # Get the next element in the queue
        current = queue[0]
        
        queue = queue[1:]
        
        # If we have already seen the current, continue
        if current in family:
            continue
        
        # Add the current to the family
        family.add(current)
                
        # If it has known parents, add them to the queue
        if parents[current][0] != -1:
            queue.append(parents[current][0])
            queue.append(parents[current][1])
        
        # If it has know children, add them to the queue
        if current in children:
        
            for child in children[current]:
                queue.append(child)
                
    return family

# Get the sum of scales of the biggest family
def get_bigget_family_sum(parents, children):
    
    # Init set of explored ducks
    explored = set()
    
    # Set for the biggest family
    biggest_family = set()
    
    # For every duck
    for child in parents:
        
        # If we have already seen this duck in one of the
        # families so far, skip it
        if child in explored:
            continue
        
        # Get the ducks family
        family = get_family(child, parents, children)
        
        # Add the whole family to explored
        explored |= family
        
        # If it is bigger than the biggest, overwrite the value
        if len(family) > len(biggest_family):
            biggest_family = family
            
    # Return the sum of the biggest family
    return sum(biggest_family)
    
    

# Read the input as a string
lines = open('input_part3.txt', 'r').readlines()

# Parse the input
sequences = parse(lines)

# Get all parents
parents, children = get_all_parents_and_children(sequences)

# Get the biggest family scale sum
biggest_family_sum = get_bigget_family_sum(parents, children)

# Print the result
print(f'The scale sum of the biggest family is {biggest_family_sum}')

# Parse input into walkable area, entry and targets
def parse(notes):
    
    nodes = set()
    targets = set()
    entry = -1
    
    for y in range(len(notes)):
        for x in range(len(notes[y])):
            
            if notes[y][x] == '#':
                continue
            
            if y == 0:
                entry = (x, y)
                
            if notes[y][x] == 'H':
                targets.add((x,y))
                
            nodes.add((x,y))
            
    return nodes, targets, entry
        
# Get neighbors of a position
def get_neighbors(position):
    
    neighbors = []
    
    neighbors.append((position[0]+1, position[1]))
    neighbors.append((position[0]-1, position[1]))
    
    neighbors.append((position[0], position[1]+1))
    neighbors.append((position[0], position[1]-1))
    
    return neighbors

# Get shortests distance from start to a target
def get_distance(start, targets, nodes):
    
    queue = [(start, 0)]
    explored = set()
    
    while len(queue) > 0:
        
        cur_pos, cur_dist = queue[0]
        queue = queue[1:]
        
        if cur_pos in explored or cur_pos not in nodes:
            continue
        
        explored.add(cur_pos)
        
        if cur_pos in targets:
            return cur_dist
        
        for neighbor in get_neighbors(cur_pos):
            queue.append((neighbor, cur_dist+1))
            
        

# Open and parse input
file = open('input_part1.txt','r')
notes = [line.strip() for line in file.readlines()]

# Parse the input
nodes, targets, entry = parse(notes)

# Compute the result
distance = get_distance(entry, targets, nodes) * 2

# Print the result
print(f'It takes at least {distance} steps to collect the herb and get out again')
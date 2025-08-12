import time

# Parse input into walkable area, entry and targets
def parse(notes):
    
    nodes = set()
    targets = dict()
    entry = -1
    
    for y in range(len(notes)):
        for x in range(len(notes[y])):
            
            if notes[y][x] in ['#', '~']:
                continue
            
            if y == 0:
                entry = (x, y)
                
            if not notes[y][x] == '.':
                
                if not notes[y][x] in targets:
                    targets[notes[y][x]] = []
                    
                targets[notes[y][x]].append((x,y))
                
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

# Get the distance from the start and all targets, to all targets
def get_all_distances(entry, targets, nodes):
    
    distances = dict()
    
    distances |= get_distances(entry, targets, nodes)
    
    for target in targets:
        
        for herb in targets[target]:
            
            distances |= get_distances(herb, targets, nodes)
            
    return distances
    
    

# Get shortests distance from start to a target
def get_distances(start, targets, nodes):
    
    queue = [(start, 0)]
    explored = set()
    
    distances = dict()
    distances[(start, start)] = 0
    
    target_coordinates = set()
    
    for target in targets:
        
        for coordinate in targets[target]:
            
            target_coordinates.add(coordinate)
    
    while len(queue) > 0:
        
        cur_pos, cur_dist = queue[0]
        queue = queue[1:]
        
        if cur_pos in explored or cur_pos not in nodes:
            continue
        
        explored.add(cur_pos)
        
        if cur_pos in target_coordinates:
            distances[(start, cur_pos)] = cur_dist
            distances[(cur_pos, start)] = cur_dist
        
        for neighbor in get_neighbors(cur_pos):
            queue.append((neighbor, cur_dist+1))
            
    return distances

# Get the shortest path from the entry, visiting each type of herb once
# and going to the entry again
def get_shortest_path(entry, current_position, targets, not_visited, length, distances, current_best):
    
    if length + distances[current_position, entry] > current_best:
        return float('inf')
    
    # If we have visited all types of nodes, add the distance to the
    # start and return result
    if len(not_visited) == 0:
        return length + distances[current_position,entry]
        
    # For every target type
    for target in not_visited:
                
        # For every possible target
        for coordinate in targets[target]:
            
            distance = get_shortest_path(entry, coordinate, targets, not_visited - {target}, length + distances[current_position, coordinate], distances, current_best)
            
            if distance < current_best:
                current_best = distance
                print(current_best)

            
    return current_best
  

def get_shortest_path_greedy(entry, not_visited, targets, distances):
    
    shortest_path_length = 0
    
    cur_pos = entry
    
    while len(not_visited) > 0:
        
        next_best = -1
        next_best_dist = float('inf')
        next_best_herb = -1
        
        for target in targets:
            for herb in targets[target]:
                
                if distances[cur_pos, herb] < next_best_dist and target in not_visited:
                    next_best = herb
                    next_best_dist = distances[cur_pos, herb]
                    next_best_herb = target
                    
        cur_pos = next_best
        shortest_path_length += next_best_dist
        not_visited.remove(next_best_herb)
        
    return shortest_path_length + distances[cur_pos, entry]
    
    
          
start_time = time.time()

# Open and parse input
file = open('input_part2.txt','r')
notes = [line.strip() for line in file.readlines()]

# Parse the input
nodes, targets, entry = parse(notes)

# Get all distances
distances = get_all_distances(entry, targets, nodes)

upper_bound = get_shortest_path_greedy(entry, set(targets.keys()), targets, distances)

# Find the shortest path
shortest_path = get_shortest_path(entry, entry, targets, set(targets.keys()), 0, distances, float('inf'))

# Print the result
print(f'The shortest path is {shortest_path}')
print("--- %s seconds ---" % (time.time() - start_time))

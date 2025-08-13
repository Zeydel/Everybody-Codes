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
            
    targets["ENTRY"] = [entry]
                        
    return nodes, targets, entry

    
# Determine wether a herb a at specific position is a prerequisite
# for obtaining a herb letter
def is_prereq(start, herb, prereq, targets, nodes):
    
    queue = [(start)]
    explored = set()
                    
    # Perform a bfs. If we cannot reach a herb with the given letter
    # without stepping on the position return true, otherwise retun false
    while len(queue) > 0:
        
        cur_pos = queue[0]
        queue = queue[1:]
        
        if cur_pos in explored or cur_pos not in nodes or cur_pos == prereq:
            continue
        
        explored.add(cur_pos)
        
        if cur_pos in targets[herb]:
            return False
        
        for neighbor in get_neighbors(cur_pos):
            queue.append(neighbor)
            
    return True    

# Get subtours needed
def get_subgroups(entry, targets, nodes):
    
    subgroups = dict()
    
    # For every pair of herbs
    for h1 in targets:
        for h2 in targets:
            if h1 == h2:
                continue
            
            # For every location of the second herb
            for location in targets[h2]:
                
                edgecount = 0
                
                for neighbor in get_neighbors(location):
                    
                    if neighbor not in nodes:
                        edgecount += 1
                        
                if edgecount < 2:
                    continue
            
                # Check if the location is needed to obtain the first herb
                if is_prereq(entry, h1, location, targets, nodes):
                    
                    # If so, add a subgroup
                    if not location in subgroups:
                        subgroups[location] = set()
                        
                    subgroups[location].add(h1)
    
    return subgroups

# Remove herbs from smaller groups from the containing grpups
def shrink_groups(groups, targets):
    
    char = 1
        
    for g1 in groups:
        for g2 in groups:
            if g1 == g2:
                continue
            
            if groups[g2].issubset(groups[g1]):
                groups[g1] -= groups[g2]
                groups[g1].add(str(char))
                groups[g2].add(str(char))
                                    
                targets[str(char)] = [g2]
                char += 1
                
                
    return groups, targets
     
# Get neighbors of a position
def get_neighbors(position):
    
    neighbors = []
    
    neighbors.append((position[0]+1, position[1]))
    neighbors.append((position[0]-1, position[1]))
    
    neighbors.append((position[0], position[1]+1))
    neighbors.append((position[0], position[1]-1))
    
    return neighbors

# Get the distance from the start and all targets, to all targets
def get_all_distances(targets, nodes, groups):
    
    distances = dict()

    for group in groups:
        
        for target in groups[group]:

            for pos in targets[target]:
            
                distances |= get_distances(pos, targets, nodes, groups[group])
            
    return distances
    

# Get shortests distance from start to a target
def get_distances(start, targets, nodes, group_targets):
    
    queue = [(start, 0)]
    explored = set()
    
    distances = dict()
    distances[(start, start)] = 0
    
    target_coordinates = set()
    num_targets = 0
    
    for target in targets:
        
        for coordinate in targets[target]:
            
            if target in group_targets:
                target_coordinates.add(coordinate)
                num_targets += 1
    
    while len(queue) > 0 and len(distances) < num_targets:
        
        cur_pos, cur_dist = queue[0]
        queue = queue[1:]
        
        if cur_pos in explored or cur_pos not in nodes:
            continue
        
        explored.add(cur_pos)
        
        if cur_pos in target_coordinates:
            distances[(start, cur_pos)] = cur_dist
        
        for neighbor in get_neighbors(cur_pos):
            queue.append((neighbor, cur_dist+1))
            
    return distances

# Get the shortest path from the entry, visiting each type of herb once
# and going to the entry again
def get_shortest_path(entry, current_position, targets, not_visited, distances, length = 0, current_best = float('inf')):
    
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
            
            distance = get_shortest_path(entry, coordinate, targets, not_visited - {target}, distances, length + distances[current_position, coordinate], current_best)
            
            if distance < current_best:
                current_best = distance

            
    return current_best
    
# Open and parse input
file = open('input_part2.txt','r')
notes = [line.strip() for line in file.readlines()]

# Parse the input
nodes, targets, entry = parse(notes)

# Init dict for subgroups
groups = dict()

# Define the upper group consiting of the entry and every type of herb
groups[entry] = set(targets.keys())

# Get subgroups, consiting of subentries with the herbs contained
groups |= get_subgroups(entry, targets, nodes)
groups[entry].add("ENTRY")

groups, targets = shrink_groups(groups, targets)

# Get all distances in subgroups
distances = get_all_distances(targets, nodes, groups)

# Init distance
total_distance = 0

# For every group
for group in groups:
    
    # Add the distance to the total
    total_distance += get_shortest_path(group, group, targets, set(groups[group]), distances)

# Print the results
print(f'The minimum number of steps is {total_distance}')        
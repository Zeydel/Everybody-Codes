# Parse the input into channels, trees and entry
def parse(notes):    
    channels = set()
    trees = set()
    
    for y in range(len(notes)):
        for x in range(len(notes[y])):
            
            if notes[y][x] == '#':
                continue
            
            channels.add((x,y))
            
            if notes[y][x] == 'P':
                trees.add((x, y))
                                
    return channels, trees
            
def get_neighbors(coordinates):
    
    neighbors = []
    
    neighbors.append((coordinates[0]+1, coordinates[1]))
    neighbors.append((coordinates[0]-1, coordinates[1]))
    
    neighbors.append((coordinates[0], coordinates[1]+1))
    neighbors.append((coordinates[0], coordinates[1]-1))
    
    return neighbors

# Perform a BFS untill all trees are found and return the time
def get_minmum_watering_time(channels, trees):

    queue = []
    
    for tree in trees:
        queue.append((tree, tree, 0))
    
    canal_distances = dict()
    
    explored = set()
        
    while len(queue) > 0:
    
        coordinates, source, time = queue[0]
        queue = queue[1:]
        
        if (coordinates, source) in explored:
            continue
        
        explored.add((coordinates, source))
        
        if coordinates not in trees:
            
            if coordinates not in canal_distances:
                canal_distances[coordinates] = []
                
            canal_distances[coordinates].append(time)
                        
        for neighbor in get_neighbors(coordinates):
            
            if neighbor not in channels:
                continue
            
            queue.append((neighbor, source, time+1))
            
    return canal_distances

# Open and parse input
file = open('input_part3.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse input
channels, trees = parse(notes)

# Get results
watering_times = get_minmum_watering_time(channels, trees)

min_time = float('inf')

for coordinate in watering_times:
    
    watering_time = sum(watering_times[coordinate])
    
    if watering_time < min_time:
        min_time = watering_time
        
print(min_time)
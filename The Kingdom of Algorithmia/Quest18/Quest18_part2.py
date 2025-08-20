# Parse the input into channels, trees and entry
def parse(notes):
    
    min_y, min_x = 0, 0
    
    max_y, max_x = len(notes) - 1, len(notes[0]) - 1
    
    channels = set()
    trees = set()
    entries = set()
    
    for y in range(len(notes)):
        for x in range(len(notes[y])):
            
            if notes[y][x] == '#':
                continue
            
            channels.add((x,y))
            
            if notes[y][x] == 'P':
                trees.add((x, y))
                
            if y in (min_y, max_y) or x in (min_x, max_x):
                entries.add((x, y))
                
    return channels, trees, entries
            
def get_neighbors(coordinates):
    
    neighbors = []
    
    neighbors.append((coordinates[0]+1, coordinates[1]))
    neighbors.append((coordinates[0]-1, coordinates[1]))
    
    neighbors.append((coordinates[0], coordinates[1]+1))
    neighbors.append((coordinates[0], coordinates[1]-1))
    
    return neighbors

# Perform a BFS untill all trees are found and return the time
def get_watering_time(entries, channels, trees):

    queue = []
    
    for entry in entries:
        queue.append((entry, 0))
    
    explored = set()
        
    while len(queue) > 0:
    
        coordinates, time = queue[0]
        queue = queue[1:]
        
        if coordinates in explored:
            continue
        
        explored.add(coordinates)
        
        if coordinates in trees:
            trees.remove(coordinates)
            
            if len(trees) == 0:
                return time
            
        for neighbor in get_neighbors(coordinates):
            
            if neighbor not in channels:
                continue
            
            queue.append((neighbor, time+1))

# Open and parse input
file = open('input_part2.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse input
channels, trees, entries = parse(notes)

# Get results
watering_time = get_watering_time(entries, channels, trees)

# Print results
print(f'The watering time is {watering_time}')
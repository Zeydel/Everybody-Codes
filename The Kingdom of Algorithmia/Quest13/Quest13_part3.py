# Get the start and end position, along with a dictionary
# of every walkable node
def parse(notes):
    
    start_positions = []
    end_pos = (-1, -1)
    
    nodes = dict()
    
    for y in range(len(notes)):
        for x in range(len(notes[y])):
            
            if notes[y][x] in ['#', ' ']:
                continue
            if notes[y][x] == 'S':
                start_positions.append((x, y))
            if notes[y][x] == 'E':
                end_pos = (x, y)
                
            nodes[(x, y)] = notes[y][x]
            
    return (nodes, start_positions, end_pos)
            
# Get the neighbors of a given position
def get_neighbours(pos):
    
    return [(pos[0] - 1, pos[1]),
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1),
            (pos[0], pos[1] + 1)]

# Get the height of a platform
def get_height(node, nodes):
    
    if nodes[node] in ['S', 'E']:
        return 0
    else:
        return int(nodes[node])

# Compute the time needed to move from one platform to the next
# including time to move the current platform
def get_time_to_move(cur_node, next_node, nodes):
    
    start_level = get_height(cur_node, nodes)
    end_level = get_height(next_node, nodes)
    
    return min(10-abs(start_level - end_level), abs(start_level - end_level)) + 1
          
# Get the shortest time to move from the start node to every other node
# using dijkstra
def get_shortest_times(nodes, start_pos):
    
    shortests_times = dict()
    shortests_times[start_pos] = 0

    queue = []
    queue.append((start_pos, 0))

    while(queue):
        
        pos, time = queue[0]
        queue = queue[1:]
        
        for next_pos in get_neighbours(pos):
            if next_pos not in nodes:
                continue
            
            time_total = time + get_time_to_move(pos, next_pos, nodes)
            
            if next_pos not in shortests_times or time_total < shortests_times[next_pos]:
                shortests_times[next_pos] = time_total
                queue.append((next_pos, time_total))
                
    return shortests_times
            
            
# Open and parse input
file = open('input_part3.txt','r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
nodes, start_positions, end_pos = parse(lines)

# Get all shortest time from end
shortest_times = get_shortest_times(nodes, end_pos)

# Init variable for best time
best_time = float('inf')

# For every start position
for start_pos in start_positions:
    
    # Check if it shorter than the best so far. Save it, if so
    if shortest_times[start_pos] < best_time:
        best_time = shortest_times[start_pos]

# Print the results
print(f"{best_time} seconds is the shortest time to get to the exit")
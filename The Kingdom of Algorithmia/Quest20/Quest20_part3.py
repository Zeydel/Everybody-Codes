from heapq import heappush, heappop

# This code is terrible and i hate it
def parse(notes):
    
    air = set()
    hot_winds = set()
    cold_winds = set()
    start = -1
    max_x = -1
    
    for y in range(len(notes)):
        for x in range(len(notes[y])):
            if notes[y][x] == '#':
                continue
            
            air.add((x, y))
            
            if notes[y][x] == '+':
                hot_winds.add((x, y))
                
            if notes[y][x] == '-':
                cold_winds.add((x,y))
                
            if notes[y][x] == 'S':
                start = (x, y)
                
            if x > max_x:
                max_x = x
                
        max_y = y
                
    return air, hot_winds, cold_winds, start, max_y, max_x

# Given a position and direction, get the next steps reachable
def get_next_steps(current):
    
    x, y, direction = current
    
    next_steps = []
            
    next_steps.append((x, y+1, 'S'))
        
    if direction != 'E':
        next_steps.append((x-1, y, 'W'))
        
    if direction != 'W':
        next_steps.append((x+1, y, 'E'))
        
    return next_steps

# Get the maximum south we can go, given a position and altitude
def get_max_south(air, hot_winds, cold_winds, start, start_alt, max_y):
    
    queue = []
    x, y = start
    
    heappush(queue, (0, x, y, '', start_alt))
    
    best_y = 0
    
    best_altitudes = dict()
    
    while len(queue) > 0:
        
        total_y, x, y, direction, alt = heappop(queue)
        
        if alt <= 0:
            if -total_y > best_y:
                best_y = -total_y
            continue
                    
        if (x, total_y, direction) not in best_altitudes:
            best_altitudes[(x, total_y, direction)] = alt
        elif best_altitudes[(x, total_y, direction)] >= alt:
            continue
        else:
            best_altitudes[(x, total_y, direction)] = alt
            
        # Get the next steps in the queue
        for next_step in get_next_steps((x, y, direction)):
            
            nx, ny, ndirection = next_step
            
            y_dif = ny-y
            
            if ny > max_y:
                ny = 0
                y_dif = 1
            
            if (nx, ny) not in air:
                continue
            
            new_alt = alt-1
            
            if (nx, ny) in hot_winds:
                new_alt = alt+1
            if (nx, ny) in cold_winds:
                new_alt = alt-2
                
                
            heappush(queue, (total_y-y_dif, nx, ny, ndirection, new_alt))

        
            
    return best_y
    
# From the starting position, get the maximum altitude we can reach each northmost position
# after a given number of iterations
def get_starting_pos(start, air, hot_winds, cold_winds, max_y, iterations, start_alt):
    
    max_iteration = iterations
    
    bests = dict()
    
    queue = []
    x, y = start
    
    heappush(queue, (0, x, y, '', start_alt))
        
    best_altitudes = dict()
    
    while len(queue) > 0:
        
        iteration, x, y, direction, alt = heappop(queue)
        
        if iteration > max_iteration and y == 0:
            if x not in bests:
                bests[x] = float('-inf')
                
            if alt > bests[x]:
                bests[x] = alt

            continue            
        
        if (x, y, iteration, direction) not in best_altitudes:
            best_altitudes[(x, y, iteration, direction)] = alt
        elif best_altitudes[(x, y, iteration, direction)] >= alt:
            continue
        else:
            best_altitudes[(x, y, iteration, direction)] = alt
            
        # Get the next steps in the queue
        for next_step in get_next_steps((x, y, direction)):
            
            nx, ny, ndirection = next_step
                        
            niteration = iteration
            
            if ny > max_y:
                ny = 0
                niteration += 1
                
            
            if (nx, ny) not in air:
                continue
            
            new_alt = alt-1
            
            if (nx, ny) in hot_winds:
                new_alt = alt+1
            if (nx, ny) in cold_winds:
                new_alt = alt-2
                
                
            heappush(queue, (niteration, nx, ny, ndirection, new_alt))
            
    return bests

# Given a starting position, gives the best altitude we can end at,
# along with its drop
def get_best_end(start, air, hot_winds, cold_winds, max_y, start_alt):
            
    queue = []
    x, y = start
    
    heappush(queue, (0, x, y, '', start_alt))
        
    best_altitudes = dict()
    
    best_alt, best_end = -1, -1
    
    while len(queue) > 0:
        
        iteration, x, y, direction, alt = heappop(queue)
        
        if y == 0 and iteration == 1:
            if alt > best_alt:
                best_alt = alt
                best_end = (x, y)
                
            continue
                
            
        if (x, y, iteration, direction) not in best_altitudes:
            best_altitudes[(x, y, iteration, direction)] = alt
        elif best_altitudes[(x, y, iteration, direction)] >= alt:
            continue
        else:
            best_altitudes[(x, y, iteration, direction)] = alt
            
        # Get the next steps in the queue
        for next_step in get_next_steps((x, y, direction)):
            
            nx, ny, ndirection = next_step
                        
            niteration = iteration
            
            if ny > max_y:
                ny = 0
                niteration += 1
                
            
            if (nx, ny) not in air:
                continue
            
            new_alt = alt-1
            
            if (nx, ny) in hot_winds:
                new_alt = alt+1
            if (nx, ny) in cold_winds:
                new_alt = alt-2
                
                
            heappush(queue, (niteration, nx, ny, ndirection, new_alt))
            
    return best_alt, best_end

# Open and parse input
file = open('input_part3.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Init starting altitude
start_alt = 384400

# Parse input
air, hot_winds, cold_winds, start, max_y, max_x = parse(notes)

# Do 10 iterations and get the best ways we can end
iterations = 10
starting_graph = get_starting_pos(start, air, hot_winds, cold_winds, max_y, iterations, start_alt)

# Init a middle graph
middle_graph = dict()

start_y = ((max_y+1)*(iterations+1))

# For every point, get the best way to end
for key in starting_graph:
    
    best_alt, best_end = get_best_end((key, 0), air, hot_winds, cold_winds, max_y, starting_graph[key])
    
    # Only keep the ones that end in the same place they start
    if key == best_end[0]:
        middle_graph[key] = (best_end, starting_graph[key]-best_alt)
             
# init furtest y
furthest_y = 0
        
# For every key
for key in middle_graph:
    
    # Get starting altitude
    path_start_alt = starting_graph[key]
    
    # Get starting y coordinate
    path_y = start_y
        
    # Get the altitude difference for following this path
    _, alt_dif = middle_graph[key]
    
    # Get how many iterations to go
    path_iterations = (path_start_alt // alt_dif) - 10
    
    # Add length
    path_y += path_iterations * (max_y+1)
    
    # Do the rest of the pathfinding manually
    path_y += get_max_south(air, hot_winds, cold_winds, (key, 0), path_start_alt - (path_iterations * alt_dif), max_y)
    
    # If better, override
    if path_y > furthest_y:
        furthest_y = path_y
        
# Print the results
print(f'The furthest south we can go is {furthest_y}')
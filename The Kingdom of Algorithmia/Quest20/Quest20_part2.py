from heapq import heappush, heappop

# This is a terrible mess, but i will eventually output the correct result

# Parse the notes into air, hot winds, cold winds, and starting points
def parse(notes):
    
    air = set()
    hot_winds = set()
    cold_winds = set()
    start = -1
    A = -1
    B = -1
    C = -1
    
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
                
            if notes[y][x] == 'A':
                A = (x, y)
                
            if notes[y][x] == 'B':
                B = (x, y)
                
            if notes[y][x] == 'C':
                C = (x, y)
                
    return air, hot_winds, cold_winds, start, A, B, C
    
def get_all_distances(start, air):
    
    dists = dict()
    
    explored = set()
    
    queue = [(start, 0)]
    
    while len(queue) > 0:
        
        node, dist = queue[0]
        queue = queue[1:]
        
        if node in explored:
            continue
        
        explored.add(node)
        
        dists[(start, node)] = dist
        
        for neighbor in get_next_steps((node[0], node[1], '')):
            
            new_node = (neighbor[0], neighbor[1])
            
            if new_node not in air:
                continue
            
            queue.append((new_node, dist+1))
            
    return dists


# Given a position and direction, get the next steps reachable
def get_next_steps(current):
    
    x, y, direction = current
    
    next_steps = []
    
    if direction != 'S':
        next_steps.append((x, y-1, 'N'))
        
    if direction != 'N':
        next_steps.append((x, y+1, 'S'))
        
    if direction != 'E':
        next_steps.append((x-1, y, 'W'))
        
    if direction != 'W':
        next_steps.append((x+1, y, 'E'))
        
    return next_steps

def get_fast_positive_route(air, hot_winds, cold_winds, start, end, dists):
            
    starting_dist = dists[(end, start)]
        
    queue = []
    heappush(queue, (((starting_dist, 0), (start[0], start[1], ''), 0)))
    
    # Init dict to save best altitudes and times
    bests = dict()
    best_altitudes = dict()
    best_times = dict()
        
    # While there are items in the queue
    while len(queue) > 0:
        
        # Take the next item
        dist_time, current, alt = heappop(queue)
        dist, time = dist_time
                
        if alt < -10000:
            continue
        
        if (current[0], current[1]) == end:
                        
            if alt > 0:
                return time
            
            continue
                
        # If we have previously seen the same position and direction
        # at the same time, but with higher altitude, continue
        if (current, time) not in best_altitudes:
            best_altitudes[(current, time)] = alt
        elif best_altitudes[(current, time)] >= alt:
            continue
        else:
            best_altitudes[(current, time)] = alt
            
        # If we have previously seen the same position and direction
        # at the same altitude, but with better time, continue
        if (current, alt) not in best_times:
            best_times[(current, alt)] = time
        elif best_times[(current, alt)] <= time:
            continue
        else:
            best_times[(current, alt)] = time
            
        if current not in bests:
            bests[current] = set()
            
        prune = False    
        
        for best in bests[current]:
            
            best_time, best_alt = best
            
            if best_time < time and best_alt > alt:
                prune = True
                break
                
        if prune:
            continue
    
        bests[current].add((time, alt))
        
        # Get the next steps in the queue
        for next_step in get_next_steps(current):
            
            x, y, direction = next_step
            
            if (x, y) not in air:
                continue
            
            new_alt = alt-1
            
            if (x, y) in hot_winds:
                new_alt = alt+1
            if (x, y) in cold_winds:
                new_alt = alt-2
                
            dist = dists[end, (x, y)]
                
            heappush(queue, ((dist, time+1), (x, y, direction), new_alt))
         
def get_loop_alt(nodes, hot_winds, cold_winds):
    
    alt = 0
    
    for node in nodes:
    
        x, y, _ = node    
    
        if (x, y) in hot_winds:
            alt += 1
        elif (x, y) in cold_winds:
            alt -= 2
        else:
            alt -= 1
            
    return alt
         
def get_routes(air, hot_winds, cold_winds, start, end, time_bound, dists):
    
    routes = set()
    
    x, y = start    

    queue = []
    heappush(queue, (0, x, y, '', 0, ''))
    
    # Init dict to save best altitudes and times
    bests = dict()
    best_altitudes = dict()
    best_times = dict()
        
    explored = set()
    
    # While there are items in the queue
    while len(queue) > 0:
        
        # Take the next item
        alt, x, y, direction, time, start_dir = heappop(queue)
        
        dist = dists[(end, (x, y))]
        
        alt = -alt           
        
        if time + dist > time_bound:
            continue
        
        if (x, y, time, alt, direction) in explored:
            continue
        
        explored.add((x, y, alt, time, direction))
        
        if (x, y) == end:
                        
            routes.add((time, alt, start_dir, direction))
            
            continue
        
        # If we have previously seen the same position and direction
        # at the same time, but with higher altitude, continue
        if (x, y, time, direction) not in best_altitudes:
            best_altitudes[(x, y, time, direction)] = alt
        elif best_altitudes[(x, y, time, direction)] >= alt:
            continue
        else:
            best_altitudes[(x, y, time, direction)] = alt
            
        # If we have previously seen the same position and direction
        # at the same altitude, but with better time, continue
        if (x, y, alt, direction) not in best_times:
            best_times[(x, y, alt, direction)] = time
        elif best_times[(x, y, alt, direction)] <= time:
            continue
        else:
            best_times[(x, y, alt, direction)] = time
            
        if (x, y, direction) not in bests:
            bests[(x, y, direction)] = set()
            
        prune = False    
        
        for best in bests[(x, y, direction)]:
            
            best_time, best_alt = best
            
            if best_time < time and best_alt > alt:
                prune = True
                break
                
        if prune:
            continue

        # Get the next steps in the queue
        for next_step in get_next_steps((x, y, direction)):
            
            nx, ny, ndirection = next_step
            
            if (nx, ny) not in air:
                continue
            
            new_alt = alt-1
            
            if (nx, ny) in hot_winds:
                new_alt = alt+1
            if (nx, ny) in cold_winds:
                new_alt = alt-2
                
            if start_dir == '':
                n_start_dir = ndirection
            else:
                n_start_dir = start_dir
            
            heappush(queue, (-new_alt, nx, ny, ndirection, time+1, n_start_dir))
            
    return routes

def is_directions_compatible(dir1, dir2):
    
    directions = {dir1, dir2}
    
    if 'N' in directions and 'S' in directions:
        return False
    
    if 'W' in directions and 'E' in directions:
        return False
    
    return True
                
def get_best_routes_combination(routes, length=0, alt=0, best_length=float('inf'), prev_end_dir=''):
    
    if len(routes) == 0:
        if alt < 0:
            return float('inf')
        else:
            return length
    
    if length > best_length:
        return float('inf')
        
    for r_time, r_alt, start_dir, end_dir in routes[0]:
        
        if not is_directions_compatible(prev_end_dir, start_dir):
            continue
        
        best_length = min(best_length, get_best_routes_combination(routes[1:], length+r_time, alt+r_alt, best_length, end_dir))

    return best_length

def prune_routes(routes):
    
    for route1 in list(routes):
        
        r1_time, r1_alt, r1_startdir, r1_enddir = route1
        
        for route2 in list(routes):
            
            r2_time, r2_alt, r2_startdir, r2_enddir = route2
            
            if r1_startdir != r2_startdir or r1_enddir != r2_enddir:
                continue
            
            if r1_time < r2_time and r1_alt > r2_alt:
                routes.remove(route2)
            
    return routes


# Open and parse input
file = open('input_part2.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the input
air, hot_winds, cold_winds, start, A, B, C = parse(notes)

dists = dict()

# Get all distances from all checkpoints to all other points
for src in [start, A, B, C]:
    dists |= get_all_distances(src, air)

# Define the order
order = [start, A, B, C, start]

# Init var that will be used for upper time bound
time_bound = 0

# Get the length of a route with a positive altitude gain andd add to bound
for i in range(len(order) - 1):
    time_bound += get_fast_positive_route(air, hot_winds, cold_winds, order[i], order[i+1], dists)
    
# Init list of routes
routes = []
 
# For every start position
for i in range(len(order) - 1):
    
    # Compute the max time we can use for this
    i_time_bound = time_bound
    
    for j in range(len(order) - 1):
        
        if i == j:
            continue
        
        i_time_bound -= dists[(order[j], order[j+1])]
        
    # Add the routes to the list of routes
    routes.append(get_routes(air, hot_winds, cold_winds, order[i], order[i+1], i_time_bound, dists))
   
# Prune routes that we definitely don't need
for i in range(len(routes)):
    routes[i] = sorted(prune_routes(routes[i]))
   
# Get the best time from the routes
best_time = get_best_routes_combination(routes)

# Output the result
print(f'The best time is {best_time}')

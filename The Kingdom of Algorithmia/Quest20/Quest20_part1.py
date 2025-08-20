# Parse the notes into air, hot winds, cold winds, and starting points
def parse(notes):
    
    air = set()
    hot_winds = set()
    cold_winds = set()
    start = -1
    
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
                
    return air, hot_winds, cold_winds, start
    
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

# Get the maximum height you can reach after a given amount
def get_max_height(air, hot_winds, cold_winds, start, max_time):
    
    # Init starting state
    queue = [((start[0], start[1], ''), 0, 1000)]
    
    # Init dict to save best altitudes and times
    best_altitudes = dict()
    best_times = dict()
    
    # While there are items in the queue
    while len(queue) > 0:
        
        # Take the next item
        current, time, alt = queue[0]
        queue = queue[1:]
        
        # If we have surpassed our time, dont do anything
        if time > max_time:
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
                
            queue.append(((x, y, direction), time+1, new_alt))
    
    # Return the best altitudes
    return best_altitudes

# Open and parse input
file = open('input_part1.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the input
air, hot_winds, cold_winds, start = parse(notes)

# Init max time
max_time = 100

# Get the max height
best = get_max_height(air, hot_winds, cold_winds, start, max_time)

# Find the best altitude at max time
best_altitude = 0

for key in best:
    
    if best[key] > best_altitude and key[1] == max_time:
        best_altitude = best[key]
     
# Print the result
print(f'The highest altitude you can reach is {best_altitude}')
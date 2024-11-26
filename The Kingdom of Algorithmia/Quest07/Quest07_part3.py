# Parse the input into a dict
def parse_devices(lines):
    
    # Init dict to keep devices in
    devices = dict()
    
    # For every line
    for line in lines:
        
        # Split into name and plan
        name, plan = line.split(':')
        
        # Store name and plan as a key-value pair
        devices[name] = plan.split(',')

    # Return the devices
    return devices

# DFS-like function to parse the racetrack
def parse_racetrack(lines, start_x, start_y):
    
    # Start with an empty string
    racetrack = ''
    
    # Init x and y from their starting values
    x = start_x
    y = start_y
    
    
    while True:
        
        # Add the current spot to the racetrack
        racetrack += lines[y][x]
                
        # If we have just added the end, break the loop
        if racetrack[-1] == 'S':
            break
                
        # Replace current spot with blank space
        lines[y] = lines[y][:x] + ' ' + lines[y][x+1:]
                
        # Find the next possible positions
        next_pos = []
        
        # Find non-space characters arround the current character
        if is_in_bounds(lines, x, y - 1) and lines[y-1][x] != ' ':
            next_pos.append((lines[y-1][x], x,y-1))
        
        if is_in_bounds(lines, x, y + 1) and lines[y+1][x] != ' ':
            next_pos.append((lines[y+1][x], x ,y+1))
        
        if is_in_bounds(lines, x - 1, y) and lines[y][x-1] != ' ':
            next_pos.append((lines[y][x-1], x-1, y))
            
        if is_in_bounds(lines, x + 1, y) and lines[y][x+1] != ' ':
            next_pos.append((lines[y][x+1], x+1, y))
            
        # If we have more than one possible position, we are at the start
        if len(next_pos) > 1:
            
            # Find the direction that goes away from start
            for np in next_pos:
                if np[0] != 'S':
                    x = np[1]
                    y = np[2]
            
        # Else just take the next space
        else:
            x = next_pos[0][1]
            y = next_pos[0][2]
            
    # Return the calculated racetrack
    return racetrack
   
# Helper to find out if two coordinates are within the grid         
def is_in_bounds(grid, x, y):
    
    if x < 0:
        return False
    if y < 0:
        return False
    if y > len(grid) - 1:
        return False
    if x > len(grid[y]) - 1:
        return False
    
    return True
            
# Function to recursively create all plans
def create_all_plans(plusses, minuses, plan):
    
    # Init empty set
    plans = set()
    
    # If there are more plusses to add
    if plusses > 0:
        
        # Add plus in the next possible possible position
        for i, c in enumerate(plan):
            if c == '=':
                
                # Recurse with the new plan
                plans.update(create_all_plans(plusses - 1, minuses, plan[:i] + '+' + plan[i+1:]))
    
    # Do the same for minuses
    elif minuses > 0:
        for i, c in enumerate(plan):
            if c == '=':
                plans.update(create_all_plans(plusses, minuses - 1, plan[:i] + '-' + plan[i+1:]))
    
    # If there are no more plusses or minuses to add, we have a complete plan. Add it to the set
    else:
        plans.add(plan)            
    
    # Return the set of plans
    return plans

    
    
    

# Get the total essence
def get_total_essence(sequence, racetrack, rounds):
    
    # Init var for total essence
    total_essence = 0
    
    # Starting power
    power = 10
    
    # We don't need to complete the race. We just need to run it until
    # an end of a plan lines up with the end of the track.
    # Running for the length of their product is the simplest way to get to that
    for i in range(len(sequence) * len(racetrack)):
        
        racetrack_action = racetrack[i % len(racetrack)]
        
        # Find out the current action
        action = sequence[i % len(sequence)]
        
        # Increment or decrement power
        if racetrack_action == '+':
            power += 1
        elif racetrack_action == '-':
            power -= 1
        elif action == '+':
            power += 1
        elif action == '-':
            power -= 1
        
        # Power cannot be negative
        if power < 0:
            power = 0
            
        # Add the current power to the essence
        total_essence += power
        
    # Return the total
    return total_essence

# Get the rankings
def get_ranking(essence):
    
    # Init empty string
    rankings = ''

    # Loop through essences stored descending
    for e in sorted(essence, reverse=True):
        
        # Concat the ranking with the name of the device
        rankings += essence[e]
        
    # Return the rankings
    return rankings


# Open file and read as lines
file = open('input_part3.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
devices = parse_devices(lines)

# Open racetrack file and read as line
file = open('racetrack2.txt', 'r')
lines = file.read().splitlines()

# Parse the racetrack
racetrack = parse_racetrack(lines, 1, 0)

# Create all plans
plans = create_all_plans(5, 3, '='*11)

# Init variable for number of winning plans
winning_plans = 0

# Init variable for rival name
rival = 'A'

# Init dict to keep results in
essence = dict()

# For every device
for plan in plans:
        
    # Calculate rival essence
    rival_essence = get_total_essence(devices[rival], racetrack, 2024)
    
    # Calculate own essence
    essence = get_total_essence(plan, racetrack, 2024)
    
    # Increment number of winning plans if we won
    if essence > rival_essence:
        winning_plans += 1
        
        
# Print the results
print(f'{winning_plans} is the number of winning plans')
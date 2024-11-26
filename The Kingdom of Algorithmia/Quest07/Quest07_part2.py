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

# Parse a square racetrack into a string
def parse_racetrack(lines):
    
    # Start with an empty string
    racetrack = ''
    
    # Start with the top line, excluding the start
    racetrack = lines[0][1:]
    
    # Take the rightmost column, excluding character in the first line
    for i in range(1, len(lines)):
        racetrack += lines[i][-1]
        
    # The the bottom line reversed, excluding the last character
    racetrack += lines[len(lines)-1][:-1][::-1]
    
    # Take the first column reversed, excluding the character in the last line
    for i in reversed(range(0, len(lines)-1)):
        racetrack += lines[i][0]
    
    return racetrack

# Get the total essence
def get_total_essence(name, sequence, racetrack, rounds):
    
    # Init var for total essence
    total_essence = 0
    
    # Starting power
    power = 10
    
    # For every round
    for i in range(rounds * len(racetrack)):
        
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
file = open('input_part2.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
devices = parse_devices(lines)

# Open racetrack file and read as lines
file = open('racetrack1.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the racestrack
racetrack = parse_racetrack(lines)

# Init dict to keep results in
essence = dict()

# For every device
for device in devices:
    
    # Caluclate the total essence
    total_essence = get_total_essence(device, devices[device], racetrack, 10)
    
    # Store the total along with the device name
    essence[total_essence] = device
    
# Get the rankings
rankings = get_ranking(essence)

# Print the results
print(f'{rankings} is the final rankings')
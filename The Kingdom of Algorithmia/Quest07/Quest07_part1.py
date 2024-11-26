# Parse the input into a dict
def parse(lines):
    
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

# Get the total essence
def get_total_essence(sequence, rounds):
    
    # Init var for total essence
    total_essence = 0
    
    # Starting power
    power = 10
    
    # For every round
    for i in range(rounds):
        
        # Find out the current action
        action = sequence[i % len(sequence)]
        
        # Increment or decrement power
        if action == '+':
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
file = open('input_part1.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
devices = parse(lines)

# Init dict to keep results in
essence = dict()

# Init number of steps to take
num_steps = 10

# For every device
for device in devices:
    
    # Caluclate the total essence
    total_essence = get_total_essence(devices[device], num_steps)
    
    # Store the total along with the device name
    essence[total_essence] = device
    
# Get the rankings
rankings = get_ranking(essence)

# Print the results
print(f'{rankings} is the final rankings')
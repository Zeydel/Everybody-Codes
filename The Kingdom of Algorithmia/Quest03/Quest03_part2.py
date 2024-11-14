# Do a Breadth First Search to get distance to closets . 
def get_number_of_blocks_to_remove(grid, x, y):
      
    # Init a set for explored nodes
    explored = set()
    
    # Start a queue and append the starting point with distance 0
    queue = []
    queue.append((x, y, 0))
    
    # While the queue is not empty
    while(len(queue) > 0):
        
        # Pop the next element
        vx, vy, depth = queue.pop(0)
        
        # If we have found a . then return its distance
        if grid[vy][vx] == '.':
            return depth
        
        # Add all neighbors to the the queue if they are inside bounds and have not yet been explored
        if vx - 1 > -1 and (vx, vy) not in explored:
            queue.append((vx - 1, vy, depth + 1))
        if vx + 1 < len(grid[vy]) and (vx, vy) not in explored:
            queue.append((vx + 1, vy, depth + 1))
        if vy - 1 > -1 and (vx, vy) not in explored:
            queue.append((vx, vy - 1, depth + 1))
        if vy + 1 < len(grid) and (vx, vy) not in explored:
            queue.append((vx, vy + 1, depth + 1))
            
        # Add current element to explored list
        explored.add((vx, vy))
        
    # Return infinity if we haven't found anything
    return float('inf')
    
    

#Open file and read as list of strings
inputfile = open('input_part2.txt', 'r')
lines = inputfile.readlines()

# Init var for number of blocks to remove in total
blocks_to_remove = 0

# For every line
for y, line in enumerate(lines):
    
    # For every character
    for x, char in enumerate(line):
        
        # If character is #, find out how many blocks to remove at that position
        if char == '#':
            blocks_to_remove += get_number_of_blocks_to_remove(lines, x, y)
        
# Print the result
print(f'{blocks_to_remove} blocks can be removed')
        


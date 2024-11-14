# Do a Breadth First Search to get distance to closets . 
def get_number_of_blocks_to_remove(grid, x, y):
            
    # Init a set for explored nodes
    explored = set()
    
    # Start a queue and append the starting point with distance 0
    queue = []
    queue.append((x, y, 0))
    explored.add((x, y))
    
    # While the queue is not empty
    while(len(queue) > 0):
        vx, vy, depth = queue.pop(0)
        
        # If we have found a . or are outside the array bounds then return its distance
        if coordinate_is_outside_grid(grid, vx, vy) or grid[vy][vx] == '.':
            return depth
                
        # Add all neighbors to the the queue if they are inside bounds and have not yet been explored
        for nx in range(vx-1, vx+2):
            for ny in range(vy-1, vy+2):
                if (nx, ny) not in explored:
                    queue.append((nx, ny, depth+1))
                    explored.add((nx, ny))        
    
    # If we haven't found a . return infinity
    return float('inf')

# Determine if coordinate is out of grid bounds
def coordinate_is_outside_grid(grid, x, y):
    if y < 0:
        return True
    if y >= len(grid):
        return True
    if x < 0:
        return True
    if x >= len(grid[y]):
        return True
    return False
    

#Open file and read as list of strings
inputfile = open('input_part3.txt', 'r')
lines = [line.strip() for line in inputfile.readlines()]

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
        


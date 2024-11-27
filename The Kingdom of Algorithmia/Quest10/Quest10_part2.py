# To make it as general as posssible, we first find the height and width of the block
def get_height_and_width(lines):
    width, height = 0, 0
    
    for line in lines:
        if len(line) == 0:
            break
        height += 1
        
    for char in lines[0]:
        if char == ' ':
            break
        width += 1
        
    return height, width
    

# Get the sets of row and column characters
def get_rows_and_columns(lines, x_start, y_start, width, height):

    # Init lists for the sets    
    rows = []
    columns = []
    
    for y in range(y_start, y_start + height):
        
        if lines[y][x_start] == '*':
            continue
        
        row_set = set()
        
        for x in range(x_start, x_start + width):
            if lines[y][x] != '.':
                row_set.add(lines[y][x])
                
        rows.append(row_set)
        
    for x in range(x_start, x_start + width):
            
        if lines[y_start][x] == '*':
            continue
            
        column_set = set()
            
        for y in range(y_start, y_start + height):
            if lines[y][x] != '.':
                column_set.add(lines[y][x])
                    
        columns.append(column_set)
                
    return rows, columns
            
def get_word_power(lines, x_start, y_start, width, height):
    
    rows, columns = get_rows_and_columns(lines, x_start, y_start, width, height)
    
    start_row = -1
    start_column = -1

    runic_word = ''
    
    for y in range(y_start, y_start + height):
        for x in range(x_start, x_start + width):
            
            char = lines[y][x]
            
            # We only care about .
            if char != '.':
                continue
            
            # If we havent found the start yet, 
            if start_row == -1:
                start_row = y
                start_column = x
                
            # Get the intersection of the sets and pop the only element
            common_char = rows[y-start_row].intersection(columns[x-start_column]).pop()
            
            # Add the common char to the runic word
            runic_word += common_char
            
    power = 0
            
    for i, char in enumerate(runic_word):
        power += (i+1) * (ord(char) - 64)
        
    
    return power
    
    
# Open file and read as list of lines
file = open('input_part2.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Get he height and the width
height, width = get_height_and_width(lines)

# Init total power
total_power = 0

# For every block, find power and add to total
for x in range(0, len(lines[0]), width+1):
    for y in range(0, len(lines), height+1):
        total_power += get_word_power(lines, x, y, width, height)
            
# Print the result
print(f'{total_power} is the power')
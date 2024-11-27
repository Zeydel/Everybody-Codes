# Get the sets of row and column characters
def get_rows_and_columns(lines):

    # Init lists for the sets    
    rows = []
    columns = []
    
    # For every line
    for line in lines:
        
        # If it starts with *, ignore it
        if line[0] == '*':
            continue
        
        # Init a set for the row
        row_set = set()
        
        # Add all non-. characters
        for char in line:
            if char != '.':
                row_set.add(char)
                
        # Add the set to list of row_sets
        rows.append(row_set)
        
    # Repeat for columns
    for i in range(len(lines[0])):
        
        if lines[0][i] == '*':
            continue
        
        column_set = set()
        
        for j in range(len(lines[i])):
            if lines[i][j] != '.':
                column_set.add(lines[j][i])
                
        columns.append(column_set)
                
    return rows, columns
            
# Open file and read as list of lines
file = open('input_part1.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Get the sets of rows and columns
rows, columns = get_rows_and_columns(lines)

# Init empty row
runic_word = ''

# Init vars for the x and y position of the first .
start_row = -1
start_column = -1

# For every character
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        
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
            
# Print the result
print(f'{runic_word} is the runic word')
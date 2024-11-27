# Class to represent a platinum block
class Block:
    
    def __init__(self):
        self.top = []
        self.bottom = []
        self.left = []
        self.right = []
        self.center = []
        self.center_rows = [set(), set(), set(), set()]
        self.center_columns = [set(), set(), set(), set()]
        
# Parse the text input into a form we can work with
def parse(lines, height, width, margin_height, margin_width):
    
    # We intent to create a 2d aray
    blocks = []
    
    # For every upper left corner
    for y in range(0, len(lines) - 3, height-2):
        
        block_line = []
        
        for x in range(0, len(lines[0]) - 3, width-2):
            
            # Create a block and add to the list
            block_line.append(parse_block(lines, x, y, height, width, margin_height, margin_width))
            
        # Add the line to the list of blocks
        blocks.append(block_line)
        
    # Return the parsed blocks
    return blocks           

# Parse a single block into a block objects
def parse_block(lines, x_start, y_start, height, width, margin_height, margin_width):
    
    # Create a block object
    block = Block()
    
    # Create a list of sets of the left boundry
    left = []
    
    # For evey row, add create a set and add the letters to a set
    for y in range(y_start + margin_height, y_start + height - margin_height):
        
        letters = set()
        
        for x in range(x_start, x_start + margin_width):
            if lines[y][x] != '?':
                letters.add(lines[y][x])

        left.append(letters)
        
    block.left = left
        
    # Repeat for the other directions
    
    right = []
    
    for y in range(y_start + margin_height, y_start + height - margin_height):
        
        letters = set()
        
        for x in range(x_start + width - margin_width, x_start + width):
            if lines[y][x] != '?':
                letters.add(lines[y][x])
           
        right.append(letters)
        
    block.right = right
    
    top = []
    
    for x in range(x_start + margin_width, x_start + width - margin_width):
        
        letters = set()
        
        for y in range(y_start, y_start + margin_height):
            if lines[y][x] != '?':
                letters.add(lines[y][x])
            
        top.append(letters)
        
    block.top = top
    
    bottom = []
    
    for x in range(x_start + margin_width, x_start + width - margin_width):
        
        letters = set()
        
        for y in range(y_start + height - margin_height, y_start + width):
            if lines[y][x] != '?':
                letters.add(lines[y][x])
            
        bottom.append(letters)
           
        
    block.bottom = bottom
    
    center = []
    
    for y in range(y_start + margin_height, y_start + height - margin_height):
        
        line = []
        
        for x in range(x_start + margin_width, x_start + width - margin_width):
            line.append(lines[y][x])
            
        center.append(line)
        
    block.center = center
    
    return block
    
# To make it as general as posssible, we first find the height and width of the block
def get_height_and_width(lines):
    
    width, height = 0, 0
    margin_width, margin_height = 0, 0
    
    starcount = 0
    
    ascending = True
    
    for line in lines:
        
        if line[0] == '*' and ascending:
            starcount += 1
        elif line[0] == '*' and not ascending:
            starcount -= 1
        else:
            ascending = False
            margin_height = starcount
        
        height += 1
        
        if starcount == 0 and not ascending:
            break
        
    ascending = True
        
    for char in lines[0]:
        
        if char == '*' and ascending:
            starcount += 1
        elif char == '*' and not ascending:
            starcount -= 1
        else:
            ascending = False
            margin_width = starcount
        
        width += 1
        
        if starcount == 0 and not ascending:
            break
        
    return height, width, margin_height, margin_width


# Fill the block as much as possible
def fill_block(block):
    
    # Use this to detect changes
    change = False
    
    # For every symbol in the center
    for y in range(len(block.center)):
        for x in range(len(block.center[y])):
            
            # Get the char
            char = block.center[y][x]
            
            # We only care about .
            if char != '.':
                continue
            
            # Get the row and column symbols
            row = block.left[y].union(block.right[y])
            column = block.top[x].union(block.bottom[x])
            
            # Get the common letters
            common_char_set = row.intersection(column)
            
            # If there is only one common letter, we can deduce that it goes in the position
            if len(common_char_set) == 1:
                
                # Get the letter
                common_char = common_char_set.pop()
                
                # Add it to its position and the row and column sets
                block.center[y][x] = common_char
                block.center_columns[x].add(common_char)
                block.center_rows[y].add(common_char)
                
                # Detect change
                change = True
                
    # Return change status
    return change
                
# Deduce empty spots from one direction
def deduce_empty_spots(block):
    
    # Be ready to detect changes
    change = False
    
    # For evey spot in the center
    for y in range(len(block.center)):
        for x in range(len(block.center[y])):
            
            # We only care about. 
            char = block.center[y][x]
            
            if char != '.':
                continue
            
            # Compute row and columns
            row = block.left[y].union(block.right[y])
            column = block.top[x].union(block.bottom[x])
                        
            # Compute the difference between the needed characters in the row
            # and column, with the ones already there
            row_dif = row.difference(block.center_rows[y])
            
            col_dif = column.difference(block.center_columns[x])
            
            # If we are only missing one character, we can deduce that it is it
            if len(row_dif) == 1 and len(row) == 4:
                missing_char = row_dif.pop()
                
                block.center[y][x] = missing_char
                block.center_columns[x].add(missing_char)
                block.center_rows[y].add(missing_char)
                change = True
            
            elif len(col_dif) == 1 and len(column) == 4:
                missing_char = col_dif.pop()
                
                block.center[y][x] = missing_char
                block.center_columns[x].add(missing_char)
                block.center_rows[y].add(missing_char)
                change = True
                
    # Return change status
    return change

# Function to fill question marks from the computed centers
def fill_question_marks(block):
    
    # Be ready to detect changes
    change = False
    
    # For every set in the top list
    for x, top_set in enumerate(block.top):
        
        # If it is empty or full, continue
        if len(top_set) == 0 or len(top_set) == 2:
            continue
        
        # Compute the union with the corresponding set in the bottom
        col_set = top_set.union(block.bottom[x])
        
        # We only care about columns with only one letter missing
        if len(col_set) != 3:
            continue
        
        # We only care about columns whose centers are completely full
        if len(block.center_columns[x]) != 4:
            continue
        
        # Compute the letter that exists in the center, but not on the top
        col_dif = block.center_columns[x].difference(col_set).pop()
        
        # Add it to the top
        block.top[x].add(col_dif)
        
        # Flip to detect change
        change = True
        
        
    # Repeat for the other boundries
    for x, bottom_set in enumerate(block.bottom):
        
        if len(bottom_set) == 0 or len(bottom_set) == 2:
            continue
        
        col_set = bottom_set.union(block.top[x])
        
        if len(col_set) != 3:
            continue
        
        if len(block.center_columns[x]) != 4:
            continue
        
        col_dif = block.center_columns[x].difference(col_set).pop()
        
        block.bottom[x].add(col_dif)
        
        change = True
        
    for y, left_set in enumerate(block.left):
        
        if len(left_set) == 0 or len(left_set) == 2:
            continue
        
        row_set = left_set.union(block.right[y])
        
        if len(row_set) != 3:
            continue
        
        if len(block.center_rows[y]) != 4:
            continue
        
        row_dif = block.center_rows[y].difference(row_set).pop()
        
        block.left[y].add(row_dif)
        
        change = True
    
    for y, right_set in enumerate(block.right):
        
        if len(right_set) == 0 or len(right_set) == 2:
            continue
        
        row_set = right_set.union(block.left[y])
        
        if len(row_set) != 3:
            continue
        
        if len(block.center_rows[y]) != 4:
            continue
        
        row_dif = block.center_rows[y].difference(row_set).pop()
        
        block.right[y].add(row_dif)
        
        change = True
        
# Function to perform boundtry union
def fix_boundries(blocks):
    
    # For evey block
    for y in range(len(blocks)):
        
        for x in range(len(blocks[y])):
            
            # Update the block on top, bottom, left and right
            # in case something on the boundry has been updated
            
            for i in range(len(blocks[y][x].bottom)):
            
                if y > 0:
                    blocks[y][x].top[i] |= blocks[y-1][x].bottom[i]
                    blocks[y-1][x].bottom[i] |= blocks[y][x].top[i]
                
                if y < len(blocks) - 1:
                    blocks[y][x].bottom[i] |= blocks[y+1][x].top[i]
                    blocks[y+1][x].top[i] |= blocks[y][x].bottom[i]
                
            for i in range(len(blocks[y][x].left)):
                
                if x > 0:
                    blocks[y][x].left[i] |= blocks[y][x-1].right[i]
                    blocks[y][x-1].right[i] |= blocks[y][x].left[i]
                
                if x > len(blocks[y]) - 1:
                    blocks[y][x].right[i] |= blocks[y][x+1].left[i]
                    blocks[y][x+1].left[i] |= blocks[y][x].right[i]

# Function to detect whether a block is full
def is_block_full(block):
    
    for line in block.center:
        for char in line:
            if char == '.':
                return False
            
    return True
        
# Function to get word power from a block
def get_word_power(block):
    
    power = 0
    
    pos = 1
    
    for line in block.center:
        for char in line:
            
            power += (ord(char) - 64) * (pos)
            
            pos += 1
        
    return power    

# Open file and read as list of lines
file = open('input_part3.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Compute problem dimensions
height, width, margin_height, margin_width = get_height_and_width(lines)

# Parse the blocks
blocks = parse(lines, height, width, margin_height, margin_width)

# We want to continue as long as there are changes
while True:
    
    # Assume no changes
    change = False
    
    # For every block
    for block_line in blocks:
        for block in block_line:
            
            # Fill the block
            change = change or fill_block(block)
            
            # Deduce empty spots
            change = change or deduce_empty_spots(block)
            
            # Fill question marks
            change = change or fill_question_marks(block)
        
    # Fix the boundies
    fix_boundries(blocks)
    
    # Break if nothing has changed
    if not change:
        break
    
# Compute the total power
total_power = 0

for block_line in blocks:
    for block in block_line:
        if is_block_full(block):
            
            total_power += get_word_power(block)
            
print(f'{total_power} is the total power')


# =============================================================================
# lines = fill_block(lines, 0, 0, width, height, margin_width, margin_height)
# =============================================================================

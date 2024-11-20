# Get the numer of blocks in the structure after a number of layers
def get_blocks_after_layer(layer, blocks_after_previous_layer, previous_layer_thickness, num_priests, num_acolytes):
    
    # Base case
    if layer == 1:
        return (1, 1)
    
    # Get the layer thickness
    layer_thickness = (previous_layer_thickness * num_priests) % num_acolytes
    
    # Get the layer width
    layer_width = (layer * 2) - 1
        
    # Add the number of blocks to the results after the previous layer
    blocks = blocks_after_previous_layer + (layer_thickness*layer_width)
    
    # Return the number of blocks and the layer thickness
    return (blocks, layer_thickness)

# Get the number of blocks in the biggest structure we can build, and the number of blocks in the structure we can almost build along with the layer
def get_bounds(num_priests, num_acolytes, num_blocks):
    
    # Init layer
    layer = 1
    
    # Init vars for current and previous block counts
    previous_block_count = -1
    current_block_count = -1
    
    # Init vars for current and previous layer thickness
    previous_layer_thickness = -1
    current_layer_hickness = -1
    
    # While we can still build the pyramid
    while current_block_count < num_blocks:
        
        # Overrid3e previous vars
        previous_block_count = current_block_count
        previous_layer_thickness = current_layer_hickness
        
        # Get the result for the new layer
        current_block_count, current_layer_hickness = get_blocks_after_layer(layer, current_block_count, current_layer_hickness, num_priests, num_acolytes)
                
        # Increment
        layer += 1
        
    # Return the bounds
    return (layer-1, previous_block_count, current_block_count)

# Open file and read number of priests
file = open('input_part2.txt', 'r')
num_priests = int(file.read())

# Init number of acolytes
num_acolytes = 1111

# Init number of blocks
num_blocks = 20240000

# Calculate the bounds
layer, lower_bound, higher_bound = get_bounds(num_priests, num_acolytes, num_blocks)

# Calculate the width
width = (layer * 2) - 1

# Calculate the number of missings blocks
missing_blocks = higher_bound - num_blocks

# Print the results
print(f'The structure is {width} blocks wide and there is {missing_blocks} blocks missing, resulting in {width*missing_blocks}')
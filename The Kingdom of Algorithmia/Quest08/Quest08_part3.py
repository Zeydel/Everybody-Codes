# Get the number of blocks it takes to build a structure
def get_blocks_for_structure(structure, num_priests, num_acolytes):
    
    # Init number of blocks to remove
    blocks_to_remove = 0
  
    # Take the width of the structure
    width = len(structure)
    
    # Init the rolling height
    rolling_height = structure[0]

    # Init the number of blocks it takes to fill out the whole structure
    blocks = 2*rolling_height

    # For every column after the first one, to the one just before the center
    for column in structure[1:len(structure)//2]:
        
        # Add the column height to the rolling total
        rolling_height += column
        
        # Add double that to the number of blocks
        blocks += rolling_height*2
        
        # Calculate the number of blocks to remove and add to total
        blocks_to_remove += ((num_priests * width * rolling_height) % num_acolytes) * 2
        
    # Add the middle column to the rolling height
    rolling_height += structure[len(structure) // 2]
    
    # Update the total number of blocks needed
    blocks += rolling_height
    
    # Update the number of blocks to remove
    blocks_to_remove += ((num_priests * width * rolling_height) % num_acolytes)
    
    # Return the number of blocks needed after removal
    return blocks - blocks_to_remove
    

# Get the structure after a layer has been added
def get_structure_after_layer(layer, previous_structure, previous_layer_thickness, num_priests, num_acolytes):
    
    # Base case
    if layer == 1:
        return ([1], 1, 1)
    
    # Calculate next layer thickness
    layer_thickness = (previous_layer_thickness * num_priests) % num_acolytes
    layer_thickness += num_acolytes
    
    # Get the new structure
    new_structure = [layer_thickness] + previous_structure + [layer_thickness]
    
    # Return the structure, the layer thickness and the number of blocks needed for the structure
    return (new_structure, layer_thickness, get_blocks_for_structure(new_structure, num_priests, num_acolytes))
    
# Get the biggest structure we can build and the one we can almost build
def get_bounds(num_priests, num_acolytes, num_blocks):
    
    # Init layer
    layer = 1
    
    # Init structure
    structure = []
    
    # Init vars for block count and layer thicknesses
    previous_block_count = -1
    current_block_count = -1
    
    previous_layer_thickness = -1
    current_layer_thickness = -1
    
    # While we can still build the structure
    while current_block_count < num_blocks:
        
        # Override the vars
        previous_block_count = current_block_count
        previous_layer_thickness = current_layer_thickness
        
        # Calculate the new structure, layer thickness and number of blocks
        structure, current_layer_thickness, current_block_count = get_structure_after_layer(layer, structure, current_layer_thickness, num_priests, num_acolytes)
                
        layer += 1
        
    return current_block_count

# Open file and read number of priests
file = open('input_part3.txt', 'r')
num_priests = int(file.read())

# Init number of acolytes
num_acolytes = 10

# Init number of blocks
num_blocks = 202400000

# Get number of blocks of structure we cannot build
higher_bound = get_bounds(num_priests, num_acolytes, num_blocks)

# Get the number of blocks needed to build tempte
missing_blocks = higher_bound - num_blocks

# Print the results
print(f'{missing_blocks} additional blocks are needed to build the structure')
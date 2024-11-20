# Get the biggest number, whose square is bigger than the number of blocks
def get_lesser_square(blocks):
    
    lower = 0
    higher = 0
    
    num = 0
    
    while True:
        
        num += 1
        
        lower = higher
        higher = num * num
        
        if lower > blocks and blocks < higher:
            return num-1
        
# Given a number of layers, return the width of a pyramid with that many layers
def get_width(layers):
    return (layers * 2 ) - 1

# Given a number of layers and a number of blocks, return the number
# of additional blocks needed to construct a pyramid with that many layers
def get_missing_squares(blocks, layers):
    return (layers * layers) - blocks

# Open file and read number of blocks as int
file = open('input_part1.txt')
blocks = int(file.readline())

# Calculate the number of layers in the pyramid
layers = get_lesser_square(blocks)

# Get the width of the pyramid
width = get_width(layers)

# Get the number of missing squares
missing = get_missing_squares(blocks, layers)

# Calculate the result as the product of the width and the number of missing squares
result = width * missing

# Print the result
print(f'The width of the pyramid is {width} and the number of missing {missing}, resulting in {result}')
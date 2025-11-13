# Parse input into list of numbers
def parse(line):
    
    return [int(n) for n in line.split(',')]

def get_center_passes(numbers, nails):
    
    center_passes = 0
    
    for i in range(len(numbers) - 1):
        
        if abs(numbers[i] - numbers[i+1]) == (nails // 2):
            center_passes += 1
            
    return center_passes

# Read the input as a string
line = open('input_part1.txt', 'r').readline()

# Parse input
numbers = parse(line)

# Init problem vars
nails = 32

center_passes = get_center_passes(numbers, nails)

print(f'The string passes {center_passes} times through the center')
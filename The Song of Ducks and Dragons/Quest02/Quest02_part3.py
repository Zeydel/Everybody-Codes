# Parse the input into a tuple of two numbers
def parse(line):
    num1, num2 = line.split('[')[1].split(']')[0].split(',')
    return [int(num1), int(num2)]

# Add two complex numbers together
def add(num1, num2):
    
    X1, Y1 = num1
    X2, Y2 = num2
    
    return [X1 + X2, Y1 + Y2]

# Multiply two complex numbers
def multiply(num1, num2):
    
    X1, Y1 = num1
    X2, Y2 = num2
    
    res1 = X1 * X2 - Y1 * Y2
    res2 = X1 * Y2 + Y1 * X2
    
    return [res1, res2]

# Divide two complex numbers
def divide(num1, num2):
    
    X1, Y1 = num1
    X2, Y2 = num2
    
    return [int(X1 / X2), int(Y1 / Y2)]

# Run one cycle
def do_cycle(num, point):
    
    num = multiply(num, num)
    num = divide(num, [100000,100000])
    return add(num, point)

# Run a number of cycles, starting with (0,0)
def is_engraved(point, cycles):
    
    result = [0, 0]
    
    for i in range(cycles):
        result = do_cycle(result, point)
                
        # Check if we are outside the bounds
        if result[0] > 1000000 or result[0] < -1000000:
            return False
        
        if result[1] > 1000000 or result[1] < -1000000:
            return False
        
    return True

# Read the input as a string
line = open('input_part3.txt', 'r').readlines()[0]

# Parse the input
A = parse(line)

# Find the last coordinate
A_end = add(A, (1000, 1000))

# Init number of engraved points
engraved_points = 0

# For each point, check if it will be ingraved
for y in range(A[1], A_end[1]+1):
    for x in range(A[0], A_end[0]+1):
                
        # Increment counter if point will be engraved
        if is_engraved((x,y), 100):
            engraved_points += 1

# Print the results
print(f'{engraved_points} points will be engraved')
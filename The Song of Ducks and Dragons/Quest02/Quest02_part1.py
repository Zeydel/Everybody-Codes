# Parse the input into a tuple of two numbers
def parse(line):
    num1, num2 = line.split('[')[1].split(']')[0].split(',')
    return int(num1), int(num2)

# Add two complex numbers together
def add(num1, num2):
    
    return num1[0]+num2[0], num1[1]+num2[1]

# Multiply two complex numbers
def multiply(num1, num2):
    
    res1 = (num1[0] * num2[0]) - (num1[1] * num2[1])
    res2 = (num1[0] * num2[1]) + (num1[1] * num2[0])
    
    return res1, res2

# Divide two complex numbers
def divide(num1, num2):
    
    return (num1[0] // num2[0]), (num1[1] // num2[1])

# Run one cycle
def do_cycle(num, A):
    
    num = multiply(num, num)
    num = divide(num, (10, 10))
    return add(num, A)

# Run a number of cycles, starting with (0,0)
def do_cycles(A, cycles):
    
    num = (0, 0)
    
    for i in range(cycles):
        num = do_cycle(num, A)
        
    return num

# Read the input as a string
line = open('input_part1.txt', 'r').readlines()[0]

# Parse the input
A = parse(line)

# Run the given number of cycles
result = do_cycles(A, 3)

# Print the result
print(f'The final result is [{result[0]},{result[1]}]')
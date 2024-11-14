# Open file and read input as list of integers
file = open('input_part2.txt', 'r')
nails = [int(n) for n in file.readlines()]

# Get the nail of minimum length
shortest_nail = min(nails)

# Init number of strikes as zero
strikes = 0

# For every nail
for nail in nails:
    
    # Get the number of strikes required to get to same length as the minimum
    strikes += nail - shortest_nail
    
# Print the result
print(f'{strikes} strikes are needed to align the nails')
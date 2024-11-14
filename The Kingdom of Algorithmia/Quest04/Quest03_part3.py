# Function to get the median value
def get_median(nails):
    
    # Sort the nails and get the middle index
    nails = sorted(nails)
    middle = (len(nails) - 1) // 2

    # If the list has uneven length, return the middle number
    if len(nails) % 2 == 1:
        return nails[middle]
    # If the list has even length, return the average of the two middle numbers
    else:
        return (nails[middle] + nails[middle+1]) // 2

# Open file and read input as list of numbers
file = open('input_part3.txt', 'r')
nails = [int(n) for n in file.readlines()]

# Get the median nail
avg_nail = get_median(nails)

# Init var for number of strikes
strikes = 0

# For every nail
for nail in nails:
    
    # Get the number of strikes required to get to same length as the minimum
    strikes += abs(nail - avg_nail)
    
# Print the results
print(f'{strikes} strikes are needed to align the nails')
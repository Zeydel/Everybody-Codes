def parse(notes):
    
    stars = set()
    
    for y in range(len(notes)):
        for x in range(len(notes[y])):
            
            if notes[y][x] == '*':
                stars.add((y,x))
                
    return stars

# Return the manhatten distance between two stars
def get_distance(star1, star2):
    
    return abs(star1[0] - star2[0]) + abs(star1[1] - star2[1])

# Find the distance between all pairs of stars
def get_all_dists(stars):
    
    dists = dict()
    
    for star1 in stars:
        for star2 in stars:
            if star1 == star2:
                continue
            
            dists[(star1, star2)] = get_distance(star1, star2)
            
    return dists
    
# Get the total distance of the minimum spanning tree between the stars
def get_minimum_distances(stars, distances):
    
    # Init the total distance as zero
    total_distance = 0
    
    # Init a set for every star
    sets = dict()
    
    for star in stars:
        sets[star] = {star}
    
    # For every pair of stars, sorted from lowest to highest distnace
    for d, d_stars in distances:
        
        # Take the two stars
        star1, star2 = d_stars
        
        # If they are already in the same subgraph, skip it
        if star1 in sets[star2]:
            continue
                
        # Add the distance to the total
        total_distance += d
        
        # Join the sets
        sets[star1] |= sets[star2]
        
        # Update every other set
        for star in sets[star1]:
            sets[star] = sets[star1]
            
        # If all stars are in the set, return the total
        if len(sets[star1]) == len(stars):
            return total_distance 
        

# Open and parse input
file = open('input_part1.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the notes
stars = parse(notes)

# Get all distances
distances = get_all_dists(stars)

# Sort pairs of stars by their distances
distances = [(distances[k], k) for k in distances]

distances = sorted(distances)

# Compute the minumum distance
minimum_distance = get_minimum_distances(stars, distances)

# Print the result
print(f'The value of the constellation is {minimum_distance + len(stars)}')
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
def get_all_dists(stars, max_distance):
    
    dists = dict()
    
    for star1 in stars:
        for star2 in stars:
            if star1 == star2:
                continue
            
            distance = get_distance(star1, star2)
            
            # Ignore all distances above the max
            if distance > max_distance:
                continue
            
            dists[(star1, star2)] = get_distance(star1, star2)
            
    return dists
    
# Get the total distance of the minimum spanning tree between the stars
def get_star_sets(stars, distances, max_distance):
        
    # Init a set for every star
    sets = dict()
    
    for star in stars:
        sets[star] = {star}
    
    # For every pair of stars, sorted from lowest to highest distnace
    for d, d_stars in distances:
        
        if d > max_distance:
            break
        
        # Take the two stars
        star1, star2 = d_stars
        
        # If they are already in the same subgraph, skip it
        if star1 in sets[star2]:
            continue
                        
        # Join the sets
        sets[star1] |= sets[star2]
        
        # Update every other set
        for star in sets[star1]:
            sets[star] = sets[star1]

    return sets

# Get the size of a constallation
def get_constellation_size(stars, distances):
    
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
        
        if star1 not in stars or star2 not in stars:
            continue
        
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
            return total_distance + len(stars)
        
    return total_distance
    
# Get all the unique sets from the set of sets
def get_unique_sets(star_sets):
    
    sets = set()
    
    for star_set in star_sets:
        
        sets.add(tuple(star_sets[star_set]))
        
    return sets

# Open and parse input
file = open('input_part3.txt','r')
notes = [line.rstrip() for line in file.readlines()]

# Parse the notes
stars = parse(notes)

max_distance = 5

# Get all distances
distances = get_all_dists(stars, max_distance)

# Sort pairs of stars by their distances
distances = [(distances[k], k) for k in distances]

distances = sorted(distances)

# Compute the minumum distance
sets = get_star_sets(stars, distances, max_distance)

# Sort out all the dublicate sets
sets = get_unique_sets(sets)

# Compute the size of every constallation
sizes = []

for star_set in sets:
    sizes.append(get_constellation_size(star_set, distances))

# Sort constallation sizes
sizes = sorted(sizes, reverse=True)

# Take the product of the three bigget pnes
product = 1

for i in range(3):
    
    product *= sizes[i]
    
# Print the results
print(f'The product of the three biggest constellation sizes is {product}')
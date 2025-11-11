import math

# Get possible mentor-mentee combinations
def get_possible_mentor_combinations(people, max_distance, repeats):
    
    # Init mentor count
    mentor_combinations = 0
    
    # Find out how many 'blocks' of people that we have to process manually
    manual_scans = math.ceil(max_distance / len(people))
    
    # Init dictionary of seen mentors
    seen_mentors = dict()
    
    # For every person in the manually proccessed blocks
    for i in range(len(people) * manual_scans):
        
        # Get the character
        character = people[i % len(people)]
        
        # If it is a mentor, add its index to the list
        if character.isupper():
            
            if character not in seen_mentors:
                seen_mentors[character] = []
                
            seen_mentors[character].append(i)
        
        # If it is a mentee, and we have seen any mentors for it
        elif character.islower() and character.upper() in seen_mentors:
            
            # Go through mentors of the same type
            for mentor in seen_mentors[character.upper()]:
                
                # If it is within distance, add one to mentor count
                if i - mentor <= max_distance:
                    mentor_combinations += 1
      
    # Find out how many blocks of people we have left after manual processing
    remaining_repetitions = repeats - manual_scans
       
    # Get start index of the remaining blocks
    start_index = len(people) * manual_scans
    
    # Init count of mentors in the block as zero
    block_mentors = 0
    
    # For every person in the block
    for i in range(start_index, len(people) + start_index):
        
        # Get the character
        character = people[i % len(people)]
        
        # If mentor, add to list
        if character.isupper():
            
            if character not in seen_mentors:
                seen_mentors[character] = []
                
            seen_mentors[character].append(i)
        
        # If mentee, increment for mentors within range
        elif character.islower() and character.upper() in seen_mentors:
            
            for mentor in seen_mentors[character.upper()]:
                
                if i - mentor <= max_distance:
                    block_mentors += 1
        
    # Add the number of mentors in the block, multiplied by the remaining blocks
    mentor_combinations += (block_mentors * remaining_repetitions)
                    
    return mentor_combinations
                    
    
# Read the input as a string
people = open('input_part3.txt', 'r').readline()

# Init problems vars
max_distance = 1000
repeats = 1000

# Get get possible mentor combinations, first forward and then backwards
mentor_combinations = get_possible_mentor_combinations(people, max_distance, repeats)
mentor_combinations += get_possible_mentor_combinations(people[::-1], max_distance, repeats)

# Print the results
print(f'There are a total of {mentor_combinations} possible combinations of mentors and mentees')
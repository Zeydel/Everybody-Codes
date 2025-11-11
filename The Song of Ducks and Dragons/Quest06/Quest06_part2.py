# Get possible mentor-mentee combinations
def get_possible_mentor_combinations(people):
    
    # Init combinations as zero
    combinations = 0
    
    # Init number of seen mentors as zero
    mentors = dict()
    
    # For every person in the list
    for p in people:
        
        # If it a mentor, increment count
        if p.isupper():
            
            if p not in mentors:
                mentors[p] = 0
                
            mentors[p] += 1
            
        # If it a mentee, add number of seen mentors to the number
        # of combinations
        elif p.islower() and p.upper() in mentors:
            combinations += mentors[p.upper()]
            
    # Return the number of combinations
    return combinations
    
    

# Read the input as a string
people = open('input_part2.txt', 'r').readline()

# Get possible mentor combinations
mentor_combinations = get_possible_mentor_combinations(people)

# Print the results
print(f'There are a total of {mentor_combinations} possible combinations of mentors and mentees')
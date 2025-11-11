# Get possible mentor-mentee combinations
def get_possible_mentor_combinations(people, mentor, mentee):
    
    # Init combinations as zero
    combinations = 0
    
    # Init number of seen mentors as zero
    mentors = 0
    
    # For every person in the list
    for p in people:
        
        # If it a mentor, increment count
        if p == mentor:
            mentors += 1
            
        # If it a mentee, add number of seen mentors to the number
        # of combinations
        elif p == mentee:
            combinations += mentors
            
    # Return the number of combinations
    return combinations
    
    

# Read the input as a string
people = open('input_part1.txt', 'r').readline()

# Get possible mentor combinations
mentor_combinations = get_possible_mentor_combinations(people, 'A', 'a')

# Print the results
print(f'There are a total of {mentor_combinations} possible combinations of mentors and mentees')
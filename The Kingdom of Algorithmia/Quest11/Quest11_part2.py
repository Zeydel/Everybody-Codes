# Parse the input a dictionary
def parse(lines):
    
    rules = dict()
    
    
    # We want a rule for each line
    for line in lines:
        
        # Split the line into parts
        termite, convertions = line.split(':')
        
        convertions = convertions.split(',')
        
        # Create a dictionary to store the parts that the termite split into 
        conv_dict = dict()
        
        # For every termite, add one to the corresponding dictionary
        for con in convertions:
            
            if con not in conv_dict:
                conv_dict[con] = 0
                
            conv_dict[con] += 1
                
        # Add the dictionary as a key to outer dict
        rules[termite] = conv_dict
        
    return rules
    
# Initialise the population
def init_population(rules):
    
    population = dict()
            
    population['Z'] = 1
    
    return population

# Do one iteraton of termite splitting
def do_iteration(rules, population):
    
    # Create a new dict
    new_pop = dict()
    
    # For every type of termite
    for termite in population:
            
        # For every rule for that type
        for conv in rules[termite]:
            
            # Add the split termites to the new population
            if conv not in new_pop:
                new_pop[conv] = 0
                
            new_pop[conv] += rules[termite][conv] * population[termite]
            
    return new_pop

# Get the total termite population
def get_population(population):
    
    total_pop =  0
    
    for termite in population:
        total_pop += population[termite]
        
    return total_pop
    
# Open and parse input
file = open('input_part2.txt','r')
lines = [line.strip() for line in file.readlines()]

rules = parse(lines)

# init the population
population = init_population(rules)

# Do the required number of iterations
num_iterations = 10

for i in range(num_iterations):
    population = do_iteration(rules, population)
    
# Print the result
print(f'{get_population(population)} is the population after {num_iterations} iterations')
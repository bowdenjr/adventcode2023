

def get_groups(springs):
    
    """
    Pass in a list of springs, with no ? and get the x,y,z etc. list of groups
    "#.#" = 1,1
    "#.##.##" = 1,2,2
    """
    output = []
    for i, spring in enumerate(springs):
        if i == 0:
            if spring == "#":
                output.append(1)
        else:
            prior_spring = springs[i-1]
            if spring == "#" and prior_spring == "#":
                output[-1] += 1
            elif spring == "#" and prior_spring != "#":
                output.append(1)
    
    return output



def generate_combinations(springs, total_broken_springs):
    
    """
    Given a string of ?,. or #, make all the possible combinations of springs
    Don't need to add more than the total number of broken springs
    e.g. ???.###, 5 -> ##..###, #.#.###, .##.###
    """
    
    output = []
    
    num_of_max_combinations = 2 ** springs.count("?")
    
    
    
    
    return output


def part1():
    
    # https://math.stackexchange.com/questions/3325221/combination-patterns-how-to-calculate
    
        
    data = open("day_12/testdata_day_12.txt").read().split("\n")
    # data = open("day_12/input_day_12.txt").read().split("\n")
    data = [x.split() for x in data]
    
    for line in data:
        generate_combinations(line[0], 5)
    




if __name__ == "__main__":
    part1()


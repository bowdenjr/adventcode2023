from itertools import combinations, permutations


def get_groups(spring):
    
    """
    Pass in a list of springs, with no ? and get the x,y,z etc. list of groups
    "#.#" = 1,1
    "#.##.##" = 1,2,2
    """
    output = []
    for i, char in enumerate(spring):
        if i == 0:
            if char == "#":
                output.append(1)
        else:
            prior_spring = spring[i-1]
            if char == "#" and prior_spring == "#":
                output[-1] += 1
            elif char == "#" and prior_spring != "#":
                output.append(1)
    
    return output



def generate_combinations(spring):

    """
    Given a string of ?,. or #, make all the possible combinations of springs
    Don't need to add more than the total number of broken springs
    e.g. ???.###, 5 -> ##..###, #.#.###, .##.###
    """

    num_of_max_combinations = 2 ** spring.count("?")
    contig_chars = []
    possible_springs = []
    
    k = -1

    # Get a list of contigious ? chars
    for i, char in enumerate(spring):
        if i == 0:
            prev_char = "."
        else:
            prev_char = spring[i-1]
        
        if char == "?" and prev_char == "?":
            contig_chars[k] += "?"
        elif char == "?":
            k += 1
            contig_chars.append("?")
    
    num_of_qmarks = spring.count("?")
    perms = set(permutations("".join(
                ["#" * num_of_qmarks, "." * num_of_qmarks]), num_of_qmarks))

    for i in perms:
        possible_springs.append(spring.replace("???", "".join(i)))        

    return possible_springs


def part1():
    
    data = open("day_12/testdata_day_12.txt").read().split("\n")
    # data = open("day_12/input_day_12.txt").read().split("\n")
    
    data = [x.split() for x in data]
    
    answer = 0
    for line in data:
        spring_combinations = generate_combinations(line[0])
        for combin in spring_combinations:
            print(f"Checking {combin}")
            if ",".join([str(x) for x in get_groups(combin)]) == line[1]:
                answer += 1

if __name__ == "__main__":
    part1()


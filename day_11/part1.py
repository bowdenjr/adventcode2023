
def expand_empty_rows_and_cols(universe):

    universe_length = len(universe[0])
    universe_height = len(universe)
    j = 0
    while j < universe_length:
        if all([x[int(j)]=="." for x in universe]):
            for k in range(universe_height):
                universe[k] = "".join([universe[k][:int(j)],(int(2-1)*"."),universe[k][int(j):]])
            j += 2-1
            universe_length = len(universe[0])
            print("I did a col expansion")
        j += 1
        
    universe_height = len(universe)
    universe_length = len(universe[0])
    i = 0 
    while i < universe_height:  
        if all([point=="." for point in universe[int(i)]]):
            universe = universe[:int(i)] + int(2-1)*["." * universe_length] + universe[int(i):] 
            i += 2
            universe_height = len(universe)
            print("I did a row expansion")
            continue
        i += 1

    return universe


def find_all_galaxy_coordinates(universe):

    coordinates = []

    for i, row in enumerate(universe):
        for j, char in enumerate(row):
            if char == "#":
                coordinates.append((i,j))

    return coordinates


def part1():

    answer = 0

    data = open("day_11/input_day_11.txt").read().split("\n")
    # data = open("day_11/testdata_day_11.txt").read().split("\n")

    universe = expand_empty_rows_and_cols(data)
    coordinates = find_all_galaxy_coordinates(universe)

    # with open("day_11/expanded_universe.txt","w") as f:
    #     for i in universe:
    #         f.write(i + "\n")
    
    for i, coordinate in enumerate(coordinates):
        for other in coordinates:
            if (other[0] > coordinate[0] 
                or (other[0] == coordinate[0] and other[1] > coordinate[1])):
                
                manhattan_dist = (abs(coordinate[0] - other[0]) + abs(coordinate[1] - other[1]))
                answer += manhattan_dist                
    
    print(answer)


    return


if __name__ == "__main__":
    part1()
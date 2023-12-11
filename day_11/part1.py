
def expand_empty_rows_and_cols(universe):

    universe_height = len(universe)
    universe_length = len(universe[0])
    i = 0 
    while i < universe_height:  
        if all([point=="." for point in universe[int(i)]]):
            universe = universe[:int(i)] + int(1e6-1)*["." * universe_length] + universe[int(i):] 
            i += 1e6
            universe_height = len(universe)
            continue
        print("I did a row expansion")
        i += 1

    universe_height = len(universe)
    j = 0
    while j < universe_length:
        if all([x[int(j)]=="." for x in universe]):
            for q in range(int(1e6-1)):
                for k in range(universe_height):
                    universe[k] = universe[k][:int(j)] +  "." + universe[k][int(j):]                
            j += 1e6-1
            universe_length = len(universe[0])
            print("I did a col expansion")
        j += 1

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

    with open("day_11/expanded_universe.txt","w") as f:
        for i in universe:
            f.write(i + "\n")
    
    for i, coordinate in enumerate(coordinates):
        for other in coordinates:
            if (other[0] > coordinate[0] 
                or (other[0] == coordinate[0] and other[1] > coordinate[1])):
                
                manhattan_dist = (abs(coordinate[0] - other[0]) + abs(coordinate[1] - other[1]))
                answer += manhattan_dist
                # print(f"Distance between {coordinate} and {other} is {manhattan_dist}")
    
    print(answer) # 9918040 too low


    return


if __name__ == "__main__":
    part1()
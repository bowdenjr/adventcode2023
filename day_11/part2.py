
def get_locations_of_gaps(universe):
    
    locations = {"rows":[],"cols":[]}

    universe_length = len(universe[0])
    universe_height = len(universe)
    j = 0
    while j < universe_length:
        if all([x[int(j)]=="." for x in universe]):
            locations["cols"].append(j)
        j += 1
        
    universe_height = len(universe)
    universe_length = len(universe[0])
    i = 0 
    while i < universe_height:  
        if all([point=="." for point in universe[int(i)]]):
            locations["rows"].append(i)
        i += 1

    return locations



def find_all_galaxy_coordinates(universe):

    coordinates = []

    for i, row in enumerate(universe):
        for j, char in enumerate(row):
            if char == "#":
                coordinates.append((i,j))

    return coordinates


def part1():

    answer = 0

    universe = open("day_11/input_day_11.txt").read().split("\n")
    # universe = open("day_11/testdata_day_11.txt").read().split("\n")

    # universe = expand_empty_rows_and_cols(data)
    gap_size = 1e6-1
    gaps = get_locations_of_gaps(universe)
    coordinates = find_all_galaxy_coordinates(universe)
    
    for i, _coordinate in enumerate(coordinates):
        for _other in coordinates:
            if (_other[0] > _coordinate[0] 
                or (_other[0] == _coordinate[0] and _other[1] > _coordinate[1])):
                
                min_row = min([_coordinate[0],_other[0]])
                min_col = min([_coordinate[1],_other[1]])
                max_row = max([_coordinate[0],_other[0]])
                max_col = max([_coordinate[1],_other[1]])                
                
                num_rows_in_distance = len(list(
                    set(gaps["rows"]) 
                    & set(list(range(min_row, max_row)))))
                num_cols_in_distance = len(list(
                    set(gaps["cols"]) 
                    & set(list(range(min_col, max_col)))))
                
                manhattan_dist = (abs(_coordinate[0] - _other[0]) 
                                  + abs(_coordinate[1] - _other[1])
                                  + gap_size * num_rows_in_distance
                                  + gap_size * num_cols_in_distance)
                answer += manhattan_dist
                
                # print(f"MD for {_coordinate} to {_other} = {manhattan_dist}")      
    
    print(answer)


    return


if __name__ == "__main__":
    part1()
from day03 import pad


def find_start(network):
    
    for i in range(len(network)):
        for j in range(len(network[i])):
            if network[i][j] == "S":
                return (i,j)
    
    return None


def get_valid_directions(network, loc, came_from=None):
    
    if not came_from:
        came_from = []
    else:
        came_from = list(came_from)
    
    west  = network[loc[0]][loc[1] - 1]
    east = network[loc[0]][loc[1] + 1]
    north = network[loc[0] - 1][loc[1]]
    south = network[loc[0] + 1][loc[1]]
    
    valid_directions = []
    
    if north in ["|","F","7", "S"] and ("N" not in came_from):
        valid_directions.append("N")
    
    if south in ["|", "L", "J", "S"] and ("S" not in came_from):
        valid_directions.append("S")
    
    if west in ["-", "L", "F", "S"] and ("W" not in came_from):
        valid_directions.append("W")
    
    if east in ["-", "J", "7", "S"] and ("E" not in came_from):
        valid_directions.append("E")
        
    return valid_directions


def get_next_direction(network, loc, came_from):
    
    current_pipe = network[loc[0]][loc[1]]
    
    next_directions = {
        "|": ["N", "S"],
        "-": ["W", "E"],
        "F": ["E", "S"],
        "7": ["W", "S"],
        "L": ["N", "E"],
        "J": ["N", "W"],
        "S": ["N","S","E","W"]
        }
    
    next_directions[current_pipe].remove(came_from)
    next_direction = next_directions[current_pipe][0]

    return next_direction
        

def get_came_from(direction):
    
    directions = {"N": "S", "S": "N", "W": "E", "E": "W"}
    
    return directions[direction]
    

def get_next_loc(current_loc, direction):
    
    next_position = {"N": (loc[0] - 1, loc[1]),
                     "S": (loc[0] + 1, loc[1]),
                     "E": (loc[0], loc[1] + 1),
                     "W": (loc[0], loc[1] - 1)}
                
    return next_position[direction]
    
        
# network = open("day_10/testdata_day_10.txt").read().split("\n")
network = open("day_10/input_day_10.txt").read().split("\n")
network = pad(network)
loc = find_start(network)
valid_directions = get_valid_directions(network, loc)
direction = valid_directions[0]
keep_moving = True
steps = 0 
distances = {loc:0}
    
# Direction 1:
while keep_moving:
    loc = get_next_loc(loc, direction)
    came_from = get_came_from(direction)
    direction = get_next_direction(network, loc, came_from)
    steps += 1
    if network[loc[0]][loc[1]] == "S":
        keep_moving = False
    else:
        distances.update({loc: steps})

#Direction 2:
# only change number if it will be lower
loc = find_start(network)
valid_directions = get_valid_directions(network, loc)
direction = valid_directions[1]
steps = 0 
keep_moving = True
while keep_moving:
    loc = get_next_loc(loc, direction)
    came_from = get_came_from(direction)
    direction = get_next_direction(network, loc, came_from)
    steps += 1
    if network[loc[0]][loc[1]] == "S":
        keep_moving = False
    else:
        if steps < distances[loc]:
            distances.update({loc: steps})

print(max([x for x in distances.values()]))
    
    
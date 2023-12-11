from day03 import pad


def find_start(network):
    
    for i in range(len(network)):
        for j in range(len(network[i])):
            if network[i][j] == "S":
                return (i,j)
    
    return None


def get_connecting_pipes(network, loc):
    
    left  = network[loc[0]][loc[1] - 1]
    right = network[loc[0]][loc[1] + 1]
    up = network[loc[0] - 1][loc[1]]
    down = network[loc[0] + 1][loc[1]]
    
    if up in ["|","F","7"]:
        print("Up connects")
    
    if down in ["|", "L", "J"]:
        print("Down connects")
    
    if left in ["-", "L", "F"]:
        print("Left connects")
    
    if right in ["-", "J", "7"]:
        print("Right connects")


network = open("day_10/testdata_day_10.txt").read().split("\n")
network = pad(network)
start = find_start(network)

connecting_pipes = get_connecting_pipes(network, start)

# Work out what the numbers are, overwriting as necessary

print("ASKJHD")
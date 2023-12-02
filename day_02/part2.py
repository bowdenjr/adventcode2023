import math


def get_minimums(game):
    
    minimums = {"red":0, "green":0, "blue":0}
    
    for subgame in game["game"]:        
        cube_colours = subgame.split(",")
        for cubes in cube_colours:
            number, colour = cubes.strip().split(" ")
            minimums[colour] = max(int(number), minimums[colour])
    
    return minimums


def part2():

    f = open("day_02\input_day_02.txt")    

    games = [{"id":game.split(": ")[0].strip(),
              "game":game.split(": ")[-1].split(";")} 
              for game in f.readlines()]
    
    game_mins = [get_minimums(game) for game in games]
    
    answer = sum([math.prod(game_min.values()) for game_min in game_mins])
                 
    print(answer) #60948


if __name__ == "__main__":
    part2()
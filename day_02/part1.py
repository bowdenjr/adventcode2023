
def get_id_if_game_valid(game, max_cubes):
    
    for subgame in game["game"]:        
        cube_colours = subgame.split(",")
        for cubes in cube_colours:
            number, colour = cubes.strip().split(" ")
            if int(number) > max_cubes[colour]:
                return 0
    
    return int(game["id"].split(" ")[-1])


def part1():

    f = open("day_02\input_day_02.txt")    
    
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    
    games = [{"id": game.split(": ")[0].strip(),
              "game": game.split(": ")[1].split(";")} 
              for game in f.readlines()]
    
    answer = sum([get_id_if_game_valid(game, max_cubes) for game in games])        
                 
    print(answer) #2169


if __name__ == "__main__":
    part1()
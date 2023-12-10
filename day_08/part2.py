import math


def get_new_keys(vals, instruction):
    
    if instruction == "L":
        keys = [val[0] for val in vals]
    else:        
        keys = [val[1] for val in vals]
    
    return keys


def get_new_key(val, instruction):
    
    if instruction == "L":
        key = val[0]
    else:
        key = val[1]
    
    return key

# data = open("day_08/test_data_day_08_part2.txt").read().split("\n\n")
data = open("day_08/input_day_08.txt").read().split("\n\n")

lr_instructions = data[0]
maps = data[1].split("\n")
maps = [x.split("=") for x in maps]
maps = [[y.strip() for y in x] for x in maps]
maps = sum(maps,[])
maps_dict = dict(zip(maps[::2],maps[1::2]))
maps_dict = {key: x.strip("()").split(",") for key, x in maps_dict.items()}
maps_dict = {key: [y.strip() for y in x] for key, x in maps_dict.items()}

steps = 0
instruction_index = 0
key = "AAA"
first_time_hit = 0
times_to_hit = []
keys = [key for key, val in maps_dict.items() if key[-1] == "A"]

for key in keys:

    while True:

        # vals = [val for key, val in maps_dict.items() if key in keys]
        val = maps_dict[key]
        
        instruction = lr_instructions[instruction_index]
        
        key = get_new_key(val, instruction)
        
        if key[-1] == "Z":
            steps += 1
            times_to_hit.append(steps)
            instruction_index = 0
            steps=0
            break
        # elif key[-1] == "Z" and first_time_hit > 0:
        #     print("Soemthing interesting")
        else:
            steps += 1
        
        instruction_index = (instruction_index + 1) % len(lr_instructions)

print(math.lcm(*times_to_hit))


        
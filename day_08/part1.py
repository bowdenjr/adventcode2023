
# data = open("day_08/test_data_day_08.txt").read().split("\n\n")
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

while True:

    val = maps_dict[key]

    if lr_instructions[instruction_index] == "L":
        key = val[0]
    else:
        key = val[1]
    
    if key == "ZZZ":
        steps += 1
        break
    else:
        steps += 1
    
    instruction_index = (instruction_index + 1) % len(lr_instructions)

print(steps)


def update_seed(seed, seed_output, map):

    for line in map:
        destination_start = line[0]
        source_start = line[1]
        range_length = line[2]
        source_max = source_start + range_length
        
        if (source_start <= seed_output[seed] <= source_max):
            seed_output.update({seed:
                                seed_output[seed] 
                                - source_start 
                                + destination_start})
            return seed_output
    
    return seed_output


def part1():
    
    almanac = {
        "seeds":[],
        "seed-":[],
        "soil-":[],
        "ferti":[],
        "water":[],
        "light":[],
        "tempe":[],
        "humid":[]
        }

    # with open("day_05/test_data_day_05.txt","r") as f:
    with open("day_05/input_day_05.txt","r") as f:

        for row in f.readlines():
            
            if row[0].isdigit():
                data_to_add = row.split()
                data_to_add = [int(val) for val in data_to_add]
                almanac[label].append(data_to_add)
            else:
                label = row[:5]
                if label == "seeds":
                    data_to_add = row.split(":")[-1].split()
                    almanac[label] = [int(val) for val in data_to_add]

    seed_output = {seed:seed for seed in almanac["seeds"]}

    for seed in almanac["seeds"]:

        for key, item in almanac.items():
            
            if key == "seeds": 
                continue
            
            seed_output = update_seed(seed, seed_output, item)

    answer = min([item for item in seed_output.values()])
    print(answer) # 604,123,666 too high, 445,717,532 too high


if __name__ == "__main__":
    part1()
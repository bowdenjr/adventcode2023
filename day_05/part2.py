import sys


def get_seed_loc(seed_output, map):

    for line in map:
        destination_start = line[0]
        source_start = line[1]
        range_length = line[2]
        source_max = source_start + range_length
        
        if (source_start <= seed_output <= source_max):
            seed_output = (seed_output - source_start + destination_start)
            return seed_output
    
    return seed_output


def part2():
    
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

    first = True
    # with open("day_05/test_data_day_05.txt","r") as f:
    with open("day_05\input_day_05.txt","r") as f:

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

    seed_starts = almanac["seeds"][::2]
    seed_ranges = iter(almanac["seeds"][1::2])

    i=0
    while i <= len(seed_starts):
        if i%2==1:
            seed_starts.insert(i, seed_starts[i-1] + next(seed_ranges))
        i+=1
    
    lowest_output = lowest_output_right = lowest_output_left = 9e99
    
    seed_output = {seed:seed for seed in seed_starts}
    seed_output = search_range(almanac, seed_starts, seed_output)
    
    while len(seed_starts) > 1:        

        lowest_output = min([lowest_output_left, lowest_output_right])
        
        for item in seed_output.values():
            if item <= lowest_output:
                lowest_output = item
                lowest_index = list(seed_output.values()).index(item)

        seed_output_keys = list(seed_output)
        
        search_right = [int(seed_output_keys[lowest_index-1] 
                                            + (seed_output_keys[lowest_index] 
                                            - seed_output_keys[lowest_index-1] + 1) / 2) + 1,
                                                seed_output_keys[lowest_index]]
        
        search_left = [seed_output_keys[lowest_index-1],
                                        int(seed_output_keys[lowest_index-1] 
                                            + (seed_output_keys[lowest_index] 
                                            - seed_output_keys[lowest_index-1] + 1) / 2)]

        seed_output = {seed:seed for seed in search_right}
        seed_output = search_range(almanac, search_right, seed_output)
        seed_starts = search_right

        for item in seed_output.values():
            if item < lowest_output_right:
                lowest_output_right = item
            else:
                lowest_output_right = 9e99

        if list(seed_output.values())[0] < list(seed_output.values())[1]:
            seed_output = {seed:seed for seed in search_left}
            seed_output = search_range(almanac, search_left, seed_output)
            seed_starts = search_left

        for item in seed_output.values():
            if item < lowest_output_left:
                lowest_output_left = item
            else:
                lowest_output_left = 9e99

        if (lowest_output_right < lowest_output_left):
            print(lowest_output_right)
            sys.exit()
        else:
            if (list(seed_output.keys())[0] == list(seed_output.keys())[1] - 1):
                print(lowest_output_left)
                sys.exit()


def search_range(almanac, seed_starts, seed_output):

    for seed in seed_starts:

        for key, item in almanac.items():

            if key == "seeds": 
                continue
                
            seed_output.update({seed:get_seed_loc(seed_output[seed], item)})
        
    return seed_output

if __name__ == "__main__":
    part2() # 547,577,859 too high
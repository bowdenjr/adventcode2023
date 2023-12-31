

def convert_map_to_list_of_intervals(map):
    
    source_intervals = [(sub_map[1], sub_map[1] + sub_map[2] - 1) 
                        for sub_map in map]
    dest_intervals = [(sub_map[0], sub_map[0] + sub_map[2] - 1) 
                      for sub_map in map]
    
    return [(a, b) for a, b in zip(source_intervals, dest_intervals)]


def filter_seed(interval_maps, x):
    for map in interval_maps:
        for block in map:
            if x in range(block[0][0], block[0][1] + 1):
                x = block[1][0] + (x - block[0][0])
                break
    return x


def filter_seed_range(interval_maps, x: tuple):
    """
    Bear in mind that the intervals may get split into different mappings
    e.g. (50,57) -> (84,14), which doesn't make sense until you realise
    that (50,54) mapped to the range (84, 88) and (55,57) mapped to (12,14).
    This creates a branching type of problem, so I need to explore all of 
    the branches. In this example, I would need to re-filter (84,88) and
    (12,14)
    """

    for map in interval_maps:

        
        # Identify how many maps overlap with my range
        for block in map:
            
            overlap_types_in_map = {"source_subset":0, "left_overlap":0,
                                    "right_overlap":0, "dest_subset":0}
            
            x_min, x_max = x
            block_min, block_max = block[1]
            
            if (x_min < block_min and x_max < block_max):
                # source subset of dest
                overlap_types_in_map["source_subset"] += 1
            
            elif (x_min < block_min and x_max > block_max):
                # left overlap
                overlap_types_in_map["left_overlap"] += 1
            
            elif (x_min > block_min and x_max < block_max):
                # right overlap
                overlap_types_in_map["right_overlap"] += 1
            
            elif (x_min > block_min and x_max > block_max):
                # dest subset of source
                overlap_types_in_map["dest_subset"] += 1        
            
            if sum(overlap_types_in_map.values()) == 0:
                return [filter_seed(interval_maps, a) for a in x]
            elif sum(overlap_types_in_map.values()) > 1:
                raise NotImplementedError
            else:
                if overlap_types_in_map["source_subset"] > 0:
                    # map the whole range
                    pass
                elif overlap_types_in_map["left_overlap"] > 0:
                    pass
                elif overlap_types_in_map["right_overlap"] > 0:
                    pass
                elif overlap_types_in_map["dest_subset"] > 0:
                    pass
            
            # if max(x[0],block[1][0]) < min():
            #     pass


            if x in range(block[0][0], block[0][1] + 1):
                x = block[1][0] + (x - block[0][0])
                break
    return None

almanac = {"seeds": [], "seed-": [], "soil-": [], "ferti": [], "water": [],
           "light": [], "tempe": [], "humid": []}

with open("day_05/test_data_day_05.txt", "r") as f:
    
    for row in f.readlines():
        
        if row[0].isdigit():
            data_to_add = row.split()
            data_to_add = list(map(int,data_to_add))
            almanac[label].append(data_to_add)
        else:
            label = row[:5]
            if label == "seeds":
                data_to_add = row.split(":")[-1].split()
                almanac[label] = [int(val) for val in data_to_add]

starts = iter(almanac["seeds"][::2])
x_range = iter(almanac["seeds"][1::2])
seed_intervals = []

i = 0
while i <= len(almanac["seeds"][::2]) + 1:
    if i % 2 == 1:
        start = next(starts)
        seed_intervals.append((start, start + next(x_range)))
    i += 1

seed_intervals = sorted(seed_intervals)

rename = {"seed-": "to-soil", "soil-": "to-fert", "ferti": "to-water",
          "water": "to-light", "light": "to-temp", "tempe": "to-humid",
          "humid": "to-loc"}

almanac.pop("seeds")
almanac = [map for map in almanac.values()]

interval_maps = []
for map in almanac:
    interval_maps.append(convert_map_to_list_of_intervals(map))

for x, y in seed_intervals:
    x = filter_seed_range(interval_maps, (x, y))

    
    print(x, y)


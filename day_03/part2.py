import math
from part1 import get_chars_in_range, pad


def extract_number_from_digit(schematic, i,j):
    """
    Given a digit point, scan left and right to find the bounds of a number
    """
    output = list(schematic[i][j])
    
    k = j
    while schematic[i][k].isdigit():
        k -= 1
        output.insert(0, schematic[i][k])
        
    k = j
    while schematic[i][k].isdigit():
        k += 1
        output.append(schematic[i][k])
        
    output = [char for char in output if char.isdigit()]
        
    return int("".join(output))


def get_gear_numbers(schematic, i, j):
    """
    Return a unique list of the numbers in range of a * character
    """
    
    gear_numbers = []
    i_max = i+1
    j_max = j+1
    j_min = j-1
                    
    i = i-1    
    while(i <= i_max):              
        j = j_min     
        while(j <= j_max):
            if schematic[i][j].isdigit():
                gear_numbers.append(extract_number_from_digit(schematic,i,j))                                
            j += 1
        i += 1
                    
    gear_numbers = set(gear_numbers)
    
    return gear_numbers
    

def part2():

    answer = 0
    schematic = open("day_03\input_day_03.txt").read().split("\n")
    schematic = pad(schematic)
    
    for i, row in enumerate(schematic):
        if i == 0: continue # The first row is my padding
        
        for j, char in enumerate(row):
            
            if char == "*":
                gear_scanned_chars = get_chars_in_range(
                    schematic, [i-1, j-1], [i+1, j+1])
                
                # If there are more than 2 digits, get gear numbers
                if sum([x.isdigit() for x in gear_scanned_chars]) >= 2:
                    # Dupes are removed in get_gear_numbers function
                    gear_numbers = get_gear_numbers(schematic, i, j) 
                    
                    if len(gear_numbers) > 1:
                        answer += math.prod(gear_numbers)
            
    print(answer)


if __name__ == "__main__":
    part2()
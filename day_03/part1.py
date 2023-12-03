
def get_symbols(schematic):
    
    symbols = []
    
    for row in schematic:
        symbols.extend(
            [char for char in row 
             if not char.isdigit() and char!="." and char!="\n"])
        
    return set(symbols)


def pad(schematic):

    max_length = max([len(row) for row in schematic])
    schematic.insert(0, "."*max_length)
    schematic.append("."*max_length)
    schematic = ["." + row + "." for row in schematic]
    
    return schematic
 

def get_chars_in_range(schematic, loc1, loc2):
    """
    Given loc1 and loc2, lists in the form: [i,j],
    return a list of chars from the schematic
    """
    output = []
    
    i_max = max(loc1[0], loc2[0])
    j_max = max(loc1[1], loc2[1])
        
    i = min(loc1[0], loc2[0])
    
    while(i <= i_max):
        j = min(loc1[1], loc2[1])
        while(j <= j_max):
            output.append(schematic[i][j])
            j += 1
        i += 1
    
    return output
    

def part1():

    answer = 0
    schematic = open("day_03\input_day_03.txt").read().split("\n")
    symbols = get_symbols(schematic)
    schematic = pad(schematic)
    
    for i, row in enumerate(schematic):
        
        getting_number_length = False
        found_number = False
        if i == 0: continue # The first row is my padding
        
        for j, char in enumerate(row):
            
            if not char.isdigit():
                if getting_number_length:
                    getting_number_length = False
                    last_digit_loc = [i, j-1]
                    found_number = True
                else:
                    continue 
            elif not schematic[i][j-1].isdigit() and not getting_number_length:
                first_digit_loc = [i,j]
                getting_number_length = True
            
            if found_number:
                number = int("".join(get_chars_in_range(
                    schematic, first_digit_loc, last_digit_loc)))
                
                for p in range(2):
                    first_digit_loc[p] = first_digit_loc[p] - 1                    
                    last_digit_loc[p] = last_digit_loc[p] + 1
                
                scanned_chars = get_chars_in_range(
                    schematic, first_digit_loc, last_digit_loc)
                
                if set(symbols).intersection(scanned_chars):
                    answer += number
                    
                first_digit_loc, last_digit_loc = [0,0], [0,0]
                found_number = False
                    
    print(answer)
  

if __name__ == "__main__":
    part1()
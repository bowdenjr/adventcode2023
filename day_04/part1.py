

def part1():
    
    f = open("day_04/input_day_04.txt")
    answer = 0
    
    for line in f.readlines():
        card_id, numbers = line.split(":")        
        my_numbers, winning_numbers = numbers.split("|")
        my_numbers = my_numbers.strip().split(" ")
        winning_numbers = winning_numbers.strip().split(" ")
        my_numbers = [int(number.replace("\n","")) 
                      for number in my_numbers if number not in [""," "]]
        winning_numbers = [int(number.replace("\n","")) 
                           for number in winning_numbers if number not in [""," "]]                
        matches = set(my_numbers).intersection(winning_numbers)
        if len(matches) > 0:
            answer += 2**(len(matches)-1)
    print(answer)


if __name__ == "__main__":
    part1()
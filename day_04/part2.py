    
def part2():    
    
    data = open("day_04/input_day_04.txt").read().split("\n")
    
    # Initialise totals
    card_copies = [1] * len(data)
    
    for i, row in enumerate(data):
        card_id, numbers = row.split(":")
        card_id = int(card_id.split(" ")[-1])
        my_numbers, winning_numbers = numbers.split("|")
        my_numbers = my_numbers.strip().split(" ")
        winning_numbers = winning_numbers.strip().split(" ")
        my_numbers = [int(number.replace("\n","")) 
                      for number in my_numbers if number not in [""," "]]
        winning_numbers = [int(number.replace("\n","")) 
                           for number in winning_numbers
                           if number not in [""," "]]                
        matches = set(my_numbers).intersection(winning_numbers)
        num_of_matches = len(matches)     

        # Don't make the data, count the totals
        for j in range(i+1, i+1+num_of_matches):
            card_copies[j] += card_copies[i]
    
    print(sum(card_copies))
    

if __name__ == "__main__":
    part2()
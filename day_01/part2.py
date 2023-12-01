from part1 import get_number_from_first_and_last_digit


def replace_words_with_digits(numbers, line):
    
    word_to_int = {"one":1,"two":2,"three":3,"four":4,"five":5,
                   "six":6,"seven":7,"eight":8,"nine":9}

    for word in word_to_int.keys():
        
        found = line.find(word)

        if found == -1:
            continue
        else:
            line = line.replace(word, str(word_to_int[word]))  

    return line


def part2():

    f = open("day_01\input_day_01.txt")
    open("day_01/output_file.txt","w")

    answer = 0
    numbers = ["one","two","three","four","five","six","seven","eight","nine"]
    
    edgecases = {"oneight":"oneeight", "twone":"twoone",
                 "threeight":"threeeight", "fiveight":"fiveeight",
                 "sevenine":"sevennine", "eightwo":"eighttwo",
                 "eighthree":"eightthree", "nineight":"nineeight"}

    for i, line in enumerate(f.readlines()):
        
        # Replace the "oneight" cases with "oneeight"
        for edgecase in edgecases.keys():        
            line = line.replace(edgecase, edgecases[edgecase])

        line = replace_words_with_digits(numbers, line)  

        # Extract the digits
        line_answer = get_number_from_first_and_last_digit(line)

        answer += line_answer

        with open("day_01/output_file.txt","a") as f:
            f.write(line)

    print(answer) # Actual answer = 55686

if __name__ == "__main__":
    part2()
from part1 import get_number_from_first_and_last_digit


def replce_words_with_digits(numbers, line):
    
    word_to_int = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

    for p in range(len(line)):

        if line[p:p+3] in numbers:
            word = line[p:p+3]
            line = line.replace(word, str(word_to_int[word]))  

        elif line[p:p+4] in numbers:
            word = line[p:p+4]
            line = line.replace(word, str(word_to_int[word]))  

        elif line[p:p+5] in numbers:
            word = line[p:p+5]
            line = line.replace(word, str(word_to_int[word]))  

        elif line[p:p+6] in numbers:
            word = line[p:p+6]
            line = line.replace(word, str(word_to_int[word]))

    return line

def part2():

    f = open("day_01\input_day_01.txt")
    open("day_01/output_file.txt","w")

    numbers_to_add = []
    numbers = ["one","two","three","four","five",
               "six","seven","eight","nine"]
    edgecases = {"oneight":"oneeight", "twone":"twoone",
                 "threeight":"threeeight", "fiveight":"fiveeight",
                 "sevenine":"sevennine", "eightwo":"eighttwo",
                 "eighthree":"eightthree", "nineight":"nineeight"}

    for i, line in enumerate(f.readlines()):
        
        # Replace the "oneight" cases with "oneeight"
        for edgecase in edgecases.keys():
            if edgecase in line:
                line = line.replace(edgecase, edgecases[edgecase])

        # Detect and replace with int when there are any txt words in the line
        number_is_found = any(word in line for word in numbers)

        while(number_is_found):

            if number_is_found:
                line = replce_words_with_digits(numbers, line)  

            number_is_found = any(word in line for word in numbers)

        # Extract the digits
        digit = get_number_from_first_and_last_digit(line)

        numbers_to_add.append(digit)

        with open("day_01/output_file.txt","a") as f:
            f.write(line)

    print(sum(numbers_to_add)) # Actual answer = 55686

if __name__ == "__main__":
    part2()

def get_number_from_first_and_last_digit(line):

    line_digits_only = []

    for char in line:
        if char.isdigit():
            line_digits_only.append(char)

    if len(line_digits_only) > 1:
        digit = int(line_digits_only[0] + line_digits_only[-1])
    else:
        digit = int(line_digits_only[0] + line_digits_only[0])

    return digit

def part1():

    f = open("day_01\input_day_01.txt")

    numbers_to_add = []

    for line in f.readlines():
        
        digit = get_number_from_first_and_last_digit(line)
        numbers_to_add.append(digit)

    print(sum(numbers_to_add)) # Actual answer = 55029

if __name__ == "__main__":
    part1()
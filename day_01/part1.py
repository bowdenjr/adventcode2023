
def get_number_from_first_and_last_digit(line):

    line_digits_only = [char for char in line if char.isdigit()]
    
    digit = int(line_digits_only[0] + line_digits_only[-1])

    return digit

def part1():

    f = open("day_01\input_day_01.txt")

    numbers_to_add = [get_number_from_first_and_last_digit(line) for line in f.readlines()]

    print(sum(numbers_to_add)) # Actual answer = 55029

if __name__ == "__main__":
    part1()
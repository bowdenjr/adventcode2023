import math

f = open(r"day_06\input_day_06.txt")
races = f.read().split("\n")
times, distances = [line.split()[1:] for line in races]
times, distances = int("".join(times)), int("".join(distances))

answer = []

ways_to_win = 0
for charge_time in range(times):
    remaining_time = times - charge_time
    my_distance = charge_time * remaining_time
    if my_distance > distances:
        ways_to_win += 1
answer.append(ways_to_win)


print(math.prod(answer))
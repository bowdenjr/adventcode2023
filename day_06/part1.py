import math

f = open(r"day_06\input_day_06.txt")
races = f.read().split("\n")
times, distances = [line.split()[1:] for line in races]
times = list(map(int,times))
distances = list(map(int,distances))

answer = []
for time, record_distance in zip(times, distances):
    ways_to_win = 0
    for charge_time in range(time):
        remaining_time = time - charge_time
        my_distance = charge_time * remaining_time
        if my_distance > record_distance:
            ways_to_win += 1
    answer.append(ways_to_win)


print(math.prod(answer))
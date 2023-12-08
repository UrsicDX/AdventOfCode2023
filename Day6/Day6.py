def process_input(input_str):
    lines = input_str.strip().split('\n')
    time = []
    distance = []

    for line in lines:
        words = line.split()
        if words[0] == 'Time:':
            time = [int(word) for word in words[1:]]
        elif words[0] == 'Distance:':
            distance = [int(word) for word in words[1:]]

    return time, distance

def calculate_distance(hold_time, total_time):
    speed = hold_time
    move_time = total_time - hold_time
    return speed * move_time

def count_ways_to_beat_record(race_time, distance_to_beat):
    count = 0
    for hold_time in range(race_time + 1):
        if calculate_distance(hold_time, race_time) > distance_to_beat:
            count += 1
    return count


with open('input.txt', 'r') as file:
    input_str = file.read()


race_times, distances = process_input(input_str)


total_combinations = 1
for race_time, distance in zip(race_times, distances):
    ways = count_ways_to_beat_record(race_time, distance)
    print(f"Number of ways to beat the record for race time {race_time} ms: {ways}")
    total_combinations *= ways
print(f"Total number of combinations to beat all records: {total_combinations}")

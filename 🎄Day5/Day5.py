#not optimal code but it works :)
def convert_number(number, conversion_map):
    for entry in conversion_map:
        if len(entry) != 3:
            print("Invalid entry in map:", entry)
            continue
        dest_start, src_start, length = entry
        if src_start <= number < src_start + length:
            return dest_start + (number - src_start)
    return number

def convert_seeds(seeds, maps):
    converted_numbers = []
    for seed in seeds:
        number = seed
        for map in maps:
            number = convert_number(number, map)
        converted_numbers.append(number)
    return converted_numbers

def parse_map(lines):
    return [tuple(map(int, line.split())) for line in lines if line.strip()]

def read_data(filename):
    with open(filename, 'r') as file:
        content = file.readlines()

    seeds_line = content[0].strip()
    seeds = list(map(int, seeds_line.split(': ')[1].split()))

    maps = []
    current_map_lines = []
    for line in content[1:]:
        line = line.strip()
        if line.endswith('map:'):
            if current_map_lines:
                maps.append(parse_map(current_map_lines))
                current_map_lines = []
        elif line:
            current_map_lines.append(line)
    if current_map_lines:
        maps.append(parse_map(current_map_lines))

    return seeds, maps

filename = 'input.txt'
seeds, maps = read_data(filename)

print("Seeds:", seeds)
for i, map in enumerate(maps):
    print(f"Map {i+1}:", map)

converted_seeds = convert_seeds(seeds, maps)
lowest_location_number = min(converted_seeds)

print("Lowest location number:", lowest_location_number)

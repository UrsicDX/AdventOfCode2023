def read_map(file_path):
    with open(file_path, "r") as f:
        return [list(line.strip()) for line in f.readlines()]

def find_start(map):
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == 'S':
                return i, j
    return None

def traverse_pipes(map, start, pipe_types, directions):
    encountered_places = {}
    search_queue = [(start, 0)]

    while search_queue:
        current, distance = search_queue.pop(0)
        if current in encountered_places:
            continue
        encountered_places[current] = distance
        i, j = current
        for direction in pipe_types[map[i][j]]:
            di, dj, opposite = directions[direction]
            ni, nj = i + di, j + dj
            if 0 <= ni < len(map) and 0 <= nj < len(map[ni]) and map[ni][nj] in pipe_types:
                if opposite in pipe_types[map[ni][nj]]:
                    search_queue.append(((ni, nj), distance + 1))

    return encountered_places

def count_enclosed_tiles(map, encountered_places, pipe_types):
    for i, row in enumerate(map):
        norths = 0
        for j, cell in enumerate(row):
            if (i, j) in encountered_places:
                if "n" in pipe_types[cell]:
                    norths += 1
            else:
                map[i][j] = "I" if norths % 2 != 0 else "O"

    return sum(row.count("I") for row in map)

def main(file_path):
    pipe_types = {
        "|": ["n", "s"], "-": ["w", "e"], "L": ["n", "e"], "J": ["n", "w"],
        "7": ["s", "w"], "F": ["s", "e"], 'S': ["n", "s", "w", "e"]
    }
    directions = {
        "n": (-1, 0, "s"), "s": (1, 0, "n"), "w": (0, -1, "e"), "e": (0, 1, "w")
    }

    map = read_map(file_path)
    start = find_start(map)
    encountered_places = traverse_pipes(map, start, pipe_types, directions)
    inside_count = count_enclosed_tiles(map, encountered_places, pipe_types)

    return inside_count


file_path = "input.txt"
inside_count = main(file_path)
print(f"inside: {inside_count}")

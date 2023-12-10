from collections import deque

def read_layout(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def is_valid_move(layout, x, y, coming_from):
    if x < 0 or y < 0 or y >= len(layout) or x >= len(layout[y]):
        return False
    if layout[y][x] == '.':
        return False

    pipe = layout[y][x]
    valid_moves = {
        '|': {'N', 'S'},
        '-': {'E', 'W'},
        'L': {'S', 'W'},
        'J': {'S', 'E'},
        '7': {'N', 'E'},
        'F': {'N', 'W'},
        'S': {'N', 'S', 'E', 'W'}
    }

    return coming_from in valid_moves[pipe]

def get_neighbors(layout, x, y):
    neighbors = []
    directions = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
    for d, (dx, dy) in directions.items():
        nx, ny = x + dx, y + dy
        if is_valid_move(layout, nx, ny, d):
            neighbors.append((nx, ny, d))
    return neighbors

def find_start(layout):
    for y, row in enumerate(layout):
        for x, tile in enumerate(row):
            if tile == 'S':
                return x, y
    return None, None

def bfs_distance_map(layout, start_x, start_y):
    max = 0
    queue = deque([(start_x, start_y, 0, 'S')])
    distance_map = [[None for _ in row] for row in layout]
    distance_map[start_y][start_x] = 0
        
    while queue:
        x, y, distance, coming_from = queue.popleft()

        for nx, ny, direction in get_neighbors(layout, x, y):
            if distance_map[ny][nx] is None:
                distance_map[ny][nx] = distance + 1
                queue.append((nx, ny, distance + 1, direction))
    return distance_map

def print_distance_map(distance_map):
    max_value = None

    for row in distance_map:
        for x in row:
            if x is not None and (max_value is None or x > max_value):
                max_value = x

    #for row in distance_map:
        #print(''.join('.' if x is None else str(x) for x in row))

    print("Max value:", max_value)

def main():
    layout = read_layout("input.txt")
    start_x, start_y = find_start(layout)

    if start_x is not None:
        distance_map = bfs_distance_map(layout, start_x, start_y)
        #print("Distance Map:")
        print_distance_map(distance_map)
    else:
        print("Starting position 'S' not found.")

if __name__ == "__main__":
    main()

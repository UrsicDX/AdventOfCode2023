def parse_game_data(game_info):
    game_data = []
    rounds = game_info.split(';')
    for round in rounds:
        round_data = {}
        colors = round.strip().split(',')
        for color in colors:
            if color.strip():  # Check if the color string is not empty
                parts = color.strip().split()
                if len(parts) == 2:
                    round_data[parts[1]] = int(parts[0])
                else:
                    print(f"Unexpected format in color data: '{color}'")
        game_data.append(round_data)
    return game_data

def is_game_valid(game_data, initial_set):
    for color, count in game_data.items():
        if count > initial_set.get(color, 0):
            return False
    return True

def sum_valid_game_ids(input_string):
    initial_set = {'red': 12, 'green': 13, 'blue': 14}
    games = input_string.split('Game')
    valid_game_ids = []

    for game in games[1:]:
        game_id, game_info = game.split(':')
        game_data = parse_game_data(game_info)
        if all(is_game_valid(data, initial_set) for data in game_data):
            valid_game_ids.append(int(game_id.strip()))
    print(valid_game_ids)
    return sum(valid_game_ids)

# Read input from file
with open('input.txt', 'r') as file:
    input_string = file.read()

# Process the input string
result = sum_valid_game_ids(input_string)
print("Sum of valid game IDs:", result)

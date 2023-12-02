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

def max_color_counts(game_data):
    max_counts = {'red': 0, 'green': 0, 'blue': 0}
    for round_data in game_data:
        for color, count in round_data.items():
            max_counts[color] = max(max_counts.get(color, 0), count)
    return max_counts

def product_of_max_counts(max_counts):
    product = 1
    for count in max_counts.values():
        product *= count
    return product

def sum_of_products(input_string):
    games = input_string.split('Game')
    total_sum = 0

    for game in games[1:]:
        game_id, game_info = game.split(':')
        game_data = parse_game_data(game_info)
        max_counts = max_color_counts(game_data)
        total_sum += product_of_max_counts(max_counts)

    return total_sum

# Read input from file
with open('input.txt', 'r') as file:
    input_string = file.read()

# Process the input string
result = sum_of_products(input_string)
print("Sum of products:", result)

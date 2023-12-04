def count_scratchcards(cards):
    num_copies = [1] * len(cards)
    for i in range(len(cards)):
        matches = sum(num in cards[i][1] for num in cards[i][0])
        new_cards = matches if matches < len(cards) - i else len(cards) - i - 1
        for j in range(i + 1, i + 1 + new_cards):
            num_copies[j] += num_copies[i]
    return sum(num_copies)

def read_cards_from_file(filename):
    cards = []
    with open(filename, 'r') as file:
        for line in file:
            
            parts = line.strip().split('|')

            # Skip the card X:
            card_numbers = list(map(int, parts[0].split(':')[1].strip().split()))
            winning_numbers = list(map(int, parts[1].strip().split()))

            cards.append((card_numbers, winning_numbers))
    return cards

cards = read_cards_from_file('input.txt')
total_cards = count_scratchcards(cards)
print(f"Total scratchcards: {total_cards}")


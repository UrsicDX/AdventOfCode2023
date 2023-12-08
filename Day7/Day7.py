def custom_sort(deck, wildcard, sequence):
    sort_key = tuple(
        sum([(deck.count(card) + [0, deck.count(wildcard)][not idx]) == count
                for idx, card in enumerate(sorted(set(deck) - {wildcard}, key=lambda c: -deck.count(c)))]
        )
        for count in range(5, 0, -1)
    ) + tuple(sequence.index(card) for card in deck)
    return [sort_key, (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)][not sum(sort_key)]

with open("input.txt", "r") as file:
    lines = [line.split() for line in file.read().splitlines()]
    for total_score, joker_card, card_order in ((0, " ", "23456789TJQKA"), (0, "J", "J23456789TQKA")):
        for index, (hand, points) in enumerate(sorted(lines, key=lambda item: custom_sort(item[0], joker_card, card_order))):
            total_score += (index + 1) * int(points)
        print(total_score)

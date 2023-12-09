def next_value(seq):
    original_seq = seq[:]
    diff_seqs = []

    # Generate sequences of differences until we reach all zeroes
    while not all(x == 0 for x in seq):
        seq = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
        diff_seqs.append(seq)

    # Work our way back up to find the next value
    for diff_seq in reversed(diff_seqs):
        original_seq.append(original_seq[-1] + diff_seq[-1])

    return original_seq[-1]

def sum_extrapolated_values(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return sum(next_value(list(map(int, line.split()))) for line in data.splitlines())

# Example usage
print(sum_extrapolated_values("input.txt"))

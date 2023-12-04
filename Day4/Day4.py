import collections

with open('input.txt', 'r') as file:
    lines = file.readlines()
    sum1 = 0
    for line in lines:

        parts = line.strip().split(' | ')

        
        first_set = [int(num) for num in parts[0].split(':')[1].split()]
        second_set = [int(num) for num in parts[1].split()]

     
        counter = collections.Counter(first_set + second_set)

       
        matching_pairs = sum(1 for num, count in counter.items() if count == 2)

        # Calculate the result as 2^matching_pairs
        result = round(2 ** (matching_pairs -1))
        sum1 += result
        #print(f"{line.strip()} - Result: {result}")
        print(sum1)
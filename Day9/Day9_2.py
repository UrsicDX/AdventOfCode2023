def sum_extrapolated_values(file_path):
    miki = 0
    

    with open(file_path, 'r') as file:
        for line in file:
            nums = list(map(int, line.split()))
            s = 1
            while nums[-1]:
                miki += s * nums[0]
                s = -s
                nums = [y - x for x, y in zip(nums, nums[1:])]

    return miki

miki = sum_extrapolated_values("input.txt")
print("Past:", miki)

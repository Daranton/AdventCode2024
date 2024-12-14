rules, updates = open('Day5input.txt').read().split('\n\n')
updates = [x.split(',') for x in updates.split('\n')]

def true_pos(x, nums):
    return len(nums) - 1 - sum(f"{x}|{y}" in rules for y in nums)

def mid(nums):
    try:
        return next(x for x in nums if true_pos(x, nums) == len(nums) // 2)
    except StopIteration:  # Handle case where no valid 'mid' is found
        return 0  # Default value (adjust as needed)

def is_ordered(nums):
    return all(i == true_pos(x, nums) for i, x in enumerate(nums))

try:
    print(sum(int(mid(nums)) for nums in updates if is_ordered(nums))) # Part 1
except ValueError:  # Handle case where int conversion fails
    print("Error encountered while processing ordered updates.")

try:
    print(sum(int(mid(nums)) for nums in updates if not is_ordered(nums))) # Part 2
except ValueError:  # Handle case where int conversion fails
    print("Error encountered while processing unordered updates.")

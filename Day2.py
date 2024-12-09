ans = 0

with open("./Day2input.txt") as f:
    lines = f.read().strip().split("\n")
    #lines = f.read().split("\n")
    #lines = f.read()
    #lines = f.read().strip()
    print(lines)

def is_safe(nums):
    inc = nums[1] > nums[0]
    if inc:
        for index in range(1, len(nums)):
            diff = nums[index] - nums[index-1]
            if not 1 <= diff <= 3:
                #print(index)
                return False
        return True
    else:
        for index in range(1, len(nums)):
            diff = nums[index] - nums[index-1]
            if not -3 <= diff <= -1:
                return False
        return True

def is_safe_2(nums):
    if is_safe(nums):
        return True
    for i in range(len(nums)):
        if is_safe(nums[:i] + nums[i+1:]):
            return True
    return False

for line in lines:
    nums = [int(i) for i in line.split()]
    #ans += is_safe(nums)
    ans += is_safe_2(nums)
    #print(nums)
    #print(ans)
print(ans)

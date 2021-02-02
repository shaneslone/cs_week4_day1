def csFindTheSingleNumber(nums):
    d = {}
    for num in nums:
        if num not in d:
            d[num] = 0
        d[num] += 1
    for k in d:
        if d[k] == 1:
            return k


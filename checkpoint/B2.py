def majorityElement(nums):
    if not nums:
        return []
    count1, count2, candidate1, candidate2 = 0, 0, None, None

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
    result = []
    n = len(nums)
    if nums.count(candidate1) > n // 3:
        result.append(candidate1)
    if candidate2 != candidate1 and nums.count(candidate2) > n // 3:
        result.append(candidate2)
    return result
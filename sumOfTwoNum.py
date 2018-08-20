nums = [3,2,4]
target = 6


def two_sum(nums, target):
    """利用dict的哈希特点进行查询，空间换时间"""
    test_dict = {}
    for i in range(len(nums)):
        test_dict[nums[i]] = i
    for i in range(len(nums)):
        a = target - nums[i]
        if a in test_dict and test_dict[a] != i:
            print(f"index: {i} {test_dict[a]}")
            # break


def twoSum2(nums, target):
    """一遍哈希,边存边比较"""
    n = len(nums)
    # 创建一个空字典
    d = {}
    for x in range(n):
        a = target - nums[x]
        # 字典d中存在nums[x]时
        if nums[x] in d:
            print(d[nums[x]], x)
        # 否则往字典增加键/值对
        else:
            d[a] = x


if __name__ == "__main__":
    two_sum(nums, target)

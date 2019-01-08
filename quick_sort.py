# encoding:utf-8

def quick_sort(nums, begin, end):
    if begin >= end:
        return
    pos = partition_two_index(nums, begin, end)
    # print(pos)
    quick_sort(nums, begin, pos)
    quick_sort(nums, pos + 1, end)


def partition_one_index(nums, begin, end):
    pivot = nums[begin]
    pos = begin
    for i in range(begin + 1, end):
        if nums[i] < pivot:
            pos += 1
            if i != pos:
                nums[pos], nums[i] = nums[i], nums[pos]
    nums[begin], nums[pos] = nums[pos], nums[begin]
    return pos


def partition_two_index(nums, begin, end):
    priot = nums[begin]
    left, right = begin+1, end-1
    while left <= right:
        while left <= right and nums[right] > priot:
            right -= 1
        while left <= right and nums[left] <= priot:
            left += 1
        if left > right:
            break
        nums[left], nums[right] = nums[right], nums[left]
    print(nums, left, right)
    nums[right], nums[begin] = nums[begin], nums[right]
    print(nums)
    return right


if __name__ == "__main__":
    test_list = [26, 101, 27, 80, -9, 17, 37, 18, 93, 25]
    # test_list = [10, 26, 26, 27, 27, -9, 17, 37, 18, 1, 25]
    # test_list = [10, 26, 26, 27, -9]
    # test_list = []
    n = len(test_list)
    quick_sort(test_list, 0, n)
    print(test_list)

# encoding:utf8
import json

#https://leetcode-cn.com/problems/move-zeroes/


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i, num in enumerate(nums):
            if num != 0:
                if i != k:
                    nums[i], nums[k] = nums[k], nums[i]
                    k += 1
                else:
                    k += 1

    # 快慢指针实现
    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 1:
            return
        slow = fast = 0
        while fast < length:
            if nums[fast] != 0:
                if slow != fast and nums[slow] == 0:
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                slow += 1
            fast += 1


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);

            ret = Solution().moveZeroes(nums)

            out = integerListToString(nums)
            if ret is not None:
                print
                "Do not return anything, modify nums in-place instead."
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

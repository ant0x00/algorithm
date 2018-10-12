# coding: utf-8

import json

'''
https://leetcode-cn.com/problems/find-pivot-index/description/

'''


class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums)):
            sum_first_part = sum_second_part = 0
            for j in range(i):
                sum_first_part += nums[j]
            for x in range(i + 1, len(nums)):
                sum_second_part += nums[x]
            if sum_first_part == sum_second_part:
                return i
        else:
            return -1

    # 优选解决方案
    def pivotIndex2(self, nums):
        res = sum(nums)
        lsum = 0
        for i, j in enumerate(nums):
            if (lsum << 1) + j == res:
                return i
            lsum += j
        return -1


def stringToIntegerList(input):
    return json.loads(input)


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
            nums = stringToIntegerList(line)

            ret = Solution().pivotIndex2(nums)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

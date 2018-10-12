# coding: utf-8

import json

'''
https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/description/

'''


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        max_num = 0
        max_index = -1
        for i, j in enumerate(nums):
            if j > max_num:
                max_num = j
                max_index = i
        if len(nums)==1:
            return max_index and max_num<<1==max_num
        elif max(nums[:max_index]+nums[max_index+1:])>>1 <= max_num:
            return max_index
        return -1

    def dominantIndex2(self, nums):
        #优化解决
        if not nums:
            return -1
        maxn = max(nums)
        for item in nums:
            if maxn < 2 * item and maxn != item:
                return -1
        return nums.index(maxn)

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

            ret = Solution().dominantIndex2(nums)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

# coding: utf-8
import json

# https://leetcode-cn.com/problems/array-partition-i/description/
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort_nums = sorted(nums)
        # sums = 0
        # for x in sort_nums[::2]:
        #     sums+=x
        return sum([x for x in sorted(nums)[::2]])


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
            nums = stringToIntegerList(line);

            ret = Solution().arrayPairSum(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

# encoding:utf8
import json

#https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i, num in enumerate(nums):
            if k < 2 or num != nums[k - 2]:
                if i != k:
                    nums[k] = num
                    k += 1
                else:
                    k += 1
        print(k)
        return k


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


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

            ret = Solution().removeDuplicates(nums)

            out = integerListToString(nums, len_of_list=ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

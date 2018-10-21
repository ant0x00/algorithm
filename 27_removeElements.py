# encoding:utf8
import json


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        begin = 0
        for e in nums:
            if e != val:
                nums[begin] = e
                begin += 1
        return begin


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
            nums = stringToIntegerList(line)
            line = next(lines)
            val = int(line)

            ret = Solution().removeElement(nums, val)

            out = integerListToString(nums, len_of_list=ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

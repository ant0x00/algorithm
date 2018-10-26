# coding: utf-8
import json


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思路：使用快慢指针
        """
        if len(nums) <= 1:
            return len(nums)
        begin = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[begin]:
                begin += 1
                nums[begin] = nums[i]
        return begin + 1

        # if len(nums) <= 1:
        #     return len(nums)
        # slow = 0
        # for i in xrange(1, len(nums)):
        #     if nums[i] != nums[slow]:
        #         slow += 1
        #         nums[slow] = nums[i]
        # return slow + 1

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

            ret = Solution().removeDuplicates(nums)

            out = integerListToString(nums, len_of_list=ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

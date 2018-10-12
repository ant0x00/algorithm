# coding: utf-8

import json

'''
https://leetcode-cn.com/problems/plus-one/description/

'''


class Solution:
    def plusOne(self, digits):
        """
        :type nums: List[int]
        :rtype: int

        """
        end = len(digits) - 1
        while end >= 0:
            digits[end] += 1
            if digits[end] == 10:
                digits[end] -= 10
                end -= 1
            else:
                return digits
        return [1] + digits


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

            ret = Solution().plusOne(nums)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

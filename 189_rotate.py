import json

# https://leetcode-cn.com/problems/rotate-array/

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n:
            k = k % n
        for i in range(n):
            if i + k < n:
                nums[i + k],nums[i] = nums[i],nums[i + k]
            else:
                nums[i + k - n] = nums[i]


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
            line = next(lines)
            k = int(line);

            ret = Solution().rotate(nums, k)

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
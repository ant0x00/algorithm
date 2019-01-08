# encoding:utf8
import json


# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
        输出: 4
        """
        return sorted(nums, reverse=True)[k - 1]

    def findKthLargest_DC(self, nums, k):
        n = len(nums)
        if k > n - 1:
            return
        index = self.quick_sort(nums, 0, n, k)
        return nums[index]

    def quick_sort(self, nums, begin, end, k):
        left = begin
        right = end - 1
        if left >= right:
            return left
        pos = self.partion(nums, left, right)
        if k == pos + 1:
            return pos
        elif k < pos + 1:
            return self.quick_sort(nums, begin, pos - 1, k)
        else:
            return self.quick_sort(nums, pos + 1, right, k)

    def partion(self, nums, begin, end):
        pass


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
            line = next(lines)
            k = int(line)

            ret = Solution().findKthLargest(nums, k)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

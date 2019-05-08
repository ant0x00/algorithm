import json

'''
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
'''


class Solution:
    def majorityElement(self, nums) -> int:  # 分治法,在leetcode提交超时了，短板
        return self.find(nums, 0, len(nums) - 1)

    def find(self, nums, begin, end):
        if begin == end:
            return nums[begin]
        else:
            mid = (begin + end) // 2
            left = self.find(nums, begin, mid)
            right = self.find(nums, mid + 1, end)
            if left == right:
                return left
            else:
                return left if nums.count(left) > nums.count(right) else right

    def majorityElement2(self, nums) -> int:  # 摩尔计数法
        count = 0
        cur = nums[0]
        for n in nums:
            if count == 0: cur = n
            if cur == n:
                count += 1
            else:
                count -= 1
        return cur

    def majorityElement1(self, nums) -> int:  # 哈希映射法
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
            if d[n] > len(nums) // 2:
                return n
        return 0

    def majorityElement0(self, nums) -> int:  # 排序取中法
        return sorted(nums)[len(nums) // 2]


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

            ret = Solution().majorityElement(nums)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

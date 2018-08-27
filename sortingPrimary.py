def buket_sorting(test_list):
    """
    桶排序，从小到大排列
    本例子可以处理 -100 到100的数
    """
    # str_input = input("请输入要排序的数字，数之间用空格隔开：")
    test_list = [x+100 for x in test_list]
    input_arr = [0 for x in range(201)]
    for num in test_list:
        input_arr[num] += 1
    for i in range(200):
        if input_arr[i] > 0: print(i-100)


def selection_sorting(test_list):
    n = len(test_list)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if test_list[j]<test_list[min]: #每一趟找出所有未排序的最小数坐标
                min = j
        test_list[i], test_list[min] = test_list[min], test_list[i] #将筛选出的最小数放在已排序数组的最后
            # print(test_list)
    print(test_list)


def bubble_sorting():
    """
    冒泡排序：
    思路：每次比较相邻的元素，如果顺序错误就交换过来
    测试用数据： 26 19 27 80 -9 17 37 25 18
    """
    str_input = input("请输入要排序的数字，数之间用空格隔开：")
    num_arr = str_input.split()
    for i in range(len(num_arr) - 1):  # 决定排序的轮次
        for j in range(len(num_arr) - i - 1):  # 决定每轮要比较的次数
            if num_arr[j] > num_arr[j + 1]:
                num_arr[j], num_arr[j + 1] = num_arr[j + 1], num_arr[j]
        print(num_arr)


def fast_sorting(test_list):
    """
    快速排序：
    思路：找一个基准元素N，然后先从右往左找第一个小于N的元素S，再由左往右找大于N的元素L，将S和L对调，再寻找，重复对调
          知道左右的坐标相遇，然后和N对调，递归。
    """
    less = []
    pivotList = []
    more = []
    if len(test_list) <= 1:
        return test_list
    else:
        pivot = test_list[0]
        for i in test_list:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        print(less + pivotList + more)
        less = fast_sorting(less)
        more = fast_sorting(more)
        return less + pivotList + more


def qsort(arr):
    """快排更简洁的写法"""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + [pivot] + qsort([x for x in arr[1:] if x >= pivot])

if __name__ == "__main__":
    test_list = [26, 19, 27, 80, -9, 17, 37, 25, 18, 93]
    # print(fast_sorting(test_list))
    # buket_sorting(test_list)
    # bubble_sorting()
    print(test_list)
    selection_sorting(test_list)

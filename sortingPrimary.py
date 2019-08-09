def buket_sorting(test_list):
    """
    桶排序，从小到大排列
    本例子可以处理 -100 到100的数
    """
    # str_input = input("请输入要排序的数字，数之间用空格隔开：")
    test_list = [x + 100 for x in test_list]
    input_arr = [0 for x in range(201)]
    for num in test_list:
        input_arr[num] += 1
    for i in range(200):
        if input_arr[i] > 0: print(i - 100)


def buket_sorting_optimize(list):
    """桶排序也可以进行优化，达到不牺牲时间复杂度，但减少空间复杂度的目的"""
    pass


def bubble_sorting():
    """
    冒泡排序：
    思路：每次比较相邻的元素，如果顺序错误就交换过来
    测试用数据： 26 19 27 80 -9 17 37 25 18
    """
    str_input = input("请输入要排序的数字，数之间用空格隔开：")
    num_arr = str_input.split()
    for i in range(len(num_arr) - 1):  # 决定排序的轮次，需要 n-1 轮
        # 决定每轮要比较的次数，第 1 轮需要比较 n-1 次，2 轮需要 n-2，最后需要 1 次
        # i 也可以理解为已经有 i 个数已排序
        for j in range(len(num_arr) - 1 - i):
            # 所以，时间复杂度为(n-1)*(n-2)*...* 1 = pow(n,2)
            if num_arr[j + 1] < num_arr[j]:  # 将最大的数冒出来，放到已排序数组的头部
                num_arr[j], num_arr[j + 1] = num_arr[j + 1], num_arr[j]
        print(num_arr)


def bubble_sorting_optimize(num_arr):
    """
    冒泡排序：
    思路：每次比较相邻的元素，如果顺序错误就交换过来
    测试用数据： 26 19 27 80 -9 17 37 25 18
    """
    len_num = len(num_arr)
    pos = 0
    endindex = len_num - 1
    for i in range(len_num - 1):  # 决定排序的轮次，需要 n-1 轮
        flag = True
        # 决定每轮要比较的次数，第 1 轮需要比较 n-1 次，2 轮需要 n-2，最后需要 1 次
        # i 也可以理解为已经有 i 个数已排序
        for j in range(0, endindex):
            # 所以，时间复杂度为(n-1)*(n-2)*...* 1 = pow(n,2)
            x = num_arr[j + 1]
            y = num_arr[j]
            if int(num_arr[j]) > int(num_arr[j + 1]):  # 将最大的数冒出来，放到已排序数组的头部；字符串比较会有问题
                num_arr[j], num_arr[j + 1] = num_arr[j + 1], num_arr[j]
                flag = False
                pos = j
        endindex = pos
        print(endindex)
        if flag:
            break
        print(num_arr)


def selection_sorting(test_list):  # 直接选择排序
    n = len(test_list)
    for i in range(n - 1):  # 比较轮次，和冒泡一样，需要n-1轮
        min = i
        for j in range(i + 1, n):
            if test_list[j] < test_list[min]:  # 每一趟找出所有未排序的最小数下标
                min = j
        test_list[i], test_list[min] = test_list[min], test_list[i]  # 将筛选出的最小数放在已排序数组的最后,只交换1次
        # print(test_list)
    print(test_list)


def insert_sorting(list):  # 插入排序，每趟循环将未排序的第一个新元素插入到已排序的正确位置
    n = len(list)
    for i in range(1, n):
        if list[i] < list[i - 1]:  # 取出尚未排序的左端数字与已排序的左边数字比较，如果左边数字较大，交换
            temp = list[i]
            index = i
            for j in range(i - 1, -1, -1):  # 依次比较已排序的数字，遇到比temp小的或者已到头，break
                if temp < list[j]:
                    list[j + 1] = list[j]
                    index = j
                else:
                    break
            list[index] = temp  # 将要插入的数字放到正确的位置
        # print(list)
    print(list)


# to do
# 堆排序（基于选择排序）等学完数据结构 堆以后完善


# 归并排序
def merge_sort(lst):  # 此方法来自维基百科：http://zh.wikipedia.org/zh/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        merged = []

        while left and right:
            # 比较两个列表第一位元素，谁小取谁
            merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))

        while left:
            merged.append(left.pop(0))

        while right:
            merged.append(right.pop(0))

        return merged

    # print(lst)
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)


def shell_sort(list):
    """
    希尔排序（基于插入排序），递减增量排序算法
    改进的地方：插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
    但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位。
    """
    n = len(list)
    # 初始步长
    gap = round(n / 2)
    print(gap)
    while gap > 0:
        for i in range(gap, n):
            # 每个步长进行插入排序
            temp = list[i]
            j = i
            # 插入排序
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        # 得到新的步长
        gap = round(gap / 2)
        print(list)
        print(gap)
    print(list)


def fast_sorting(test_list):
    # 简单易懂，但在递归调用过程中需要生成新的数组，空间复杂度高
    # 最糟糕的情况下复杂度为 O(n²)
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


def qsort2(alist, l, u):  # 单索引原地快排one index for partion
    """
    """
    if l >= u:
        return

    m = l
    for i in range(l + 1, u):
    # for i in range(l + 1, u + 1):
        if alist[i] < alist[l]:
            m += 1
            alist[m], alist[i] = alist[i], alist[m]
            # print(alist)
    # swap between m and l after partition, important!
    alist[m], alist[l] = alist[l], alist[m]
    print(m)
    print(alist)

    qsort2(alist, l, m)
    qsort2(alist, m + 1, u)
    return alist


def qsort3(arr, lower, upper):
    """
    快速排序,双索引原地快排：
    思路：找一个基准元素N，然后先从右往左找第一个小于N的元素S，再由左往右找大于N的元素L，将S和L对调，再寻找，重复对调
          知道左右的坐标相遇，然后和N对调，递归。
          这种两边推进的办法，主要是提高了分区效率，减少了swap次数
    """
    if lower >= upper: return
    pivot = arr[lower]
    left, right = lower + 1, upper
    while left <= right:
        while left <= right and arr[left] < pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left > right:
            break
        arr[left], arr[right] = arr[right], arr[left]
        print(arr)
    arr[lower], arr[right] = arr[right], arr[lower]
    print(f"{left}:{right}")
    print(arr)
    qsort3(arr, lower, right - 1)
    qsort3(arr, right + 1, upper)
    return arr


def qsort4(alist, lower, upper):  # 双索引原地快排two index for partion
    print(alist)
    if lower >= upper:
        return

    pivot = alist[lower]
    left, right = lower + 1, upper
    while left <= right:
        while left <= right and alist[left] < pivot:
            left += 1
        while left <= right and alist[right] >= pivot:
            right -= 1
        if left > right:
            break
        # swap while left <= right
        alist[left], alist[right] = alist[right], alist[left]
    # swap the smaller with pivot
    alist[lower], alist[right] = alist[right], alist[lower]

    qsort4(alist, lower, right - 1)
    qsort4(alist, right + 1, upper)


if __name__ == "__main__":
    test_list = [26, 101, 27, 80, -9, 17, 37, 18, 93, 25, 1, 2, 3,-1,-2, 888, 0]
    test_list1 = [1, 2, 3, 4, 5]
    # print(qsort2(test_list,0,len(test_list)))
    # bubble_sorting_optimize(test_list)
    # print(merge_sort(test_list))
    # print(fast_sorting(test_list))
    # buket_sorting(test_list)
    # bubble_sorting()
    # selection_sorting(test_list)
    print(qsort3(test_list, 0, len(test_list) - 1))
    # import timeit #统计函数执行时间
    # print(timeit.timeit("bubble_sorting", setup="from __main__ import bubble_sorting",number=1000))
    # insert_sorting(test_list)

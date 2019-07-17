# encoding:utf-8

def buildMaxHeap(arr):
    import math
    # for i in range(math.floor(len(arr)/2),-1,-1):#构建堆由下往上构建所以用-1
    for i in range(len(arr) // 2, -1, -1):  # 构建堆由下往上构建所以用-1
        heapify(arr, i)


def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    # 左右两个子节点和父节点比较，哪个更大，父节点与之交换
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    print(arr)
    # 依序取出元素
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        arrLen -= 1  # 每次踢掉求出的最大值
        heapify(arr, 0)
    return arr


def heap_use_python_fun(arr):
    import heapq
    heapq.heapify(arr)
    return arr


if __name__ == "__main__":
    arr = [26, 101, 27, 80, -9, 8, 22]
    # print(heapSort(arr))
    # print(heap_use_python_fun(arr))
    import heapq

    print(heapq.nsmallest(len(arr), arr))

# coding: utf-8

import json


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def stringToIntegerList(input):
    print(json.loads(input))
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    if numbers:
        for number in numbers:
            ptr.next = ListNode(number)
            ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

import sys
import io
def readlines():
    for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
        yield line.strip('\n')


if __name__ == '__main__':
    lines = readlines()
    while True:
        try:
            line = next(lines)
            l = stringToListNode(line)
        except StopIteration:
            break
def merge_sort(list):
    n = len(list)
    if n==1: return list
    def merge(left, right):
        merged = []
        while left and right:
            merged.append(left.pop(0) if left[0]<=right[0] else right.pop(0))
        while left:
            merged.append(left.pop(0))
        while right:
            merged.append(right.pop(0))
        return merged
    middle = round(n/2)
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    return merge(left, right)

if __name__ == ('__main__'):
    s = [26, 19, 27, 80, -9, 17, 37, 25, 18, 93]
    print(merge_sort(s))
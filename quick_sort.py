"""Module of sorting functions"""

def quick_sort(arr):
    """Sorting function"""
    if len(arr) > 1:
        less = []
        pivot_list = []
        more = []
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivot_list.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        arr = less + pivot_list + more
    return arr

a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
a = quick_sort(a)

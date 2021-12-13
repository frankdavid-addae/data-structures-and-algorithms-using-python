def merge_sort(py_list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sub-lists
    Conquer: Recursively sort the sub-lists created in the previous step
    Combine: Merge the sorted sub-lists create in the previous step

    Takes O(kn log n) time
    """

    if len(py_list) <= 1:
        return py_list

    left_half, right_half = split(py_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(py_list):
    """
    Divides the unsorted list at midpoint into sub-lists
    Returns two sub-lists - left and right

    Takes overall O(k log n) time
    """
    mid = len(py_list) // 2
    left = py_list[:mid]
    right = py_list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall O(n) time
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(lst):
    n = len(lst)

    if n == 0 or n == 1:
        return True

    return lst[0] < lst[1] and verify_sorted(lst[1:])


a_list = [54, 62, 93, 17, 77, 31, 44, 55, 20]
l1 = merge_sort(a_list)
print(verify_sorted(l1))






















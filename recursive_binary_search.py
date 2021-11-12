def recursive_binary_search(items, target):
    if len(items) == 0:
        return False
    else:
        midpoint = (len(items)) // 2

        if items[midpoint] == target:
            return True
        else:
            if items[midpoint] < target:
                return recursive_binary_search(items[midpoint + 1:], target)
            else:
                return recursive_binary_search(items[:midpoint], target)


def verify(result):
    print("Target found: ", result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

verify(recursive_binary_search(numbers, 12))
verify(recursive_binary_search(numbers, 5))

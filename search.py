#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if index >= len(array):
        return None
    if array[index] == item:
        return index
    return linear_search_recursive(array, item, index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item, 0, len(array)-1)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    l = 0
    r = len(array) - 1

    while (l <= r):
        middleindex = (l+r) // 2
        middlepoint = array[middleindex]

        if middlepoint > item:
            r = middleindex - 1
        elif middlepoint < item:
            l = middleindex + 1
        else:
            return middleindex
    return None

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left, right):
    # TODO: implement binary search recursively here
    middleindex = (left+right) // 2
    print(array[middleindex],middleindex)
    if left>right:
        return None
    elif array[middleindex] > item:
        return binary_search_recursive(array, item, left, middleindex - 1)
    elif item > array[middleindex]:
        return binary_search_recursive(array, item,  middleindex + 1, right)
    else:
        return middleindex
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests


# print(linear_search_recursive([1,3,5,7],3))

# print(linear_search_recursive([1,3,5,7],7))

# print(linear_search_recursive([1,3,5,7],8))

# print(linear_search_recursive(['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick'],'Nick'))

# print(linear_search_recursive(['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick'],'Winnie'))

# print(linear_search_recursive(['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick'],'Tom'))

# print(binary_search_iterative(["contribute","ide", "practice"], "ide"))

# print(binary_search_iterative(["contribute","ide", "sam", "practice"], "sam"))

if __name__ == '__main__':
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    print(binary_search(names, 'Julia'))
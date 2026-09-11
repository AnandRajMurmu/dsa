def largest_element_naive(array):
    """
    Approach:
        Sort the array and return the last element.

    Time Complexity:
        O(N log N)

    Space Complexity:
        O(N)
    """
    sorted_array = sorted(array)
    return sorted_array[-1]


def largest_element_optimal(array):
    """
    Approach:
        Traverse once while tracking the largest element.

    Time Complexity:
        O(N)

    Space Complexity:
        O(1)
    """
    largest = array[0]

    for element in array:
        if element > largest:
            largest = element

    return largest

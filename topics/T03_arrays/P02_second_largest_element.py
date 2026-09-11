def second_largest_element_naive(array):
    """
    Approach:
        Sort the array and find the second largest
        by traversing backwards and then return it.

    Time Complexity:
        O(N log N + N)

    Space Complexity:
        O(N)
    """
    sorted_array = sorted(array)

    for i in range(len(sorted_array)-1, 0, -1):
        if sorted_array[i] != sorted_array[i-1]:
            return sorted_array[i-1]

    return None

def second_largest_element_better(array):
    """
    Approach:
        Traverse twice.
        One -> Find the first largest
        Two -> Find the second largest by satisfying
               - element < first_largest
               - element > second_largest

    Time Complexity:
        O(2N)

    Space Complexity:
        O(1)
    """
    first_largest = array[0]
    second_largest = float('-inf')

    for element in array:
        if element > first_largest:
            first_largest = element

    for element in array:
        if element < first_largest and element > second_largest:
            second_largest = element

    if second_largest == float('-inf'):
        return None
    else:
        return second_largest

def second_largest_element_optimal(array):
    """
    Approach:
        Traverse once while tracking the second largest element.

    Time Complexity:
        O(N)

    Space Complexity:
        O(1)
    """
    first_largest = array[0]
    second_largest = float('-inf')

    for element in array:
        if element > first_largest:
            second_largest = first_largest
            first_largest = element

        elif element < first_largest and element > second_largest:
            second_largest = element

    if second_largest == float('-inf'):
        return None
    else:
        return second_largest

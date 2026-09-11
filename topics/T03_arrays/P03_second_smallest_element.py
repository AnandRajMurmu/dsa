def second_smallest_element_naive(array):
    """
    Approach:
        Sort the array and find the second smallest
        by traversing forward and then return it.

    Time Complexity:
        O(N log N + N)

    Space Complexity:
        O(N)
    """
    sorted_array = sorted(array)

    for i in range(0, len(sorted_array)-1, 1):
        if sorted_array[i] != sorted_array[i+1]:
            return sorted_array[i+1]

    return None

def second_smallest_element_better(array):
    """
    Approach:
        Traverse twice.
        One -> Find the first smallest
        Two -> Find the second smallest by satisfying
               - element > first_smallest
               - element < second_smallest

    Time Complexity:
        O(2N)

    Space Complexity:
        O(1)
    """
    first_smallest = array[0]
    second_smallest = float('inf')

    for element in array:
        if element < first_smallest:
            first_smallest = element

    for element in array:
        if element > first_smallest and element < second_smallest:
            second_smallest = element

    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest

def second_smallest_element_optimal(array):
    """
    Approach:
        Traverse once while tracking the second smallest element.

    Time Complexity:
        O(N)

    Space Complexity:
        O(1)
    """
    first_smallest = array[0]
    second_smallest = float('inf')

    for element in array:
        if element < first_smallest:
            second_smallest = first_smallest
            first_smallest = element

        elif element > first_smallest and element < second_smallest:
            second_smallest = element

    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest

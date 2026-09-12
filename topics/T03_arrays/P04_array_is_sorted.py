def array_is_sorted_optimal(array):
    """
    Approach:
        - If array[i] > array[i+1], return False
        - Otherwise, continue traversing
        - If no violation is found, return True

    Time Complexity:
        O(N)

    Space Complexity:
        O(1)
    """

    for i in range(0, len(array) - 1, 1):
        if array[i] > array[i + 1]:
            return False

    return True

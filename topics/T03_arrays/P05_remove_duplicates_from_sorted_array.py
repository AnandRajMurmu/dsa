def remove_duplicates_from_sorted_array_naive(array):
    """
    Approach:
        - Take empty set() --> unique_array_set
        - Iterate over array and insert (set.add()) elements in this set
        - To return array:
            - Insert the replace set values from the array till the set ends
            - Leave the remaining as it is
        - To return length of the unique array:
            - return len(unique_array_set)

    Time Complexity:
        O(Nlog N + N)

    Space Complexity:
        O(N)
    """

    unique_array_set = set()

    for i in range(len(array)):
        unique_array_set.add(array[i])

    index = 0
    for element in unique_array_set:
        array[index] = element
        index = index + 1

    return array, len(unique_array_set)


def remove_duplicates_from_sorted_array_optimal(array):
    """
    Approach:
        - Start with two pointers - left = 1 and right = 1
        - Compare (right - 1) != (right) till array ends
        - If condition is
            True:
                Do: array[right] = array[left]
            False:
                Pass
        - Return:
            array,
            left if the array is non-empty else return 0

    Time Complexity:
        O(N)

    Space Complexity:
        O(1)
    """

    left = 1

    for right in range(1, len(array)):
        if array[right - 1] != array[right]:
            array[left] = array[right]
            left += 1

    return array, 0 if (array == []) else (left)

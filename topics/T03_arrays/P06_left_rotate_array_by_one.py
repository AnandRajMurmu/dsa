def left_rotate_array_by_one_optimal(array):
    """
    Approach:
        - Store the array[0] in temp variable
        - Iterate over array from 1 to len(array)
        - Do: array[i-1] = array[i] for each iteration
        - After loop ends,
            Do: array[len(array)-1] = temp
        - Return:
            array

    Time Complexity:
        O(N)

    Space Complexity:
        O(1)
    """

    temp = array[0]

    for i in range(1, len(array)):
        array[i - 1] = array[i]

    array[len(array) - 1] = temp

    return array

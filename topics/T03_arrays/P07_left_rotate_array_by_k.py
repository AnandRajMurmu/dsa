from topics.utility import reverse_array_in_place


def left_rotate_array_by_k_naive(array, rotate):
    """
    Approach:
        - Return immediately if the array is empty.
        - Normalize the rotation count: k = rotate % N.
        - Store the first k elements in a temporary array.
        - Shift the remaining N-k elements left by k positions.
        - Copy the temporary elements into the last k positions.
        - Return the modified array.

    Time Complexity:
        O(N + k)

    Space Complexity:
        O(k)
    """

    n = len(array)

    if n == 0:
        return array

    k = rotate % n

    temp = array[0:k]

    for i in range(k, n):
        array[i - k] = array[i]

    for i in range((n - k), n):
        array[i] = temp[i - (n - k)]

    return array


def left_rotate_array_by_k_optimal(array, rotate):
    """
    Approach:
        - Return immediately if the array is empty.
        - Normalize the rotation count: k = rotate % N.
        - Reverse the first k elements.
        - Reverse the remaining N-k elements.
        - Reverse the entire array.
        - Return the modified array.

    Time Complexity:
        = O(k) + O(N-k) + O(N)
        = O(2N)

    Space Complexity:
        O(1)
    """

    n = len(array)

    if n == 0:
        return array

    k = rotate % n

    reverse_array_in_place(array, 0, k - 1)
    reverse_array_in_place(array, k, n - 1)
    reverse_array_in_place(array, 0, n - 1)

    return array

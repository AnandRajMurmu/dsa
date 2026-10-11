from topics.utility import swap_array_elements

def move_zeroes_to_end_naive(array):
    """
    Approach:
        - Create a temporary array to store non-zero elements
        - Iterate through the array and add all non-zero elements to temp
        - Copy elements from temp back to original array
        - Fill remaining positions with zeros

    Time Complexity:
        = O(N) + O(x) + O(N-x)  ,where x = Number of non-zero elements
        = O(2N)
        = O(N)

    Space Complexity:
        = O(x) --> O(N)         ,if all elements are non-zero, i.e, x = N
    """

    temp = []

    array_length = len(array)

    for element in array:
        if element != 0:
            temp.append(element)

    if len(temp) == array_length:
        return array

    for i in range(len(temp)):
        array[i] = temp[i]

    for i in range(len(temp), array_length):
        array[i] = 0

    return array

def move_zeroes_to_end_optimal(array):
    """
    Approach:
        - Use two pointers: left and right
        - Move left pointer to find the first zero
        - Move right pointer from left+1 to find first non-zero
        - Swap the zero at left with non-zero at right
        - Continue until right reaches end of array
        - All zeroes will be at the end while preserving order of non-zeros

    Time Complexity:
        = O(N)  ,single pass through array

    Space Complexity:
        = O(1)  ,only using two pointers, no extra space
    """

    left = 0
    right = 0

    for left in range(0, len(array)):
        if array[left] == 0:
            break

    for right in range(left + 1, len(array)):
        if array[right] != 0:
            swap_array_elements(array, left, right)
            left = left + 1

    return array

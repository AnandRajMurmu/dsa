def reverse_array_in_place(array, left, right):
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

def swap_array_elements(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

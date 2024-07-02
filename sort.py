def bubble_sort(array):
    num_of_iterations = 0
    n = len(array)

    print(f"initial array: {array}")
    for i in range(n):
        is_sorted = True

        for j in range(1, n-i):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                is_sorted = False
                num_of_iterations += 1
                print(array)
            
        if is_sorted:
            break
    
    print(f"\n# of iterations: {num_of_iterations}")
    return array

def insertion_sort(array):
    num_of_iterations = 0
    to_print = False
    n = len(array)

    print(f"initial array: {array}")

    for i in range(1, n):
        key_item = array[i]

        j = i-1

        while j >= 0:
            if key_item < array[j]:
                num_of_iterations += 1
                array[j+1] = array[j]
                j -= 1
                to_print = True
            else:
                break
        
        array[j+1] = key_item
        if to_print:
            print(array)
        
    print(f"\n# of iterations: {num_of_iterations}")
    return array


def merge(array_left, array_right):
    if len(array_left) == 0:
        return array_right
    
    if len(array_right) == 0:
        return array_left
    
    result = []
    left_index = right_index = 0

    while len(result) < len(array_left) + len(array_right):
        if array_left[left_index] <= array_right[right_index]:
            result.append(array_left[left_index])
            left_index += 1
        
        else:
            result.append(array_right[right_index])
            right_index += 1

        if left_index == len(array_left):
            result += array_right[right_index:]
            break
        
        if right_index == len(array_right):
            result += array_left[left_index:]
            break
    
    print(result)
    return result

def merge_sort(array):
    n = len(array)
    if n < 2:
        return array
    
    divide = n // 2
    print(f"left: {array[:divide]}, right: {array[divide:]}")
    result = merge(merge_sort(array[:divide]), merge_sort(array[divide:]))
    return result



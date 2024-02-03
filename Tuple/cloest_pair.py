import math

def closest_pair(input_tuple, k):
    
    kth_element = input_tuple[k]
    closest = None
    min_distance = float('inf')

    for i in range(len(input_tuple)):
        if i != k:
            distance = abs(input_tuple[i] - kth_element)
            if distance < min_distance:
                min_distance = distance
                closest = (kth_element, input_tuple[i])

    return closest


my_tuple = (1, 5, 9, 7, 2, 8,3)
k_index = 3

result_pair = closest_pair(my_tuple, k_index)

print(f"Closest pair to the {k_index}th index element: {result_pair}")

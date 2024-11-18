def move_zeros(lst: list):
    zero_count = []
    no_zero_list = lst
    while 0 in lst:
        zero_count.append(0)
        lst.remove(0)
                
    return lst + zero_count

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))



# def move_zeros(array):
#     for i in array:
#         if i == 0:
#             array.remove(i) # Remove the element from the array
#             array.append(i) # Append the element to the end
#     return array

# def move_zeros(arr):
#     l = [i for i in arr if isinstance(i, bool) or i!=0]
#     return l+[0]*(len(arr)-len(l))
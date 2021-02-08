arr = input()

arr = arr.split(' ')
arr = list(map(int,arr))

arr_sorted = sorted(arr)
arr_reverse = sorted(arr,reverse=True)


if arr == arr_sorted:
    print('ascending')

elif arr == arr_reverse:
    print('descending')

else:
    print('mixed')




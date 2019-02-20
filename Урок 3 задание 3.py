arr = [0, 3, 24, 2, 3, 7]
max=-1
for i in range(0, 6):
 #   print(arr[i])
    if arr[0] > arr[i]:
        (arr[0], arr[i]) = (arr[i], arr[0])

    elif arr[1] > arr[i]:
        (arr[1], arr[i]) = (arr[i], arr[1])

    elif arr[2] > arr[i]:
        (arr[2], arr[i]) = (arr[i], arr[2])

    elif arr[3] > arr[i]:
        (arr[3], arr[i]) = (arr[i], arr[3])

    elif arr[4] > arr[i]:
        (arr[4], arr[i]) = (arr[i], arr[4])
print(arr)


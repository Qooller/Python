# Бинарный поиск

def binfind(a_list,x,left,right):
    if left > right or len(a_list) == 0:
        return -1
    middle = (left + right) // 2
    if a_list[middle] == x:
        return middle
    elif (a_list[middle] < x):
        return binfind(a_list,x,middle + 1, right)
    else:         # a_list{middle} > x
        return binfind(a_list,x,left,middle - 1)


# a = range(6,16)
# for i in a:
#    print("Elem: {0}, Index: {1}".format(i, binfind(a,i,0, len(a)-1)))


# Сортировка кучей

import heapq
def heapsort(b_list):
    h = []
    for value in b_list:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

print(heapsort([1,3,5,7,9,2,6,4,8,0]))

#  %timeit heapsort(1,3,5,4,7,9,2,6,9,0)   ??? не сработал, встроеный измеритель времени, т.е. не встроеный.



# QuickSort без выбора рандомного аргумента, всегда берёться arr[0]
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return quick_sort([x for x in arr[1:] if x < arr[0]]) + \
            [arr[0]] + \
            quick_sort([x for x in arr[1:] if x >= arr[0]])
print(quick_sort([1,3,5,10,8,9,2,4,6,0,7,12,11]))
import pygameSortVisualization as sv
import random as rd

#array size
size = 0
if size <= 0:
    size = sv.DEFAULT_ARR_SIZE

# animation loop
arr = rd.sample(range(1,size+1),size)
for i in range(0,size-1):
    min = i
    for j in range(i+1,size):
        sv.display_flip(arr, min, j, i)
        if arr[min]>arr[j]:
            min = j
            sv.display_flip(arr, min, -1, i)
    else:
        if min != size-1:
            sv.display_flip(arr, min, -1, i)
        arr[i], arr[min] = arr[min], arr[i]
        sv.display_flip(arr, i)

sv.display_flip(arr)
sv.check_sort(arr)
sv.display_flip(arr)
sv.end_screen()
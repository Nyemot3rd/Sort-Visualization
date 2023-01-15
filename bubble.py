import pygameSortVisualization as sv
import random as rd

#array size
size = 0
if size <= 0:
    size = sv.DEFAULT_ARR_SIZE
arr = rd.sample(range(1,size+1),size)

# animation loop
for i in range(size):
    for j in range(1,size-i):
        sv.display_flip(arr, j-1, j, size-i)
        if arr[j-1]>arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            sv.display_flip(arr, j, j-1, size-i)
        else:
            sv.display_flip(arr, j, -1, size-i)

sv.display_flip(arr)
sv.check_sort(arr)
sv.display_flip(arr)
sv.end_screen()
import pygameSortVisualization as sv
import random as rd

#array size
size = 0
if size <= 0:
    size = sv.DEFAULT_ARR_SIZE
arr = rd.sample(range(1,size+1),size)

# animation loop
for i in range(1,size):
    for j in range(i,0,-1):
        sv.display_flip(arr, j, j-1, i)
        if arr[j]<arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            sv.display_flip(arr, j-1, j, i)
        else:
            sv.display_flip(arr, j, j, i)
            break

sv.display_flip(arr)
sv.check_sort(arr)
sv.display_flip(arr)
sv.end_screen()
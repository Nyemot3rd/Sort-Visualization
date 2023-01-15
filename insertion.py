import pygameSortVisualization as sv
import random as rd

#array size
size = 0
if size <= 0:
    size = sv.DEFAULT_ARR_SIZE

# animation loop
arr = rd.sample(range(1,size+1),size)
for i in range(1,size):
    pick = arr[i]
    for j in range(i,0,-1):
        sv.display_flip(arr, -1, j-1, i)
        if pick<arr[j-1]:
            arr[j] = arr[j-1]
            sv.display_flip(arr, j, j-1, i)
        else:
            arr[j] = pick
            sv.display_flip(arr, j, -1, i)
            break
    else:
        arr[0] = pick
        sv.display_flip(arr, j, -1, i)

sv.display_flip(arr)
sv.check_sort(arr)
sv.display_flip(arr)
sv.end_screen()
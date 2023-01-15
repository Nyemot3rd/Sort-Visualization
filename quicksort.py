import pygameSortVisualization as sv
import random as rd

#array size
size = 15
if size <= 0:
    size = sv.DEFAULT_ARR_SIZE
arr = rd.sample(range(1,size+1),size)

#quicksort function
def quicksort(l, r):
    if l>=r:
        return
    pivot = arr[l]
    i = l+1
    j = r
    count = 25
    while i<=j and count>0:
        sv.display_flip(arr,i,j,l)
        while j>=l+1 and arr[j]>=pivot:
            j-=1
            if j>l+1:
                sv.display_flip(arr,i,j,l)
        sv.display_flip(arr,j,i,l)
        while i<=r and arr[i]<=pivot:
            i+=1
            if i<r:
                sv.display_flip(arr,j,i,l)
        if i<j:
            sv.display_flip(arr,[i,j],-1,l)
            arr[i], arr[j] = arr[j], arr[i]
            sv.display_flip(arr,[i,j],-1,l)
    sv.display_flip(arr,[l,j])
    arr[l], arr[j] = arr[j], arr[l]
    sv.display_flip(arr,[l,j])
    quicksort(l, j-1)
    quicksort(j+1, r)
    
# animation loop
quicksort(0,len(arr)-1)

sv.display_flip(arr)
sv.check_sort(arr)
sv.display_flip(arr)
sv.end_screen()
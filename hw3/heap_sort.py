def parent(i):
    return (i-1)//2

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def is_max_heap(arr, i=0, key=lambda x: x):
    for j in range(i+1, len(arr)):
        p_idx=parent(j)
        if p_idx>=i:
            if key(arr[parent(j)])<key(arr[j]):
                return False
    return True
            
#בדיקה
print(is_max_heap([10, 8, 9, 7, 6]))
print(is_max_heap([10, 5, 9, 8, 6]))+


def max_heapify(arr, i, heap_size, key=lambda x: x):
    left_current=left(i)
    right_current=right(i)
    current=i
    #מציאת הערך הגדול מבין האבא ושני הבנים
    if left_current<heap_size and key(arr[left_current])>key(arr[current]):
        current=left_current

    if right_current<heap_size and key(arr[right_current])>key(arr[current]):
        current=right_current

    if current!=i:
        arr[i], arr[current]=arr[current], arr[i]
        max_heapify(arr,current, heap_size, key)

def build_max_heap(arr, key=lambda x: x):
    heap_size=len(arr)
    i=heap_size//2
    for j in range(i,-1,-1):
        max_heapify(arr, j,heap_size,key)

def heap_sort(arr, key=lambda x: x):
    build_max_heap(arr,key)
    for i in range(len(arr)-1, 0,-1):
        arr[i], arr[0]=arr[0],arr[i]
        max_heapify(arr,0,i,key)

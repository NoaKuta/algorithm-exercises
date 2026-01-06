def partition(arr, left, right, key):
    pivot=arr[right]
    i=left-1
    for j in range(left, right):
        if key(arr[j])<key(pivot):
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    i=i+1
    arr[right], arr[i]=arr[i],arr[right]
    return i

def quick_kth(arr, left, right, k, key = lambda x: x):
    if left==right:
        return arr[right]
    pivot=partition(arr, left, right, key)
    if k==pivot:
        return arr[pivot]
    if k<pivot:
        return quick_kth(arr, left, pivot-1, k, key)
    if k>pivot:
        return quick_kth(arr, pivot+1, right, k, key)



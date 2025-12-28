def merge(a, b, key):
    result = []
    i = 0
    j = 0
    
    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
            
    while i < len(a):
        result.append(a[i])
        i += 1
        
    while j < len(b):
        result.append(b[j])
        j += 1
        
    return result

if __name__ == "__main__":
    list_a = [1, 4, 7]
    list_b = [2, 3, 5, 8, 9]
    
    final_list = merge(list_a, list_b, key=lambda x: x)
    print(final_list)

def is_sorted(a, key):
    for i in range(len(a) - 1):
        if key(a[i]) > key(a[i+1]):
            return False
    return True
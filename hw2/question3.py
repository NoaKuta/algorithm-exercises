def is_sorted(a, key):
    for i in range(len(a) - 1):
        if key(a[i]) > key(a[i+1]):
            return False
    return True

def merge(a, b, key):
    if not is_sorted(a, key) or not is_sorted(b, key):
        return None
    
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    
    result.extend(a[i:])
    result.extend(b[j:])
    return result

def merge_sorted_lists(lists, key):
    if not lists:
        return []
    if len(lists) == 1:
        return lists[0]
    
    merged_res = lists[0]
    for i in range(1, len(lists)):
        merged_res = merge(merged_res, lists[i], key)
        if merged_res is None:
            return None
            
    return merged_res
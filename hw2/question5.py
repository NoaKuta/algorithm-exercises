def dual_pivot_partition(a, key):
    if key(a[0]) > key(a[-1]):
        a[0], a[-1] = a[-1], a[0]
    
    p1_val = key(a[0])
    p2_val = key(a[-1])
    
    lt = 1
    gt = len(a) - 2
    i = 1 
    
    while i <= gt:
        if key(a[i]) < p1_val:
            a[i], a[lt] = a[lt], a[i]
            lt += 1
        
        elif key(a[i]) > p2_val:
            while key(a[gt]) > p2_val and i < gt:
                gt -= 1
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
            if key(a[i]) < p1_val:
                a[i], a[lt] = a[lt], a[i]
                lt += 1
        i += 1
    
    a[0], a[lt-1] = a[lt-1], a[0]
    a[-1], a[gt+1] = a[gt+1], a[-1]
    
    return lt - 1, gt + 1
numbers = [24, 8, 42, 75, 2, 16, 53, 31]

p1_idx, p2_idx = dual_pivot_partition(numbers, lambda x: x)
print("המערך לאחר החלוקה:", numbers)
print("אינדקס ציר ראשון:", p1_idx)
print("אינדקס ציר שני:", p2_idx)
def lomuto_partition(a, key):
    # בחירת הציר כאיבר האחרון
    pivot_value = key(a[-1])
    i = 0
    
    for j in range(len(a) - 1):
        # אם האיבר הנוכחי קטן מהציר, "נאסוף" אותו שמאלה
        if key(a[j]) <= pivot_value:
            a[i], a[j] = a[j], a[i]
            i += 1
            
    # החלפת הציר למקומו הקבוע
    a[i], a[-1] = a[-1], a[i]
    return i

def hoare_partition(a, key):
    # נבחר את האיבר הראשון כציר
    pivot_value = key(a[0])
    
    # נתחיל את הסמנים מחוץ לטווח (נשתמש בקידום לפני הבדיקה)
    i = -1
    j = len(a)
    
    while True:
        # נקדם את הסמן השמאלי ימינה כל עוד האיבר קטן מהציר
        i += 1
        while key(a[i]) < pivot_value:
            i += 1
            
        # נקדם את הסמן הימני שמאלה כל עוד האיבר גדול מהציר
        j -= 1
        while key(a[j]) > pivot_value:
            j -= 1
            
        # אם הסמנים נפגשו או חצו זה את זה, נחזיר את j
        if i >= j:
            return j
            
        # אם הגענו לכאן, סימן שמצאנו שני איברים שצריך להחליף
        a[i], a[j] = a[j], a[i]
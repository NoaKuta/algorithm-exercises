from random_tuples import create_random_tuples

def find_min(a, key=lambda x: x):
   
    if not a:
        return None, None

    min_item = a[0]
    max_item = a[0]
    
    min_key = key(min_item)
    max_key = key(max_item)

    for item in a[1:]:
        current_key = key(item)
        
        if current_key < min_key:
            min_key = current_key
            min_item = item
            
        if current_key > max_key:
            max_key = current_key
            max_item = item
            
    return min_item, max_item

def insertion_sort(a, key=lambda x: x):

    for j in range(1, len(a)):
        current_item = a[j]
        current_key = key(current_item)
        i = j - 1
        
        while i >= 0 and current_key < key(a[i]):
            a[i + 1] = a[i] 
            i = i - 1
            
        a[i + 1] = current_item

if __name__ == "__main__":
    
    ARRAY_SIZE = 100
    LIST_SIZE_FOR_DEMO = 10
    TUPLE_SIZE = 3
    TUPLE_TYPES = [int, float, str]
    
    data_array = create_random_tuples(ARRAY_SIZE, TUPLE_SIZE, TUPLE_TYPES)
    
    key_function = lambda x: x[2]
    
    min_tuple, max_tuple = find_min(data_array, key=key_function)
    
    print(f"min=<{min_tuple[2]}>")
    print(f"max=<{max_tuple[2]}>")
    


    print("--- מיון Insertion Sort על 3 רשימות שונות ---")
    #מיון לפי INDEX 0
    list1 = create_random_tuples(LIST_SIZE_FOR_DEMO, TUPLE_SIZE, TUPLE_TYPES)
    insertion_sort(list1, key=lambda x: x[0])
    print("מיון לפי אינטגר:", list1)
   # מיון לפי INDEX 1
    list2 = create_random_tuples(LIST_SIZE_FOR_DEMO, TUPLE_SIZE, TUPLE_TYPES)
    insertion_sort(list2, key=lambda x: x[1])
    print("מיון לפי פלואט:", list2)
   # מיון לפי INDEX 2
    list3 = create_random_tuples(LIST_SIZE_FOR_DEMO, TUPLE_SIZE, TUPLE_TYPES)
    insertion_sort(list3, key=lambda x: x[2])
    print("מיון לפי מחרוזת:", list3)

import random
import string

def create_random_tuples(n, k, types=None):
    if types is None:
        types = [int] * k 

    if len(types) != k:
        raise ValueError("Length of types must be equal to k")

    def random_element(t):
        if t == int:
            return random.randint(0, 1000)
        elif t == float:
            return random.uniform(0.0, 1000.0)
        elif t == str:
            return ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        else:
            raise ValueError(f"Unsupported type: {t}")

    result = []
    for _ in range(n):
        tuple_elements = tuple(random_element(t) for t in types)
        result.append(tuple_elements)

    return result

if __name__ == "__main__":
    tuples_list = create_random_tuples(5, 3, [int, float, str])

    print("--- Generated List ---")
    for t in tuples_list:
        print(t)

    sort_by_int = sorted(tuples_list, key=lambda x: x[0])
    print("\n--- Sorted by Integer (Index 0) ---")
    for t in sort_by_int:
        print(t)

    sort_by_float = sorted(tuples_list, key=lambda x: x[1])
    print("\n--- Sorted by Float (Index 1) ---")
    for t in sort_by_float:
        print(t)

    sort_by_str = sorted(tuples_list, key=lambda x: x[2])
    print("\n--- Sorted by String (Index 2) ---")
    for t in sort_by_str:
        print(t)
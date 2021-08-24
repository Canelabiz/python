import timeit
from string import ascii_lowercase


numbers = [1, 2, 3, 4, 5, 6]
for n in numbers:
    print(n)

### create list from range(10)
l_range = []
for n in range(10):
    l_range.append(n)

# List comprehension
l_range = [n for n in range(10)]

###

# integer split into digits
n = 123456
[int(d) for d in str(n)]

# join array of split digits
n = [1, 2, 3, 4, 5, 6]
int("".join(str(d) for d in n))


###
fruits = ["Apple", "Banana", "Pear", "Orange"]

for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")


### Dict comprehension
{
    i: fruit for i, fruit in enumerate(fruits)
}  # -> {0: 'Apple', 1: 'Banana', 2: 'Pear', 3: 'Orange'}
###


# splitting a string into components
def stringsplitting(string: str) -> list:
    return [character for character in string]


print(stringsplitting("this is a string"))
# print("this is a string".split())

# squares
def using_for_loop():
    squares = []
    for i in range(10):
        squares.append(i * i)


# new_list = [expression for member in iterable]
def using_list_comprehension():
    squares = [i * i for i in range(10)]


def for_loop_conditional():
    even_sqrs = []
    for i in range(10):
        if i ** 2 % 2 == 0:
            even_sqrs.append(i ** 2)
    return even_sqrs


print(for_loop_conditional())


# new_list = [expression for member in iterable (if conditional)]
def comprehension_w_if_conditionals():
    return [i ** 2 for i in range(10) if i ** 2 % 2 == 0]


print(comprehension_w_if_conditionals())


# new_list = [expression if condition this else expression for member in iterable]
def comprehension_w_if_else_conditional():
    return [i ** 2 if i % 2 == 0 else i * 2 for i in range(10)]


print(comprehension_w_if_else_conditional())


# Flatten nested array

array_3d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def using_forloop():
    flat = []
    for sub_array in array_3d:
        for item in sub_array:
            flat.append(item)
    return flat


def using_comprehension():
    return [item for sub_array in array_3d for item in sub_array]


array_xd = [[]]

flat_list = [item for sublist in array_xd for item in sublist]


"""
print(f"3D Array: {array_3d}")
print("for-loop: ", timeit.timeit(using_forloop, number=100))
# print('1D Array using for-loop: ', using_forloop())
print("comprehension: ", timeit.timeit(using_comprehension, number=100))
# print('1D Arrayy using comprehension: ', using_comprehension())
"""

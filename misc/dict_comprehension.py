dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

d_keys = dict1.keys()  # Put all keys of 'dict1' in a list
d_values = dict1.values()  # Put all values of 'dict1' in a list
d_items = dict1.items()  # Put all key-value pairs in a list of tuples

# Dict Comprehension

# dict_variable = {key: value for (key, value) in dictonary.items()}

double_dict1 = {k: v * 2 for (k, v) in dict1.items()}
print(double_dict1)
{'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}

vowels = ["a", "e", "i", "o", "u"]


# dict comprehension
v = {v: n for n, v in enumerate(["a", "e", "i", "o", "u"], 1)}
n = {n: v for n, v in enumerate(["a", "e", "i", "o", "u"], 1)}

{v: n for n, v in enumerate(vowels, 1)}
{n: v for n, v in enumerate(vowels, 1)}

print("v: ", v)  # {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
print("n: ", n)  # {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}


# iterate through dictionary via keys directly
for key in {"color": "blue", "fruit": "apple", "pet": "dog"}:
    print(key)


def letter_count(s):
    return {x: s.count(x) for x in sorted(set(s))}

    # for x in sorted(set(s)):
    #         print(x, s.count(x))


print(letter_count("codewars"))
print(letter_count("activity"))
print(letter_count("arithmetics"))
print(letter_count("traveller"))
print(letter_count("daydreamer"))

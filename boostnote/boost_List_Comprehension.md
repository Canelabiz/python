# Python List Comprehension

List comprehensions one of many ways of creating lists

using a for-loop:

```python
def using_for_loop():
    squares = []
    for i in range(10):
        squares.append(i * i)
```

can also be written:

```python
def using_list_comprehension():
    squares = [i * i for i in range(10)]
```

Conditionals

```python
def for_loop_conditional():
    even_sqrs = []
    for i in range(10):
        if i ** 2 % 2 == 0:
            even_sqrs.append(i ** 2)
    return even_sqrs
```

```python
# new_list = [expression for member in iterable (if conditional)]
def comprehension_w_conditionals():
    return [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
```

---
#### Iterating over a dictionary

```python
dct = {i: colors[i] for i, color in enumerate(colors)}
```

```python
ps = ""
for key in order_key:
    ps += symbol[key]()
```

```python
return "".join(symbol[key]() for key in order_key)
```

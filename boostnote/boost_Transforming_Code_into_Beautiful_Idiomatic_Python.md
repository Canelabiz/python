# [Transforming Code into Beautiful, Idiomatic Python](https://youtu.be/OSGv2VnC0go)

### Looping over a range of numbers

Ugly

```python
for i in [0, 1, 2, 3, 4, 5]:
    print(i**2)
```

Pretty

```python
for i in range(6):
    print(i**2)
```

### Looping over a collection

Collection

```python
colors = ['red', 'green', 'blue', 'yellow']
```

Ugly

```python
for i in range(len(colors)):
    print(colors[i])
```

Pretty

```python
for color in colors:
    print(color)
```

### Looping backwards

Ugly

```python
for i in range(len(colors)-1, -1, -1):
    print(colors[i])
```

Pretty

```python
for color in reversed(colors):
    print(color)
```

### Looping over a collection and indices

Ugly

```python
for i in range(len(colors)):
    print(i, '-->', colors[i])
```

Pretty

```python
for i,  color in enumerate(colors):
    print(i, '-->', colors[i])
```

### Looping over a dictionary

```python
dct = {i: colors[i] for i, color in enumerate(colors)}
```

### Looping over two collections

```python
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']
```

```python
n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '-->', colors[i])
```

pythonic

```python
for name, color in zip(n ames, colors):
    print(f"{name} --> {color})
```

```python
for name, color in izip(names, colors):
print(f"{name} --> {color})
```

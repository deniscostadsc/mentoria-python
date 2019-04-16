# Data structures

## list

```python
foo = []
bar = list([iterable])

foo.append(x)
foo.extend(iterable)
foo.insert(i, x)
foo.remove(x)
foo.pop([x])
foo.clear()
foo.index(x, [start, [end]])
foo.count(x)
foo.sort(key=None, reverse=False)
foo.copy()

stack.append(x)
stack.pop(x)

from collections import deque
queue = deque([iterable])
queue.append(x)
queue.popleft()


bar = [i for i in foo]
del bar[i]
del bar[:]
```

## tuple

```python
foo = ()
bar = x,
foobar = tuple()
```

## set

```python
foo = {x, y, z}
bar = set([iterable])

foo - bar
foo | bar
foo & bar
foo ^ bar

foobar = {x for x in foo}
```

## dict

```python
foo = dict(one=1, two=2, three=3)
foo = {'one': 1, 'two': 2, 'three': 3}
foo = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
foo = dict([('two', 2), ('one', 1), ('three', 3)])
foo = dict({'three': 3, 'one': 1, 'two': 2})

foo[i]
foo[i] = x
```

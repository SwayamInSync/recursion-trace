# Recursion Trace

## Overview
`recursion_trace` is a Python package that provides a decorator to trace recursive function calls. It generates a visual recursion tree using Graphviz, making it easier to understand and debug recursive algorithms.

## Features
- Trace single and mutual recursion.
- Generate a Graphviz plot to visualize the recursion tree.
- Capture function arguments, return values, and recursion depth.
- Render Animation demonstrating construction of recursion-tree

## Installation
- Download the [graphviz](https://graphviz.org/download/) for the respective system (Windows/Mac/Linux)
```bash
pip install recursion-trace
```

## Usage
- Decorate the in-usage recursive functions with the decorator `@trace_recursion`

### Example: Merge Sort with Animation
```python
from recursion_trace import trace_recursion, show_recursion_tree

@trace_recursion  # use the decorator to trace the recursion stack
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    L = merge_sort(left_half)
    R = merge_sort(right_half)
    return merge(L, R)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == '__main__':
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    sorted_arr = merge_sort(arr)
    show_recursion_tree(make_animation=True)  # display recursion tree
    # setting make_animation=True also renders an animation of recursion-tree construction
```
### Output:
<img width="1374" alt="Screenshot 2023-09-18 at 10 42 54 AM" src="https://github.com/practice404/recursion-trace/assets/74960567/9197331d-51a0-4b85-a37d-0f0ea6311aa0">


https://github.com/practice404/recursion-trace/assets/74960567/f6fbd987-5b77-42c8-9e3a-25096a8f4466



### Example: Mutual Recursive Functions
```python
from recursion_trace import trace_recursion, show_recursion_tree

@trace_recursion  # use the decorator to trace the recursion stack
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

@trace_recursion  # use the decorator to trace the recursion stack
def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)

if __name__ == '__main__':
    is_even(4)
    show_recursion_tree()
```
### Output:
<img width="280" alt="Screenshot 2023-09-18 at 11 55 59 AM" src="https://github.com/practice404/recursion-trace/assets/74960567/963fb800-6dc6-418e-8016-40293a6f829b">

## Author
[Swayam Singh](https://twitter.com/_s_w_a_y_a_m_)

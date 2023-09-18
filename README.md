# Recursion Trace

## Overview
`recursion_trace` is a Python package that provides a decorator to trace recursive function calls. It generates a visual recursion tree using Graphviz, making it easier to understand and debug recursive algorithms.

## Features
- Trace single and mutual recursion.
- Generate a Graphviz plot to visualize the recursion tree.
- Capture function arguments, return values, and recursion depth.

## Installation
```bash
pip install recursion_trace
```

## Usage

```python
from recursion_trace import trace_recursion, show_recursion_tree

@trace_recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

result = factorial(5)

# Show the recursion tree
show_recursion_tree(factorial.logs)
```
## Dependencies
- graphviz

## Author
[Swayam Singh](https://twitter.com/_s_w_a_y_a_m_)

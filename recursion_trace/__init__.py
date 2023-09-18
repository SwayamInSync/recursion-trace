from functools import wraps
from graphviz import Digraph


def trace_recursion(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        wrapper.logs = getattr(wrapper, 'logs', [])
        wrapper.call_stack = getattr(wrapper, 'call_stack', [])
        wrapper.node_count = getattr(wrapper, 'node_count', 0)

        current_node = str(wrapper.node_count)
        wrapper.node_count += 1
        depth = len(wrapper.call_stack)

        log_entry = {
            'depth': depth,
            'function': f.__name__,
            'args': args,
            'kwargs': kwargs,
            'return': None,
            'node': current_node
        }
        wrapper.logs.append(log_entry)

        wrapper.call_stack.append(current_node)

        result = f(*args, **kwargs)

        log_entry['return'] = result

        if depth > 0:
            parent_node = wrapper.call_stack[-2]

        wrapper.call_stack.pop()

        return result

    return wrapper


def show_recursion_tree(logs):
    dot = Digraph(comment='Recursion Tree')
    for log in logs:
        current_node = log['node']
        dot.node(current_node, f"{log['function']}({log['args'], log['kwargs']})\nReturn: {log['return']}")

        if log['depth'] > 0:
            parent_node = [entry['node'] for entry in reversed(logs) if entry['depth'] == log['depth'] - 1][0]
            dot.edge(parent_node, current_node)

    # Save or render the Graphviz object
    dot.render('recursion_tree.gv', view=True)

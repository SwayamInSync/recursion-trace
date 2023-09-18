from functools import wraps
from graphviz import Digraph


def trace_recursion(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # Temporarily update the global function to point to the wrapper
        original_global_function = f.__globals__.get(f.__name__)
        f.__globals__[f.__name__] = wrapper

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
            log_entry['parent_node'] = parent_node

        wrapper.call_stack.pop()

        # Restore the original global function
        if original_global_function is not None:
            f.__globals__[f.__name__] = original_global_function

        return result

    return wrapper


def show_recursion_tree(logs):
    dot = Digraph(comment='Recursion Tree')

    # Determine the total depth of the recursion tree
    max_depth = max(log['depth'] for log in logs)

    # Set the label for the graph
    dot.graph_attr['label'] = f"Total Depth: {max_depth}"
    dot.graph_attr['labelloc'] = 't'  # Position at the top
    dot.graph_attr['labeljust'] = 'r'  # Justify to the right

    for log in logs:
        current_node = log['node']
        dot.node(current_node, f"{log['function']}({log['args'], log['kwargs']})\nReturn: {log['return']}")

        parent_node = log.get('parent_node')
        if parent_node is not None:
            dot.edge(parent_node, current_node)

    dot.render('recursion_tree.gv', view=True)

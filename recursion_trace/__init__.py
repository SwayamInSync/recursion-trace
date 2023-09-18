from functools import wraps
from graphviz import Digraph

# Global context for logging and tracking
global_context = {
    'logs': [],
    'node_count': 0,
    'call_stack': []
}


def trace_recursion(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        current_node = str(global_context['node_count'])
        global_context['node_count'] += 1
        depth = len(global_context['call_stack'])

        log_entry = {
            'depth': depth,
            'function': f.__name__,
            'args': args,
            'kwargs': kwargs,
            'return': None,
            'node': current_node,
            'parent_node': global_context['call_stack'][-1] if global_context['call_stack'] else None
        }
        global_context['logs'].append(log_entry)

        global_context['call_stack'].append(current_node)

        result = f(*args, **kwargs)

        log_entry['return'] = result

        global_context['call_stack'].pop()

        return result

    return wrapper


def show_recursion_tree():
    dot = Digraph(comment='Recursion Tree')
    dot.graph_attr['labelloc'] = 't'
    dot.graph_attr['labeljust'] = 'r'

    max_depth = max(log['depth'] for log in global_context['logs'])
    dot.graph_attr['label'] = f"Total Depth: {max_depth}"

    for log in global_context['logs']:
        current_node = log['node']
        dot.node(current_node, f"{log['function']}({log['args'], log['kwargs']})\nReturn: {log['return']}")

        parent_node = log.get('parent_node')
        if parent_node is not None:
            dot.edge(parent_node, current_node)

    dot.render('recursion_tree.gv', view=True)
    global_context['logs'] = []
    global_context['node_count'] = 0
    global_context['call_stack'] = []

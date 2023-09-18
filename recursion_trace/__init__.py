from functools import wraps
from graphviz import Digraph
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pydot
import networkx as nx
from matplotlib.animation import FFMpegWriter  # Import the writer

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


def generate_dot(logs):
    dot = Digraph(comment='Recursion Tree')
    for log in logs:
        current_node = log['node']
        label = f"{log['function']}{log['args'], log['kwargs']}\nReturn: {log['return']}"
        dot.node(current_node, label, shape='ellipse')
        parent_node = log.get('parent_node')
        if parent_node is not None:
            dot.edge(parent_node, current_node)

    return dot.source


def animate(i):
    plt.clf()
    dot_string = generate_dot(global_context['logs'][:i + 1])
    pydot_graph = pydot.graph_from_dot_data(dot_string)[0]
    nx_graph = nx.drawing.nx_pydot.from_pydot(pydot_graph)

    # Create a dictionary of labels
    labels = {}
    for log in global_context['logs'][:i + 1]:
        current_node = log['node']
        label = f"{log['function']}{log['args'], log['kwargs']}\nReturn: {log['return']}"
        labels[current_node] = label

    pos = nx.drawing.nx_pydot.graphviz_layout(nx_graph, prog="dot")
    nx.draw(nx_graph, pos, with_labels=True, labels=labels, node_size=700, node_color="lightblue", font_size=10)


def show_recursion_tree():
    fig, ax = plt.subplots(figsize=(14, 12))
    ani = animation.FuncAnimation(fig, animate, frames=len(global_context['logs']), repeat=False,
                                  interval=2000)  # 2-second interval

    writer = FFMpegWriter(fps=1, metadata=dict(artist='Me'), bitrate=1800)  # Use FFMpegWriter
    ani.save('recursion_tree.mp4', writer=writer)  # Save as MP4

    dot = Digraph(comment='Recursion Tree')
    dot.graph_attr['labelloc'] = 't'
    dot.graph_attr['labeljust'] = 'r'
    max_depth = max(log['depth'] for log in global_context['logs'])
    dot.graph_attr['label'] = f"Total Depth: {max_depth}\nTotal Nodes: {len(global_context['logs'])}"

    for log in global_context['logs']:
        current_node = log['node']
        dot.node(current_node, f"{log['function']}{log['args'], log['kwargs']}\nReturn: {log['return']}")

        parent_node = log.get('parent_node')
        if parent_node is not None:
            dot.edge(parent_node, current_node)

    dot.render('recursion_tree', view=True, format="png")
    global_context['logs'] = []
    global_context['node_count'] = 0
    global_context['call_stack'] = []

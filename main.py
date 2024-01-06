import pydot
import json

def create_mind_map(title = 'root', categories):
    # Initialize the graph
    graph = pydot.Dot(graph_type='digraph', rankdir="LR", shape="rectangle")

    # Increase DPI for better image quality
    graph.set_graph_defaults(dpi="500")

    # Create the root node for the mind map
    root = pydot.Node(title, style="filled", fillcolor="white", shape="rectangle", fontname="bold")
    graph.add_node(root)

    # Add categories and subcategories to the graph
    for category, subcategories in categories.items():
        # Create and add the category node
        category_node = pydot.Node(category, style="filled", 
                                   fillcolor="white", shape="rectangle", 
                                   fontname="bold", fontcolor="#638c61",
                                   color="#b1c5b0")
        graph.add_node(category_node)
        graph.add_edge(pydot.Edge(root, category_node))

        for subcategory in subcategories:
            # PyDot will treat colon as a special character, so we need to escape it
            subcategory = subcategory.replace(":", "-")
            # Create and add the subcategory node
            subcategory_node = pydot.Node(subcategory, style="filled", 
                                          fillcolor="white", shape="rectangle",
                                          fontcolor="#365674", color="#9aaab9")
            graph.add_node(subcategory_node)
            graph.add_edge(pydot.Edge(category_node, subcategory_node))

    return graph

if __name__ == "__main__":
    # Load the categories from the JSON file
    with open("faas.json", "r") as f:
        categories = json.load(f)
    # Create the mind map
    mind_map = create_mind_map("Faas", categories)
    # Save the mind map as a PNG image
    mind_map.write_png("mind_map.png")


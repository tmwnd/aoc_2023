def part_one():
    import re

    with open("./data/08_one.txt") as f:
        data = f.readlines()

    nodes = {}
    instructions = [0 if instruction == "L" else 1 for instruction in data[0].strip()]
    
    for line in data[2:]:
        node, l, r = re.findall("\w+", line)
        nodes[node] = [l, r]

    current_node = "AAA"
    result = 0

    while current_node != "ZZZ":
        for instruction in instructions:
            current_node = nodes[current_node][instruction]
            result += 1
    
    print(result)

def part_two():
    import re
    import numpy as np

    with open("./data/08_one.txt") as f:
        data = f.readlines()

    nodes = {}
    instructions = [0 if instruction == "L" else 1 for instruction in data[0].strip()]
    
    current_nodes = set()  
    for line in data[2:]:
        node, l, r = re.findall("\w+", line)
        nodes[node] = [l, r]

        if node.endswith("A"):
            current_nodes.add(node)

    result = []
    for current_node in current_nodes:
        result.append(0)

        while not current_node.endswith("Z"):
            for instruction in instructions:
                current_node = nodes[current_node][instruction]
                result[-1] += 1
    
    print(np.lcm.reduce(result))

if __name__ == "__main__":
    part_one()
    part_two()
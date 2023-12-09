def part_one():
    import re
    import numpy as np

    with open("./data/09_one.txt") as f:
        data = f.readlines()
    
    def diff(x):
        dx = np.diff(x)
        
        if all(dx == dx[0]):
            return x[-1] + dx[-1]
        
        return x[-1] + diff(dx)
    
    result = 0
    for line in data:
        result += diff(np.array(re.findall("-?\d+", line), dtype=int))
    
    print(result)

def part_two():
    import re
    import numpy as np

    with open("./data/09_one.txt") as f:
        data = f.readlines()
    
    def diff(x):
        dx = np.diff(x)
        
        if all(dx == dx[0]):
            return x[0] - dx[0]
        
        return x[0] - diff(dx)
    
    result = 0
    for line in data:
        result += diff(np.array(re.findall("-?\d+", line), dtype=int))
    
    print(result)

if __name__ == "__main__":
    part_one()
    part_two()
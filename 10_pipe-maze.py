def part_one():
    with open("./data/10_one.txt") as f:
        data = [[c for c in line.strip()] for line in f.readlines()]

    def find_start():
        for i, line in enumerate(data):
            for j, c in enumerate(line):
                if c == "S":
                    return i, j
    
    i, j = find_start()

    def get_direction(c, d):
        if d == "n":
            if c == "|": return "n"
            if c == "7": return "w"
            if c == "F": return "o"
        if d == "o":
            if c == "-": return "o"
            if c == "J": return "n"
            if c == "7": return "s"
        if d == "s":
            if c == "|": return "s"
            if c == "L": return "o"
            if c == "J": return "w"
        if d == "w":
            if c == "-": return "w"
            if c == "L": return "n"
            if c == "F": return "s"
    
    if data[i+1][j] in ["|", "L", "J"]:
        i += 1
        d = "s"
    elif data[i][j+1] in ["-", "J", "7"]:
        j += 1
        d = "o"
    elif data[i-1][j] in ["|", "7", "F"]:
        i -= 1
        d = "n"
    elif data[i][j-1] in ["-", "L", "F"]:
        j -= 1
        d = "w"
    
    result = 1
    while data[i][j] != "S":
        d = get_direction(data[i][j], d)

        if d == "n": i -= 1
        elif d == "o": j += 1
        elif d == "s": i += 1
        elif d == "w": j -= 1

        result += 1
    
    print(result // 2)

def part_two():
    import sys

    with open("./data/10_one.txt") as f:
        data = [[c for c in line.strip()] for line in f.readlines()]

    def find_start(data):
        for i, line in enumerate(data):
            for j, c in enumerate(line):
                if c == "S":
                    return i, j
    
    i, j = find_start(data)
    mask = [[False for _ in range(len(data[0]))] for _ in range(len(data))]
    mask[i][j] = True

    def get_direction(c, d):
        if d == "n":
            if c == "|": return "n"
            if c == "7": return "w"
            if c == "F": return "o"
        if d == "o":
            if c == "-": return "o"
            if c == "J": return "n"
            if c == "7": return "s"
        if d == "s":
            if c == "|": return "s"
            if c == "L": return "o"
            if c == "J": return "w"
        if d == "w":
            if c == "-": return "w"
            if c == "L": return "n"
            if c == "F": return "s"
    
    if data[i+1][j] in ["|", "L", "J"]:
        i += 1
        d = "s"
    elif data[i][j+1] in ["-", "J", "7"]:
        j += 1
        d = "o"
    elif data[i-1][j] in ["|", "7", "F"]:
        i -= 1
        d = "n"
    elif data[i][j-1] in ["-", "L", "F"]:
        j -= 1
        d = "w"

    while data[i][j] != "S":
        mask[i][j] = True

        d = get_direction(data[i][j], d)

        if d == "n": i -= 1
        elif d == "o": j += 1
        elif d == "s": i += 1
        elif d == "w": j -= 1
    
    import copy

    data = [[c if hit else "." for c, hit in zip(line, frame)] for line, frame in zip(data, mask)]
    border = copy.deepcopy(mask)
    i, j = find_start(data)
    
    n, o, s, w = data[i-1][j], data[i][j+1], data[i+1][j], data[i][j-1]
    if o == "." and w == ".": data[i][j] = "|"
    elif n == "." and s == ".": data[i][j] = "-"
    elif s == "." and w == ".": data[i][j] = "L"
    elif o == "." and s == ".": data[i][j] = "J"
    elif n == "." and o == ".": data[i][j] = "7"
    elif n == "." and w == ".": data[i][j] = "F"

    sys.setrecursionlimit(len(mask) * len(mask[0]))

    def fill_mask(mask, i, j):
        if mask[i][j] == True: return
        mask[i][j] = True
        
        if i > 0: fill_mask(mask, i-1, j)
        if j > 0: fill_mask(mask, i, j-1)
        if i < len(data)-1: fill_mask(mask, i+1, j)
        if j < len(data[0])-1: fill_mask(mask, i, j+1)
    
    for i in range(len(data)):
        fill_mask(mask, i, 0)
        fill_mask(mask, i, len(data[0])-1)
    for j in range(len(data[0])):
        fill_mask(mask, 0, j)
        fill_mask(mask, len(data)-1, j)
    
    result = 0
    for i, line in enumerate(mask):
        for j, c in enumerate(line):
            if not c:
                inner = False
                latest = None
                for k in range(j):
                    match data[i][k]:
                        case "|": inner = not inner
                        case "L": latest = "L"
                        case "F": latest = "F"
                        case "J":
                            inner = inner == (latest == "L")
                            latest = None
                        case "7":
                            inner = inner == (latest == "F")
                            latest = None
                result += inner
    
    print(result)

if __name__ == "__main__":
    part_one()
    part_two()
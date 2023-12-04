def part_one():
    import re

    with open("./data/03_one.txt") as f:
        data = f.readlines()

    symbols = []
    for line in data:
        symbols.append([])
        for match in re.finditer("[^\d\.]", line.strip()):
            symbols[-1].append(match.start())
            
    result = 0
    for i, line in enumerate(data):
        mask = []
        for di in [-1, 0, 1]:
            if i+di >= 0 and i+di < len(symbols):
                mask.extend(symbols[i+di])
        
        for match in re.finditer("\d+", line):
            if any([match.start()-1 <= hit < match.end()+1 for hit in mask]):
                result += int(match.group())
    
    print(result)
    
def part_two():
    import re

    with open("./data/03_one.txt") as f:
        data = f.readlines()

    gears = []
    for i, line in enumerate(data):
        for match in re.finditer("\*", line.strip()):
            gears.append([i, match.start()])

    result = 0
    for gear in gears:
        i, hit = gear

        ratios = []
        for di in [-1, 0, 1]:
            if i+di >= 0 and i+di < len(data):
                for match in re.finditer("\d+", data[i+di]):
                    if match.start()-1 <= hit < match.end()+1:
                        ratios.append(int(match.group()))
        
        if len(ratios) == 2:
            result += ratios[0] * ratios[1]

    print(result)                
    
if __name__ == "__main__":
    # part_one()
    part_two()
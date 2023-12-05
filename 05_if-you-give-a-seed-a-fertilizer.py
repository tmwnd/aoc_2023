def part_one():
    with open("./data/05_one.txt") as f:
        data = f.read()
    
    result, *data = data.split("\n\n")
    result = [int(seed) for seed in result.removeprefix("seeds: ").split(" ")]

    for block in data:
        map = [[int(x) for x in line.split(" ")] for line in block.split("\n")[1:]]
        
        for i, seed in enumerate(result):
            for destination, source, length in map:
                if source <= seed < source + length:
                    result[i] = destination + (seed - source)
                    break

    print(min(result))

def part_two():
    import re

    with open("./data/05_one.txt") as f:
        data = f.read()
    
    seeds, *data = data.split("\n\n")

    result = []
    for seed in re.findall("\d+ \d+", seeds.removeprefix("seeds: ")):
        seed, length = [int(x) for x in seed.split(" ")]

        result.append([seed, seed + length - 1])
    
    for block in data:
        temp = []
        map = [[int(x) for x in line.split(" ")] for line in block.split("\n")[1:]]
        
        while len(result) > 0:
            seed = result.pop(0)
            
            for destination, source, length in map:
                x0 = max(source, seed[0])
                x1 = min(source + length, seed[1])
                
                if x0 < x1:
                    if seed[0] < x0:
                        result.append([seed[0], x0])
                    if x1 < seed[1]:
                        result.append([x1, seed[1]])
                    
                    temp.append([destination + (x0 - source), destination + (x1 - source)])

                    seed = None
                    break

            if seed is not None:
                temp.append(seed)

        result = temp

    print(min([x[0] for x in result]))

if __name__ == "__main__":
    part_one()
    part_two()
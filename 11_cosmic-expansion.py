def part_one():
    with open("./data/11_one.txt") as f:
        data = [[c for c in line] for line in f.readlines()]
    
    galaxies = []
    di = 0
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == "#":
                if len(galaxies) > 0 and galaxies[-1][0] < i+di-1:
                    di += 1
                galaxies.append([i+di, j])

    galaxies = sorted(galaxies, key=lambda galaxy: galaxy[1])
    dj = 0
    latest = 0
    for i in range(len(galaxies)):
        if galaxies[i][1] > latest+1:
            dj += 1
        latest = galaxies[i][1]
        galaxies[i][1] += dj

    result = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            for k in [0, 1]:
                result += abs(galaxies[i][k] - galaxies[j][k])
    
    print(result)

def part_two():
    with open("./data/11_one.txt") as f:
        data = [[c for c in line] for line in f.readlines()]
    
    galaxies = []
    di = 0
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == "#":
                if len(galaxies) > 0 and galaxies[-1][0] < i+di-1:
                    di += 999999
                galaxies.append([i+di, j])

    galaxies = sorted(galaxies, key=lambda galaxy: galaxy[1])
    dj = 0
    latest = 0
    for i in range(len(galaxies)):
        if galaxies[i][1] > latest+1:
            dj += 999999
        latest = galaxies[i][1]
        galaxies[i][1] += dj

    result = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            for k in [0, 1]:
                result += abs(galaxies[i][k] - galaxies[j][k])
    
    print(result)

if __name__ == "__main__":
    part_one()
    part_two()
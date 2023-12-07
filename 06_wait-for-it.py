def part_one():
    import re

    with open("./data/06_one.txt") as f:
        data = f.readlines()

    games = [[int(x) for x in re.findall("\d+", line)] for line in data]

    result = 1
    for time, distance in zip(*games):
        f = lambda x: (time - x) * x - distance

        p = -time
        q = distance

        x_min = int(-p / 2 - ((p / 2)**2 - q)**0.5)
        x_max = int(-p / 2 + ((p / 2)**2 - q)**0.5)

        while f(x_min) <= 0:
            x_min += 1
        while f(x_max) <= 0:
            x_max -= 1
        
        result *= int(x_max - x_min) + 1
    print(result)

def part_two():
    import re

    with open("./data/06_one.txt") as f:
        data = f.readlines()

    time, distance = [int("".join(re.findall("\d+", line))) for line in data]
    f = lambda x: (time - x) * x - distance

    p = -time
    q = distance

    x_min = int(-p / 2 - ((p / 2)**2 - q)**0.5)
    x_max = int(-p / 2 + ((p / 2)**2 - q)**0.5)

    while f(x_min) <= 0:
        x_min += 1
    while f(x_max) <= 0:
        x_max -= 1
    
    print(int(x_max - x_min) + 1)

if __name__ == "__main__":
    part_one()
    part_two()
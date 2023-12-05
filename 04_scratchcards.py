def part_one():
    import re

    with open("./data/04_one.txt") as f:
        data = f.readlines()
    
    result = 0
    for line in data:
        winning_numbers, my_numbers = line.split(": ")[1].split(" | ")

        winning_numbers = set(re.findall("\d+", winning_numbers))
        my_numbers = set(re.findall("\d+", my_numbers))

        result += int(2 ** (len(winning_numbers & my_numbers) - 1))
    
    print(result)

def part_two():
    import re

    with open("./data/04_one.txt") as f:
        data = f.readlines()
    
    result = [1 for _ in range(len(data))]
    for i, line in enumerate(data):
        winning_numbers, my_numbers = line.split(": ")[1].split(" | ")

        winning_numbers = set(re.findall("\d+", winning_numbers))
        my_numbers = set(re.findall("\d+", my_numbers))

        for di in range(len(winning_numbers & my_numbers)):
            if i+di+1 < len(result):
                result[i+di+1] += result[i]
    
    print(sum(result))

if __name__ == "__main__":
    part_one()
    part_two()
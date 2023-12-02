def part_one():
    import re

    with open("data/01_one.txt") as f:
        data = f.readlines()
    
    result = 0
    for line in data:
        numbers = re.findall("\d", line)
        result += int(numbers[0] + numbers[-1])
    
    print(result)

def part_two():
    import re

    def to_int(s: str) -> str:
        if re.match("\d", s):
            return s
        match s:
            case "one": return "1"
            case "two": return "2"
            case "three": return "3"
            case "four": return "4"
            case "five": return "5"
            case "six": return "6"
            case "seven": return "7"
            case "eight": return "8"
            case "nine": return "9"

    with open("data/01_two.txt") as f:
        data = f.readlines()
    
    result = 0
    for line in data:
        numbers = re.findall("(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
        result += int(to_int(numbers[0]) + to_int(numbers[-1]))
    
    print(result)

if __name__ == "__main__":
    part_one()
    part_two()
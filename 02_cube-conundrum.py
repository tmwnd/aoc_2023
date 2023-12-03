def part_one():
    with open("data/02_one.txt") as f:
        data = f.readlines()

    bag_max = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    
    result = 0
    for line in data:
        game = {}

        game_id, line = line.split(": ")
        for cube_set in line.strip().split("; "):
            for cubes in cube_set.split(", "):
                key, val = cubes.split(" ")[::-1]

                game[key] = max(int(val), game[key] if key in game else 0)
        
        if all([game[key] <= val if key in game else True for key, val in bag_max.items()]):
            result += int(game_id.split(" ")[1])
    
    print(result)

def part_two():
    with open("data/02_one.txt") as f:
        data = f.readlines()
    
    result = 0
    for line in data:
        game = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        game_id, line = line.split(": ")
        for cube_set in line.strip().split("; "):
            for cubes in cube_set.split(", "):
                key, val = cubes.split(" ")[::-1]

                game[key] = max(int(val), game[key])
        
        game_power = 1
        for val in game.values():
            game_power *= val
        
        result += game_power
    
    print(result)

if __name__ == "__main__":
    part_one()
    part_two()
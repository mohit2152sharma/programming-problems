import os


def read_file(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        f = file.readlines()
    return f


def numbers(line: str) -> int: 
    first_number, second_number= '0','0'
    for c in line: 
        if c.isnumeric():
            first_number = c
            break 
    for c in line[::-1]: 
        if c.isnumeric():
            second_number = c
            break 
    return int(first_number + second_number)


if __name__ == "__main__": 

    dir = os.path.dirname(os.path.abspath(__file__))
    lines = read_file(os.path.join(dir, 'lines.txt'))
    print(sum(map(numbers, lines)))





def reversed_file(file_name):
    result = []

    with open('xxx.txt', 'r') as f:
        for line in f:
            result.append(line.replace("\n", ""))

    for line in result[::-1]:
        yield line


lines = reversed_file('xxx.txt')
print(next(lines))
print(next(lines))
print(next(lines))

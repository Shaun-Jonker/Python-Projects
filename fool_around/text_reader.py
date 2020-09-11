with open('') as file:
    arr = []
    for line in file:
        arr.append(line.split(','))

    for sentence in arr:
        for statement in sentence:
            print(statement.strip())

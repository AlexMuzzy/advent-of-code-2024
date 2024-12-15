

with open("day2/puzzle-input2.txt", "r") as infile:
    list = [list(map(int, line.split())) for line in infile]
    number_of_safes = 0
    for line in list:
        problem_count = 0
        safe = True
        is_increasing = line[0] < line[1]
        list_length = len(line) - 1
        for i in range(0, list_length):
            diff = abs(int(line[i]) - int(line[i + 1]))
            if diff < 1 or diff > 3:
                print("line diff is not safe", line, diff, i)
                safe = False
                problem_count += 1
                line.remove(line[i + 1]) if problem_count < 1 else None
                list_length -= 1
            elif is_increasing and line[i] > line[i + 1]:
                print("line is not increasing", line, i)
                safe = False
                line.remove(line[i + 1]) if problem_count < 1 else None
                list_length -= 1
            elif not is_increasing and line[i] < line[i + 1]:
                print("line is not decreasing", line, i)
                safe = False
                line.remove(line[i + 1]) if problem_count < 1 else None
                list_length -= 1
        if safe:
            print("line is safe", line)
            number_of_safes += 1
    print(number_of_safes)

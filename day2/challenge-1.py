

with open("day2/puzzle-input.txt", "r") as infile:
    list = [list(map(int, line.split())) for line in infile]
    number_of_safes = 0
    for line in list:
        safe = True
        is_increasing = line[0] < line[1]
        for i in range(0, len(line) - 1):
            diff = abs(int(line[i]) - int(line[i + 1]))
            if diff < 1 or diff > 3:
                print("line diff is not safe", line, diff, i)
                safe = False
            elif is_increasing and line[i] > line[i + 1]:
                print("line is not increasing", line, i)
                safe = False
            elif not is_increasing and line[i] < line[i + 1]:
                print("line is not decreasing", line, i)
                safe = False
            if not safe:
                break
        if safe:
            print("line is safe", line)
            number_of_safes += 1
    print(number_of_safes)
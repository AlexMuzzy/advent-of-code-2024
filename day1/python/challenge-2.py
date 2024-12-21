

with open("puzzle-input.txt", "r") as infile:
    list1, list2 = zip(*[map(int, line.split()) for line in infile])
    print(sum(list2.count(x) * x for x in list1))


if __name__ == "__main__":
    with open("puzzle-input.txt") as infile:
        list1, list2 = zip(*[map(int, line.split()) for line in infile])
        print(sum(abs(x - y) for x, y in zip(sorted(list1), sorted(list2))))
        
#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == 0 and j == 0:
            continue
        print(f"{i}{j}", end=', ' if (i, j) != (8, 9) else '\n')

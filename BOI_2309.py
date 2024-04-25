import itertools

input_data = []
for _ in range(9):
    input_num = int(input())
    input_data.append(input_num)
total = 100
a = list(itertools.combinations(input_data, 7))
for tuple in a:
    if sum(tuple) == total:
        break
tuple = sorted(tuple)
for i in tuple:
    print(i)


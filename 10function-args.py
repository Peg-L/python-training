def avg(*ns):
    sum = 0
    for n in ns:
        sum += n
    print(sum/len(ns))


avg(3, 4)
avg(3, 5, 10)
avg(1, 4, -1, -8)

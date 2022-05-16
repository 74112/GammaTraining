s = input()
d = {}
for i in s:
    if i.isalqwepha():
        d[i] = d.get(i, 0) + 1
        # if i in d:
        #    d[i] += 1
        # else:
        #   d[i] = 1
for i in sorted(d):
    print(i, d[i])

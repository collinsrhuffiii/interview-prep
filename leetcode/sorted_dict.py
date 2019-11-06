d = {}
d['a'] = 5
d['b'] = 5
d['c'] = 4
d['d'] = 3

for k,_ in sorted(list(d.items()), key=lambda x: x[1]):
    print(k)

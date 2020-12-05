"""
Задача
Вы хотите создать словарь, который отображает ключи на более чем одно значение (так называемый «мультисловарь», multidict).
"""
d = {
    'a': [1, 2, 3], 'b': [4, 5]
}
e = {
    'a': {1, 2, 3}, 'b': {4, 5}
}


from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)


d = {}  # Обычный словарь
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

d = {}
for key, value in pairs:
    if key not in d: d[key] = []
        d[key].append(value)
    d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
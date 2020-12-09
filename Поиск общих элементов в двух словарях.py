"""
Задача
У вас два словаря, и вы хотите выяснить, что у них общего (одинаковые ключи, значения и т. п.)."""

a = {
    'x': 1,
    'y': 2,
    'z': 3}
b = {
    'w': 10,
    'x': 11,
    'y': 2}

c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print((a.keys() & b.keys()))

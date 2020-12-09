"""
Задача
Вы хотите создать словарь, который позволит контролировать порядок элементов при итерировании по нему или при сериализации.
"""
from collections import OrderedDict


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

print(type(d).__name__)


"""
Задача
Вы хотите проводить различные вычисления (например, поиск минимального и максимального значений, сортировку) на словаре с данными.
Решение"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
price_sorted = sorted(zip(prices.values(),prices.keys()))
min(prices, key=lambda k: prices[k])
max(prices, key=lambda k: prices[k])


# print(min(prices))
# print(min(prices.values()))


"""max(prices, key=lambda k: prices[k])"""

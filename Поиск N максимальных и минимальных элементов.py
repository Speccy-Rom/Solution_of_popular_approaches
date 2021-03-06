"""
Задача
Cоздайте список N максимальных или минимальных элементов коллекции."""

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(4, nums))
print(sorted(nums)[-1:-5:-1])

print(heapq.nsmallest(4, nums))
print(sorted(nums)[:4])


portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
cheap_s = heapq.nsmallest(3, portfolio, key=lambda s: s['shares'])

expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(cheap_s)
print(expensive)

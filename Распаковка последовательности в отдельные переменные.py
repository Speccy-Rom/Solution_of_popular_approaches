# Задача
# У вас есть кортеж из N элементов или последовательность, которую вы хотите рас- паковать в коллекцию из N переменных.


data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

print(name)
print(shares)
print(price)
print(date)

# name, shares, price, date, var = data
# print(var) # исключение при не совпадении количества элементов ValueError: not enough values to unpack (expected 5, got 4)

# отбраковка некоторых элементов

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data

print(shares)
print(price)
print(_)
"""Используя метод format(), дополните приведённый ниже код так, чтобы он вывел текст:

In 2010, someone paid 10k Bitcoin for two pizzas."""

year = 2010
price = '10k'
currency = 'Bitcoin'

line = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, price, currency)

print(line)
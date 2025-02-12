"""Церемония взвешивания 🥊
Известен вес боксёра-любителя (целое число). Известно, что вес таков, что боксер может быть отнесён к одной из трёх весовых категорий:

1. Легкий вес – до 60 кг (невключительно);
2. Первый полусредний вес – до 64 кг (невключительно);
3. Полусредний вес – до 69 кг (невключительно)."""

LIGHT_WEIGHT = 60
FIRST_WELTERWEIGHT = 64
WELTERWEIGHT = 69

boxers_weight = int(input())

if boxers_weight < LIGHT_WEIGHT:
    print('Легкий вес')
elif LIGHT_WEIGHT <= boxers_weight < FIRST_WELTERWEIGHT:
    print('Первый полусредний вес')
elif FIRST_WELTERWEIGHT <= boxers_weight < WELTERWEIGHT:
    print('Полусредний вес')
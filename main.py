import math
import statistics

min_price = 1.0

purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

"""
    item — название товара,
    category — категория товара,
    price — цена за единицу товара,
    quantity — количество единиц, купленных за один раз.
"""

def total_revenue(purchases: dict) -> float:
    summa = 0
    for i in purchases:
        summa += i['price']
    return round(summa * len(purchases))

def items_by_category(purchases: dict) -> dict:
    unique_items_by_category = {}
    for i in purchases:
        unique_items_by_category[i['category']] = unique_items_by_category.get(i['category'], [])
        unique_items_by_category[i.get('category')].append(i['item'])
    return unique_items_by_category

def expensive_purchases(purchases : dict, min_price: float) -> list:
    expensive_items = []
    for i in purchases:
        if i['price'] >= min_price:
            expensive_items.append(i)
    return expensive_items

def average_price_by_category(purchases: dict) -> dict:
    prices_by_category = {}
    avg_price_by_category = {}
    for i in purchases:
        prices_by_category[i['category']] = prices_by_category.get(i['category'], [])
        avg_price_by_category[i['category']] = prices_by_category.get(i['category'], 0.0)
        prices_by_category[i.get('category')].append(i['price'])
        avg_price_by_category[i.get('category')] = float(statistics.mean(prices_by_category[i.get('category')]))
    return avg_price_by_category

def most_frequent_category(purchases: dict) -> str:
    quantity_by_category = {}
    sum_quantity_by_category = {}
    for i in purchases:
        quantity_by_category[i['category']] = quantity_by_category.get(i['category'], [])
        sum_quantity_by_category[i['category']] = quantity_by_category.get(i['category'], 0.0)
        quantity_by_category[i.get('category')].append(i['quantity'])
        sum_quantity_by_category[i.get('category')] = math.fsum(quantity_by_category[i.get('category')])
    return max(sum_quantity_by_category, key=sum_quantity_by_category.get)

print("Общая выручка: {:.1f}".format(total_revenue(purchases)))
print(f"Товары по категориям: {items_by_category(purchases)}")
print(f"Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}")
print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")

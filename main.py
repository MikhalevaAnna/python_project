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

def create_dict_by_category(purchases: dict, field: str) -> dict:
    dict_by_category = {}
    for i in purchases:
        dict_by_category[i['category']] = dict_by_category.get(i['category'], [])
        dict_by_category[i.get('category')].append(i[field])
    return dict_by_category

def total_revenue(purchases: dict) -> float:
    summa = 0
    for i in purchases:
        summa += i['price']
    return round(summa * len(purchases))

def items_by_category(purchases: dict) -> dict:
    unique_items_by_category = create_dict_by_category(purchases, 'item')
    return unique_items_by_category

def expensive_purchases(purchases : dict, min_price: float) -> list:
    expensive_items = []
    for i in purchases:
        if i['price'] >= min_price:
            expensive_items.append(i)
    return expensive_items

def average_price_by_category(purchases: dict) -> dict:
    avg_price_by_category = {}
    prices_by_category = create_dict_by_category(purchases, 'price')
    for i in purchases:
        avg_price_by_category[i['category']] = prices_by_category.get(i['category'], 0.0)
        avg_price_by_category[i.get('category')] = float(statistics.mean(prices_by_category[i.get('category')]))
    return avg_price_by_category

def most_frequent_category(purchases: dict) -> str:
    sum_quantity_by_category = {}
    quantity_by_category = create_dict_by_category(purchases, 'quantity')
    for i in purchases:
        sum_quantity_by_category[i['category']] = quantity_by_category.get(i['category'], 0.0)
        sum_quantity_by_category[i.get('category')] = math.fsum(quantity_by_category[i.get('category')])
    return max(sum_quantity_by_category, key=sum_quantity_by_category.get)

print("Общая выручка: {:.1f}".format(total_revenue(purchases)))
print(f"Товары по категориям: {items_by_category(purchases)}")
print(f"Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}")
print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")

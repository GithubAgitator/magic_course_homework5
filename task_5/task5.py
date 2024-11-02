# Система учета заказов
import json

# У вас есть JSON-файл orders.json,
# содержащий данные о заказах интернет-магазина.
# Каждый заказ включает информацию о клиенте,
# заказанных товарах, количестве и цене.
# Напишите программу, которая:
# Выводит общую сумму каждого заказа.
# Находит клиента с наибольшей суммой заказа и выводит его имя и сумму.
d = {}
with open('orders.json', 'r', encoding='utf-8') as f:
    file_read = json.load(f)
    print(file_read)
    for i in file_read['orders']:
        order_id = i.get('order_id')
        for j in i['items']:
            count = j['quantity'] * j['price']
            if order_id in d:
                d[order_id] += count
            else:
                d[order_id] = count

print(d)
sorts = sorted(d.values(), reverse=True)
print(sorts[0])
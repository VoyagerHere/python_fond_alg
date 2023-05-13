import random

# генерация случайных данных
n = 120  # количество дней
m = 5  # максимальное количество лотов в день
s = 10000  # доступные денежные средства
obligations = ["alfa-05", "beta-07", "gazprom-17", "rosneft-22", "sberbank-14"]
data = []
for day in range(1, n + 1):
    for i in range(random.randint(0, m)):
        name = random.choice(obligations)
        price = round(random.uniform(90, 110), 2)
        quantity = random.randint(1, 10)
        data.append((day, name, price, quantity))

# запись данных в файл
with open("example.txt", "w") as f:
    f.write(f"{n} {m} {s}\n")
    for day, name, price, quantity in data:
        f.write(f"{day} {name} {price} {quantity}\n")
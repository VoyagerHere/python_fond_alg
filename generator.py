import random
import argparse



def gen_data(n: int, m: int, s:int):
    obligations = ["alfa-05", "beta-07", "gazprom-17", "rosneft-22", "sberbank-14"]
    data = []
    for day in range(1, n + 1):
        for i in range(random.randint(1, m)):
            name = random.choice(obligations)
            price = round(random.uniform(90, 110), 2)
            quantity = random.randint(1, 10)
            data.append((day, name, price, quantity))

    # запись данных в файл
    with open("example.txt", "w") as f:
        f.write(f"{n} {m} {s}\n")
        for day, name, price, quantity in data:
            f.write(f"{day} {name} {price} {quantity}\n")





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="Value of n")
    args = parser.parse_args()
    
    m = 5  # максимальное количество лотов в день
    s = 10000  # доступные денежные средства
    n = args.n # количество дней
    gen_data(n, m, s)
import time

def process_input_file(input_file: str) -> tuple[int, int, float, list[tuple[str, str, float, int]]]:
    with open(input_file, 'r') as f:
        n, m, s = map(int, f.readline().strip().split())
        bond_info = []
        while True:
            line = f.readline().strip()
            if not line:
                break
            day, bond, price, amount = line.split()
            bond_info.append((day, bond, float(price), int(amount)))
        return n, m, s, bond_info


def dynamic_cost(bond_info: list[tuple[str, str, float, int]], index: int) -> None:
    bond = bond_info[index]
    bond_day, bond_name, bond_price, bond_lot_size = bond
    total_cost = bond_price / 100 * bond_lot_size * 1000
    dynamic_income_max = 0
    max_index = index
    for j in range(index + 1, len(bond_info) - 1):
        dyn_bond = bond_info[j]
        if int(dyn_bond[0]) >= int(bond_day):
            continue
        day, bond_name, price, lot_size = dyn_bond
        dynamic_income = calculate_income(dyn_bond, int(bond_day) - int(dyn_bond[0])) - calculate_income(bond_info[index])
        if dynamic_income > 0:
            dynamic_income_max = dynamic_income
            max_index = j
    if dynamic_income_max > 0:
        bond_info[index], bond_info[max_index] = bond_info[max_index], bond_info[index]


def algorithm(n: int, m: int, s: float, bond_info: list[tuple[str, str, float, int]]) -> list[tuple[str, str, float, int]]:
    bond_info.sort(key=lambda x: (x[3], -x[2]), reverse=True)
    purchased_bonds = []
    for i in range(len(bond_info)):
        dynamic_cost(bond_info, i)
        bond = bond_info[i]
        bond_day, bond_name, bond_price, bond_lot_size = bond
        total_cost = bond_price / 100 * bond_lot_size * 1000
        if s >= total_cost:
            s -= total_cost
            purchased_bonds.append((bond))
    return purchased_bonds


def calculate_income(bond: tuple[str, str, float, int], coupon_days: int = 0) -> int:
    day, bond_name, price, lot_size = bond
    cost = int(lot_size * (price * 10))
    coupon = lot_size * coupon_days
    price = 1000 * lot_size
    income = price - cost + coupon
    return income


if __name__ == '__main__':
    input_file: str = 'example.txt'
    n, m, s, bond_info = process_input_file(input_file)
    start_time = time.time()
    purchased_bonds: list[tuple[str, str, float, int]] = algorithm(n, m, s, bond_info)

    total_income: int = 0

    for bond in purchased_bonds:
        coupon_days = n - int(bond[0]) + 30
        income = calculate_income(bond, coupon_days)
        total_income += income
    print(total_income)
    for bond_day, bond_name, price, lot_size in purchased_bonds:
          print(f"{bond_day} {bond_name} {price} {lot_size}")
    print()
    end_time = time.time()
    print(f"It took {end_time-start_time:.2f} seconds to compute")
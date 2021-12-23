dict_bruteforce = {
    "action-1": {"cost": 20, "profit": 5},
    "action-2": {"cost": 30, "profit": 10},
    "action-3": {"cost": 50, "profit": 15},
    "action-4": {"cost": 70, "profit": 20},
    "action-5": {"cost": 60, "profit": 17},
    "action-6": {"cost": 80, "profit": 25},
    "action-7": {"cost": 22, "profit": 7},
    "action-8": {"cost": 26, "profit": 11},
    "action-9": {"cost": 48, "profit": 13},
    "action-10": {"cost": 34, "profit": 27},
    "action-11": {"cost": 42, "profit": 17},
    "action-12": {"cost": 110, "profit": 9},
    "action-13": {"cost": 38, "profit": 23},
    "action-14": {"cost": 14, "profit": 1},
    "action-15": {"cost": 18, "profit": 3},
    "action-16": {"cost": 8, "profit": 8},
    "action-17": {"cost": 4, "profit": 12},
    "action-18": {"cost": 10, "profit": 14},
    "action-19": {"cost": 24, "profit": 21},
    "action-20": {"cost": 114, "profit": 18},
}


def two_years_profit():
    """Calcul le profit de chaque action au bout de deux ans."""
    for key, value in dict_bruteforce.items():
        two_years_profit = value["cost"] * value["profit"] / 100
        dict_bruteforce[key]["two_years_profit"] = two_years_profit
    # print(dict_bruteforce)


two_years_profit()


list_action = [
    "action-1",
    "action-2",
    "action-3",
    "action-4",
    "action-5",
    "action-6",
    "action-7",
    "action-8",
    "action-9",
    "action-10",
    "action-11",
    "action-12",
    "action-13",
    "action-14",
    "action-15",
    "action-16",
    "action-17",
    "action-18",
    "action-19",
    "action-20",
]

list_cost = [
    20,
    30,
    50,
    70,
    60,
    80,
    22,
    26,
    48,
    34,
    42,
    110,
    38,
    14,
    18,
    8,
    4,
    10,
    24,
    114,
]

list_profit = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]

list_profit_two_years = []


def profit_two_years():
    for i in range(len(list_action)):
        profit = list_cost[i] * list_profit[i] / 100
        list_profit_two_years.append(profit)


profit_two_years()

# print(len(list_action), len(list_cost), len(list_profit), len(list_profit_two_years))
# print(list_profit_two_years)

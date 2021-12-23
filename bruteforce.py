import time
from data.donnees_bruteforce import dict_bruteforce

start = time.process_time()

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


def two_years_profit():
    """Calcul le profit de chaque action au bout de deux ans."""
    action_profit = {}
    for key, value in dict_bruteforce.items():
        two_years_profit = value["cost"] * value["profit"] / 100
        print(key, " : ", two_years_profit, "€")
        action_profit[key] = two_years_profit
    print(action_profit)


def maximum_expense_per_client():
    cost_list = []
    max_expense = 0
    for key, value in dict_bruteforce.items():
        if max_expense <= 500:
            cost_list.append(value["cost"])
            max_expense += value["cost"]
        if max_expense > 500:
            adjust = cost_list.pop()
            max_expense -= adjust
            break
    print(cost_list)
    print(max_expense)


def test(maximum_expense, list_cost, list_profit_two_years, n):
    if n == 0 or maximum_expense == 0:
        return 0

    if list_cost[n - 1] > maximum_expense:
        return test(maximum_expense, list_cost, list_profit_two_years, n - 1)

    else:
        return max(
            list_profit_two_years[n - 1]
            + test(
                maximum_expense - list_cost[n - 1],
                list_cost,
                list_profit_two_years,
                n - 1,
            ),
            test(maximum_expense, list_cost, list_profit_two_years, n - 1),
        )


def main():
    # profit = two_years_profit()
    profit_two_years()
    # max = maximum_expense_per_client()
    maximum_expense = 500
    n = len(list_cost)
    print(test(maximum_expense, list_cost, list_profit_two_years, n))


if __name__ == "__main__":
    main()

end = time.process_time()
print("Time to execute program : ", end - start, "Seconds")

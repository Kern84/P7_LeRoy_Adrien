import time

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

list_two_years_profit = []

list_of_tuples = []


def two_years_profit():
    """Calculate the return after two years in dollars for each actions."""
    for i in range(len(list_action)):
        profit = list_cost[i] * list_profit[i] / 100
        list_two_years_profit.append(profit)


def create_tuple():
    """Create a tuple with the actions : names, prices, returns in % and returns in $."""
    for i in range(len(list_action)):
        prep_tuple = (
            list_action[i],
            list_cost[i],
            list_profit[i],
            list_two_years_profit[i],
        )
        list_of_tuples.append(prep_tuple)


def optimized_dynamic(maximum_expense, elements):
    matrice = [
        [0 for x in range(maximum_expense + 1)] for x in range(len(elements) + 1)
    ]

    for i in range(1, len(elements) + 1):
        for w in range(1, maximum_expense + 1):
            if elements[i - 1][1] <= w:
                matrice[i][w] = max(
                    elements[i - 1][3] + matrice[i - 1][w - elements[i - 1][1]],
                    matrice[i - 1][w],
                )
            else:
                matrice[i][w] = matrice[i - 1][w]

    m = maximum_expense
    n = len(elements)
    elements_selection = []

    while m >= 0 and n >= 0:
        e = elements[n - 1]
        if matrice[n][m] == matrice[n - 1][m - e[1]] + e[3]:
            elements_selection.append(e)
            m -= e[1]

        n -= 1

    return "\nTotal return : {} $; \nTotal cost : {} $;\nList of actions taken : {}.".format(
        round(matrice[-1][-1], 2),
        sum([i[1] for i in elements_selection]),
        elements_selection,
    )


def main():
    two_years_profit()
    create_tuple()
    print("Best solution : ", optimized_dynamic(500, list_of_tuples))


if __name__ == "__main__":
    main()

end = time.process_time()
print("Program executed in : ", end - start, "Seconds")

import time

# Algorithme 2**n

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


def brute_force(maximum_expense, elements, elements_selection=[]):
    """
    Breakpoint if no more elements. Return the actions total cost, total profit and the actions taken.
    While there are still elements. First ligne ignore the first element and do not add elements to the list.
    Check if first element is in range of the max expense. If so, withdraw the price from max expense, remove the first
    element from the list and add it to the selected elements.
    check the best solution, with or without the action.
    """
    if elements:
        val1, lstVal1, lstVal1_1 = brute_force(
            maximum_expense, elements[1:], elements_selection
        )
        val = elements[0]
        if val[1] <= maximum_expense:
            val2, lstVal2, lstVal2_2 = brute_force(
                maximum_expense - val[1], elements[1:], elements_selection + [val]
            )
            if val1 < val2:
                return val2, lstVal2, lstVal2_2
        return val1, lstVal1, lstVal1_1
    else:
        return (
            sum([i[1] for i in elements_selection]),
            sum([i[3] for i in elements_selection]),
            elements_selection,
        )


def main():
    two_years_profit()
    create_tuple()
    print("Best solution : ", brute_force(500, list_of_tuples))


if __name__ == "__main__":
    main()

end = time.process_time()
print("Program executed in : ", end - start, "Seconds")

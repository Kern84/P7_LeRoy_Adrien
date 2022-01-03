import time

start = time.process_time()

action = [
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

cost = [
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

value = []

maximum_expense = 500


def two_years_profit():
    """Calculate the return after two years in dollars for each actions."""
    for i in range(len(action)):
        profit = cost[i] * list_profit[i] / 100
        value.append(profit)


class Greedy:
    """
    Define the shares cost, profit and the index.
    The greedy approach consists in building a complete solution by a succession of local choices
    systematically giving the best partial solution.
    """

    def __init__(self, name, cost, profit, index):
        self.name = name
        self.index = index
        self.cost = cost
        self.profit = profit
        self.ratio = profit // cost

    """
    Function for the comparison between two "Greedy".
    We compare the calculatred ratio to sort them.
    """

    def __lt__(self, other):
        return self.ratio < other.ratio


def get_best_value(action, cost, value, maximum_expense):
    """
    Add best action ratio to the list.
    Ignore the 0$ and negative number actions.
    Sort elements by ratio.
    Check if action can be bought and if so withdraw the cost from max expense.
    Add the profit and the action taken to the list.
    """
    sorting_table = []
    list_of_actions_taken = []
    for i in range(len(cost)):
        if cost[i] <= 0 or value[i] <= 0:
            pass
        else:
            sorting_table.append(Greedy(action[i], cost[i], value[i], i))

    sorting_table.sort(reverse=True)

    cost_counter = 0
    value_counter = 0
    for objet in sorting_table:
        current_name = objet.name
        current_cost = objet.cost
        current_value = objet.profit
        if maximum_expense - current_cost >= 0:
            maximum_expense -= current_cost
            value_counter += current_value
            cost_counter += current_cost
            action_taken = current_name, current_cost, current_value
            list_of_actions_taken.append(action_taken)
    return "\nTotal return : {} $; \nTotal cost : {} $;\nList of actions taken : {}.".format(
        round(value_counter, 2), round(cost_counter, 2), list_of_actions_taken
    )


def main():
    two_years_profit()
    print()
    print("Best solution : ", get_best_value(action, cost, value, maximum_expense))


if __name__ == "__main__":
    main()

end = time.process_time()
print()
print("Program executed in : ", end - start, "Seconds")

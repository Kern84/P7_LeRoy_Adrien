import csv
import time

start = time.process_time()

action = []
cost = []
value = []

maximum_expense = 500


"""Retrieves information from .csv file and sorts them in lists."""
with open("data/dataset1_Python+P7.csv", "r", newline="") as csvfile:
    actions_info = csv.reader(csvfile)
    next(actions_info)
    for row in actions_info:
        profit = float(row[1]) * float(row[2]) / 100
        action.append(row[0])
        cost.append(float(row[1]))
        value.append(round(profit, 2))


class Glouton:
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
    Function for the comparison between two "Glouton".
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
        if float(cost[i]) <= 0 or float(value[i]) <= 0:
            pass
        else:
            sorting_table.append(Glouton(action[i], float(cost[i]), float(value[i]), i))

    sorting_table.sort(reverse=True)

    cost_counter = 0
    value_counter = 0
    for objet in sorting_table:
        current_name = objet.name
        current_cost = float(objet.cost)
        current_value = float(objet.profit)
        if maximum_expense - current_cost >= 0:
            maximum_expense -= current_cost
            value_counter += current_value
            cost_counter += current_cost
            action_taken = current_name, current_cost, current_value
            list_of_actions_taken.append(action_taken)
    return "\nTotal return : {} $; \nTotal cost : {} $;\nList of actions taken : {}.".format(
        round(value_counter, 2), round(cost_counter, 2), list_of_actions_taken
    )


print()
print("Best solution : ", get_best_value(action, cost, value, maximum_expense))


end = time.process_time()
print()
print("Program executed in : ", end - start, "Seconds")

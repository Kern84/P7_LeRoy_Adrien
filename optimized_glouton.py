import csv
import time

start = time.process_time()

list_of_tuples = []
cost = []
value = []

maximum_expense = 500


"""Retrieves information from .csv file and sorts them in lists."""
with open("data/dataset1_Python+P7.csv", "r", newline="") as csvfile:
    actions_info = csv.reader(csvfile)
    next(actions_info)
    for row in actions_info:
        profit = float(row[1]) * float(row[2]) / 100
        create_tuple = row[0], float(row[1]), float(row[2]), float(round(profit, 2))
        cost.append(float(row[1]))
        value.append(profit)
        list_of_tuples.append(create_tuple)


class Glouton:
    """
    Define the shares cost, profit and the index.
    The greedy approach consists in building a complete solution by a succession of local choices
    systematically giving the best partial solution.
    """

    def __init__(self, cost, profit, index):
        self.index = index
        self.cost = cost
        self.profit = profit
        self.ratio = profit / cost

    """
    Function for the comparison between two "Glouton".
    We compare the calculatred ratio to sort them.
    """

    def __lt__(self, other):
        return self.ratio < other.ratio


def get_best_value(cost, value, maximum_expense):
    """
    Add best action ratio to the list.
    Ignore the 0$ action.
    Sort elements by ratio.
    Check if action can be bought and if so withdraw the cost from max expense.
    Add the profit and the action taken to the list.

    """
    sorting_table = []
    for i in range(len(cost)):
        try:
            sorting_table.append(Glouton(float(cost[i]), float(value[i]), i))
        except ZeroDivisionError:
            pass

    sorting_table.sort(reverse=True)

    list_of_actions_taken = []
    cost_counter = 0
    value_counter = 0
    for objet in sorting_table:
        current_cost = float(objet.cost)
        current_value = float(objet.profit)
        if maximum_expense - current_cost >= 0:
            maximum_expense -= current_cost
            value_counter += current_value
            cost_counter += current_cost
            list_of_actions_taken.append(list_of_tuples[i])
    return "\nTotal return : {} $; \nTotal cost : {} $;\nList of actions taken : {}.".format(
        round(value_counter, 2), round(cost_counter, 2), list_of_actions_taken
    )


print()
print("Best solution : ", get_best_value(cost, value, maximum_expense))


end = time.process_time()
print()
print("Program executed in : ", end - start, "Seconds")

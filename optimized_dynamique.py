import time
import csv

start = time.process_time()

list_of_tuples = []


with open("data/dataset2_Python+P7.csv", "r", newline="") as csvfile:
    """
    Retrieves information from .csv file and sorts them in lists.
    Ignore actions price and two years profit if <= 0 $.
    Convert Dollars to cents to have int and not float.
    """
    actions_info = csv.reader(csvfile)
    next(actions_info)
    for row in actions_info:
        profit = float(row[1]) * float(row[2]) / 100
        if float(row[1]) <= 0 or profit <= 0:
            pass
        else:
            create_tuple = (
                row[0],
                int(round(float(row[1]), 2) * 100),
                float(row[2]),
                round(profit, 2),
            )
            list_of_tuples.append(create_tuple)


def optimized(maximum_expense, elements):
    """
    Create a matrice and initialize it to 0.
    (+1) is to keep a column and a row at 0, when there is no elements or no cost.
    Walk through the elements and for each element walk throught the cost.
    If the cost is lower than the maximum expense, I compare the maximum between the element in the prvious raw
    and the current element + the optimized solution minus the cost of the previous raw.
    If the cost is higher than the maximum expense, I keep by default the optimize solution from previous raw.

    Find an element by it's cost.
    While there is still elements and max expense to spent, we take the matrice by the end.
    If the matrice row is equal to the element cost + the previous row minus the cost of the element,
    we add the element to the list of elements taken.
    We reduce the max expense by the cost of the element and move to the next element.
    """
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
        sum([i[1] / 100 for i in elements_selection]),
        elements_selection,
    )


def main():
    """
    Maximum expense is 500$, convert to cents = 50000.
    """
    print("Best solution : ", optimized(50000, list_of_tuples))


if __name__ == "__main__":
    main()

end = time.process_time()
print("Program executed in : ", end - start, "Seconds")

import time
import csv

start = time.process_time()

list_of_tuples = []


with open("data/dataset1_Python+P7.csv", "r", newline="") as csvfile:
    actions_info = csv.reader(csvfile)
    next(actions_info)
    for row in actions_info:
        profit = float(row[1]) * float(row[2]) / 100
        # create_tuple = row[0], float(row[1]), float(row[2]), int(round(profit, 2) * 100)
        create_tuple = (
            row[0],
            int(round(float(row[1]), 2) * 100),
            float(row[2]),
            int(round(profit, 2) * 100),
        )
        list_of_tuples.append(create_tuple)

# print(list_of_tuples)


def optimized(maximum_expense, elements):
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

    return matrice[-1][-1], elements_selection


def main():
    print("meilleur solution : ", optimized(500, list_of_tuples))


if __name__ == "__main__":
    main()

end = time.process_time()
print("Program executed in : ", end - start, "Seconds")

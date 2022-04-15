def sum_over(arr, axis):
    sum_total = []
    if axis == "cols":
        sum_total = [0] * len(arr[-1])
        for row in arr:
            sum_total = [sum(t) for t in list(zip(sum_total, row))]
    if axis == "rows":
        sum_total = [sum(row) for row in arr]
    if axis == "diag":
        sum_total = [0, 0]
        for i, row in enumerate(arr):
            ax1 = row[i]
            ax2 = row[-i - 1]
            sum_total[0] += ax1
            sum_total[1] += ax2
    return sum_total


def flatten(myList):
    for item in myList:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


def main(*args, **kwargs):
    pass


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def arr3d_to_dict(arr):
    d = {}
    for i, row in enumerate(arr):
        for j, col in enumerate(row):
            d[(i, j)] = col
    return d


class arr_3d:
    def __init__(self, arr):
        self.arr = arr
        self.d = arr3d_to_dict(arr)
        self.n_cols = len(arr[0])
        self.n_rows = len(arr)
        # lef diagonal
        self.l_diag = [self.d[(i, i)] for i in range(self.n_r)]
        # right diagonal
        self.r_diag = [self.d[(i, self.n_c - i - 1)] for i in range(self.n_r)]
        # Diagonals sum
        self.l_diag_sum = sum(self.l_diag)
        self.r_diag_sum = sum(self.r_diag)

    def __getitem__(self, key):
        return self.d[key]


if __name__ == "__main__":
    main()

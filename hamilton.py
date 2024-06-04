import random

def generate_hamiltonian_graph(n, s):
    edges_amount = s * (n * (n - 1) / 2)
    matrix = [[0] * n for _ in range(n)]
    count = 0
    if edges_amount < n - 1:
        print("Wrong node count or saturation")
        return

    start = random.randint(0, n-1)
    lst = []
    tmp = start
    lst.append(start)
    while count < n - 1:
        v2 = random.randint(0, n-1)
        if v2 not in lst:
            matrix[tmp][v2] = 1
            matrix[v2][tmp] = 1
            lst.append(v2)
            tmp = v2
            count += 1

    matrix[start][tmp] = 1
    matrix[tmp][start] = 1
    count += 1

    while count <= edges_amount:
        v1 = random.randint(0, n-1)
        v2 = random.randint(0, n-1)
        v3 = random.randint(0, n-1)
        if v1 != v2 and v1 != v3 and v2 != v3:
            if matrix[v1][v2] == 0 and matrix[v2][v3] == 0 and matrix[v1][v3] == 0:
                matrix[v1][v2] = 1
                matrix[v2][v1] = 1
                matrix[v1][v3] = 1
                matrix[v3][v1] = 1
                matrix[v3][v2] = 1
                matrix[v2][v3] = 1
                count += 3

    return matrix

def generate_non_hamiltonian_graph(n):
    edges_amount = 0.5 * (n * (n - 1) / 2)
    matrix = [[0] * n for _ in range(n)]
    count = 0
    if edges_amount < n - 1:
        print("Wrong node count or saturation")
        return

    start = random.randint(0, n-1)
    lst = []
    tmp = start
    lst.append(start)
    while count < n - 1:
        v2 = random.randint(0, n-1)
        if v2 not in lst:
            matrix[tmp][v2] = 1
            matrix[v2][tmp] = 1
            lst.append(v2)
            tmp = v2
            count += 1

    matrix[start][tmp] = 1
    matrix[tmp][start] = 1
    count += 1

    while count <= edges_amount:
        v1 = random.randint(0, n-1)
        v2 = random.randint(0, n-1)
        v3 = random.randint(0, n-1)
        if v1 != v2 and v1 != v3 and v2 != v3 and v1 != start and v3 != start and v2 != start:
            if matrix[v1][v2] == 0 and matrix[v2][v3] == 0 and matrix[v1][v3] == 0:
                matrix[v1][v2] = 1
                matrix[v2][v1] = 1
                matrix[v1][v3] = 1
                matrix[v3][v1] = 1
                matrix[v3][v2] = 1
                matrix[v2][v3] = 1
                count += 3

    for i in range(n):
        matrix[start][i] = 0
    for i in range(n):
        matrix[i][start] = 0

    return matrix
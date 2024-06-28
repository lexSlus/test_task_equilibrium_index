def equilibrium(arr):
    left_sum = 0
    right_sum = 0
    n = len(arr)

    for i in range(n):
        left_sum = 0
        right_sum = 0

        # get left sum
        for j in range(i):
            left_sum += arr[j]

        # get right sum
        for j in range(i+1, n):
            right_sum += arr[j]

        # get index
        if left_sum == right_sum:
            return i
    return -1
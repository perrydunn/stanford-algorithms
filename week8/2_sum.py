def naive_2sums(integers, t_value_range):
    n = 0
    t = t_value_range[0]
    while t <= t_value_range[1]:
        for i in integers:
            if t - i != i:
                if (t - i) in integers:
                    n += 1
                    break
        t += 1
    return n


def two_sums(integers, t_value_range):
    A = list(integers)
    A.sort()
    sums = set()
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] < t_value_range[0]:
            i += 1
        elif A[i] + A[j] > t_value_range[1]:
            j -= 1
        else:
            this_sum = A[i] + A[j]
            J = j
            while t_value_range[0] <= this_sum <= t_value_range[1]:
                sums.add(this_sum)
                J -= 1
                this_sum = A[i] + A[J]
            i += 1
    return len(sums)


if __name__ == "__main__":
    integers = set()
    with open("2sum.txt", "r") as f:
        num = f.readline()
        integers.add(int(num))
        while num:
            integers.add(int(num))
            num = f.readline()
    print(two_sums(integers, [-10000, 10000]))

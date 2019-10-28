def chooseFirst(arr, l, _):
    return arr[l]


def chooseLast(arr, l, r):
    elem = arr[r-1]
    arr[r-1] = arr[l]
    arr[l] = elem
    return arr[l]


def chooseOfThree(arr, l, r):
    n = r - l
    med = n // 2 - 1 if n % 2 == 0 else n // 2
    elem0 = arr[l]
    elemM = arr[l+med]
    elemN = arr[r-1]
    if elem0 <= elemM <= elemN or elem0 >= elemM >= elemN:
        arr[l+med] = arr[l]
        arr[l] = elemM
        return arr[l]
    elif elemM <= elem0 <= elemN or elemM >= elem0 >= elemN:
        return arr[l]
    else:
        arr[r-1] = arr[l]
        arr[l] = elemN
        return arr[l]


def quicksort(arr, choosePivot):
    lIdx = 0
    rIdx = len(arr)
    n = 0

    def recQuicksort(arr, l, r, choosePivot):
        if r - l < 2:
            return
        nonlocal n
        n += r - l - 1  # This could be < 0 so it's important this follows the above if and return
        p = choosePivot(arr, l, r)
        i = l  # i splits the < p and >= p
        for j in range(l+1, r):
            if arr[j] < p:
                i += 1
                elem = arr[i]
                arr[i] = arr[j]
                arr[j] = elem
        arr[l] = arr[i]
        arr[i] = p
        recQuicksort(arr, l, i, choosePivot)
        recQuicksort(arr, i+1, r, choosePivot)

    recQuicksort(arr, lIdx, rIdx, choosePivot)
    return n


if __name__ == "__main__":
    intArray = [int(line.rstrip('\n')) for line in open("quicksort.txt")]
    print(quicksort(intArray, chooseFirst))
    intArray = [int(line.rstrip('\n')) for line in open("quicksort.txt")]
    print(quicksort(intArray, chooseLast))
    intArray = [int(line.rstrip('\n')) for line in open("quicksort.txt")]
    print(quicksort(intArray, chooseOfThree))

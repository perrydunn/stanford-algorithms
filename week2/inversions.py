def sortAndCount(A, n):

    def mergeAndCount(L, R):
        resArr = []
        resCounts = 0
        lenL = len(L)
        lenR = len(R)
        i = 0
        j = 0
        while i < lenL and j < lenR:
            if L[i] < R[j]:
                resArr.append(L[i])
                i += 1
            else:
                resCounts += lenL - i
                resArr.append(R[j])
                j += 1
        if i >= lenL:
            resArr += R[j:]
        else:
            resArr += L[i:]
        return resArr, resCounts

    if n == 1: return A, 0
    B, x = sortAndCount(A[:n//2], n//2)
    C, y = sortAndCount(A[n//2:], n - n//2)
    D, z = mergeAndCount(B, C)
    return D, x + y + z


if __name__ == "__main__":
    intArray = [int(line.rstrip('\n')) for line in open("integer.txt")]
    _, invCounts = sortAndCount(intArray, len(intArray))
    print(invCounts)

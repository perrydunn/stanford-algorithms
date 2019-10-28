def karatsuba(x, y):
    n = len(x)
    if n == 1:
        return str(int(x) * int(y))
    else:
        cutoff = n//2
        a = x[:cutoff]
        b = x[cutoff:]
        c = y[:cutoff]
        d = y[cutoff:]
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        aPb = str(int(a) + int(b))
        cPd = str(int(c) + int(d))
        if len(aPb) != len(cPd):
            diff = len(aPb) - len(cPd)
            if diff < 0:
                aPb = "0" * -diff + aPb
            else:
                cPd = "0" * diff + cPd
        if len(aPb) % 2 != 0 and len(aPb) != 1:
            aPb = "0" + aPb
            cPd = "0" + cPd
        abcd = karatsuba(aPb, cPd)
        return str(
            int(ac + n * "0") +
            int(bd) +
            int(str(int(abcd) - int(bd) - int(ac)) + n//2 * "0")
        )


if __name__ == "__main__":
    x = input("x: ")
    y = input("y: ")
    print(karatsuba(x, y))

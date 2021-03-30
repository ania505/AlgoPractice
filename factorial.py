# print("what")
def factorial(n):
    fac = 1

    def helper(n, fac):
        print("n:", n)
        if n == 1:
            return fac
        else:
            print("fac:", fac)
            multi = helper(n-1, fac)
            print(multi)
            fac = fac * multi * n
            return fac
    
    return helper(n, fac)

print(factorial(3))

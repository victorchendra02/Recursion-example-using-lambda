numbers = list(map(int, input("Input numbers: ").split()))
fact = lambda n: 1 if n == 0 or n == 1 else n * fact(n - 1)
print(list(map(fact, numbers)))


print(fact(5))

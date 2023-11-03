numbers = list(range(10))

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def first_digit(n):
    return 1

digits = []
term = 999999
residual = 0
remainder = 0
for i in range(9):
    fac = factorial(9-i)
    print("term:", term, " fac:", fac  )
    remainder = term % fac                 
    residual = int(term / fac)
    term = remainder
    print("index:", residual, " next_term:", remainder)
    print("numbers:", numbers)
    digits.append(numbers[residual])
    numbers.remove(digits[-1])
    print(digits, numbers)

for n in digits:
    print(n, end="")

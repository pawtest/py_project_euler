count=0

def divisible_by_n(n, i):
    return True if i % n == 0 else False
    
for i in range(1000):
    if divisible_by_n(3, i) or divisible_by_n(5, i):
        count += i

print(count)

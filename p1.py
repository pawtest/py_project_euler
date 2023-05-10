count=0
def divisible_by_n(i, n):
    return True if i % n == 0 else False
    
for i in range(1000):
    if divisible_by_n(i, 3) or divisible_by_n(i, 5):
        count += i
print(count)

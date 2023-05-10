cache = dict()
cache[1] = 1

def collatz_seq(n):
    if n % 2 == 0:
        return int(n/2)   
    else:
        return int(3 * n + 1)

for i in range(2,1000000):
    seen = [i]
    while seen[-1] not in cache:
        seen.append(collatz_seq(seen[-1]))   
    prev = cache[seen[-1]]
    for j in reversed(seen[:-1]):
        cache[j] = prev + 1
        prev = prev + 1

print(max(cache, key=cache.get))



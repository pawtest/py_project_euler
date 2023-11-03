

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
number_to_divisors = dict()

def proper_divisors(n):
    p_divisors = [1]
    for prime in primes:
        candidate_divisor = prime
        while candidate_divisor ** 2 <= n:
            if n % candidate_divisor == 0:
                p_divisors.append(candidate_divisor)
                p_divisors.append(n / candidate_divisor)
            candidate_divisor += prime 
    return p_divisors

total = 0
for i in range(1,10000):
    if i not in number_to_divisors:
        sum_proper_divisor = int(sum(set(proper_divisors(i))))
        number_to_divisors[i] = sum_proper_divisor
        if sum_proper_divisor not in number_to_divisors:
            sum_proper_divisor_rev = int(sum(set(proper_divisors(sum_proper_divisor))))
            number_to_divisors[sum_proper_divisor] = sum_proper_divisor_rev
        if i != sum_proper_divisor and number_to_divisors[sum_proper_divisor] == i:
            total += i + sum_proper_divisor

print(total)

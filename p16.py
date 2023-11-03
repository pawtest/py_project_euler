digits = [2]
for i in range(2,1001):
    print("i:", i)
    remainder = 0
    for j in range(len(digits)):  
        digits[j] = remainder + digits[j] * 2
        remainder = 0
        if digits[j] >= 10:
            digits[j] = digits[j] % 10
            if j + 2 > len(digits):
                digits.append(1)
            else:
                remainder = 1
    print("\t\tdigits:", digits)
                
print(sum(digits))


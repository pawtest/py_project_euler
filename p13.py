f = open("13_input.txt", "r")
numbers = f.read().splitlines()
print(numbers[0])
print(numbers[2])

answer = []
remainder = 0
for i in range(50):
    sum = remainder
    for number in numbers:
        sum += int(number[49-i])
    digit = sum % 10
    answer.append(digit)
    remainder = int((sum - digit) / 10)

print(remainder)
print(answer[40:])



def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Nhập một số nguyên không âm: "))
print(f"{n}! = {factorial(n)}")

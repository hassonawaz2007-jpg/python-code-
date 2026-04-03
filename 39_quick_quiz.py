def count_zeros(n):
    # Base case: if n becomes 0, stop
    if n == 0:
        return 0
    
    # Check the last digit
    if n % 10 == 0:
        return 1 + count_zeros(n // 10)
    else:
        return count_zeros(n // 10)


# Example
number = 102030
print("Number of zeros in", number, "is:", count_zeros(number))
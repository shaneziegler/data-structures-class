# Practice Problem¶
# Implement sum_integers(n) to calculate the sum of all integers from  1  to  𝑛  using recursion. For example, sum_integers(3) should return  6  ( 1+2+3 ).

def sum_integers(n):
    if n == 1:
        return 1
    return n + sum_integers(n-1)

print(sum_integers(1))
print(sum_integers(2))
print(sum_integers(3))
print(sum_integers(6))

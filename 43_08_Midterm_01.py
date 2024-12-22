def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def sum_fibonacci(sequence):
    return sum(sequence)
n = int(input("Enter the number of terms: "))
fib_sequence = fibonacci_sequence(n)
fib_sum = sum_fibonacci(fib_sequence)
print("Fibonacci sequence:", fib_sequence)
print("Sum of the Fibonacci sequence:", fib_sum)
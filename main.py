# 1. Simple Recursive Algorithm
# 2. Algorithms within Data Structures
# 3. Divide & Conquer
# 4. Greedy Algorithms
# 5. Dynamic Programming


def main():
    print(iterative_factorial(5))
    print(recursive_factorial(5))


def iterative_factorial(n):
    """Iterative factorial function"""
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def recursive_factorial(n):
    """Recursive factorial function"""
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)


if __name__ == "__main__":
    main()

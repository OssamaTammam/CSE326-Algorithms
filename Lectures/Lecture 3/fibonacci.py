def fibonacci_top_down(n, memo={}):
    # base case
    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        memo[n] = n
    else:
        memo[n] = fibonacci_top_down(n-1, memo) + fibonacci_top_down(n-2, memo)

    return memo[n]


def fibonacci_bottom_up(n):
    pass


n = 10

print(f"Top down approach = {fibonacci_top_down(n)}\nBottom up approach = ")

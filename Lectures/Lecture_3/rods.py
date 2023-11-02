def rod_bottom_up(p, n):
    revenue = [0] * (n+1)

    for i in range(1, n + 1):
        max_revenue = -1

        for j in range(1, i+1):
            max_revenue = max(max_revenue, p[j] + revenue[i - j])

        revenue[i] = max_revenue

    return revenue[n]


def rod_top_down(p, n):
    revenues = [0] * (n + 1)

    def rod_top_down_helper(length):
        # if problem has been solved before return the answer
        if revenues[length] != 0:
            return revenues[length]

        if length == 0:
            max_revenue = 0
        else:
            max_revenue = -1
            for i in range(1, length + 1):
                max_revenue = max(
                    max_revenue, p[i] + rod_top_down_helper(length - i))
        revenues[length] = max_revenue
        return max_revenue

    return rod_top_down_helper(n)


# Price for rods of length 0 to 10
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

max_rev_bottom_up = [rod_bottom_up(prices, length)
                     for length in range(len(prices))]
print(f"Bottom up = {max_rev_bottom_up}")

max_rev_top_down = [rod_top_down(prices, length)
                    for length in range(len(prices))]
print(f"Top down = {max_rev_top_down}")

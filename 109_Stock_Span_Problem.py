def calculate_stock_span(prices):
    n = len(prices)
    span = [0] * n
    stack = []  # stores index of prices

    for i in range(n):
        # Pop elements from stack while stack is not empty and price[stack top] <= price[i]
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        # If stack is empty, span = i + 1 (no greater element to the left)
        span[i] = i + 1 if not stack else i - stack[-1]

        # Push this element's index to stack
        stack.append(i)

    return span

def main():
    prices = [100, 80, 60, 70, 60, 75, 85]
    print("Prices:", prices)
    print("Spans: ", calculate_stock_span(prices))

if __name__ == "__main__":
    main()

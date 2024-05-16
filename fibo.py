import sys

def fibo(n):
    try:
        n = int(n)
    except ValueError:
        raise ValueError("入力は整数でなければなりません。")

    if n < 0:
        raise ValueError("負数の入力は無効です。")
    elif n > 99:
        raise ValueError("100以上の入力は無効です。")

    memo = [-1 for _ in range(max(n, 2))]
    memo[0] = 1
    memo[1] = 1

    for i in range(2, n):
        if (memo[i] == -1):
            memo[i] = memo[i-1] + memo[i-2]

    return memo[n-1]

if __name__ == "__main__":
    n = int(sys.argv[1])

    print('input:', n)
    result = fibo(n)
    print('ans:', result)
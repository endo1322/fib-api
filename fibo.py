import sys

def fibo(n):

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
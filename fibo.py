import sys

def fibo(n):
    return n

if __name__ == "__main__":
    n = int(sys.argv[1])

    print('input:', n)
    result = fibo(n)
    print('ans:', result)
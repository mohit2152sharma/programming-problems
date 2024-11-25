import sys
from time import time


def iterate(n):

    for i in range(int(n)):
        pass


if __name__ == "__main__":
    n = sys.argv[-1]
    t0 = time()
    iterate(n)
    print(f"Time taken for {n} iterations: {time() - t0} seconds")

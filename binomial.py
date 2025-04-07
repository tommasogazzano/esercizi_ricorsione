#Exercise
import scipy
def binomial(n, k):
    if n == k or k == 0:
        return 1
    else:
        return binomial(n - 1, k - 1) + binomial(n - 1, k)

if __name__ == '__main__':
    print(binomial(5, 2))
    print(scipy.special.binom(5, 2))

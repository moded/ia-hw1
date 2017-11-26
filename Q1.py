import math

def k_perms(k):
    return (math.factorial(2*k))/2**k




if __name__ == '__main__':
    for i in range(1, 11):
        print("#permutations for k = {} is {}".format(i,k_perms(i)))


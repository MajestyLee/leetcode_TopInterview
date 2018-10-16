'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''
class Solution:
    number = []
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # primes = []
        # for possiblePrime in range(2, n):
        # # Assume number is prime until shown it is not.
        #     isPrime = True
        #     for num in range(2, int(possiblePrime ** 0.5) + 1):
        #         if possiblePrime % num == 0:
        #             isPrime = False
        #             break
        #     if isPrime:
        #         primes.append(possiblePrime)
        # return(len(primes))
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)
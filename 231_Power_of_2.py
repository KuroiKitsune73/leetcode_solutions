class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n & (n-1) == 0) and n != 0:
            return True
        else:
            return False
'''
Explanation:
The natural number represented by the power of two has one unit in its binary notation

For example:

n: 10000000, 01000000, 00100000, ..., 00000001

What happens if we take one from such a number?

n-1: 01111111, 00111111, 00011111, ..., 00000000

Now, taking and between n and n-1, we get all the zeros in the binary record.
For a number that is not a power of two, we will not get such "inverted" records.
By analogy with the decimal system: only after taking a round number like
10000 or 1000 a unit, we will get all the nines as a result.

You can not check for n=0, because according to the condition of the task
n is natural. That is, the final decision will look like this:
(n & (n-1) == 0)

https://ru.stackoverflow.com/questions/1192288
'''
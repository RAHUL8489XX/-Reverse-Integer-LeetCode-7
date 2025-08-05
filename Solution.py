class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = int(str(x)[::-1]) * sign

        if -2**31 <= reversed_num <= 2**31 - 1:
            return reversed_num
        return 0

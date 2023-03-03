class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i = 0
        while True:
            if i == len(x) // 2:
                break
            if x[i] != x[len(x) - 1 - i]:
                return False
            i += 1
        return True
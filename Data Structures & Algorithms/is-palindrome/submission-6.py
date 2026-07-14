class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            leftC, rightC = s[l], s[r]

            if not self.isAlphaNum(leftC):
                l += 1
                continue

            if not self.isAlphaNum(rightC):
                r -= 1
                continue

            if leftC.lower() != rightC.lower():
                return False

            l += 1
            r -= 1

        return True

    def isAlphaNum(self, c):
        return (('A' <= c <= 'Z') or 
                ('a' <= c <= 'z') or 
                ('0' <= c <= '9'))
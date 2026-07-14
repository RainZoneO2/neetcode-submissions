class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            leftC, rightC = s[l], s[r]

            if not (('A' <= leftC <= 'Z') or ('a' <= leftC <= 'z') or ('0' <= leftC <= '9')) :
                l += 1
                continue

            if not (('A' <= rightC <= 'Z') or ('a' <= rightC <= 'z') or ('0' <= rightC <= '9')):
                r -= 1
                continue

            if leftC.lower() != rightC.lower():
                return False

            l += 1
            r -= 1

        return True
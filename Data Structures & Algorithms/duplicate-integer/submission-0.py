class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkList: list[int] = []
        for n in nums:
            if n in checkList:
                return True
            else:
                checkList.append(n)
        return False

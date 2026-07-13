class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffDict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffDict:
                return [diffDict.get(diff), i]
            else:
                diffDict[nums[i]] = i
            print(diffDict)
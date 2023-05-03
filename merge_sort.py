class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                print(x,y)
                if (nums[x] + nums[y]) == target:
                    return [x, y]


a = [5, 4, 2, 7]
t = 11
b = Solution()
print(b.twoSum(a, t))

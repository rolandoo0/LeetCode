class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sum = None
        counter = 0
        startNumber = nums[0]
        index = nums.index(startNumber)
        while sum != target:
            if (startNumber + nums[index]) != target:
                if index < (len(nums) - 1):
                    index += 1
                else:
                    counter += 1
                    startNumber = nums[counter]
                    index = nums.index(startNumber) + 1
                    if index == (len(nums) - 1):
                        index = 0
            else:
                if nums.index(startNumber) == nums.index(nums[index]):
                    indices = [i for i, x in enumerate(nums) if x == startNumber]
                    if len(indices) > 1:
                        sum = startNumber + nums[indices[1]]
                        index = indices[1]
                        break
                    else:
                        if index < (len(nums) - 1):
                            index += 1
                else:
                    sum = startNumber + nums[index]

        print([nums.index(startNumber), index])


sol = Solution()
sol.twoSum(nums=[-1, -2, -3, -4, -5], target=-8)

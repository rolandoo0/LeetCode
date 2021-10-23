from operator import itemgetter


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        try:
            counter = 0
            starter = nums[0]
            if len(nums) < 3:
                raise
            else:
                while True:
                    for i in range(len(nums)):
                        if i == (len(nums) - 1):
                            for t in triplets:
                                t.sort()

                            sorteedd = sorted(triplets)

                            for item in sorteedd:
                                indices = [
                                    i for i, x in enumerate(sorteedd) if x == item
                                ]
                                if len(indices) > 1:
                                    sorteedd.remove(item)
                            print(sorteedd)
                            return sorteedd

                        for j in range(i + 1, len(nums)):
                            for k in range(j + 1, len(nums)):
                                numOnIndexI = nums[i]
                                numberOnIndexJ = nums[j]
                                numberOnIndexIplusOne = nums[k]
                                sum = (
                                    numOnIndexI + numberOnIndexJ + numberOnIndexIplusOne
                                )
                                if sum == 0:
                                    listed = [
                                        numOnIndexI,
                                        numberOnIndexJ,
                                        numberOnIndexIplusOne,
                                    ]
                                    try:
                                        triplets[0]
                                    except:
                                        check = False
                                    for t in triplets:
                                        check = all(item in t for item in listed)
                                        if listed[0] == listed[1]:
                                            check = False
                                        if check is True:
                                            break
                                    if check is True:
                                        pass
                                    else:
                                        if listed in triplets:
                                            pass
                                        else:
                                            triplets.append(
                                                [
                                                    numOnIndexI,
                                                    numberOnIndexJ,
                                                    numberOnIndexIplusOne,
                                                ]
                                            )
                                else:
                                    pass

        except Exception as e:
            if len(triplets) > 0:
                print(triplets)
                return triplets
            else:
                print("[]")
                return []


sol = Solution()
sol.threeSum(nums=[-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0])

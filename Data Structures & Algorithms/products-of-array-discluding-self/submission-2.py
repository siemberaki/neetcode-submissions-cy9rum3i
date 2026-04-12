class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        resu = [0] * len(nums)

        for i in range(len(nums)):

            num = 1


            for j in range(len(nums)):

                if i == j :

                    continue


                num = num *nums[j] 

            resu[i] = num  

        return resu            


        
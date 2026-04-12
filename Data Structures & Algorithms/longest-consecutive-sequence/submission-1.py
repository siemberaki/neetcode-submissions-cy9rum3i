class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

       
        a = set(nums)

        longest = 0
         
        for i in a :

            if (i-1) not in a :

                l = 1

                while (i + l) in a :
                    
                    l = l + 1 


                longest = max (longest, l)   


        return longest         

        


        


        
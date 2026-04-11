
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        
        my_check = set()

 
        for i in nums :

            if i in my_check :

                return True

            else :
                my_check.add(i)


        return  False          
            



        
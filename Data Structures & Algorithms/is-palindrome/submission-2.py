class Solution:
    def isPalindrome(self, s: str) -> bool:
        chara = ""

        for i in s :

            if i.isalnum():

                chara = chara + i.lower()

        return chara == chara[::-1]    

        


        
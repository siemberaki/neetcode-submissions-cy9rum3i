class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        a = set()
        max_num = 0

        for r in range(len(s)):

            while s[r] in a:

                
                a.remove(s[l])


                l += 1
            
 
            a.add(s[r])
            max_num = max(max_num, r - l + 1)

        return max_num





   
        






        

     
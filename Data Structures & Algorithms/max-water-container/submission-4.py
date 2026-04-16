class Solution:
    def maxArea(self, heights: List[int]) -> int:        
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r :
            w = r - l
            h = min(heights[r], heights[l]) 
            area = h * w
            max_area = max (area, max_area)
            if heights[l] <  heights[r]:
                l = l + 1
            else : 
                r = r - 1
        return max_area        












































        l = 0 
        r= len(heights) - 1
        max_area = 0
        while l < r :
            w = r - l

            height = min (heights[l] , heights[r])
            area = height * w

            max_area = max(max_area , area)

            if heights[l] < heights[r] :
                l += 1

            else :
                r -= 1    

        return max_area    

        
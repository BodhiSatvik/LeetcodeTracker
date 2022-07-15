class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        maxL = []
        maxR = []
        res = 0

        for i in range(len(height)):
            if i == 0:
                l = 0
                maxL.append(l)
                continue
            l = max(height[i-1], l)
            maxL.append(l)

        for i in range(len(height) - 1, -1, -1):
            if i == len(height)-1:
                r = 0
                maxR.append(r)
                continue
            r = max(height[i+1], r)
            maxR.append(r)

        maxR = maxR[::-1]
        res = 0
        for i in range(len(height)):
            mini = min(maxR[i], maxL[i])
            water = mini - height[i]
            if water < 0:
                water = 0
            res += water
        return res
            
            
            
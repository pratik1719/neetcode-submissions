class Solution:
    def trap(self, height: List[int]) -> int:
        # water trap condition 
        l,r=0,len(height)-1
        lmax=0
        rmax=0
        area = 0
        while(l<r):
            if (height[l]<=height[r]):
                if(height[l]>lmax):
                    lmax=height[l]
                else:
                    area += lmax - height[l]
                l+=1
            else:
                if(height[r]>rmax):
                    rmax=height[r]
                else:
                    area += rmax - height[r]
                r-=1
        return area



        
            




            

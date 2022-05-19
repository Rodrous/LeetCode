class Solution(object):
    def searchRange(self, nums, target):
        l = 0
        r = len(nums)-1
        foundTarget = False
        breakP = 0
        firstP = 0
        lastP = 0
        while l<=r :
            mid = (l+r)//2
            if nums[mid]==target :
                if not breakP :
                    breakP = mid
                    foundTarget = True
                l=mid+1
                lastP = mid
            elif nums[mid] > target :
                r= mid-1
            else :
                l=mid+1
        if foundTarget :
            r = breakP
            l = 0
            while l<=r:
                mid = (l+r)//2
                if nums[mid]==target :
                    r=mid-1
                    firstP = mid
                else :
                    l=mid+1
        if not foundTarget :
            return [-1,-1]
        return [firstP,lastP]
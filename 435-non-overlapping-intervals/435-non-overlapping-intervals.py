class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key= lambda x:x[0])
        res = [intervals[0]]
        
        for s,e in intervals:
            
            lastEnd = res[-1][1]
            
            if s < lastEnd:
                res[-1][1] = min(lastEnd,e)
            else:
                res.append([s,e])
        
        return len(intervals)-len(res)
        
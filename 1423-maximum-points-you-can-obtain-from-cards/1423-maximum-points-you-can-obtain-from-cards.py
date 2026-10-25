class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        lsum=0
        rsum=0
        n=len(cardPoints)
        if k==n:
            return sum(cardPoints)
        for i in  range(0,k):
            lsum=lsum + cardPoints[i]
            maxsum=lsum
        right_idx=n-1
        for j in range(k-1,-1,-1 ):
            lsum=lsum-cardPoints[j]
            rsum=rsum + cardPoints[right_idx]
            right_idx=right_idx - 1
            maxsum= max(maxsum,lsum+rsum)
        return maxsum
        
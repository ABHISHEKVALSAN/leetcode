class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        a = [1 for _ in ratings]
        i = 1
        while i < n:
            if ratings[i] > ratings[i-1]:
                a[i] = a[i-1]+1
            i+=1
        print(a)
        i = n - 2
        while i>=0:
            if ratings[i]>ratings[i+1]:
                a[i] = max(a[i],a[i+1]+1)
            i-=1 
        print(a)
        return sum(a)
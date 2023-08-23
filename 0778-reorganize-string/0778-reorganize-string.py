from collections import deque
from heapq import heappush as hpush, heappop as hpop
class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}
        for ch in s:
            d[ch] = d.get(ch,0)+1

        hp = []
        for ch,freq in d.items():
            hpush(hp,(-freq,ch))
        result =''
        while len(hp)>1:
            freq1, ch1 = hpop(hp)
            freq2, ch2 = hpop(hp)
            result+=ch1
            result+=ch2
            if freq1<-1:
                hpush(hp,(freq1+1,ch1))
            if freq2<-1:
                hpush(hp,(freq2+1,ch2))
        if len(hp)==1:
            freq, ch = hpop(hp)
            if freq==-1:
                result+=ch
            else:
                return ''
        return result

            



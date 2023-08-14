from itertools import combinations
from heapq import heappush as hpush, heappop as hpop, heappushpop as hpp
from collections import deque
class Solution:
    def __init__(self):
        self.mxb = 0
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort()
        n = len(items)
        i = 0
        new_items = []
        rest_items = []
        curr_cat_dict = {}
        total_profit = 0
        while i<n and len(new_items)<k:
            profit, cat = items.pop()
            if cat not in curr_cat_dict:
                hpush(new_items,(profit,cat))
                total_profit += profit
                curr_cat_dict[cat] = 1
            else:
                rest_items.append((profit,cat))
            i+=1
        j = 0
        while len(new_items)<k:
            profit, cat = rest_items[j]
            total_profit += profit
            curr_cat_dict[cat] = curr_cat_dict.get(cat,0)+1
            hpush(new_items,(profit,cat))
            j+=1
            
        self.mxb = max(self.mxb, total_profit+len(curr_cat_dict)**2)
        for r_profit,r_cat in rest_items[j:]:
            h_profit, h_cat = hpop(new_items)
            total_profit = total_profit - h_profit + r_profit
            if curr_cat_dict[h_cat]==1:
                del curr_cat_dict[h_cat]
            else:
                curr_cat_dict[h_cat]-=1
            curr_cat_dict[r_cat] = curr_cat_dict.get(r_cat,0)+1
            self.mxb = max(self.mxb, total_profit+len(curr_cat_dict)**2)
            hpush(new_items,(r_profit,r_cat))
        return self.mxb
        
        
            
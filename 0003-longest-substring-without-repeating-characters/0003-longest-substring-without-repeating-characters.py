class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start_index = 0
        end_index = 0
        d = {}
        for i, ch in enumerate(s):
            if ch in d:
                start_index = max(start_index,d[ch]+1)
            end_index = i
            d[ch]=i
            max_len = max(max_len, end_index - start_index + 1)
            #print(i, ch, d[ch], start_index, end_index, max_len)
        return max_len


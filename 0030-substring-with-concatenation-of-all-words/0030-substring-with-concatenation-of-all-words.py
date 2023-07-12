class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        m = len(words)
        word_len = len(words[0])
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word,0)+1
        left_index = 0
        right_index = 0
        ans = []
        ss_word_freq = {}
        i = 0
        while i < word_len:
            left_index = i
            while left_index <= len(s) - len(words)*len(words[0]):
                right_index = left_index
                ss_word_freq = {}
                while right_index < len(s):
                    word = s[right_index:right_index+word_len]
                    if word in word_freq:
                        ss_word_freq[word] = ss_word_freq.get(word,0)+1
                        if ss_word_freq==word_freq:
                            ans.append(left_index)
                            left_word = s[left_index:left_index+word_len]
                            ss_word_freq[left_word]-=1
                            left_index+=word_len
                        else:
                            while ss_word_freq[word] > word_freq[word]:
                                left_word = s[left_index:left_index+word_len]
                                ss_word_freq[left_word]-=1
                                left_index+=word_len
                    else:
                        break
                    right_index+=word_len
                left_index+=word_len
            i+=1
        return ans
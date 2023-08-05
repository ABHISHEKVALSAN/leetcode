class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_hash(word):
            word = list(word)
            word.sort()
            word_hash = {}
            for ch in word :
                word_hash[ch] = word_hash.get(ch,0)+1
            hash_word = ''
            for k,v in word_hash.items():
                hash_word+=k
                hash_word+=str(v)
            return hash_word
        result = {}
        for word in strs:
            hw = get_hash(word)
            result[hw] = result.get(hw,[]) + [word]
        return result.values()

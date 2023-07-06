class Solution:
    def justify_row(self, row, maxWidth):
        if " " not in row:
            return row+" "*(maxWidth-len(row))
        row = row.split(' ')
        n = len(row)
        l = 0
        for word in row:
            l+=len(word)
        spaces = [(maxWidth-l)//(n-1) for _ in range(n-1)]
        i = 0
        while i < (maxWidth-l)%(n-1):
            spaces[i]+=1
            i+=1
        i = 0
        s = ''
        while i < n-1:
            s += row[i]+' '*spaces[i]
            i+=1
        s+=row[-1]
        return s

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        n = len(words)
        i = 0
        while i < n:
            if len(words[i])==maxWidth:
                result.append(words[i])
                i+=1
                continue
            s = words[i]
            j = i+1
            while j < n:
                if len(s+' '+words[j]) > maxWidth:
                    break
                else:
                    s+=f' {words[j]}'
                j+=1
            result.append(s)
            i=j
        i = 0
        n = len(result)
        while i < n-1:
            result[i] = self.justify_row(result[i], maxWidth)
            i+=1
        result[-1] = result[-1]+' '*(maxWidth - len(result[-1]))
        return result
class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n-1):
            curr = result[0]
            count = 1
            temp_result = ""
            i = 1
            while i < len(result):
                if result[i]==curr:
                    count+=1
                    i+=1
                else:
                    temp_result+=str(count)+curr
                    curr = result[i]
                    count = 0
            temp_result+=str(count)+curr
            result = temp_result
        return result

        
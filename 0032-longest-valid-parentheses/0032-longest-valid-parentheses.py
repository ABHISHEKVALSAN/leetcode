class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        is_valid = [0 for i in s]

        for i, ch in enumerate(s):
            if ch=='(':
                stack.append([ch,i])
            elif ch==')':
                if len(stack)>=1:
                    if stack[-1][0]=='(':
                        chi = stack.pop()
                        is_valid[i] = 1
                        is_valid[chi[1]] = 1
                    else:
                        stack.append([ch,i])
                else:
                    stack.append([ch,i])
        csum = 0
        max_len = 0
        for i in is_valid:
            if i==1:
                csum+=1
                max_len = max(max_len,csum)
            else:
                csum = 0

        print(is_valid)
        return max_len
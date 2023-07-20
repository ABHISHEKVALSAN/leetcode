class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #print(tokens)
        stack = []
        for e in tokens:
            if e not in '+-/*':
                stack.append(int(e))
            elif e in '+-/*':
                #print(e,stack)
                b = stack.pop()
                a = stack.pop()
                if e=='+':
                    stack.append(a+b)
                elif e=='-':
                    stack.append(a-b)
                elif e=='*':
                    stack.append(a*b)
                elif e=='/':
                    if a>0 and b>0 or a<0 and b<0 or a/b==a//b:
                        stack.append(a//b)
                    else:
                        stack.append((a//b)+1)
        return int(stack[-1])
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace('//','/')
        stack = []
        for directory in path.split('/'):
            if directory=='':
                continue
            if directory=='..':
                if len(stack)>0:
                    stack.pop()
            elif directory=='.':
                pass
            else:
                stack.append(directory)
        return '/'+'/'.join(stack)
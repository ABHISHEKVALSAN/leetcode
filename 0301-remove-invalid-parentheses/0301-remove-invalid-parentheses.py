from itertools import combinations
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string):
            stack = []
            for ch in string:
                if ch not in ['(',')']:
                    continue
                if len(stack)==0:
                    if ch==')':
                        return False
                    else:
                        stack.append(ch)
                else:
                    if ch==')':
                        if stack[-1]=='(':
                            stack.pop()
                        else:
                            return False
                    else:
                        stack.append(ch)
            return len(stack)==0

        def get_invalid(string):
            stack = []
            for ind, ch in enumerate(list(string)):
                if ch not in ['(',')']:
                    continue
                if len(stack)==0:
                    stack.append([ch,ind])
                else:
                    if ch==')'and stack[-1][0]=='(':
                        stack.pop()
                    else:
                        stack.append([ch,ind])
            return stack
        def strip_left(string):
            if len(string)==0:
                return string
            string = string[::-1]
            stack = []
            while string:
                if string[-1]=='(':
                    break
                ch = string[-1]
                string = string[:-1]
                if ch!=')':
                    stack.append(ch)
            while stack:
                string+=stack.pop()
            return string[::-1]
        def strip_right(string):
            if len(string)==0:
                return string
            stack = []
            while string:
                if string[-1]==')':
                    break
                ch = string[-1]
                string = string[:-1]
                if ch!='(':
                    stack.append(ch)
            while stack:
                string+=stack.pop()
            return string
        def get_string(string,ch,count):
            index_list = []
            for i, c in enumerate(list(string)):
                if c==ch:
                    index_list.append(i)
            print(string,ch,count,index_list)
            for index_comb in combinations(index_list,count):
                temp_string = list(string).copy()
                for index in index_comb:
                    temp_string[index]=''
                yield ''.join(temp_string)

    
        string = strip_left(strip_right(s))
        invalid_stack = get_invalid(string)
        cb_count = 0
        cb_index = -1
        ob_count = 0
        ob_index = len(string)
        for ip in invalid_stack:
            if ip[0]==')':
                cb_count+=1
                cb_index = ip[1]
        for ip in invalid_stack:
            if ip[0]=='(':
                ob_count+=1
                ob_index=min(ob_index,ip[1])

        curr_left = []
        for s in get_string(string[:cb_index+1],')',cb_count):
            curr_left.append(s)
        curr_right = []
        for s in get_string(string[ob_index:],'(',ob_count):
            curr_right.append(s)

        mid_string = string[cb_index+1:ob_index]
        for i,e in enumerate(curr_left):
            curr_left[i]+=mid_string
    
        final_ans = set()
        i = 0
        while i < len(curr_left):
            j = 0
            while j < len(curr_right):
                final_ans.add(curr_left[i]+curr_right[j])
                j+=1
            i+=1
        ans = []
        for s in final_ans:
            if is_valid(s):
                ans.append(s)
        return ans

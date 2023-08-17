class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_valid_ipv4(string):
            if '.' not in string:
                return False
            x = string.split('.')
            if len(x)!=4:
                return False
            for num in x:
                if 1<=len(num)<=3:
                    pass
                else:
                    return False
                for d in num:
                    if d not in '1234567890':
                        return False
                if num.startswith('0'):
                    if int(num)!=0:
                        return False
                    elif len(num)!=1:
                        return False
                if 0<=int(num)<=255:
                    pass
                else:
                    return False
            return True
        def is_valid_ipv6(string):
            if ':' not in string:
                return False
            x = string.split(':')
            if len(x)!=8:
                return False
            for num in x:
                if 1<=len(num)<=4:
                    pass
                else:
                    return False
                for d in num:
                    if d not in '1234567890ABCDEFabcdef':
                        return False
            return True
        if is_valid_ipv4(queryIP):
            return "IPv4"
        elif is_valid_ipv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
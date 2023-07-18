from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.count = 0
        self.cap = capacity
        self.d = {}
        self.arr = deque([])
        

    def get(self, key: int) -> int:
        #print('g',key,self.arr,self.d,self.count,self.cap)
        if key not in self.d:
            return -1
        else:
            val = self.d[key]
            self.arr.remove(key)
            self.d.pop(key)
            self.count-=1
            self.put(key,val)
            return val


    def put(self, key: int, value: int) -> None:
        #print('p',key,value,self.arr,self.d,self.count,self.cap)
        if key in self.d:
            self.arr.remove(key)
            self.count-=1
            self.d.pop(key)
            self.put(key,value)
        elif self.count==self.cap:
            remove_key = self.arr.popleft()
            self.count-=1
            self.d.pop(remove_key)
            self.put(key, value)
        else:
            self.arr.append(key)
            self.d[key]=value
            self.count+=1



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
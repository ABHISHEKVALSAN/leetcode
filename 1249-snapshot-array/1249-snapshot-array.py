class SnapshotArray:

    def __init__(self, length: int):
        self.arr = {}
        self.arr_snap = {index: {0:0} for index in range(length)}
        self.snap_id = 0

    def bin_search(self,arr, id):
        first = 0
        last = len(arr)
        mid = (first+last)//2
        if id < arr[0]:
            return 0
        if id > arr[-1]:
            return arr[-1]
        while first<=last:
            if arr[mid]==id:
                return id
            elif arr[mid]<id:
                first = mid+1
            elif arr[mid]>id:
                last = mid-1
            mid = (first+last)//2
        if arr[mid]<id:
            return arr[mid]
        else:
            return arr[mid-1]



    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        for index,value in self.arr.items():
            self.arr_snap[index][self.snap_id]=value
        self.arr = {}
        self.snap_id+=1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        try:
            return self.arr_snap[index][snap_id]
        except:
            snap_id =self.bin_search(list(self.arr_snap[index].keys()),snap_id)
            return self.arr_snap[index][snap_id]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
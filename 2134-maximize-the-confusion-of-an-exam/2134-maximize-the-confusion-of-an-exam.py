class Solution:
    def max_sum(self, arr, k):
        n = len(arr)
        ans = 0
        i = 0
        j = 1
        curr_sum = arr[0]
        alt_rem = k
        ans = curr_sum + alt_rem
        while i < j and j < n:
            if arr[j] > k:
                if j==n-1:
                    ans = max(ans, curr_sum+alt_rem)
                    break
                i = j + 1
                j += 2
                curr_sum = arr[i]
                alt_rem = k
                ans = max(ans,curr_sum+alt_rem)
            elif alt_rem >= arr[j]:
                alt_rem-=arr[j]
                curr_sum+=arr[j]
                if j+1 < n:
                    curr_sum+=arr[j+1]
                ans = max(ans, curr_sum + alt_rem)
                j+=2
            else:
                ans = max(ans,curr_sum+alt_rem)
                curr_sum-=arr[i]
                curr_sum-=arr[i+1]
                alt_rem+=arr[i+1]
                i+=2
        print(alt_rem, ans, curr_sum, i, j)
        ans = max(curr_sum, ans)
        return ans
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        if n==1:
            return 1
        elif n<=k:
            return n
        i = 0
        curr = answerKey[0]
        arr = [0]
        while i < n:
            if answerKey[i]==curr:
                arr[-1]+=1
            else:
                curr = answerKey[i]
                arr.append(1)
            i+=1

        n = len(arr)
        even_sum = 0
        odd_sum = 0
        i = n-1
        while i>=0:
            if i%2==0:
                even_sum+=arr[i]
            else:
                odd_sum+=arr[i]
            i-=1
        if even_sum <= k or odd_sum<=k:
            return len(answerKey)
        print(arr, len(arr))
        sum_even = self.max_sum(arr,k)
        if n%2==0:
            sum_odd = self.max_sum(arr[::-1],k)
        else:
            arr[-1]+=arr[0]
            sum_odd = self.max_sum(arr[1:],k)
        print(sum_even, sum_odd)
        return min(max(sum_odd,sum_even), len(answerKey))
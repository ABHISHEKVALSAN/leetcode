class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(target, nums):
            for i,num in enumerate(nums):
                if num == target:
                    yield [num]
                elif num < target:
                    for ans in solve(target-num,nums[i:]):
                        yield [num]+ans
        candidates.sort()
        while len(candidates)>0 and candidates[-1]>target:
            candidates.pop()
        if len(candidates)==0:
            return []
        canidates = candidates[::-1]
        result = []
        for ans in solve(target,candidates):
            result.append(ans)
        return result

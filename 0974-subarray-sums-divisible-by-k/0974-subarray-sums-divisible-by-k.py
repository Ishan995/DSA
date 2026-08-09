class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        curr_sum=0
        seen_rem={0:1}
        n=len(nums)

        for i in range (n):
            curr_sum+=nums[i]
            rem=curr_sum%k
            if (curr_sum%k) in seen_rem:
                count+=seen_rem[rem]
            seen_rem[rem]=seen_rem.get(rem,0)+1
        return count

        
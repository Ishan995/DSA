class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n=len(nums)

        def get_next(index,curr_dir):
            next_index=(index+nums[index])%n
            next_dir=1 if nums[next_index]>0 else -1
            if curr_dir!=next_dir or index==next_index:
                return -1
            return next_index

        for i in range(n):
            slow=i
            fast=i
            curr_dir=1 if nums[i]>0 else -1

            while True:
                slow=get_next(slow,curr_dir)
                fast=get_next(fast,curr_dir)

                if slow==-1 or fast==-1:#invalid index
                    break
                
                fast=get_next(fast,curr_dir)

                if fast==-1:#invalid index
                    break
                
                if slow==fast:
                    return True
        return False

    
        
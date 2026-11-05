class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a = nums1
        b = nums2
        
        # Ensure 'a' is the smaller array for O(log(min(m, n))) binary search speed
        if len(a) > len(b):
            a, b = b, a
            
        total = len(a) + len(b)
        half = total // 2
        
        # Binary search pointers over the indices of array 'a'
        low = -1
        high = len(a)
        
        while low <= high:
            # Find the partition index for array 'a'
            i = (low + high) // 2
            # Automatically derive the partition index for array 'b'
            j = half - i - 2

            # Define left and right boundaries for both arrays (with infinity fallbacks)
            aleft = a[i] if i >= 0 else float("-inf")
            aright = a[i + 1] if i + 1 < len(a) else float("inf")
            bleft = b[j] if j >= 0 else float("-inf")
            bright = b[j + 1] if j + 1 < len(b) else float("inf")

            # Check if we have successfully partitioned both arrays correctly
            if aleft <= bright and bleft <= aright:
                # If total elements is odd, the median is the minimum of the right side
                if total % 2 != 0:
                    return min(aright, bright)
                # If total elements is even, average the max of left side and min of right side
                return (max(aleft, bleft) + min(aright, bright)) / 2
            
            # If a's left value is too big, we took too many elements from 'a' -> shift left
            elif aleft > bright:
                high = i - 1
            # Otherwise, we took too few elements from 'a' -> shift right
            else:
                low = i + 1


        
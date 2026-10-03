class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        a = nums
        # int n = a.size();
        n = len(a)

        # vector<int> res(n);
        res = [0] * n

        # for (i = 0; i < n; i++)
        for i in range(n):

            # res[i] = 1;
            res[i] = 1

            # for (j = 0; j < i; j++)
            for j in range(i):

                # if (a[j] < a[i])
                if a[j] < a[i]:
                    # res[i] = max(res[i], res[j] + 1);
                    res[i] = max(res[i], res[j] + 1)

        # int ans = 1;
        ans = 1

        # for (i = 0; i < n; i++) ans = max(ans, res[i]);
        for i in range(n):
            ans = max(ans, res[i])

        # return ans;
        return ans
  
        
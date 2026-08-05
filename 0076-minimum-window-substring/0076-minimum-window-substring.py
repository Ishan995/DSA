class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        window = {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have = 0
        need = len(countT)

        res = [-1, -1]
        reslen = float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update result
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1

                # shrink from left
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        if reslen == float("infinity"):
            return ""

        return s[l:r + 1]



       

    
        
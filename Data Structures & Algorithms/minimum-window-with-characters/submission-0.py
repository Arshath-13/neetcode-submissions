class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s  :
            return ""
        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0 ) + 1
        required = len(dict_t)
        left, right = 0,0
        formed = 0
        window_count = {}
        ans = float("inf"),None,None

        while right < len(s):
            char = s[right]
            window_count[char] = window_count.get(char,0)+1
            if char in dict_t and window_count[char]==dict_t[char]:
                formed += 1
            
            while left <= right and formed == required :
                char = s[left]

                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left,right)
                window_count[char]-=1
                if char in dict_t and window_count[char] < dict_t[char]:
                    formed -= 1
                left += 1
            right += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
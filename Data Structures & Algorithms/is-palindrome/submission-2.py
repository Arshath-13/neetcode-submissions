class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = ""
        for i in s:
            if i.isalnum():
                d+=i.lower()

        return d==d[::-1]
    
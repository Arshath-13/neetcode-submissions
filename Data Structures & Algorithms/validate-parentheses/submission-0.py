class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for ch in s:
            if ch in brackets:
                top_element = stack.pop() if stack else '#'
                if brackets[ch] != top_element:
                    return False
            else:
                stack.append(ch)
                
        return not stack
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if n > m:
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        # Build frequency arrays
        for i in range(n):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        # Check first window
        if freq1 == freq2:
            return True

        # Slide the window
        for i in range(n, m):
            # Add new character
            freq2[ord(s2[i]) - ord('a')] += 1
            # Remove leftmost character
            freq2[ord(s2[i - n]) - ord('a')] -= 1

            if freq1 == freq2:
                return True

        return False
        
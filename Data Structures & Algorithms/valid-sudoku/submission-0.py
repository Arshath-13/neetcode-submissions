class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for a in range(9)]
        cols = [set() for a in range(9)]
        boxes = [set() for a in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                box = (r//3)*3 + (c//3)
                
                if num == ".":
                    continue
                if num in rows[r]:
                    return False
                if num in cols[c]:
                    return False
                if num in boxes[box]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)
        return True
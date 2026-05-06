class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        quadrants = {}

        rows = {}

        cols = {}

        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n == ".":
                    continue
                quadrant = (i // 3, j // 3)
                
                if quadrant not in quadrants:
                    quadrants[quadrant] = set()
                if i not in rows:
                    rows[i] = set()
                if j not in cols:
                    cols[j] = set()
                
                if n in quadrants[quadrant] or n in rows[i] or n in cols[j]:
                    return False
                
                quadrants[quadrant].add(n)
                rows[i].add(n)
                cols[j].add(n)

        return True

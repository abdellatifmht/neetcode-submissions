from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for num in row:
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
        
        for col in zip(*board):
            seen = set()
            for num in col:
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
        
        seen_square = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[0])):
                square_index = (row // 3) * 3 + (col // 3)
                num = board[row][col]
                if num == ".":
                    continue
                if num in seen_square[square_index]:
                    return False
                seen_square[square_index].add(num)
        return True
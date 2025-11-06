def solve_n_queens(n):
    
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True

    def backtrack(row):
        # If all queens are placed, record solution
        if row == n:
            result.append([''.join(r) for r in board])
            return
        
        # Try placing a queen in each column
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'  # backtrack

    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0)
    return result


# Example usage:
if __name__ == "__main__":
    n = 4
    solutions = solve_n_queens(n)
    print(f"Number of solutions for {n}-Queens: {len(solutions)}\n")
    for sol in solutions:
        for row in sol:
            print(row)
        print()

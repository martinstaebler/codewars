import numpy as np

def valid_solution(board):
    is_valid = True
    arr_numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    board = np.array(board)

    print(arr_numbers[1:5])

    for x in board:
        if (np.sort(x) == arr_numbers).all() != True:
            is_valid = False
    else:
        board = np.swapaxes(board, 0, 1)
        for x in board:
            if (np.sort(x) == arr_numbers).all() != True:
                is_valid = False
        board = np.swapaxes(board, 0, 1)
        board = board.reshape(-1, 3)
        d1 = 0
        for a1 in range(0, 3):
            d2 = 0
            for a2 in range(0, 3):
                arr_quadrant = board[d1 + d2]
                arr_quadrant = np.append(arr_quadrant, board[d1 + d2 + 3])
                arr_quadrant = np.append(arr_quadrant, board[d1 + d2 + 6])
                if (np.sort(arr_quadrant) == arr_numbers).all() != True:
                    is_valid = False
                d2 += 1
            d1 += 9

    return is_valid





print(valid_solution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
])) # true

print(valid_solution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
])) # false


def validSolution_1(board):
    valid = set(range(1, 10))

    for row in board:
        if set(row) != valid: return False

    for col in [[row[i] for row in board] for i in range(9)]:
        if set(col) != valid: return False

    for x in range(3):
        for y in range(3):
            if set(sum([row[x * 3:(x + 1) * 3] for row in board[y * 3:(y + 1) * 3]], [])) != valid:
                return False

    return True
# https://www.codewars.com/kata/5ffc226ce1666a002bf023d2/train/python

def solution(mtrx):
    for line in mtrx:
        rest_string = "".join(line).replace(" ", "")
        if 0 < len(rest_string) < 2:
            return False
        if rest_string == ">x" or rest_string == "x<":
            return True
    return False




print(solution([
  ['>', ' '],
  [' ', 'x']
]))#False)

print(solution([
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', '>', ' ', 'x'],
  [' ', ' ', '', ' ', ' ']
]))#True)
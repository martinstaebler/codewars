# https://www.codewars.com/kata/52ec24228a515e620b0005ef

def exp_sum(sum_result):
    num_sums = 0

    return num_sums

exp_sum(1) # 1
exp_sum(2) # 2  -> 1+1 , 2
exp_sum(3) # 3 -> 1+1+1, 1+2, 3
exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

exp_sum(10) # 42

exp_sum(50) # 204226
exp_sum(80) # 15796476
exp_sum(100) # 190569292
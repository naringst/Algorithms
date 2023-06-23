# https://www.acmicpc.net/problem/1063

king, stone, n = input().split()

dict = {'R' : [1,0], 'L' :[-1,0],"B" : [0,-1],'T' :[0,1],'RT' : [1,1], "LT" :[-1,1], "RB" : [1,-1], 'LB':[-1,-1]}

## 아스키코드활용 abcd >> 123.. 
king = list(king)
stone= list(stone)

king[0] = (ord(king[0]) - 64) 
king[1] = int(king[1])

stone[0] = (ord(stone[0]) - 64)
stone[1] = int(stone[1])

n = int(n)


def letsmove(king,stone,move) :
  lr, ud = dict[move] 
  
  ## king의 다음자리
  k_row_next = king[0] +lr
  k_col_next = king[1] +ud
  
  ## king이 판을 벗어나면 리턴
  if k_row_next > 8 or k_row_next <1 or k_col_next >8 or k_col_next <1 :
    return king,stone

  ## king이 stone과 같은 자리가 될 때
  if k_row_next == stone[0] and k_col_next == stone[1] :
    s_row_next = stone[0] +lr
    s_col_next = stone[1] +ud

    ## stone이 판을 안벗어 나면 그대로 king,stone 움직이고 리턴
    if 0< s_row_next <9 and 0 < s_col_next<9 :
      stone[0] = s_row_next
      stone[1] = s_col_next

      king[0] = k_row_next
      king[1] = k_col_next

    ## stone이 판을 벗어나면 안움직이고 리턴 
    else :
      return king,stone
      
  ## king이 판을 안벗어나고 stone에 영향 없을 때
  else :
    ## king만 옮기고 리턴
    king[0] = k_row_next
    king[1] = k_col_next

  return king,stone
  

## 입력되는 움직임마다 king, stone 움직이기
for i in range(n) :
  move = input()
  king, stone = letsmove(king,stone,move)


## 아스키코드 활용해 1234.. >> abcd로 바꾸고 출력
king_answer = str(chr(king[0] +64)) + str(king[1])
stone_answer = chr(stone[0]+64) +str(stone[1])

print(king_answer)
print(stone_answer)
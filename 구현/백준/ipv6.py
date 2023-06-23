import sys

input = sys.stdin.readline
ipv6 = list(input().rstrip().split(":"))

answer = []

if ipv6[0] == "" :
  del ipv6[0]

if ipv6[-1] == "" :
  del ipv6[-1]

for i in range(len(ipv6)) :
  if ipv6[i] != "" :
    if len(ipv6[i]) !=4 :
      answer.append(ipv6[i].zfill(4))
    else :
      answer.append(ipv6[i])
  else :
    answer.append("0000")
    addNum = 8-len(ipv6)
    for k in range(addNum) :
      answer.append("0000")


print(":".join(answer))
import sys

input_pos = []
for i in range(int(sys.stdin.readline().strip())):
    xpos, ypos = map(int, sys.stdin.readline().split())
    input_pos.append((xpos, ypos))

pivot_xpos = sorted(input_pos, key = lambda x : (x[0], x[1])) 
pivot_ypos = sorted(input_pos, key = lambda x : (x[1], x[0])) 
answer = 0
for i in range(len(pivot_xpos)//2):
    first = pivot_xpos[i*2][1]
    second = pivot_xpos[i*2+1][1]
    answer = answer + (second - first)    
    first = pivot_ypos[i*2][0]
    second = pivot_ypos[i*2+1][0]
    answer = answer + (second - first)  

print(answer)

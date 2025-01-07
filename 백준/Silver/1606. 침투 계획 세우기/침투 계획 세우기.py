import sys
def get_sign(A):
    if A == 0 :
        return 0
    if A > 0 :
        return 1
    if A < 0 :
        return -1
x,y = map(int, sys.stdin.readline().strip().split())
sx, sy = get_sign(x), get_sign(y)
rule = {
    (0,0): 1,
    (1,-1): 5,
    (-1,1): 2,
    (0,1): 1,
    (0,-1): 4,
    (1,0): 6,
    (-1,0): 3
}
if sx == 0 and sy == 0:
    print(1)
else:
    pivot = 0
    mm = 1
    pp = 1
    if sx == 1 and sy == 1:
        sx = 0
        sy = 1
        y += x
        pp = -1
    if sx == -1 and sy == -1:
        sx = -1
        sy = 0
        x += y
        mm = -1
        
        
    depth = max(abs(x),abs(y))
    target_x, target_y = sx*depth, sy*depth
    pibot = pivot + 1 + rule[(sx,sy)]*depth + 6*(depth*(depth-1)//2)
    diff_x = abs(x) - abs(target_x)
    diff_y = abs(y) - abs(target_y)
    pibot = pibot + diff_x*pp - diff_y*mm
    print(pibot)

    


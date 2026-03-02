ylen, xlen = 9, 9
maps = []
for _ in range(ylen):
    maps.append(input().split(" "))
middle_target = []
mt_dict = {}
for xpos in [1, 4, 7]:
    for ypos in [1,4,7]:
        if xpos == 4 and ypos == 4:
            pass
        else:
            middle_target.append(maps[ypos][xpos])
            mt_dict[maps[ypos][xpos]] = (ypos, xpos)
middle_target.sort()
for mdix, mt in enumerate(middle_target):
    print(f"#{mdix+1}. {mt}")
    mt_position_y, mt_position_x = mt_dict[mt]
    sub_target = []
    for yp in range(mt_position_y-1, mt_position_y+2):
        for xp in range(mt_position_x-1, mt_position_x+2):
            if yp == mt_position_y and xp == mt_position_x:
                pass
            else:
                sub_target.append(maps[yp][xp])
            
    sub_target.sort()
    for sidx, st in enumerate(sub_target):
        print(f"#{mdix+1}-{sidx+1}. {st}")
    

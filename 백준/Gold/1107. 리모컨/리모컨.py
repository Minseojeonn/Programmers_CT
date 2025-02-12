
target_channel = input()
start_channel = 100
broken_buttons = None
broken_button_number = int(input())
buttons = [0,1,2,3,4,5,6,7,8,9]
setting_channel = ""
if broken_button_number!= 0:
    broken_buttons = input().split(" ")
    for i in broken_buttons:
        buttons.remove(int(i))
undermax = -333333
uppermin = 9999999


##under max
for i in range(0,int(target_channel)+1):
    string_i = str(i)
    same = 0
    for j in string_i :
        if int(j) in buttons:
            same = same+1
    if same == len(string_i):
        undermax = i

##uppder min
for i in range(999999,int(target_channel),-1):
    string_i = str(i)
    same = 0
    for j in string_i :
        if int(j) in buttons:
            same = same+1
    if same == len(string_i):
        uppermin = i

##just up&down
just_button = abs(int(target_channel)-100)

count = min(abs(int(undermax)-int(target_channel))+len(str(undermax)),abs(int(uppermin)-int(target_channel))+len(str(uppermin)),just_button)


print(count)

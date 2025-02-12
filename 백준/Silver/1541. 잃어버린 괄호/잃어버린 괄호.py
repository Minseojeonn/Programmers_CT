import sys
#최소가 되려면, -를 기준으로 나누어서 +를 더해주면 된다.

raw_line = sys.stdin.readline().strip()
split_line = raw_line.split('-')
summation = sum(list(map(int, split_line[0].split("+"))))
for term in split_line[1:]:
    term2 = sum(list(map(int, term.split("+"))))
    summation -= term2

print(summation)     
    

 

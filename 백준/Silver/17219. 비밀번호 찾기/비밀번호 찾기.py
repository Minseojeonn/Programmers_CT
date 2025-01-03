import sys
num_site, find_num = map(int, sys.stdin.readline().split())
site_dict = {}
for i in range(num_site):
    url, passwd = sys.stdin.readline().split()
    site_dict[url] = passwd
for i in range(find_num):
    print(site_dict[sys.stdin.readline().strip()])
    


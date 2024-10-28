def make_dict(len_dict):
    poketmon_list = []
    poketmon_reverse_dict = {}
    for i in range(len_dict):
        key = input()
        poketmon_list.append(key)
        poketmon_reverse_dict[key.lower()] = len(poketmon_list)
    return poketmon_list, poketmon_reverse_dict


len_dict, len_query = input().split()
poketmon_list, poketmon_reverse_dict = make_dict(int(len_dict))
for i in range(int(len_query)):
    query = input()
    try:
        int(query)
        print(poketmon_list[int(query)-1])
    except:
        print(poketmon_reverse_dict[query.lower()])



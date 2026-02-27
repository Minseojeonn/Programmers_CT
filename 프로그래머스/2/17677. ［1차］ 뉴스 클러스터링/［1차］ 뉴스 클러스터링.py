def solution(str1, str2):
    str_list = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    def parsing_two(str3):
        lowerstr = str3.lower()
        p_list = []
        for idx in range(len(lowerstr)-1):
            candid = lowerstr[idx:idx+2]
            save = True
            for i in candid:
                if i not in str_list:
                    save=False
            if save:
                p_list.append(candid)
        return p_list
    a = parsing_two(str1)
    b = parsing_two(str2)
    
    def multi_jacard(a, b):
        adict = {}
        bdict = {}
        for i in a:
            if i not in adict:
                adict[i] = 1
            else:
                adict[i] += 1
        for i in b:
            if i not in bdict:
                bdict[i] = 1
            else:
                bdict[i] += 1
        
        len_intersect = 0
        len_union = 0
        
        candidate_inter = set(adict.keys()).intersection(set(bdict.keys()))
        candidate_union = set(adict.keys()).union(set(bdict.keys()))
        for candid in candidate_inter:
            len_intersect += min(adict[candid], bdict[candid])
        for candid in candidate_union:
            if candid in adict and candid in bdict:
                len_union += max(adict[candid], bdict[candid])
            elif candid in adict and candid not in bdict:
                len_union += adict[candid]
            else:
                len_union += bdict[candid]
        
        return len_intersect, len_union
    
    len_intersection, len_union = multi_jacard(a, b)
    if len_union == 0:
        return 65536
    else:
        return int((len_intersection /len_union) * 65536) 
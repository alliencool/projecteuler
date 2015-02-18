
trinities = [(0, 1, 2),
             (3, 2, 4),
             (5, 4, 6),
             (7, 6, 8),
             (9, 8, 1),
            ]
trin_len = len(trinities)
            
results = []
            
def gen_solution(left_lst, formed_lst):
    
    l_lst = len(left_lst)
    
    for t_ind in range(1, trin_len):
        if trinities[t_ind][0] < len(formed_lst) and \
           formed_lst[trinities[t_ind][0]] < formed_lst[trinities[0][0]]:
            return
    
    sm = -1        
    for tr in trinities:
        lsm = 0
        if max(tr) >= len(formed_lst):
            break
            
        for i in tr:
            lsm += formed_lst[i]
        
        if sm != -1 and lsm != sm:
            return
        else:
            sm = lsm
    
    if l_lst == 0:
        ring = []
        for tr in trinities:
            for i in tr:
                ring.append(formed_lst[i])
        
        results.append(ring)
        return
        
    for i in range(l_lst):
        gen_solution(left_lst[:i] + left_lst[i + 1:], formed_lst + [left_lst[i]])
        
if __name__ == "__main__":
    gen_solution(list(range(1, 11))[-1::-1], [])
    results = [int("".join([str(j) for j in i])) for i in results]
    results = [i for i in results if len(str(i)) == 16]
    results = sorted(results, reverse=True)
    print("Result is", results[0])
        

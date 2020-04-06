def latin_square():
    N = int(input().strip())
    
    trace = 0
    
    nbr_row = 0
    
    nbr_col = 0
    
    list_colmn = []
    
    bool_val = [True]*N
    
    for i in range(N):
        list_colmn.append(set())
    
    for r in range(N):
        
        L = input().strip().split(' ')
        
        #la trace
        trace += int(L[r])
        
        #nbr_ligne
        if( N != len(set(L))):
            nbr_row += 1
        
        #nbr_colonne
        cpt = 0 

        for v in L:
            
            if(bool_val[cpt]):
                
                list_colmn[cpt].add(int(v))
            
                if(len(list_colmn[cpt]) != r+1):
                    nbr_col += 1
                    bool_val[cpt] = False
            
            cpt += 1
    
    return str(trace)+" "+ str(nbr_row) +" "+ str(nbr_col)
    
number_cases = input().strip()
    
for case in range(int(number_cases)):
    print("Case #{}: {}".format(case+1, latin_square()))

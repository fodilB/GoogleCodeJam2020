def overlap(a, b):
    
    val = min(a[1], b[1]) - max(a[0], b[0])
    
    if(val > 0):
        return True

    return False

def activity_overlap(list_activities, item):
    
    ll = sorted(list_activities, key=lambda x: x[0])
    
    for act in ll:
        
        if(act[0]>=item[1]):
            return False
        
        elif(overlap(act, item)):
            
                return True
    
    return False

def parenting_partnering():

    N = int(input().strip())
    
    solution = ""
    
    activities_jamie = []
    
    activities_cameron = []    
    
    for i in range(N):
        
        activity = input().strip().split(' ')
    
        item = (int(activity[0]), int(activity[1]))
        
        overlaped = activity_overlap(activities_jamie, item)
        
        if(overlaped):
            
            overlaped = activity_overlap(activities_cameron, item)
            
            if(overlaped):
                
                return "IMPOSSIBLE"
            
            else:
                
                activities_cameron.append(item)
                
                solution = solution + "C"
        else:
            
            activities_jamie.append(item)
            
            solution = solution + "J"
            
    return solution
            
number_cases = input().strip()

for case in range(int(number_cases)):
    print("Case #{}: {}".format(case+1, parenting_partnering()))

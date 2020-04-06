def nesting_depth():
    
    number = input()

    string_number = "("*int(number[0])+"" 

    for i in range(len(number)-1):
        val = int(number[i+1]) - int(number[i])

        if(val > 0):
            string_number += number[i] + "(" * val
        else:
            string_number += number[i] + ")" * (-val)

    string_number += number[len(number)-1]+")"*int(number[len(number)-1])
    
    return string_number
    
number_cases = input().strip()

for case in range(int(number_cases)):
    print("Case #{}: {}".format(case+1, nesting_depth()))

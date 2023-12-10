
data = open("day_09/input_day_09.txt").read().split("\n")
# data = open("day_09/testdata_day_09.txt").read().split("\n")
data = [x.split() for x in data]
data = [list(map(int, x)) for x in data]

answer = 0
diff_is_non_zero = True

#find d
for row in data: 
    diffs = []
    diff = row
    diff_is_non_zero = True
    while diff_is_non_zero:
        diff = [j-i for i, j in zip(diff[:-1], diff[1:])]
        diffs.append(diff)
                
        if len(set(diff)) == 1:       
            diff_is_non_zero = False
            diffs = list(reversed(diffs))                                       
            d = diffs[0][0]
            if len(diffs) > 1:
                n = len(diffs[1]) + 1
                a_1 = diffs[1][0]
                a_n = a_1 + ((n - 1) * d)
                diffs[1].append(a_n)
                diffs.pop(0) # remove the first, static diffs
                diffs.append(row)
            
                for i, diff in enumerate(diffs):
                    if diff == diffs[-2]:
                        answer += diffs[i][-1] + diffs[i+1][-1]
                        break                                             
                    else:
                        diffs[i+1].extend([diffs[i][-1] + diffs[i+1][-1]])
                    
            else: # simple case where there diffs are only one level down
                n = len(row) + 1
                a_1 = row[0]            
                a_n = a_1 + ((n - 1) * d)
                answer += a_n
                
                
            
            
                
                
                

print(answer)
        
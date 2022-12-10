import math

def findend(i,j,a,output,index,visited):
    x = len(a)
    y = len(a[0])

    flagc = 0
    flagr = 0
    currc = j

    for m in range(i,x):
        for n in range(j, currc):
            if a[m][n] == 1 or visited[m][n] == 1:
                flagr = 1
                break
        if flagr == 1:
            break
 
        if a[m][j] == 5:
            pass
 
        for n in range(j, y):
            if a[m][n] == 1 or visited[m][n] == 1:
                flagc = 1 
                break
            currc = n + 1
            a[m][n] = 5
 
    if flagr == 1:
        output[index].append( m-1)
    else:
        output[index].append(m)
 
    if flagc == 1:
        output[index].append(n-1)
    else:
        output[index].append(n)

def boundingBoxes(mtrx):
    x = len(mtrx)
    output = []
    idx = -1
    visited = [[0 for i in range(len(mtrx[0]))] for j in range(len(mtrx))]
    for i in range(len(mtrx)):
        for j in range(len(mtrx[0])):
            if mtrx[i][j] == 0:
                output.append([i,j])
                idx = idx + 1
                findend(i,j,mtrx,output,idx,visited)
                for k in range(output[idx][0],output[idx][2]+1):
                    for l in range(output[idx][1],output[idx][3]+1):
                        visited[k][l] = 1
    
    ans = []
    for out in output:
        ans.append([(float(out[0]+out[2]))/2,float(out[1]+out[3])/2,abs(out[2] - out[0]) + 1,abs(out[3] - out[1]) + 1])

    return ans


A = [[1,0,0],[0,0,1]]
ans = boundingBoxes(A)
print(ans)
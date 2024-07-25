import numpy as np
numbers = np.arange(24)
matrix = numbers.reshape(6, 4)
result = np.zeros_like(matrix)


for i in range(1,4):
    result[i][i]=numbers[i]
    
    for j in range (0,4):
        result[j+1][j]=numbers[j+i+1]
        
        for k in range (0,4):
            result[k+2][k]=numbers[k+j+i+2]

            for l in range (0,3):
                result[l+3][l]=numbers[l+k+j+i+3]

                for s in range (3,6):
                    if s==3:
                        result[s-3][s]=numbers[l+k+j+i+4]
                    else:
                        result[s][s-4]=numbers[l+k+j+s+4]
                
                    for r in range (0,3):
                        result[r][r+2]=numbers[l+k+j+i+s+4]
                        if r==2:
                            result[r+3][0]=numbers[l+k+j+i+s+4]
'''for i in range(1,4):
    result[i+1][i] = numbers[i]
    result[i+2][i] = numbers[i+4]
'''

for row in result:
    print('      '.join(map(str, row)))






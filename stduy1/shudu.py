solustion=[[0,7,8,4,1,0,0,0,9],
           [2,0,1,0,2,0,4,7,0],
           [0,2,9,0,6,0,0,0,0],
           [0,3,0,0,0,7,6,9,4],
           [0,4,5,3,0,0,8,1,0],
           [1,0,0,0,0,0,3,0,0],
           [9,0,4,6,7,2,1,3,0],
           [6,0,0,0,0,0,7,0,8],
           [0,0,0,8,3,1,0,0,0]]

print(sum(solustion[0]))

sum1=0
while(1):
    for i in range(0,9):
        sum1 = sum1+sum(solustion[i])
    if(sum1 == 405):
        break

    for i in range(0,9):
        t = solustion[i]
        for j in range(0,9):
            if(solustion[i][j]!=0):
                continue
            for n in range(0,9):
                t.append(solustion[n][i])
            if (i <= 2 and i >= 0 and j <= 2 and j >= 0):
                t.append(solustion[0][0])
                t.append(solustion[0][1])
                t.append(solustion[0][2])
                t.append(solustion[1][0])
                t.append(solustion[1][1])
                t.append(solustion[1][2])
                t.append(solustion[2][0])
                t.append(solustion[2][1])
                t.append(solustion[2][2])
            if (i <= 2 and i >= 0 and j > 2 and j < 6):
                t.append(solustion[0][3])
                t.append(solustion[0][4])
                t.append(solustion[0][5])
                t.append(solustion[1][3])
                t.append(solustion[1][4])
                t.append(solustion[1][5])
                t.append(solustion[2][3])
                t.append(solustion[2][4])
                t.append(solustion[2][5])
            if (i <= 2 and i >= 0 and j < 9 and j > 5):
                t.append(solustion[0][6])
                t.append(solustion[0][7])
                t.append(solustion[0][8])
                t.append(solustion[1][6])
                t.append(solustion[1][7])
                t.append(solustion[1][8])
                t.append(solustion[2][6])
                t.append(solustion[2][7])
                t.append(solustion[2][8])
            if (i <= 5 and i >= 3 and j <= 2 and j >= 0):
                t.append(solustion[3][0])
                t.append(solustion[3][1])
                t.append(solustion[3][2])
                t.append(solustion[4][0])
                t.append(solustion[4][1])
                t.append(solustion[4][2])
                t.append(solustion[5][0])
                t.append(solustion[5][1])
                t.append(solustion[5][2])
            if (i <= 5 and i >= 3 and j < 6 and j > 2):
                t.append(solustion[3][3])
                t.append(solustion[3][4])
                t.append(solustion[3][5])
                t.append(solustion[4][3])
                t.append(solustion[4][4])
                t.append(solustion[4][5])
                t.append(solustion[5][3])
                t.append(solustion[5][4])
                t.append(solustion[5][5])
            if (i <= 5 and i >= 3 and j < 9 and j > 5):
                t.append(solustion[3][6])
                t.append(solustion[3][7])
                t.append(solustion[3][8])
                t.append(solustion[4][6])
                t.append(solustion[4][7])
                t.append(solustion[4][8])
                t.append(solustion[5][6])
                t.append(solustion[5][7])
                t.append(solustion[5][8])
            if (i <= 8 and i >= 6 and j <= 2 and j >= 0):
                t.append(solustion[6][0])
                t.append(solustion[6][1])
                t.append(solustion[6][2])
                t.append(solustion[7][0])
                t.append(solustion[7][1])
                t.append(solustion[7][2])
                t.append(solustion[8][0])
                t.append(solustion[8][1])
                t.append(solustion[8][2])
            if (i <= 8 and i >= 6 and j <= 5 and j >= 3):
                t.append(solustion[6][3])
                t.append(solustion[6][4])
                t.append(solustion[6][5])
                t.append(solustion[7][3])
                t.append(solustion[7][4])
                t.append(solustion[7][5])
                t.append(solustion[8][3])
                t.append(solustion[8][4])
                t.append(solustion[8][5])
            if (i <= 8 and i >= 6 and j <= 8 and j >= 6):
                t.append(solustion[6][6])
                t.append(solustion[6][7])
                t.append(solustion[6][8])
                t.append(solustion[7][6])
                t.append(solustion[7][7])
                t.append(solustion[7][8])
                t.append(solustion[8][6])
                t.append(solustion[8][7])
                t.append(solustion[8][8])

            count1 = []
            for k in range(1, 10):
                if (t.count(k) == 0):
                    count1.append(k)
            if(len(count1)==1):
                solustion[i][j] = count1[0]


print(solustion)









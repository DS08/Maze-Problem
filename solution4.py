##Maze Problem

String = [ 
 "##..#", 
 "#.#.#", 
 "#.#.#", 
 "#####" 
]

def count(row, col):
    result = 0
    if(row==0 and col==0):
        result +=2
        if String[row][col+1]== '.':
            result +=1
        if String[row+1][col] == '.':
            result +=1
        return result

    if(row==0 and col==len(String[0])-1):
        result += 2
        if String[row][col-1]== '.':
            result +=1
        if String[row+1][col] == '.':
            result +=1
        return result

    if(row==len(String)-1 and col==len(String[0])-1):
        result += 2
        if String[row-1][col]== '.':
            result +=1
        if String[row][col-1] == '.':
            result +=1
        return result


    if(row==len(String)-1 and col==0):
        result += 2
        if String[row-1][col]== '.':
            result +=1
        if String[row][col+1] == '.':
            result +=1
        return result

    if (row==0):
        result +=1
        if String[row][col-1]== '.':
            result +=1
        if String[row][col+1] == '.':
            result +=1
        if String[row+1][col] == '.':
            result +=1
        return result

    if (row==len(String)-1):
        result +=1
        if String[row][col-1]== '.':
            result +=1
        if String[row][col+1] == '.':
            result +=1
        if String[row-1][col] == '.':
            result +=1
        return result

    if (col==0):
        result +=1
        if String[row+1][col]== '.':
            result +=1
        if String[row-1][col] == '.':
            result +=1
        if String[row][col+1] == '.':
            result +=1
        return result

    if (col==len(String[0])-1):
        result +=1
        if String[row+1][col]== '.':
            result +=1
        if String[row-1][col] == '.':
            result +=1
        if String[row][col-1] == '.':
            result +=1
        return result

    if String[row+1][col]== '.':
        result +=1
    if String[row-1][col] == '.':
        result +=1
    if String[row][col-1] == '.':
        result +=1
    if String[row][col+1] == '.':
        result +=1
    return result
    
    

visited_hash = []
length_of_elm = len(String[0])
amount_of_paint = 0
for j in range(length_of_elm):
    direction = 'right'
    i = 0
    if(String[i][j]=='#'and (i,j) not in visited_hash):
        amount_of_paint += count(i, j)
        visited_hash.append((i,j))
    elif(String[i][j]=='.'):
        i = 0
        while(i<len(String)):
            if (String[i][j]=='#' and (i,j) not in visited_hash):
                amount_of_paint += count(i, j)
                visited_hash.append((i,j))
                
            i +=1

for i in range(len(String)):
    direction = 'down'
    j = len(String[0])-1
    if(String[i][j]=='#' and (i, j) not in visited_hash):
        amount_of_paint += count(i, j)
        visited_hash.append((i,j))
    elif(String[i][j]=='.'):
        j = len(String[0]-1)
        while(j>=0):
            if (String[i][j]=='#' and (i,j) not in visited_hash):
                amount_of_paint += count(i, j)
                visited_hash.append((i,j))
                
            j -=1


for j in range(length_of_elm-1,-1,-1):
    direction = 'left'
    i = len(String)-1
    if(String[i][j]=='#'and (i,j) not in visited_hash):
        amount_of_paint += count(i, j)
        visited_hash.append((i,j))
    elif(String[0][j]=='.'):
        i = len(String)-1
        while(i>=0):
            if (String[i][j]=='#' and (i,j) not in visited_hash):
                amount_of_paint += count(i, j)
                visited_hash.append((i,j))
                
            i -=1



for i in range(len(String)-1,-1,-1):
    direction = 'up'
    j = 0
    if(String[i][j]=='#' and (i, j) not in visited_hash):
        amount_of_paint += count(i, j)
        visited_hash.append((i,j))
    elif(String[i][j]=='.'):
        j = 0
        while(j<len(String[0])):
            if (String[i][j]=='#' and (i,j) not in visited_hash):
                amount_of_paint += count(i, j)
                visited_hash.append((i,j))
                
            j +=1


print('The total amount of paint required '+str(amount_of_paint))

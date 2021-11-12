import random
import copy
#----------------------------------------------BFS-------------------------------------------
class cur:
    def __init__(self, a , i , p):
        self.arr = a[:]
        self.idx = i
        self.path = p[:]

def bfs(n): # can use list as queue in python, with append() & pop()
    queue =[]
    ans = 0

    if n==2 or n==3:
        f = open(str(n)+"_bfs_output.txt" ,"w")
        f.write('No Solution')
        return
    
    for i in range(n): # 0 ~ n-1
        lt = [-1]
        for j in range(n):
            lt.append(0)
        lt[1] = i+1
        p=[i+1]
        c = cur(lt, 1 , p)
        queue.append(c)
        
    while(queue):
        front = queue.pop(0)
        arr = front.arr[:]
        idx = front.idx
        
        if idx == n :
            ans+=1
            print(p)
            f = open(str(n)+"_bfs_output.txt" ,"w")
            for i in range(len(p)):
                f.write(str(p[i])+" ")
            break;
        else :
            for j in range(1,n+1):
                arr[idx+1]=j
                chk=0
                for k in range(1,idx+1):
                    if arr[k] == arr[idx+1] :
                        arr[idx+1] =0
                        chk=1
                    elif abs(k-(idx+1)) == abs(arr[k]-arr[idx+1]):
                        arr[idx+1]= 0
                        chk =1
                if chk == 0:
                    p = front.path[:]
                    p.append(j)
                    add = cur(arr , idx+1, p)
                    queue.append(add)
                arr[idx+1] = 0
    if ans == 0 :
        f = open(str(n)+"_bfs_output.txt" ,"w")
        f.write("No solution")
#--------------------------------------Hll Climbing-----------------------------------------
class Coor:
    def __init__(self, row, col):
        self.row = row
        self.col = col

def makeRandom(n):
    pos = []
    for i in range(n):
        row = random.randrange(0,n)
        cor = Coor(row , i)
        pos.append(cor)
    return pos

def heuristic(boar ,n): 
    tot = 0
    for i in range(n):
        for j in range(i+1 , n):
            q1 = boar[i]
            q2 = boar[j]
            if q1.row == q2.row or q1.col == q2.col or abs(q1.col-q2.col) == abs(q1.row-q2.row) :
##                if q1.row != q2.col :
                    tot+=1
                
    return tot
h=0 #heuristic
    
def hc(n):
    start = makeRandom(int(n))
    h = heuristic(start,int(n))
    ccol = -1
    crow = -1

    if n==2 or n==3:
        f = open(str(n)+"_hc_output.txt" ,"w")
        f.write("No solution")
        return
    
    while( h!= 0 ):
        #next=[]
        curPair = heuristic(start , int(n))
        
        next = copy.deepcopy(start) #should deep copy
        lower = curPair
        
        for i in range(int(n)):
            for j in range(0 , int(n)):
                if j == start[i].row:
                    continue
                
                next[i].row = j
                nextPair = heuristic(next , int(n))

                if(lower > nextPair):
                    lower = nextPair
                    crow = j
                    ccol = i

                next[i].row = start[i].row

        if lower < curPair :
            h = lower
            next[ccol].row = crow
            start=[]
            start = next[:]                     
        else :
            start = makeRandom(int(n))
            h = heuristic(start , int(n))

    f = open(str(n)+"_hc_output.txt" ,"w")
    for i in range(len(start)):
        f.write(str(start[i].row+1)+" ")
        print(start[i].row+1)
    
#-------------------------------------------CSP---------------------------------------------
result = 0

def check(cspM , col , row , n):
    for i in range(col+1 , n):
        for j in range(n):
            if i==col or j==row or abs(i-col) == abs(j-row):
                if cspM[i][j]==1 :
                    cspM[i][j] = 0
    return cspM

def search(arr , col,row ,n ,tmp):
    global result
    if result == 1 :
        return
    if col == n :
        f = open(str(n)+"_csp_output.txt" ,"w")
        for i in range(n):
            arr[i]+=1
            f.write(str(arr[i])+" ")
        print(arr)
        result = 1
        return
    else :

        if col!=0:
            tmp=[]
            for j in range(n):
                acol=[]
                for k in range(n):
                    acol.append(1)
                tmp.append(acol)
            for i in range( 0, col): 
                tmp = check(tmp , i , arr[i] , n)
            tmp=check(tmp, col , row , n)
          
        for i in range(n): # 0 ~ n-1
            if col!= n-1 and tmp[col+1][i] == 1 :
                arr[col] = row
                search(arr , col+1 ,i ,n , tmp)
            if col == n-2 and tmp[col+1][i] == 1 :
                arr[col+1] = i
                search(arr , n , i , n ,tmp)
           
def csp(n):
    arr = [0]*n
    global result
    if n==2 or n==3 :
        f = open(str(n)+"_csp_output.txt" ,"w")
        f.write("No solution")
    else : 
        for i in range(n):
            if result == 1 :
                break
            tmp=[]
            for j in range(n):
                acol=[]
                for k in range(n):
                    acol.append(1)
                tmp.append(acol)
            tmp = check(tmp , 0 , i , n)
            
            search(arr ,0 , i ,n , tmp )

#------------------------------------------main---------------------------------------------  
def main():
    f = open('input.txt',mode='r',encoding='utf-8')
    while True:
        line = f.readline()
        if not line:
            break
        parse = line.split()
        if len(parse) == 0 :
            continue
        if parse[1] == 'bfs':
            bfs(int(parse[0]))
        elif parse[1]=='csp':
            csp(int(parse[0]))
        elif parse[1]=='hc':
            hc(int(parse[0]))

if __name__ == '__main__':
    main()

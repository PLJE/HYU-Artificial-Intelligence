#AI assignment2 Q-learning
import random

board =[]
table =[]

si=0
sj=0

gi=0
gj=0

class qtable:
    def __init__(self, a,b,c,d):
        self.arr = []
    def initarr(self,a,b,c,d):
        self.arr.append(a)
        self.arr.append(b)
        self.arr.append(c)
        self.arr.append(d)

def init_table():
    for i in range(5):
        tmp=[]
        for j in range(5):
            t = qtable(0,0,0,0)
            t.initarr(0,0,0,0)
            tmp.append(t)
        table.append(tmp)

def rand():
    r = random.randrange(1,5) #1~4
    return r

def nextpos(i,j,num):
    if num ==1: #up
        i-=1
    elif num == 2: #right
        j+=1
    elif num ==3: #down
        i+=1
    elif num==4: #left
        j-=1
    return i, j

def checkBound(i,j):
    if i<0 or j<0 or i>=5 or j>=5 :
        return 0 # out of board
    else:
        return 1

def returnR(i,j):
    if board[i][j] == 'G':
        return 100
    elif board[i][j] == 'B':
        return -100
    elif board[i][j] =='T':
        return 1
    else:
        return 0
def returnMax(i,j):
    a = max(table[i][j].arr)
    return a

path = []

def returnPath(i,j):
    return i*5 + j

def learning():
    global board, si, sj, gi , gj, table
    global path
    
    ci = si #start
    cj = sj

    test=0

    while(1):
        
        if ci==gi and cj==gj :
            ci=si
            cj=sj
            if test >= 100000:
                break
            continue
        
        togo = rand()
        ti,tj = nextpos(ci,cj,togo)
        if checkBound(ti,tj)==0:
            while(1):
                togo = rand()
                ti,tj=nextpos(ci,cj,togo)
                chk = checkBound(ti,tj)
                if chk == 1:
                    break
                
        table[ci][cj].arr[togo-1] = returnR(ti,tj) + 0.9*returnMax(ti,tj)

        if returnR(ti,tj)==-100:
            ci=si
            cj=sj
            continue
        
        ci = ti
        cj = tj

        test+=1
        
def findPath():
    global path , si, sj, gi, gj
    path.append(returnPath(si,sj))

    ci = si
    cj = sj

    while(1):
       #print(str(ci)+' '+str(cj))
       togo = table[ci][cj].arr.index(max(table[ci][cj].arr))+1
       ti = ci
       tj = cj
       if togo == 1:
           ti -=1
       elif togo==2:
            tj+=1
       elif togo ==3:
            ti+=1
       elif togo ==4:
            tj-=1

       if returnPath(ti,tj) in path:
           backup = table[ci][cj].arr[togo-1]
           table[ci][cj].arr[togo-1] = 0
           togo = table[ci][cj].arr.index(max(table[ci][cj].arr))+1
           ti = ci
           tj = cj
           if togo == 1:
               ti -=1
           elif togo==2:
                tj+=1
           elif togo ==3:
                ti+=1
           elif togo ==4:
                tj-=1
           table[ci][cj].arr[togo-1] = backup
           
       path.append(returnPath(ti,tj))

       if ti==gi and tj==gj:
           break
       ci = ti
       cj = tj

##def recursive(ci,cj,arr):
##    global path , si, sj, gi, gj
##    parr = arr[:]
##
##    if ci==gi and cj ==gj :
##        path.append(parr)
##        return
##    
##    togo = table[ci][cj].arr.index(max(table[ci][cj].arr))+1
##       ti = ci
##       tj = cj
##       if togo == 1:
##           ti -=1
##       elif togo==2:
##            tj+=1
##       elif togo ==3:
##            ti+=1
##       elif togo ==4:
##            tj-=1
##
##       if returnPath(ti,tj) in parr:
##           backup = table[ci][cj].arr[togo-1]
##           table[ci][cj].arr[togo-1] = 0
##           togo = table[ci][cj].arr.index(max(table[ci][cj].arr))+1
##           ti = ci
##           tj = cj
##           if togo == 1:
##               ti -=1
##           elif togo==2:
##                tj+=1
##           elif togo ==3:
##                ti+=1
##           elif togo ==4:
##                tj-=1
##           table[ci][cj].arr[togo-1] = backup
##
##       parr.append(returnPath(ti,tj))
##       recursive(ti,tj,parr)
        
def main():
    global board , si, sj, gi , gj
    
    f = open('input.txt' , mode ='r' , encoding = 'utf-8')
    row = 0
    while True:
        line = f.readline()
        if not line:
            break
        parse = line.split()
        if len(parse) == 0:
            continue
        tmp=[]

        for i in range(5):
            tmp.append(parse[0][i])
            if parse[0][i]== 'S':
                si = row
                sj = i
            if parse[0][i]== 'G':
                gi = row
                gj = i
        board.append(tmp)

        row+=1
    init_table()
    learning()
    print(table[0][0].arr)
    print(table[1][1].arr)
    findPath()
    print(path)

    f = open('output.txt',"w")
    for i in range(len(path)):
        f.write(str(path[i])+' ')
    f.write('\n')
    f.write(str(max(table[0][0].arr)))
    
if __name__ == '__main__':
    main()

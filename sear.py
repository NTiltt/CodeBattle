from CodeBattleClient import GameClient
import random
import logging
from sds import *
import time
import numpy as np
import random
from internals.TurnAction import TurnAction
from internals.Board import Board
from internals.Point import Point
from boom import Boom

def rasst(MAP,board):
    coord = board.get_bomberman()
    x = coord.get_x()
    y = coord.get_y()
    bomber = board.get_other_bombermans()
    rasst = []
    k = 0
    for i in bomber:
        rasst.append([abs(x-i.get_x())+abs(y-i.get_y()),k])
        k+=1
    rasst = sorted(rasst)
    
    lab = []
    rdl = len(MAP)
    n = m = rdl
    
    for i in range(n):
        rdl = MAP[i]
        cur = []
        for k in range(m):
            if rdl[k] != ' ':
                cur.append(-1)   
            else:    
                cur.append(0)
        lab.append(cur)
    
    
    x1, y1 = x, y
    laba = lab[:]
    for i in rasst:
        lab = laba[:]
        
        x2, y2 = bomber[i[1]].get_x(), bomber[i[1]].get_y()
        print(x1, y1)
        print(x2, y2)
        lab = voln(x1,y1,1,n,m,lab,x2,y2)
        
        if lab[x2][y2] > 0:
            for i in lab:
                print(i)
                return
                
                
        else:
            print("Ne mozhet")    
def voln(x,y,cur,n,m,lab,x2,y2):
    lab[x][y] = cur
    if lab[x2][y2] > 0:
        return lab
    if y<m:
        if lab[x][y+1] == 0 or (lab[x][y+1] != -1 and lab[x][y+1] > cur):
            voln(x,y+1,cur+1,n,m,lab,x2,y2)
    if x<n:
        if lab[x+1][y] == 0 or (lab[x+1][y] != -1 and lab[x+1][y] > cur):
            voln(x+1,y,cur+1,n,m,lab,x2,y2)
    if x>=0:
        if lab[x-1][y] == 0 or (lab[x-1][y] != -1 and lab[x-1][y] > cur):
            voln(x-1,y,cur+1,n,m,lab,x2,y2)
    if y>=0:
        if lab[x][y-1] == 0 or (lab[x][y-1] != -1 and lab[x][y-1] > cur):
            voln(x,y-1,cur+1,n,m,lab,x2,y2)
    return lab


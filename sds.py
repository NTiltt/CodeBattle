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

stick = [['♣','D'],['☼','T'],['♥','B'],['♠','V'],['☺','S'],['#','#'], ['H','H'],['҉','P'],['Ѡ','L'],['☻','K']]

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3
ACT_LEFT = 4
ACT_DOWN = 5
ACT_RIGHT = 6
ACT_UP = 7
STOP = 8
kol_min = 0
def chelik(board,mapa):
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
    
    for i in rasst:
        poop = False
        bx = bomber[i[1]].get_x()
        by = bomber[i[1]].get_y()
        
        maxcoordx = max(bx,x)
        mincoordx = min(bx,x)
        maxcoordy = max(by,y)
        mincoordy = min(by,y)
        if (bx > x and by > y) or (bx < x and by < y):
            
            for j in range(mincoordx,maxcoordx+1):
                if mapa[maxcoordy][j] in 'T#12345':
                    poop = True
                    break
            
            if poop != True:
                for j in range(mincoordy,maxcoordy+1):
                    if mapa[j][mincoordx] in 'T#12345':
                        poop = True
                        break
            
            if poop != True:
                print(1,bx,by)
                if bx > x:
                    return 2
                elif bx < x:
                    return 0
                
                else:
                    if by < y:
                        return 3
                    elif by > y:
                        return 1
                    
        
            
            
            poop = False
            for j in range(mincoordy,maxcoordy+1):
                if mapa[maxcoordx][j] in 'T#12345':
                    poop = True
                    break
            if poop != True:
                for j in range(mincoordx,maxcoordx+1):
                    if mapa[j][mincoordy] in 'T#12345':
                        poop = True
                        break
            if poop != True:
                print(2,bx,by)
                if by < y:
                    return 3
                elif by > y:
                    return 1
                else:
                    if bx < x:
                        return 2
                    elif bx > x:
                        return 0
        else:
            
            
            for j in range(mincoordx,maxcoordx+1):
                if mapa[mincoordy][j] in 'T#12345':
                    poop = True
                    break
            
            if poop != True:
                for j in range(mincoordy,maxcoordy+1):
                    if mapa[j][mincoordx] in 'T#12345':
                        poop = True
                        break
            
            if poop != True:
                print(1,bx,by)
                if bx > x:
                    return 2
                elif bx < x:
                    return 0
                
                else:
                    if by < y:
                        return 3
                    elif by > y:
                        return 1
                    
        
            
            
            poop = False
            for j in range(mincoordy,maxcoordy+1):
                if mapa[maxcoordx][j] in 'T#12345':
                    poop = True
                    break
            if poop != True:
                for j in range(mincoordx,maxcoordx+1):
                    if mapa[j][maxcoordy] in 'T#12345':
                        poop = True
                        break
            if poop != True:
                print(2,bx,by)
                if by < y:
                    return 3
                elif by > y:
                    return 1
                else:
                    if bx < x:
                        return 2
                    elif bx > x:
                        return 0
        
                
    return -1
        
    
    
def bom(desc,row, col,timer):
            stor = []
            left = desc[row, max(col-1,0)]
            if left != 'T':
                stor.append(left)
                left2 = desc[row, max(col - 2, 0)]
                if left2 != 'T':
                    stor.append(left2)
                    left3 = desc[row, max(col - 3, 0)]
                    if left3 != 'T':
                        stor.append(left3)
    
                        
            down = desc[min(row+1,nrow-1), col]
            if down != 'T':
                stor.append(down)
                down2 = desc[min(row + 2, nrow - 2), col]
                if down2 != 'T':
                    stor.append(down2)
                    down3 = desc[min(row + 3, nrow - 3), col]
                    if down3 != 'T':
                        stor.append(down3)
                        
            right = desc[row, min(col+1,ncol-1)]
            if right != 'T':
                stor.append(right)
                right2 = desc[row, min(col + 2, ncol - 2)]
                if right2 != 'T':
                    stor.append(right2)
                    right3 = desc[row, min(col + 3, ncol - 3)]
                    if right3 != 'T':
                        stor.append(right3)     
            
            up = desc[max(row-1,0), col]
            if up != 'T':
                stor.append(up)
                up2 = desc[max(row - 2, 0), col]
                if up2 != 'T':
                    stor.append(up2)
                    up3 = desc[max(row - 3, 0), col]
                    if up3 != 'T':
                        stor.append(up3) 
            return stor
        
def timer_bomb(board,mapa):
    bombs = board.get_bombs()
    
    ln =len(bombs)
    if ln == 0:
        return mapa
    for i in range(ln-1):
        coord = bombs[i]
        
        cord  = [coord.get_x(), coord.get_y()]
        
        timer = mapa[cord[0]][cord[1]]
        if timer in 'SKL':
                return mapa
        if timer not in '12345':
            timer = 1
        timer = int(timer)
        
        for j in range(i,ln):
            coord1 = bombs[j]
            cord1  = [coord1.get_x(), coord1.get_y()]
            
            timer1 = mapa[cord1[0]][cord1[1]]
            if timer1 in 'SKL':
                return mapa
            if timer1 not in '12345':
                timer1 = 1
            timer1 = int(timer1)
            
            if cord[0] == cord1[0] and abs(cord[1]-cord1[1]) < 4:
                timer = min(timer,timer1)
                
                
                mapa[cord[0]] = mapa[cord[0]][:cord[1]]+str(timer)+mapa[cord[0]][cord[1]+1:]
                mapa[cord1[0]] = mapa[cord1[0]][:cord1[1]]+str(timer)+mapa[cord1[0]][cord1[1]+1:]
                print(mapa[cord[0]])
                print(mapa[cord1[0]])
                
    return mapa
    
def minimap(MAP):
    
    for i in stick:
        MAP = MAP.replace(i[0],i[1])
    ln = len(MAP)
    sz = int(ln**0.5)
    mapa = []
    for i in range(0, ln, sz):
        mapa.append(MAP[i:i+sz])
    return mapa

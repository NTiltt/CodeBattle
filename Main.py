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
from sear import rasst
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                    level=logging.INFO)


def turn(board,message):
    global kol_min
    global shag
    global stateold
    global q_table
    global actionold
    global action
    coord = board.get_bomberman()
    
    mapa = minimap(message)
    strmap = ''
    for i in mapa:
        strmap+=i
    #mapa = timer_bomb(board,mapa)
    for i in mapa:
        print(i)
    env = Boom(mapa)
    state = env.ncol*coord.get_y()+coord.get_x()
    
    for i in env.P[state]:
        print(env.P[state][i])
    nextstate = 0
    reward = -11000000000000
    od = []
    for i in env.P[state]:
        if env.P[state][i][0][2]>reward:
            od = []
            reward = env.P[state][i][0][2]
            nextstate = i
            od.append(i)
        elif env.P[state][i][0][2]==reward:
            od.append(i)
    if len(od)>1:
        
        action = random.choice(od)
        chel = chelik(board,mapa)
        
        if chel in od:
            print(chel)
            #rasst(mapa,board)
            action = chel
        
    else:
        action = nextstate
    if action in [4,5,6,7]:
        kol_min += 1
    elif action in [0,1,2,3]:
        kol_min = 0
    if kol_min >2:
        action -=4
        kol_min = 0
    print(coord)

       
    if action == LEFT:
        actionn = TurnAction.LEFT
    elif action == DOWN:
        actionn = TurnAction.DOWN
    elif action == RIGHT:
        actionn = TurnAction.RIGHT
    elif action == UP:
        actionn = TurnAction.UP
    elif action == ACT_DOWN:
        actionn = TurnAction.ACT_DOWN
    elif action == ACT_RIGHT:
        actionn = TurnAction.ACT_RIGHT
    elif action == ACT_UP:
        actionn = TurnAction.ACT_UP
    elif action == ACT_LEFT:
        actionn = TurnAction.ACT_LEFT
    elif action == STOP:
        actionn = TurnAction.STOP
    return actionn





def main():
    gcb = GameClient(
        "http://codebattle2020final.westeurope.cloudapp.azure.com/codenjoy-contest/board/player/o2rhafe157s5eu1fznaa?code=5241997958883357959&gameName=bomberman")
    gcb.run(turn)

if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as a:
            print(a)

    

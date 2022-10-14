# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:58:59 2022

@author: 65935
"""

# import random module
import random
  
# Generates a random number between a given positive range
A=(1,2,3,4,5,6,7,8,9)
ans = random.sample(A,4)
print(ans)
player_input =()
player_input=(int(s) for s in player_input())
print(player_input)
a = 0
b = 0
while 1==1:
    for i in range(4):
        for j in range(4):
            if ans[i]==player_input[j] and i==j:a+=1
            if ans [i]==player_input[j] and i!=j:b+=1
            print(a,'A',b,'B')
    if a==4:
        print('game over')
        break
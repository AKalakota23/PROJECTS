import random
import pygame
import os
import time
from getpass import getpass
import keyboard

size = [int(x) for x in input("Choose a size for nxm matrix: ").split()]  #asks user for the size of the board 
snake = '*' #the body of the snake (starts off as one asterik)
startx = 0 #starting y - position of the snake  (yes, ik now the naming is contradictory but there is a reason for it)
starty = 0 #starting x- position of the snake 
counter = 0

#calculates random position of the apple (need to modularize this process later through functions)
random_x = random.randint(0, size[1]-1)
random_y= random.randint(0, size[0]-1)
random_coord = [random_x, random_y]
#print(random_coord)

#mechanism for creating the board by placing 0's in a 2d matrix with the size specified by the user
l = []
sub = []
for i in range(size[0]):
    for j in range(size[1]):
        sub.append(0)
    l.append(sub)
    sub = []

#prints the board with the snake and the "apple" (1)
l[random_coord[1]][random_coord[0]] = 1 
l[startx][starty] = snake
#print(l)
os.system('cls')
for i in range(len(l)):
    for j in l[i]:
        print(j, end = " ")
    print() 


#keyboard controls 
while True:

    #if d is pressed 
    if(keyboard.is_pressed('d')):

        #clearing:
        os.system('cls') 
        l[random_coord[1]][random_coord[0]] = 1 #resets the apple in the same position 
        l[startx][starty] = 0 #previous position of the snake becomes 0 again so that "bits" don't get left behind

        #keeps the snake within the board and updates its position
        if starty+1 != size[1]:
            starty += 1
        l[startx][starty] = snake

        #mechanism for eating the apple and updating the size of the snake 
        if l[startx][starty] == l[random_coord[1]][random_coord[0]]: #if the position of the snake (l[startx][starty]) is equal to the positon of the apple (l[random_coord[1]][random_coord[0]])

            l[random_coord[1]][random_coord[0]] = 0 #set the previous postion of the apple to 0 

            snake += '*' #update the size of the snake 

            random_x = random.randint(0, size[1]-1) #generate a random x position for the apple
            random_y= random.randint(0, size[0]-1) #generate a random y-postion for the apple 
            random_coord = [random_x, random_y] #set them as coordinates 
        
        #reprints the board
        for i in range(len(l)):
            for j in l[i]:
                print(j, end = " ")
            print()
        time.sleep(0.10) #delay between movement *Warning*: Need delay, otherwise infinite loop :(
        

    #if a is pressed
    if(keyboard.is_pressed('a')):

        #clearing:
        os.system('cls')
        l[random_coord[1]][random_coord[0]] = 1 
        l[startx][starty] = 0

        #keeps the snake within the board and updates its position
        if starty-1 != -1:
            starty -= 1
        l[startx][starty] = snake

        #mechanism for eating the apple and updating the size of the snake         
        if l[startx][starty] == l[random_coord[1]][random_coord[0]]:
            l[random_coord[1]][random_coord[0]] = 0
            snake += '*'
            random_x = random.randint(0, size[1]-1)
            random_y= random.randint(0, size[0]-1)
            random_coord = [random_x, random_y]

        #reprints the board
        for i in range(len(l)):
            for j in l[i]:
                print(j, end = " ")
            print()
        time.sleep(0.10)


    #if w is pressed
    if(keyboard.is_pressed('w')):

        #clearing
        os.system('cls')
        l[random_coord[1]][random_coord[0]] = 1 
        l[startx][starty] = 0

        #spaces out the body of the snake so that each "bit" or asterik of the body is in place of the 0 on the board as opposed to the entire body squeezed into one 0  
        if len(snake) > 1:
            if startx -1 != -1:
                counter +=1
                if counter ==1:
                    l[startx][starty] = 0
                temp = []
                for i in range(len(snake)):
                    if startx-1 != -1:
                        startx -=1
                        l[startx+1][starty] = snake[i]
                temp.append(startx+(len(snake)))
                l[temp[0]][starty] = 0
                        
                        
        else:
            if startx -1 != -1:
                startx -= 1
            l[startx][starty] = snake
        if l[startx][starty] == l[random_coord[1]][random_coord[0]]:
            l[random_coord[1]][random_coord[0]] = 0
            snake += '*'
            random_x = random.randint(0, size[1]-1)
            random_y= random.randint(0, size[0]-1)
            random_coord = [random_x, random_y]
        for i in range(len(l)):
            for j in l[i]:
                print(j, end = " ")
            print()
        time.sleep(0.10)


    if(keyboard.is_pressed('s')):
        os.system('cls')
        l[random_coord[1]][random_coord[0]] = 1 
        l[startx][starty] = 0
        if startx != size[0]-1:
            startx += 1
        l[startx][starty] = snake
        if l[startx][starty] == l[random_coord[1]][random_coord[0]]:
            l[random_coord[1]][random_coord[0]] = 0
            snake += '*'
            random_x = random.randint(0, size[1]-1)
            random_y= random.randint(0, size[0]-1)
            random_coord = [random_x, random_y]
        for i in range(len(l)):
            for j in l[i]:
                print(j, end = " ")
            print()
        time.sleep(0.10)
        

    
    

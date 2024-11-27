import pygame as p
# from pygame.locals  import *

p.init() 

Screen_width = 300
Screen_height = 300 

screen = p.display.set_mode((Screen_width , Screen_height))
p.display.set_caption("X-O-X")
 
 #define variable 
lineWidth = 6
markers = []
clicked = False
pos = []
player = 1
winner = 1 
gameOver = False

font = p.font.SysFont(None,40)

#create again rect 
again_rect = p.Rect(Screen_width // 2 - 80 , Screen_height // 2 + 10 , 175 , 50)

#define colours
green = (0,0,255)
red = (255 , 0,0)

def drawGrid():
    grid = (50 , 50 ,50)
    bg = (255 ,200,200)
    screen.fill(bg)
    for x in range(1,3):
        p.draw.line(screen , grid , (0, x*100),(Screen_height , x*100),lineWidth)
        p.draw.line(screen , grid , (x*100 , 0),(x*100 , Screen_width),lineWidth)

for x in range(3) :
    row = [0]*3
    markers.append(row)

def drawMarker():
    x_pos = 0 
    for x in markers :
        y_pos = 0
        for y in x :
            if y == 1 :
                p.draw.line(screen,green,(x_pos*100 + 15 , y_pos*100 + 15),(x_pos*100 + 85,y_pos*100 + 85),lineWidth)
                p.draw.line(screen,green,(x_pos*100 + 15 , y_pos*100 + 85),(x_pos*100 + 85,y_pos*100 + 15),lineWidth)
            elif y == -1 :
                p.draw.circle(screen, red,(x_pos*100 + 50 ,y_pos*100 + 50),38,lineWidth)
            y_pos += 1
        x_pos += 1

def check_Winner():
    global winner
    global gameOver
    y_pos = 0

    for x in markers:
    # check columns
        if sum(x) == 3 :
            winner = 1
            gameOver = True
        if sum(x) == -3 :
            winner = 2
            gameOver = True
    # check rows
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3 :
            winner = 1
            gameOver = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3 :
            winner = 2
            gameOver = True
        y_pos += 1

    # check cross 
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        gameOver = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        gameOver = True
        
def drawWinner(winner) :
    win_text = "Player " + str(winner) +" Wins !"
    win_img = font.render(win_text, True , red)
    p.draw.rect(screen , green , (Screen_width // 2 - 100, Screen_height// 2 - 60, 220 , 50))
    screen.blit(win_img,(Screen_width // 2 - 90, Screen_height// 2 - 50))

    playAgain = "Play Again ?" 
    again_img = font.render(playAgain , True , red)
    p.draw.rect(screen , green , again_rect)
    screen.blit(again_img , (Screen_width // 2 - 80 , Screen_height // 2 + 20))

run = True
while run :

    drawGrid()
    drawMarker()

    for events in p.event.get():
        if events.type == p.QUIT :
            run = False 
        if gameOver == 0 :
            if events.type == p.MOUSEBUTTONDOWN and clicked == False :
                clicked = True
            if events.type == p.MOUSEBUTTONUP and clicked == True :
                clicked = False
                pos = p.mouse.get_pos()
                cell_x = pos[0] // 100
                cell_y = pos[1] // 100
                if markers[cell_x][cell_y] == 0 : 
                    markers[cell_x][cell_y] = player
                    player *= -1
                    check_Winner() 

    
    if gameOver == True :
        drawWinner(winner)  
    # check for mouse click on play again  
    if events.type == p.MOUSEBUTTONDOWN and clicked == False :
            clicked = True
    if events.type == p.MOUSEBUTTONUP and clicked == True :
            clicked = False
            pos = p.mouse.get_pos()
            if again_rect.collidepoint(pos) :
                #reset variables 
                markers = []
                pos = []
                player = 1
                winner = 1 
                gameOver = False

                for x in range(3):
                    row = [0] * 3
                    markers.append(row)

    
    p.display.update()

p.quit()
import turtle
import time
import random
delay=0.1
#score
score=0
high_score=0

#set up screen
wn=turtle.Screen()
wn.title("snake game")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0) #turns off the screen updates

#snake head
head=turtle.Turtle()
head.speed(0) #animation speed not snake speed
head.shape("square")
head.color("black")
head.penup() #turtle module usually draws lines & penup doesnt allow to do so
head.goto(0,0) #when head starts ,want it to be at the center of the screen
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0) #animation speed not snake speed
food.shape("circle")
food.color("red")
food.penup() #turtle module usually draws lines & penup doesnt allow to do so
food.goto(0,0) #when head starts ,want it to be at the center of the screen

segments=[]

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,270)
pen.write("score:0 high score:0",align="center",font=("courier",24,"normal"))


#function
def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction!="up":
        head.direction="down"
def go_left():
    if head.direction!="right":
        head.direction="left"
def go_right():
    if head.direction!="left":
        head.direction="right"        
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)            
#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")



#main loop
while True:
    wn.update() #everytime updates the screen
    
    #collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #hide segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear segments list when snake goes off the screen
        segments.clear()  

        #reset delay
        delay=0.1

        #reset score
        score=0   
        pen.clear()    
        pen.write("score:{} high score:{}".format(score,high_score),align="center",font=("courier",24,"normal"))    
    
    #collision with food
    if head.distance(food)<20:
        #move food to random spot
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        #shorten delay (vn snake gets too long)
        delay-=0.001 
        #inc score
        score+=10
        if score>high_score:
            high_score=score
        pen.clear()    
        pen.write("score:{} high score:{}".format(score,high_score),align="center",font=("courier",24,"normal"))    
    #move end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y) 

    #move seg0 to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)      

    move()

    #collision with body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            #hide segments
            for segment in segments:
                segment.goto(1000,1000)

            #clear segments list when snake goes off the screen
            segments.clear()  

            #reset delay
            delay=0.1

            #reset score
            score=0   
            pen.clear()    
            pen.write("score:{} high score:{}".format(score,high_score),align="center",font=("courier",24,"normal"))    
       



    time.sleep(delay)
#resetting delays(border & body segments collisions), 
# because as the length of the snake incs the speed increases,
# if the snake hits border or its own body segment the snake must restart vth a normal speed.

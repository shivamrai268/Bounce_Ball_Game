from tkinter import *
import time
tk = Tk()
tk.title("Bouncing Ball Game")
canvas_width = 900
canvas_height = 500
y_padding = 20
canvas = Canvas(tk, width=canvas_width, height=canvas_height, bg="grey")
platform_y = canvas_height - y_padding

bat_height = 20
bat_width = 200
ball_radius = 20


#create bat width , height
bat_x1_position = canvas_width // 2 - 50
bat_y1_position = canvas_height - bat_height
bat_x2_position = bat_x1_position + bat_width
bat_y2_position = canvas_height

# create bat
bat = canvas.create_rectangle(bat_x1_position, bat_y1_position, bat_x2_position, bat_y2_position, fill='black')
print("bat ", bat)

#create_oval with their axis and value
#x1, y1, x2, y2,

ball_x1_position = canvas_width // 2 - 20
ball_y1_position = canvas_height // 6 - 30
ball_x2_position = ball_x1_position + 2 * ball_radius

ball_y2_position = ball_y1_position + 2 * ball_radius

# create ball

ball = canvas.create_oval(ball_x1_position, ball_y1_position, ball_x2_position, ball_y2_position, fill="green")
canvas.pack()

#bat moving variable and their value
bat_speed_right = 9
bat_id = 1
bat_speed_right_down = 0
bat_speed_left = -bat_speed_right
bat_speed_left_down = bat_speed_right_down


#text x and y
text_X = canvas_width // 2
text_Y = canvas_height // 2



def play_game(ball_x_speed=2, ball_y_speed=2):
    """play game ,ball speed , ball coords"""

#run forever - until game is over
    count=0
    while True:
        canvas.move(ball, -ball_x_speed, -ball_y_speed)
        ball_X1, ball_Y1, ball_X2, ball_Y2 = canvas.coords(ball)


        # hit top wall, reverse ball_y_speed
        if ball_Y2 >= canvas_height or ball_Y1 <= 0:
            ball_y_speed = -ball_y_speed

        # hit wall, reverse ball_x_speed
        elif ball_X2 >= canvas_width or ball_X1 <= 0:
            ball_x_speed = -ball_x_speed



        #see if the ball is below bat..
        elif ball_Y2 >= platform_y:

            ball_radius = (ball_X1 + ball_X2) // 2 # checking center of ball
            print("Ball Radius : ", ball_radius)

            # checking bat is hit
            bat_X1, bat_Y1, bat_X2, bat_Y2 = canvas.coords(bat)

            #print(batX1, ball_radius, batX2)

            # hit bat, reverse ball_x_speed
            # hit bat, reverse ball_y_speed
            if bat_X1 <= ball_radius <= bat_X2:
                ball_y_speed = -ball_y_speed + 0.5
                ball_x_speed = -ball_x_speed + 0.5
                count +=1
                #Score=("Your Score: {} ".format(count))
                #print(Score)
                #print("total score ",count)


                #canvas.create_text(450, 250, text='Game Not Over', font=("Calibri",100), fill='red')

            # did not hit bat, show the Game Over
            else:

                canvas.create_text(text_X, text_Y, text='Game Over', font=("Calibri", 100), fill='red')
                Score = ("Your Score: {} ".format(count))
                #print(Score)
                canvas.create_text(110, 40, text=Score, font=("Calibri", 25), fill='blue')
                return

            #return
        #update the game
        tk.update()

        time.sleep(0.02)

    # time delay and a function name
    canvas.after(2, play_game)

    #tk.mainloop()


#move bat right
def bat_right(event, bat_id=1, bat_speed_right=7, bat_speed_right_down=0):
    """bat move right direction and bat speed"""

    #global bat_speed_right, bat_x, bat_speed_right_down

    canvas.move(bat_id, bat_speed_right, bat_speed_right_down)
    tk.update()


#move bat left
def bat_left(event, bat_id=1, bat_speed_left=-bat_speed_right, bat_speed_left_down=0):
    """bat move left direction and bat speed"""
    #global bat_speed_left, bat_x, bat_speed_left_down

    canvas.move(bat_id, bat_speed_left, bat_speed_left_down)
    tk.update()



# bind the Python method and function into event
canvas.bind_all("<Right>", bat_right)
canvas.bind_all("<Left>", bat_left)

play_game(ball_x_speed=2, ball_y_speed=2)
tk.mainloop()
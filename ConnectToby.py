#Toby Aug 16 2023
#This is a connect 4 type game with customizable height, width, and winning conditions

import operator
import time

def make_square_fall(screen_width, screen_height, x_coordinate, starting_y, ending_y, square_size, square_color, speed, red_clicked_boxes_list, yellow_clicked_boxes_list, lines_to_draw, bottom_box):
    import pygame
    dis = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    current_y_coordinate = starting_y
    while True:
        pygame.draw.rect(dis, square_color, pygame.Rect(x_coordinate, current_y_coordinate, square_size, square_size))
        for my_box in red_clicked_boxes_list:
            pygame.draw.rect(dis, "red", my_box)
        for my_box in yellow_clicked_boxes_list:
            pygame.draw.rect(dis, "yellow", my_box)
        for my_line in lines_to_draw:
            pygame.draw.rect(dis, "sky blue", my_line)
            pygame.draw.rect(dis, "green", bottom_box)
        pygame.display.flip()
        clock.tick(60)
        current_y_coordinate = current_y_coordinate + speed
        dis.fill((0, 0, 0))
        if (current_y_coordinate > ending_y):
            break

def vertical_horizontal_wins(direction):
    global did_player_win
    global text_to_write
    red_points = 0
    yellow_points = 0
    checking_num = 1
    reset_num = 1
    if (direction == "vertical"):
        rounds_till_done = width_in_squares
        rounds_till_section_change = height_in_squares
    else:
        rounds_till_done = height_in_squares
        rounds_till_section_change = width_in_squares + 1
    while True:
        if (red_points == squares_to_win):
            text_to_write = (red_player + " is the Winner!!!")
            if (did_player_win == "No"):
                did_player_win = "Yes"
        if (yellow_points == squares_to_win):
            text_to_write = (yellow_player + " is the Winner!!!")
            if (did_player_win == "No"):
                did_player_win = "Yes"
        if (rounds_till_done == 0):
            break
        if (rounds_till_section_change == 0):
            if (direction == "vertical"):
                rounds_till_section_change = height_in_squares
            else:
                rounds_till_section_change = width_in_squares + 1
            rounds_till_done = rounds_till_done - 1
            red_points = 0
            yellow_points = 0
            if (direction == "horizontal"):
                reset_num = reset_num + 1
                checking_num = reset_num - height_in_squares
        if (checking_num in red_num_boxes_list):
            red_points = red_points + 1
            yellow_points = 0
        elif (checking_num in yellow_num_boxes_list):
            yellow_points = yellow_points + 1
            red_points = 0
        else:
            red_points = 0
            yellow_points = 0
        rounds_till_section_change = rounds_till_section_change - 1
        if (direction == "vertical"):
            checking_num = checking_num + 1
        else:
            checking_num = checking_num + height_in_squares

def make_clickable_regions():
    squares_drawn = 0
    while True:
        if (squares_drawn == width_in_squares):
            squares_drawn = 0
            break
        if (squares_drawn == 0):
            starting_box = 0
        else: 
            starting_box = WIDTH * (squares_drawn / width_in_squares)
        box = Rect(starting_box + 10, 0, box_width + 10, height_amount + height_above)
        boxes_to_draw.append(box)
        squares_drawn = squares_drawn + 1

def diagonal_wins_for_one_player(person, checking_num, direction, points):
    global did_player_win
    global text_to_write
    if (person == red_player):
        color_num_boxes_list = red_num_boxes_list
    else:
        color_num_boxes_list = yellow_num_boxes_list
    color_points = 1
    while True:
        if (direction == "right"):
            checking_num = checking_num + height_in_squares + 1
        else:
            checking_num = checking_num + height_in_squares - 1
        if (checking_num in color_num_boxes_list):
            color_points = color_points + 1
        else:
            color_points = 0
            break
        if (color_points == squares_to_win):
            if ((points - squares_to_win) > -1):
                text_to_write = (person + " is the Winner!!!")
                if (did_player_win == "No"):
                    did_player_win = "Yes"
    return text_to_write

def diagonal_wins(direction):
    checking_num = 1
    if (direction == "right"):
        points = height_in_squares
    else:
        points = 1
    while True:
        if (direction == "right"):
            if (points == 0):
                points = height_in_squares
        else:
            if (points == height_in_squares + 1):
                points = 1
        if (checking_num == width_in_squares * height_in_squares + 1):
            break
        if (checking_num in red_num_boxes_list):
            diagonal_wins_for_one_player(red_player, checking_num, direction, points)
        elif (checking_num in yellow_num_boxes_list):
            diagonal_wins_for_one_player(yellow_player, checking_num, direction, points)
        checking_num = checking_num + 1  
        if (direction == "right"):
            points = points - 1
        else:
            points = points + 1

def make_vertical_lines():
    lines_drawn = 0
    while True:
        if (lines_drawn == width_in_squares + 1):
            break
        if (lines_drawn == 0):
            starting_line = 0
        else:
            starting_line = width_amount * (lines_drawn / width_in_squares)
        line = Rect(starting_line, height_above, line_thickness, height_amount + height_above)
        line_width_list.append(starting_line)
        lines_to_draw.append(line)
        lines_drawn = lines_drawn + 1

def make_horizontal_lines():
    lines_drawn = 2
    while True:
        if (lines_drawn == height_in_squares + 1):
            break
        starting_line = height_amount * (lines_drawn / height_in_squares)
        line = Rect(0, starting_line - (height_above / 2) + 30, WIDTH, line_thickness)
        line_height_list.append(starting_line - (height_above / 2) + 30)
        lines_to_draw.append(line)
        lines_drawn = lines_drawn + 1

def call_win_check_functions():
    vertical_horizontal_wins("vertical")
    vertical_horizontal_wins("horizontal")
    diagonal_wins("right")
    diagonal_wins("left")

def quack():
    music.play("quack.mp3")
    time.sleep(0.5)
    music.stop()

end_game = "No"
import pygame
height_amount = int(input("What is the pixel height of the board? "))
width_amount = int(input("What is the pixel width of the board? "))
height_in_squares = int(input("How many vertical squares? "))
width_in_squares = int(input("How many horizontal squares? ")) 
squares_to_win = int(input("How many squares do you need in a row to win? "))
red_player = input("What is the name of the red player? ")
yellow_player = input("What is the name of the yellow player? ")
height_above = (height_amount / (height_in_squares + 2)) + 20 
HEIGHT = height_amount + 100 + height_above
line_thickness = 5
WIDTH = width_amount + line_thickness
squares_drawn = 0
boxes_to_draw = list()
test = 0
turns_gone = 0
box_width = int((WIDTH / width_in_squares) - 20)
lines_to_draw = list()
red_clicked_boxes_list = list()
yellow_clicked_boxes_list = list()
red_num_boxes_list = list()
yellow_num_boxes_list = list()
boxes_list = list()
text_to_write = ("It is time for " + red_player + " to go now!")
player_turn = 0
line_height_list = list()
line_width_list = list()
did_player_win = "No"
boxes_already_clicked_list = list()
bottom_box = Rect(0, height_amount + height_above, WIDTH, 100)
make_horizontal_lines()
dif = line_height_list[1] - line_height_list[0] 
line_height_list.append(line_height_list[0] - dif)
line_height_list.insert(0, line_height_list.pop())
make_clickable_regions()
make_vertical_lines()
#print (line_width_list)
def on_mouse_down(pos):
    global text_to_write
    global player_turn
    global did_player_win
    global turns_gone
    index = 1
    for box in boxes_list:
        if (index == width_in_squares + 1):
            break
        if box.collidepoint(pos):
            #print("Clicked on box " + str(index))
            while True:
                if (did_player_win == "True"):
                    break
                multiply_by = (2 * index - 1)
                box_x_value = WIDTH / width_in_squares / 2 * multiply_by
                x_size = WIDTH / width_in_squares
                y_size = HEIGHT / height_in_squares
                dimension_size = WIDTH / width_in_squares
                if (x_size <= y_size):
                    dimension_size = WIDTH / width_in_squares / 2
                else:
                    dimension_size = HEIGHT / height_in_squares / 2
                amount_of_box_clicked = operator.countOf(boxes_already_clicked_list,index)
                if (amount_of_box_clicked == height_in_squares):
                    break
                pos_timesed_by_num = index - 1
                square_pos = pos_timesed_by_num * height_in_squares + amount_of_box_clicked + 1
                height_value = line_height_list[height_in_squares - amount_of_box_clicked - 1]
                width_value = line_width_list[index - 1]
                #print (square_pos)
                new_box = Rect(width_value + line_thickness + (line_width_list[1] - dimension_size) / 2, height_value + line_thickness + (dif - dimension_size) / 2, dimension_size, dimension_size)
                if (player_turn == 0):
                    current_color = "red"
                else:
                    current_color = "yellow"
                if (end_game == "No"):
                    make_square_fall(WIDTH, HEIGHT, width_value + line_thickness + (line_width_list[1] - dimension_size) / 2, 0, height_value + line_thickness + (dif - dimension_size) / 2, dimension_size, current_color, 5, red_clicked_boxes_list, yellow_clicked_boxes_list, lines_to_draw, bottom_box)
                quack()
                if (player_turn == 0):
                    text_to_write = ("It is time for " + yellow_player + " to go now!")
                    red_num_boxes_list.append(square_pos)
                    player_turn = 1
                    red_clicked_boxes_list.append(new_box)
                else:
                    text_to_write = ("It is time for " + red_player + " to go now!")
                    yellow_num_boxes_list.append(square_pos)
                    player_turn = 0
                    yellow_clicked_boxes_list.append(new_box)
                boxes_already_clicked_list.append(index)
                call_win_check_functions()
                turns_gone = turns_gone + 1
                if (turns_gone >= height_in_squares * width_in_squares):
                    text_to_write = red_player + " and " + yellow_player + " tied."
                break                 
        index = index + 1
def draw():
    global did_player_win
    global end_game
    if (end_game == "No"):
        for my_box in boxes_to_draw:
            screen.draw.filled_rect(my_box, "black")
            boxes_list.append(my_box)
        for my_box in red_clicked_boxes_list:
            screen.draw.filled_rect(my_box, "red")
        for my_box in yellow_clicked_boxes_list:
            screen.draw.filled_rect(my_box, "yellow")
        for my_line in lines_to_draw:
            screen.draw.filled_rect(my_line, "sky blue")
            screen.draw.filled_rect(bottom_box, "green")
        screen.draw.textbox(text_to_write, bottom_box, color=("blue"))
        if (did_player_win == "Yes"):
            end_game = "Yes"

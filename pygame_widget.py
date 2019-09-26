import pygame
import subprocess

def button(window, text, x, y, width, height, inactivecolor, activecolor, font, size, fg, command = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(window, activecolor,(x, y, width, height))

        if click[0] == 1 and command != None:
            command()
    else:
        pygame.draw.rect(window, inactivecolor,(x, y, width, height))

    text_font = pygame.font.SysFont(font, size)
    textSurf, textRect = text_objects(text, text_font, fg)
    textRect.center = ( (x + (width / 2)), (y + (height / 2)) )
    window.blit(textSurf, textRect)

def level_button(window, text, x, y, width, height, inactivecolor, activecolor, font, size, fg, user_xp, xp, activecolor2, command = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y and int(user_xp) >= xp:
        pygame.draw.rect(window, activecolor,(x, y, width, height))
        if click[0] == 1 and command != None:
            command()
    elif x + width > mouse[0] > x and y + height > mouse[1] > y and int(user_xp) < xp:
        pygame.draw.rect(window, activecolor2,(x, y, width, height))
        if click[0] == 1:
            label(window, text = "You don't have enought xp! " + str(xp) + " xp required.", x = 600, y = 500, font = "Century", size = 40, fg = (238, 85, 0))
    elif int(user_xp) < xp:
        pygame.draw.rect(window, activecolor2,(x, y, width, height))
    else:
        pygame.draw.rect(window, inactivecolor,(x, y, width, height))

    text_font = pygame.font.SysFont(font, size)
    textSurf, textRect = text_objects(text, text_font, fg)
    textRect.center = ( (x + (width / 2)), (y + (height / 2)) )
    window.blit(textSurf, textRect)

def label(window, text, x, y, font, size, fg):
    label_font = pygame.font.SysFont(font, size)
    label = label_font.render(text, 1, fg)
    width = label.get_width()
    window.blit(label, ( (x - (width / 2)), y))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    # Create the text rect.
    textRect = textSurface.get_rect()
    # Return a tuple consisting of the surface and the rect.
    return textSurface, textRect

def user_create(name):
    file = open(directory() + "users\\" + name + ".HoM", "w")

    file.write(name + "\n")#name
    file.write("100" + "\n")#health
    file.write("10" + "\n")#attack
    file.write("0" + "\n")#defense
    file.write("5" + "\n")#accuracy
    file.write("0" + "\n")#xp
    file.write("0")#money

    file.close()

def directory():
    global current_directory_string
    current_directory = subprocess.check_output('echo %cd%', shell = True)
    current_directory_list = list(str(current_directory))
    if "b" in current_directory_list and "'" in current_directory_list:
        current_directory_list.remove("b")
        current_directory_list.remove("'")

    for _ in range(0, 4):
        current_directory_list.pop()

    current_directory_string = ''.join(current_directory_list)
    return current_directory_string

def load_information(user_name):
    global file_lines
    global username, health, attack, defense, accuracy, xp, money
    file_lines = []
    with open(directory() + "users\\" + user_name + ".HoM", "r") as file:
        for file_line in file:
            file_lines.append(file_line)

    while True:
        try:
            file_lines.remove("\n")
        except:
            break

    username = file_lines[0]
    health = file_lines[1]
    attack = file_lines[2]
    defense = file_lines[3]
    accuracy = file_lines[4]
    xp = file_lines[5]
    money = file_lines[6]

    return file_lines

def modify_information(user_name, health, attack, defense, accuracy, xp, money):
    user_name_list = list(user_name)
    for _ in range(0, 1):
        user_name_list.pop()

    user_name = ''.join(user_name_list)
    
    file = open(directory() + "users\\" + user_name + ".HoM", "w")

    file.write(user_name + "\n")#name
    file.write(str(health) + "\n")#health
    file.write(str(attack) + "\n")#attack
    file.write(str(defense) + "\n")#defense
    file.write(str(accuracy) + "\n")#accuracy
    file.write(str(xp) + "\n")#xp
    file.write(str(money))#money

    file.close()
import pygame
import subprocess

def button(window, text, x, y, width, height, inactivecolor, activecolor, font, size, fg, command = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(window, activecolor, (x, y, width, height))

        if click[0] == 1 and command != None:
            command()
    else:
        pygame.draw.rect(window, inactivecolor, (x, y, width, height))

    textSurf, textRect = text_objects(text, pygame.font.SysFont(font, size), fg)
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

    textSurf, textRect = text_objects(text, pygame.font.SysFont(font, size), fg)
    textRect.center = ( (x + (width / 2)), (y + (height / 2)) )
    window.blit(textSurf, textRect)

def label(window, text, x, y, font, size, fg):
    label_font = pygame.font.SysFont(font, size)
    label = label_font.render(text, 1, fg)
    window.blit(label, ( (x - (label.get_width() / 2)), y))

def text_objects(text, font, color):
    # Create the text rect and return a tuple consisting of the surface and the rect.
    return font.render(text, True, color), textSurface.get_rect()

def user_create(name):
    file = open(directory() + "users\\" + name + ".HoM", "w")
    file.write(name + "\n100\n10\n0\n5\n0\n0")#name, health, attack, defense, accuracy, xp and money
    file.close()

def directory():
    global current_directory_string
    current_directory_list = list(str(subprocess.check_output('echo %cd%', shell = True)))
    
    if "b" in current_directory_list and "'" in current_directory_list:
        current_directory_list.remove("b")
        current_directory_list.remove("'")

    for _ in range(0, 4): current_directory_list.pop()

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

    username, health, attack, defense, accuracy, xp, money = file_lines

    return file_lines

def modify_information(user_name, health, attack, defense, accuracy, xp, money):
    user_name_list = list(user_name)
    user_name_list.pop()
    user_name = ''.join(user_name_list)
    
    file = open(directory() + "users\\" + user_name + ".HoM", "w")
    file.write('\n'.join([user_name, str(health), str(attack), str(defense), str(accuracy), str(xp), str(money)]))#name, health, attack, defense, accuracy, xp and money
    file.close()

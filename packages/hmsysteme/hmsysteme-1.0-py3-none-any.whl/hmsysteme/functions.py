import pygame
import pickle
import os
import errno
from pathlib import Path


BUFFER_SIZE = 10
BUFFER_SIZE2 = 100
path = os.path.realpath(__file__)
path = path.replace('functions.py', '')

pipe_name = '/tmp/screenhot_pipe'
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)
pipe_screen = os.open(pipe_name, os.O_RDONLY | os.O_NONBLOCK)

pipe_name = '/tmp/isactive_pipe'
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)
pipe_isactive = os.open(pipe_name, os.O_RDONLY | os.O_NONBLOCK)

pipe_name = '/tmp/hit_pipe'
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)
pipe_hit = os.open(pipe_name, os.O_RDONLY | os.O_NONBLOCK)

pipe_name = '/tmp/action_pipe'
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)
pipe_action = os.open(pipe_name, os.O_RDONLY | os.O_NONBLOCK)

pipe_name = '/tmp/buttonnames_pipe'
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)
pipe_buttonnames = os.open(pipe_name, os.O_RDONLY | os.O_NONBLOCK)

pipe_name = '/tmp/temp_pipe'
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)
pipe_temp = os.open(pipe_name, os.O_RDONLY | os.O_NONBLOCK)

pipe_name = '/tmp/pos_pipe'
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)
pipe_pos = os.open(pipe_name, os.O_RDONLY | os.O_NONBLOCK)

pipe_name = '/tmp/pos_color'
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)
pipe_color = os.open(pipe_name, os.O_RDONLY | os.O_NONBLOCK)




def get_path():
    return path


def get_size():
    return (1360, 768)

def clear_pickle(filename, val):
    file = open((os.path.join(path, filename)), 'wb')
    pickle.dump(val, file)
    file.close()


def get_rgbcolor():
    try:
        buffer = os.read(pipe_color, BUFFER_SIZE2)
        # print(buffer)
        # buffer contains some received data -- do something with it
        buffer = buffer.decode("utf-8")
        a = buffer.split(';')
        print(a)
        return a

    except Exception as e:
        print(e)
        return False


def put_rgbcolor(color):
    # Open the pipe for writing
    namestring = ""
    for ele in color:
        namestring = namestring + str(ele) + str(";")
    namestring=namestring[:-1]
    pipe_name = '/tmp/color_pipe'
    pipe_out = open(pipe_name, 'w')
    pipe_out.write(namestring)
    pipe_out.flush()




def take_screenshot(screen):
    try:
        os.remove(os.path.join(path, "screencapture.jpg"))
    except:
        pass
    pygame.image.save(screen, os.path.join(path, "screencapture.jpg"))
    # Open the pipe for writing
    pipe_name = '/tmp/screenhot_pipe'
    pipe_out = open(pipe_name, 'w')
    pipe_out.write('True')
    pipe_out.flush()


def screenshot_refresh():
    try:
        buffer = os.read(pipe_screen, BUFFER_SIZE)
        # print(buffer)
        # buffer contains some received data -- do something with it
        if buffer == b'True':
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False


def game_isactive():
    try:
        buffer = os.read(pipe_isactive, BUFFER_SIZE)
        # print(buffer)
        # buffer contains some received data -- do something with it
        if buffer == b'True':
            return False
        else:
            return True

    except Exception as e:
        print(e)
        return False


def close_pygame():
    # Open the pipe for writing
    pipe_name = '/tmp/isactive_pipe'
    pipe_out = open(pipe_name, 'w')
    pipe_out.write('True')
    pipe_out.flush()


def get_pos():
    try:
        buffer = os.read(pipe_pos, BUFFER_SIZE2)
        # print(buffer)
        # buffer contains some received data -- do something with it
        buffer = buffer.decode("utf-8")
        a = buffer.split(';')
        print(a)
        return a

    except Exception as e:
        print(e)
        return False


def put_pos(pos):
    # Open the pipe for writing
    namestring = ""
    for ele in pos:
        namestring = namestring + str(ele) + str(";")
    namestring=namestring[:-1]
    pipe_name = '/tmp/pos_pipe'
    pipe_out = open(pipe_name, 'w')
    pipe_out.write(namestring)
    pipe_out.flush()



def get_temp():
    try:
        buffer = os.read(pipe_temp, BUFFER_SIZE)
        # print(buffer)
        # buffer contains some received data -- do something with it
        buffer = buffer.decode("utf-8")
        if buffer != "":
            a = int(buffer)
            return a
        else:
            return False

    except Exception as e:
        print(e)
        return False


def put_temp(temp):
    # Open the pipe for writing
    pipe_name = '/tmp/temp_pipe'
    pipe_out = open(pipe_name, 'w')
    pipe_out.write(str(temp))
    pipe_out.flush()




def get_button_names():
    try:
        buffer = os.read(pipe_buttonnames, BUFFER_SIZE2)
        # print(buffer)
        # buffer contains some received data -- do something with it
        buffer = buffer.decode("utf-8")
        a = buffer.split(';')
        #print(a)
        if a == [""]:
            return False
        else:
            return a

    except Exception as e:
        print(e)
        return False


def put_button_names(names):
    # Open the pipe for writing
    namestring = ""
    for ele in names:
        namestring = namestring + str(ele) + str(";")
    namestring=namestring[:-1]
    pipe_name = '/tmp/buttonnames_pipe'
    pipe_out = open(pipe_name, 'w')
    pipe_out.write(namestring)
    pipe_out.flush()


def hit_detected():
    try:
        buffer = os.read(pipe_hit, BUFFER_SIZE)
        # print(buffer)
        # buffer contains some received data -- do something with it
        if buffer == b'True':
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False


def put_hit():
    # Open the pipe for writing
    pipe_name = '/tmp/hit_pipe'
    pipe_out = open(pipe_name, 'w')
    pipe_out.write('True')
    pipe_out.flush()


def get_action():
    try:
        buffer = os.read(pipe_action, BUFFER_SIZE)
        # print(buffer)
        # buffer contains some received data -- do something with it
        buffer = buffer.decode("utf-8")
        if buffer != "":
            a = int(buffer)
            return a
        else:
            return False

    except Exception as e:
        print(e)
        return False


def put_action(number):
    # Open the pipe for writing
    pipe_name = '/tmp/action_pipe'
    pipe_out = open(pipe_name, 'w')
    pipe_out.write(str(number))
    pipe_out.flush()


def put_playernames(playernames):
    file = open((os.path.join(path, "hmplayers")), 'wb')
    pickle.dump(playernames, file)
    file.close()


def get_playernames():
    try:
        file = open((os.path.join(path, "hmplayers")), 'rb')
        q = pickle.load(file)
        file.close()
        if q != False:
            w = []
            for i in range(0, len(q)):
                if q[i][1] == True:
                    w.append(q[i][0])
            return w
        else:
            return False
    except:
        return False



def clear_all():
    clear_pickle("hmplayers", False)






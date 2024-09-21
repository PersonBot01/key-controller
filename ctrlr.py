import pyglet
import pyautogui

controllers = pyglet.input.get_controllers()

up = False
down = False
left = False
L1 = False
L2 = False
R1 = False
R2 = False
active_trigger_L2 = False
active_trigger_R2 = False
Lstick = False
Rstick = False
pos_threshold = 0.5
neg_threshold = -0.5
current_x, current_y = pyautogui.position()
keys = [['a','b','c','d'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p'], ['q', 'r', 's', 't'], ['u', 'v', 'w', 'x'], ['y', 'z', ',', '.']]
active = []


if controllers:
    controller = controllers[0]
    controller.open()

@controller.event
def on_stick_motion(controller, name, x_value, y_value):
    global Lstick, Rstick, current_x, current_y
    sensitivity = 100
#mouse cursor control
    if name == "leftstick":
        if y_value >= pos_threshold:#moves cursor up from current postition
            Lstick = not Lstick
            if Lstick:
                pyautogui.moveTo(None, current_y - sensitivity, 1)
                current_x, current_y = pyautogui.position()
            if not Lstick:
                pyautogui.moveTo(None, None)
        if y_value <= neg_threshold:#moves cursor down from current postition
            Lstick = not Lstick
            if Lstick:
                pyautogui.moveTo(None, current_y + sensitivity, 1)
                current_x, current_y = pyautogui.position()
            if not Lstick:
                pyautogui.moveTo(None, None)
        if x_value >= pos_threshold:#moves cursor right from current postition
            Lstick = not Lstick
            if Lstick:
                pyautogui.moveTo(current_x + sensitivity, None, 1)
                current_x, current_y = pyautogui.position()
            if not Lstick:
                pyautogui.moveTo(None, None)
        if x_value <= neg_threshold:#moves cursor left from current postition
            Lstick = not Lstick
            if Lstick:
                pyautogui.moveTo(current_x - sensitivity, None, 1)
                current_x, current_y = pyautogui.position()
            if not Lstick:
                pyautogui.moveTo(None, None)
#arrow keys control:
    if name == "rightstick":
        if y_value >= pos_threshold:
            pyautogui.keyDown('up')
    if name == "rightstick":
        if y_value <= neg_threshold:
            pyautogui.keyDown('down')
    if name == "rightstick":
        if x_value >= pos_threshold:
            pyautogui.keyDown('right')
    if name == "rightstick":
        if x_value <= neg_threshold:
            pyautogui.keyDown('left')
#L2 and R2 bool control
@controller.event
def on_trigger_motion(controller, button_name, value):
    global L2, R2, active, active_trigger_L2, active_trigger_R2
    threshold = 0.5
    if button_name == 'lefttrigger':
        if value >= threshold:
            if not active_trigger_L2:
                L2 = not L2
                active_trigger_L2 = not active_trigger_L2
        else:
            active_trigger_L2 = not active_trigger_L2
    if button_name == 'righttrigger':
        if value >= threshold:
            if not active_trigger_R2:
                R2 = not R2
                active_trigger_R2 = not active_trigger_R2
        else:
            active_trigger_R2 = not active_trigger_R2
#L1 and R1 bool control
@controller.event
def on_button_press(controller, button_name):
    global L1, R1, active
    if button_name == 'leftshoulder':
        L1 = not L1
    if button_name == 'rightshoulder':
        R1 = not R1

#face button state control
    
    if (L1 and L2 and R1 and R2) == False: #default setting when shoulder and triggers are false ['a','b','c','d']
        active = keys[0]
    if L1 and (not L2) and (not R1) and (not R2): #setting when only left shoulder is active ['e', 'f', 'g', 'h']
        active = keys[1]
    if R1 and (not L1) and(not L2) and (not R2): #setting when only right shoulder is active ['i', 'j', 'k', 'l']
        active = keys[2]
    if L2 and (not L1) and (not R1) and (not R2): #setting when only left trigger is active ['m', 'n', 'o', 'p']
        active = keys[3]
    if R2 and (not L1) and (not R1) and (not L2): #setting when only right trigger is active ['q', 'r', 's', 't']
        active = keys[4]
    if L1 and R1 and (not L2) and (not R2): #setting when left and right shoulders are active ['u', 'v', 'w', 'x']
        active = keys[5]
    if L2 and R2 and (not L1) and (not R1): #setting when left and right triggers are active ['y', 'z', ',', '.']
        active = keys[6]
    # if L1 and R1 and L2 and (not R2):
    #     active = keys[4]
    # if L1 and R1 and L2 and R2:
    #     active = keys[5]





    if button_name == 'a':
        pyautogui.press(active[0])
        print(active[0])
    if button_name == 'x':
        pyautogui.press(active[1])
        print(active[1])
    if button_name == 'y':
        pyautogui.press(active[2])
        print(active[2])
    if button_name == 'b':
        pyautogui.press(active[3])
        print(active[3])
    if button_name == 'guide':
        pyglet.app.exit()

@controller.event
def on_dpad_motion(controller, dpleft, dpright, dpup, dpdown):
    global up, down, left
    if dpup:
        up = not up
        if not up:
            print(up)
            # pyautogui.hold('shift')
    if dpdown:
        pyautogui.hold('ctrl')
    if dpleft:
        print(dpleft)
    if dpright:
        pyautogui.press('space')

pyglet.app.run()

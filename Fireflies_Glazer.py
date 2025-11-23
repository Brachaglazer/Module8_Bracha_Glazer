"""
Import libraries - simplegui, math, and random

w, h = set canvas width and height
cx, cy = set canvas center- width and height divided by 2
r = [] - create list to hold values for radii

angle = [] - create list to hold radian values for orbitting circle
runnning = declare global variable that will handle the start/stop toggle
speed = declare global variable that will display the current speed in comparison to its origonal speed
color_options = create list to hold the color options that random will choose from
balls= [] - create a list that will hold a dictionary
    one entry per dot {random velocity chosen from range, random color chosen from color_options, random size chosen from range}

define draw handler that frame will call(c):
    c.draw_text(Welcome display, location, size, color)
    c.draw_text(count=6, speed, location, size, color)
    
    for loop- for each angle/dot, compute the x, y along its circular path
        x = CX + R[i] * math.cos(a)
        y = CY + R[i] * math.sin(a)
        
        c.draw_circle(location, size chosen from dictionary,line width, inner and outer color chosen from dictionary)


define timer function that will handle timer():
    for loop to iterate through list, once per angle/dot:
        angle += velocity


define faster function that will handle faster button():
    declare global speed to change it
    speed *= 1.25 
    for loop to iterate through list, once per angle/dot:
        velocity *= 1.25 - speed up the dots


define slower function that will handle slower button():
    declare global speed to change it
    speed /= 1.25 
    for loop to iterate through list, once per angle/dot:
        velocity /= 1.25 - slow up the dots


define toggle function that will handle the start/stop button():
    declare global running to change it
    if running is true:
        t.stop - stop the timer
        running = false - change the timer value to false
        status.set_text(timer is off)
    else running is false:
        t.start - start the timer
        running = true - change the timer value to true
        status.set_text(timer is on)
        
Setup:

frame = simplegui.creat_frame(title, width, height) - create the frame
frame.set_draw_handler(draw-function that will draw)
frame.set_canvas_background(color for canvas)

t = simplegui.create_timer(calls per second, tick0-function to call that will handle timer)

frame.add_button(label=start/stop, function handler=toggle, width)
status = frame.add_label(timer off, width)
frame.add_button(label=faster, function handler=faster, width)
frame.add_button(label=slower, function handler=slower, width)

frame.start() - start the frame loop

"""

# Import libraries necessary to run program.
import simplegui, math, random

W, H = 600, 400  # canvas width/height
CX, CY = W / 2, H / 2  # canvas center
R = [80, 90, 100, 110, 120, 130]  # radii for the six orbits

angle = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]  # angles (radians) for each orbitting dot, will be updated by timer.
running = False  # toggle starts off
speed = 1  # declare global variable that will be edited by user pressing the faster/slower buttons.
color_options = ["Gold", "DeepSkyBlue", "Magenta", "Red", "Blue", "Green"]  # list of colors for random to choose from for the dots.
# Each dots velocity, color, and size will be chosen from this list.
balls = [
    {"vel": random.uniform(0.01, 0.05), "color": random.choice(color_options), "size": random.uniform(10,20)},
    {"vel": random.uniform(0.01, 0.05), "color": random.choice(color_options), "size": random.uniform(10,20)},
    {"vel": random.uniform(0.01, 0.05), "color": random.choice(color_options), "size": random.uniform(10,20)},
    {"vel": random.uniform(0.01, 0.05), "color": random.choice(color_options), "size": random.uniform(10,20)},
    {"vel": random.uniform(0.01, 0.05), "color": random.choice(color_options), "size": random.uniform(10,20)},
    {"vel": random.uniform(0.01, 0.05), "color": random.choice(color_options), "size": random.uniform(10,20)}
]


def draw(c):  # draw handler
    """ Draws title, number of dots, speed, and in a for loop, draws the actual dots."""
    c.draw_text("Welcome to fireflies!", (10, 24), 16, "White")  # title written
    c.draw_text(f"count=6 speedx {speed:.2f}", (10, 36), 12, "White")  # count of dots and current speed relative to starting speed written.

    # For each angle, compute the (x, y) along its circular path and draw it.
    for i, a in enumerate(angle):
        # Convert polar (radius R[i], angle a) to Cartesian (x, y)
        x = CX + R[i] * math.cos(a)
        y = CY + R[i] * math.sin(a)

        # draw circle, the inner and outer color is the same.
        c.draw_circle((x, y), balls[i]["size"], 4, balls[i]["color"], balls[i]["color"])


def tick0():  # timer handler
    """ In a for loop, iterates through angle list to set velocity for each dot."""
    for i in range(len(angle)):  # Iterate through list for each angle
        angle[i] += balls[i]["vel"]  # angle velocity is randomly chosen from the range given
    
    
def faster():  # faster button handler
    """ In a for loop increases the velocity by multiplying the current velocity by 1.25.
    Updates the global variable, speed.
    """
    global speed  # declare global to edit variable value
    speed *= 1.25  # change speed to be displayed
    for i in range(len(angle)):
        balls[i]["vel"] *= 1.25  # multiply the current velocity to speed up
     
    
def slower():  # slower button handler
    """ In a for loop decreases the velocity by dividing the current velocity by 1.25.
    Updates the global variable, speed.
    """
    global speed  # declare global to edit variable value
    speed /= 1.25  # change speed to be displayed
    for i in range(len(angle)):
        balls[i]["vel"] /= 1.25  # divide the current velocity to slow down
       
    
def toggle():  # start/stop button handler
    """ Starts timer if timer was stopped and stops timer if timer was running. 
    Updates the global variabel, running, prints the status of the timer.
    """
    global running  # declare global to edit variable value
    if running:  # if running is true then stop timer and change to false when button clicked
        t.stop()
        running = False
        status.set_text("Timer: OFF")  # display status
    else:  # if running is false then start timer and change to true when button clicked
        t.start()
        running = True
        status.set_text("Timer: ON")  # display status

        
frame = simplegui.create_frame("6 Fireflies: rotate", W, H)  # create the program frame

frame.set_draw_handler(draw)  # set the draw handler

frame.set_canvas_background("#203040")  # set the canvas background color

t = simplegui.create_timer(30, tick0)  # set the timer and function to call

frame.add_button("Start / Stop", toggle, 120)  # create start/stop button and function to handle
status = frame.add_label("Timer: OFF", 120)
frame.add_button("Faster x1.25", faster, 120)  # create faster button and function to handle
frame.add_button("Slower +1.25", slower, 120)  # create slower button and function to handle

frame.start()  # Start the frame loop

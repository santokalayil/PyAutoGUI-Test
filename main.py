import pyautogui as pag
import os

print(pag.position()) # current mouse x and y
print(pag.size()) # current screen resolution width and height
print(pag.onScreen(x=300,y= 300))  # True if x & y are within the screen.

pag.PAUSE = 1 #Set up a 2.5 second pause after each PyAutoGUI call
# When fail-safe mode is True, moving the mouse to the upper-left will raise a pyautogui.
pag.FAILSAFE = True # FailSafeException that can abort your program

num_seconds = 0.2
pag.moveTo(x=1000, y=600, duration=num_seconds)  # move mouse to XY coordinates over num_second seconds
pag.moveRel(xOffset=20, yOffset=20, duration=num_seconds)  # move mouse relative to its current position

pag.dragTo(x=300, y=300, duration=num_seconds, button='left')  # drag mouse to XY
pag.dragRel(xOffset=20, yOffset=20, duration=num_seconds, button='left')  # drag mouse relative to its current position

secs_between_clicks = 0.3
num_of_clicks = 5
pag.click(x=300, y=300, clicks=num_of_clicks, interval=secs_between_clicks, button='left') # 'left','middle','right'

# pag.rightClick(x=moveToX, y=moveToY)
# pag.middleClick(x=moveToX, y=moveToY)
# pag.doubleClick(x=moveToX, y=moveToY)
# pag.tripleClick(x=moveToX, y=moveToY)

# Positive scrolling will scroll up, negative scrolling will scroll down:
amount_to_scroll=200
pag.scroll(amount_to_scroll, x=900, y=500)
amount_to_scroll=-200
pag.scroll(amount_to_scroll, x=900, y=500)

pag.write('Hello world!')                 # prints out "Hello world!" instantly
# Key presses go to wherever the keyboard cursor is at function-calling time
secs_between_keys = 0.5
pag.typewrite('Hello world!\n', interval=secs_between_keys)  # useful for entering text, newline is Enter

# A list of key names can be passed too:
pag.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)

pag.press('f1')                 # presss the key
# The full list of key names is in pag.KEYBOARD_KEYS.
print(pag.KEYBOARD_KEYS)

# Keyboard hotkeys like Ctrl-S or Ctrl-Shift-1
pag.hotkey('ctrl', 'c')  # ctrl-c to copy
pag.hotkey('ctrl', 'v')  # ctrl-v to paste

# Individual button down and up events can be called separately:
pag.keyDown('g')
pag.keyUp('g')

# need to pause the program until the user clicks OK on something
pag.alert('This displays some text with an OK button.')
# alert(text='', title='', button='OK')

pag.confirm('This displays text and has an OK and Cancel button.')
# confirm(text='', title='', buttons=['OK', 'Cancel'])

pag.prompt('This lets the user type in a string and press OK.') # super I can get input from user this function returns it
          # if clicked cancel it will return None
#prompt(text='', title='' , default='')

pag.password(text='', title='', default='', mask='*')

pag.screenshot()  # returns a Pillow/PIL Image object

pag.screenshot('foo.png')  # returns a Pillow/PIL Image object, and saves it to a file

im2 = pyautogui.screenshot('my_screenshot.png') # this method will capture that pillow image to variable im2
pyautogui.screenshot(region=(0,0, 300, 400))

# If you have an image file of something you want to click on, you can find it on the screen with locateOnScreen().

pag.locateOnScreen('looksLikeThis.png')  # returns (left, top, width, height) of first place it is found

# The locateAllOnScreen() function will return a generator for all the locations it is found on the screen
for i in pyautogui.locateAllOnScreen('looksLikeThis.png'):
    print(i)

# OR
list(pyautogui.locateAllOnScreen('looksLikeThis.png'))


# The locateCenterOnScreen() function just returns the XY coordinates of the middle of where the image 
#                                                                                   is found on the screen:

pag.locateCenterOnScreen('looksLikeThis.png')  # returns center x and y

loc = pag.locateOnScreen('help.png')
print(loc.left,loc.top,loc.width,loc.height)

pag.center(loc)

loc = pag.locateCenterOnScreen('help.png')
pag.click(x=loc.x,y=loc.y)

pag.click('help.png')

pag.click('trusted.png')

# pag.click('chrome.png') # shows error
# The optional confidence keyword argument specifies the accuracy with which the function should locate the image on screen

loc= pyautogui.locateOnScreen('chrome.png', confidence=0.9)
#You need to have OpenCV installed for the confidence keyword to work
loc = pag.center(loc)
print(loc)

pag.click(x=loc.x,y=loc.y, button='left')

x, y = pyautogui.locateCenterOnScreen('trusted.png')
print(x, y)

"""
Window handling features:
pyautogui.getWindows() # returns a dict of window titles mapped to window IDs
pyautogui.getWindow(str_title_or_int_id) # returns a “Win” object
win.move(x, y)
win.resize(width, height)
win.maximize()
win.minimize()
win.restore()
win.close()
win.position() # returns (x, y) of top-left corner
win.moveRel(x=0, y=0) # moves relative to the x, y of top-left corner of the window
win.clickRel(x=0, y=0, clicks=1, interval=0.0, button=’left’) # click relative to the x, y of top-left corner of the window
Additions to screenshot functionality so that it can capture specific windows instead of full screen.
"""



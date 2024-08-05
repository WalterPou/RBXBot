import cv2
import numpy as np
import mss
import pydirectinput
import random
import time

# Initialize screen capture
sct = mss.mss()
monitor = sct.monitors[1]
move_interval = 0.5
last_move_time = time.time()

while True:
    # Capture screen
    screenshot = sct.grab(monitor)
    frame = np.array(screenshot)
    
    # Apply Canny edge detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    
    # Randomly move the avatar or send a message
    current_time = time.time()
    if current_time - last_move_time >= move_interval:
        # Randomly choose an action
        action = random.choice(['left', 'right', 'forward', 'backward', 'space', 'wave', 'message'])
        
        if action == 'left':
            pydirectinput.keyDown('left')
            time.sleep(1)
            pydirectinput.keyUp('left')
        elif action == 'right':
            pydirectinput.keyDown('right')
            time.sleep(1)
            pydirectinput.keyUp('right')
        elif action == 'forward':
            pydirectinput.keyDown('up')
            time.sleep(1)
            pydirectinput.keyUp('up')
        elif action == 'backward':
            pydirectinput.keyDown('down')
            time.sleep(1)
            pydirectinput.keyUp('down')
        elif action == 'space':
            pydirectinput.keyDown('space')
            time.sleep(0.1)
            pydirectinput.keyUp('space')
        elif action == 'wave':
            pydirectinput.press('/')
            time.sleep(0.25)
            pydirectinput.write('/e wave')
            time.sleep(0.25)
            pydirectinput.press('enter')
            time.sleep(1)
        elif action == 'message':
            pydirectinput.keyDown('up')
            pydirectinput.keyDown('space')
            time.sleep(0.2)
            pydirectinput.keyUp('up')
            pydirectinput.keyDown('down')
            time.sleep(0.2)
            pydirectinput.keyUp('down')
            pydirectinput.keyUp('space')
        
        last_move_time = current_time
    
    # Display the Canny edge detection
    cv2.imshow('Canny Edge Detection', cv2.resize(edges, (600, 400)))
    #cv2.imshow('Canny Edge Detection', edges)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

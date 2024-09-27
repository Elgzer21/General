import pyautogui
import time
import keyboard

flag = 0
image_clicked = False

while flag == 0:
    if keyboard.is_pressed('q'):
        flag = 1
        break
    
    image_location = pyautogui.locateOnScreen('stickman.png', confidence=0.8)
    
    if image_location is not None and not image_clicked:
        print("I can see it")
        image_center_x = image_location.left + image_location.width / 2
        image_center_y = image_location.top + image_location.height / 2
        pyautogui.click(image_center_x, image_center_y)
        image_clicked = True
        time.sleep(0.5)
    elif image_location is None:
        image_clicked = False
        print("I am unable to see it")
        time.sleep(0.5)

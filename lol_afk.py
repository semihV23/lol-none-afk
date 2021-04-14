from pynput.mouse import Button, Controller
import time
import keyboard

print("Starts after 10 seconds...")
time.sleep(10)

mouse = Controller()
while True:
    mouse.position = (1250, 570)
    mouse.click(Button.right, 1)
    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('quit')
            break  # finishing the loop
    print("mouse.position = (1250, 570)")
    time.sleep(2)
    mouse.position = (840, 600)
    mouse.click(Button.right, 1)
    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('quit')
            break  # finishing the loop
    print("mouse.position = (840, 600)")
    time.sleep(2)
    mouse.position = (1100, 350)
    mouse.click(Button.right, 1)
    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('quit')
            break  # finishing the loop
    print("mouse.position = (1100, 350)")
    time.sleep(2)
print("Shutting down...")
time.sleep(3)
import keyboard
from time import sleep

start = int(input("Please provide the starting number: "))
end = int(input("Please provide the end number: "))
print('''The program will start shortly, tab into discord to start.''')
sleep(4)
for i in range(start,end+1):
    keyboard.write(str(i),0.02)
    keyboard.press("enter")
    sleep(0.01)
    keyboard.release("enter")
    sleep(3)
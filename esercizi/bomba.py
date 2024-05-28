import time
import os
import pyfiglet 
import emoji
  
# http://www.figlet.org/examples.html
'''
countdown = 10
for i in range(0,10):
    print(countdown)
    countdown = countdown - 1
print("BOOM!")
'''

for countdown in range(3, 0,-1):
    time.sleep(1)
    os.system('cls||clear')
    print(countdown)
time.sleep(1)
os.system('cls||clear')
result = pyfiglet.figlet_format("BOOM!", font = "chunky"  ) 
print(result) 
print(emoji.emojize(":red_heart:"))
import pigpio
import time


pi1 = pigpio.pi()
#I decided to use a dictionary to declare color values to make the code more readable 
COLORS = {'BLUE': 13, 'RED': 19, 'GREEN': 26}

#Cycle method that turns brightness on and off for given color
#colors is a pointer in case multiple arguements are passed to create a different color
def cycle(*colors):
    for level in range(1, 256):
        for color in colors:
            pi1.set_PWM_dutycycle(color, level)
        time.sleep(0.00196)
    for level in range(255, 0, -1):
        for color in colors:
            pi1.set_PWM_dutycycle(color, level)
        time.sleep(0.00196)

def main():
    while(1):
        pi1.write(COLORS['BLUE'], 0)
        pi1.write(COLORS['RED'], 0)
        pi1.write(COLORS['GREEN'], 0)
        time.sleep(1)

        cycle(COLORS['RED'])
        cycle(COLORS['GREEN'])
        cycle(COLORS['BLUE'])
        cycle(COLORS['RED'], COLORS['GREEN'], COLORS['BLUE'])

if __name__ == "__main__":
    main()

    

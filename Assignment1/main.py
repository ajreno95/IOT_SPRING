import pigpio
import time

pi1 = pigpio.pi()
COLORS = {'BLUE': 13, 'RED': 19, 'GREEN': 26}

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

    

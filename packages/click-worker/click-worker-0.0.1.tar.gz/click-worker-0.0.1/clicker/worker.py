#! python3
import pyautogui, sys
print('Press Ctrl-C to quit.')
def click(interval):
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
            pyautogui.click(clicks=2, interval=interval)
    except KeyboardInterrupt:
        print('\n')

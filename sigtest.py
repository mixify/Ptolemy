import signal
import time
import sys

original_sigint = signal.getsignal(signal.SIGINT)

def print_info():
    print('sibal')

def ctrlc_handler(signum, frame):
    signal.signal(signal.SIGINT, original_sigint)
    try:
        while(1):
            ans = input('\nPaused learning\npress (i) to see input\npress (y) to quit\npress (r) to resume\n:').lower()
            if(ans.startswith('y')):
                sys.exit()
            elif(ans.startswith('i')):
                print_info()
            elif(ans.startswith('r')):
                break

    except KeyboardInterrupt:
        print('I\'m quiting really')
        sys.exit()

signal.signal(signal.SIGINT, ctrlc_handler)

while True:
    time.sleep(1)
    print("a")

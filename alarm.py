import time
from playsound3 import playsound


CLEAR = "\033[H\033[J"
CLEAR_AND_RETURN = "\033[H\033[J\r"


def alarm(seconds):
    time_elapsed = 0
    
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        
        time_left = seconds - time_elapsed
        minutes, seconds_left = divmod(time_left, 60)
        print(f"{CLEAR_AND_RETURN}Time left: {minutes:02d}:{seconds_left:02d}", end="\r")
        
    print(f"{CLEAR_AND_RETURN}Time's up!            ")
    playsound("alarm_sound.mp3") 
    
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
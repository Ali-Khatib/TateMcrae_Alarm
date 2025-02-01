import datetime
import time
import pygame
import os


def alarm(alarm_time):
    print(f"Alarm time set for {alarm_time}\n")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\rCurrent Time: {current_time}", end="", flush=True)  # Overwrites the same line

        if current_time == alarm_time:
            print("\nWAKE UP! 🚨")
            play_sound()
            break

        time.sleep(1)


def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("tatemcraee.mp3")
    pygame.mixer.music.play()
    time.sleep(157)  
    pygame.mixer.music.stop()


# Get user input for alarm
alarm_time = input("Please enter alarm time (HH:MM:SS): ")
alarm(alarm_time)

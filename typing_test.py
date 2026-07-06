import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Welcome to the Typing Test!")
    stdscr.addstr(1, 0, "Press any key to start...")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target_text, current_text, wpm=0):
    stdscr.addstr(0, 0, target_text)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current_text):
        current_char = target_text[i]
        color = curses.color_pair(1)
        if char != current_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)

def load_text_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return random.choice(lines).strip()

def typing_test(stdscr):
    target_text = load_text_from_file("texts.txt")
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        elapsed_time = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (elapsed_time / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:  # ESC key to exit
            break
        
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        typing_test(stdscr)
        stdscr.addstr(3, 0, "Test completed! Press any key to restart or ESC to exit.")
        stdscr.refresh()
        key = stdscr.getkey()
        if ord(key) == 27:  # ESC key to exit
            break


wrapper(main)

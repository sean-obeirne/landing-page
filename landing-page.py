#!/usr/bin/env python3

#
# Author: Sean O'Beirne
# Date: 7-29-2024
# File: landing-page.py
# Usage: python3 landing-page
#

#
# Boilerplate for curses application
#


import curses
from curses.textpad import rectangle

import subprocess, os, sys

import time

import logging

stdscr = curses.initscr()


curses.start_color()
curses.use_default_colors()
# for i in range(0, curses.COLORS):
    # curses.init_pair(i, i, -1);


# Define colors
def hex_to_rgb(hexstring):
    r = int(int(hexstring[0:2], 16) * 1000 / 255)
    g = int(int(hexstring[2:4], 16) * 1000 / 255)
    b = int(int(hexstring[4:6], 16) * 1000 / 255)
    return (r, g, b)

if curses.can_change_color():
    black_rgb = (0, 0, 0)
    white_rgb = hex_to_rgb("c0caf5")
    red_rgb = hex_to_rgb("db4b4b")
    purple_rgb= hex_to_rgb("9d7cd8")
    green_rgb = hex_to_rgb("9ece6a")
    blue_rgb = hex_to_rgb("24283b")

    curses.init_color(curses.COLOR_BLACK, *black_rgb)
    curses.init_color(curses.COLOR_WHITE, *white_rgb)
    curses.init_color(curses.COLOR_RED, *red_rgb)
    curses.init_color(curses.COLOR_MAGENTA, *purple_rgb)
    curses.init_color(curses.COLOR_GREEN, *green_rgb)
    curses.init_color(curses.COLOR_BLUE, *blue_rgb)
curses.init_pair(1, curses.COLOR_RED, -1)
curses.init_pair(2, curses.COLOR_WHITE, -1)
curses.init_pair(3, curses.COLOR_MAGENTA, -1)
curses.init_pair(4, curses.COLOR_GREEN, -1)
curses.init_pair(5, curses.COLOR_WHITE, -1)
curses.init_pair(6, curses.COLOR_RED, -1)
RED_ON_BG = curses.color_pair(1)
WHITE_ON_BG = curses.color_pair(2)
PURPLE_ON_BG = curses.color_pair(3)
GREEN_ON_BG = curses.color_pair(4)

curses.use_default_colors()

    
HEADER = [
r"""       ____   U _____ u    _      _   _   _   ____         _   _      _       ____     ____   __   __      ____      _         _        ____ U _____ u """,
r"""      / __"| u\| ___"|/U  /"\  u | \ |"| |"| / __"| u     |'| |'| U  /"\  u U|  _"\ uU|  _"\ u\ \ / /    U|  _"\ u  |"|    U  /"\  u U /"___|\| ___"|/ """,
r"""     <\___ \/  |  _|"   \/ _ \/ <|  \| |>|_|<\___ \/     /| |_| |\ \/ _ \/  \| |_) |/\| |_) |/ \ V /     \| |_) |/U | | u   \/ _ \/  \| | u   |  _|"   """,
r"""      u___) |  | |___   / ___ \ U| |\  |u    u___) |     U|  _  |u / ___ \   |  __/   |  __/  U_|"|_u     |  __/   \| |/__  / ___ \   | |/__  | |___   """,
r"""      |____/>> |_____| /_/   \_\ |_| \_|     |____/>>     |_| |_| /_/   \_\  |_|      |_|       |_|       |_|       |_____|/_/   \_\   \____| |_____|  """,
r"""       )(  (__)<<   >>  \\    >> ||   \\,-.   )(  (__)    //   \\  \\    >>  ||>>_    ||>>_ .-,//|(_      ||>>_     //  \\  \\    >>  _// \\  <<   >>  """,
r"""      (__)    (__) (__)(__)  (__)(_")  (_/   (__)        (_") ("_)(__)  (__)(__)__)  (__)__) \_) (__)    (__)__)   (_")("_)(__)  (__)(__)(__)(__) (__) """,
        ]

HEADER_COLOR_MAP= """\
0000000333300010333330100003000000300030003000333300000000030003000000300000003333000003333000330003300000033330000003000000000300000000333301033333010\
0000003033130113033313110031300103030313031303033330100000313031301003130010130031301130031301303030300001300313010031300001003130010103133331303331310\
0000013333031003003310001303031013003303133313333031000001303330310130303100130333031130333031030303000003303330311030301000130303100330301000300331000\
0000001333303003033330003033303013033003100001333303000001300300310303330300030033300030033300113131100000300333000130313300303330300030333300303333000\
0000003333331103333333033300033303330333000003333331100000333033303330003330033300000033300000003330000000333000000033333333330003330003333330333333300\
0000000110011111100011001100001101100011111000110011110000110001100110000110011111000011111111111111000000111110000011001100110000110011101100110001100\
0000001111000011110111111110011111111001110001111000000001111011111111001111111111100111111101110111100001111111000111111111111001111111111111111011110\
"""


def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Turn off cursor blinking
    curses.curs_set(0)

    # Get screen height and width
    height, width = stdscr.getmaxyx()

    i = 0
    x = 0
    y = 0
    for line in HEADER:
        for char in line:
            this = int(HEADER_COLOR_MAP[i])
            stdscr.addch(y, x, char, curses.color_pair(this))
            i += 1
            x += 1
        y += 1
        x = 0

    # Create a window for input
    stdscr.bkgd(curses.color_pair(2))

    # Main loop
    while True:
        # Display a message in the middle of the screen
        # msg = "Welcome to your custom Neovim landing page!"
        # stdscr.addstr(height // 2, (width - len(msg)) // 2, msg, curses.color_pair(1))

        # rectangle(stdscr, 1, 1, height - 1, width - 2)
        stdscr.refresh()

        # Get user input
        curses.echo()
        curses.noecho()


if __name__ == "__main__":
    curses.wrapper(main)


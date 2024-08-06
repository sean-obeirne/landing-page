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

import random

import subprocess, os, sys

import time

import logging

# Configure logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG, filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

stdscr = curses.initscr()


curses.start_color()
curses.use_default_colors()

# Define colors
def hex_to_rgb(hexstring):
    r = int(int(hexstring[0:2], 16) * 1000 / 255)
    g = int(int(hexstring[2:4], 16) * 1000 / 255)
    b = int(int(hexstring[4:6], 16) * 1000 / 255)
    return (r, g, b)

green = hex_to_rgb("29ad2b")
brown = hex_to_rgb("896018")
white = hex_to_rgb("ffffff")

tn_bg = hex_to_rgb("24283b")
tn_bg_dark = hex_to_rgb("1f2335")
tn_bg_highlight = hex_to_rgb("292e42")
tn_blue = hex_to_rgb("7aa2f7")
tn_blue0 = hex_to_rgb("3d59a1")
tn_blue1 = hex_to_rgb("2ac3de")
tn_blue2 = hex_to_rgb("0db9d7")
tn_blue5 = hex_to_rgb("89ddff")
tn_blue6 = hex_to_rgb("b4f9f8")
tn_blue7 = hex_to_rgb("394b70")
tn_comment = hex_to_rgb("565f89")
tn_cyan = hex_to_rgb("7dcfff")
tn_dark3 = hex_to_rgb("545c7e")
tn_dark5 = hex_to_rgb("737aa2")
tn_fg = hex_to_rgb("c0caf5")
tn_fg_dark = hex_to_rgb("a9b1d6")
tn_fg_gutter = hex_to_rgb("3b4261")
tn_green = hex_to_rgb("9ece6a")
tn_green1 = hex_to_rgb("73daca")
tn_green2 = hex_to_rgb("41a6b5")
tn_magenta = hex_to_rgb("bb9af7")
tn_magenta2 = hex_to_rgb("ff007c")
tn_orange = hex_to_rgb("ff9e64")
tn_purple = hex_to_rgb("9d7cd8")
tn_red = hex_to_rgb("f7768e")
tn_red1 = hex_to_rgb("db4b4b")
tn_teal = hex_to_rgb("1abc9c")
tn_terminal_black = hex_to_rgb("414868")
tn_yellow = hex_to_rgb("e0af68")
tn_git_add = hex_to_rgb("449dab")
tn_git_change = hex_to_rgb("6183bb")
tn_git_delete = hex_to_rgb("914c54")



COLOR_BLACK = 0
COLOR_RED = 1
COLOR_GREEN = 2
COLOR_ORANGE = 3
COLOR_BLUE = 4
COLOR_MAGENTA = 5
COLOR_CYAN = 6
COLOR_WHITE = 7
COLOR_DARK_GREY = 8
COLOR_LIGHT_RED = 9
COLOR_LIGHT_GREEN = 10
COLOR_YELLOW = 11
COLOR_LIGHT_BLUE = 12
COLOR_PURPLE = 13
COLOR_BROWN = 14
COLOR_DIM_WHITE = 15

# RGB values (0-1000 scale)
color_definitions = {
    COLOR_BLACK: tn_terminal_black,
    COLOR_RED: tn_red1,
    COLOR_GREEN: green,
    COLOR_ORANGE: tn_orange,
    COLOR_BLUE: tn_blue0,
    COLOR_MAGENTA: tn_magenta2,
    COLOR_CYAN: tn_cyan,
    COLOR_WHITE: white,
    COLOR_DARK_GREY: tn_dark5,
    COLOR_LIGHT_RED: tn_red,
    COLOR_LIGHT_GREEN: tn_green,
    COLOR_YELLOW: tn_yellow,
    COLOR_LIGHT_BLUE: tn_blue,
    COLOR_PURPLE: tn_purple,
    COLOR_BROWN: brown,
    COLOR_DIM_WHITE: tn_fg,
}



# Initialize 16 colors
def init_16_colors():
    curses.start_color()
    
    if curses.can_change_color():
        for color, rgb in color_definitions.items():
            curses.init_color(color, *rgb)
    
    # Define color pairs using custom color numbers
    curses.init_pair(1, COLOR_BLACK, -1)
    curses.init_pair(2, COLOR_RED, -1)
    curses.init_pair(3, COLOR_GREEN, -1)
    curses.init_pair(4, COLOR_ORANGE, -1)
    curses.init_pair(5, COLOR_BLUE, -1)
    curses.init_pair(6, COLOR_MAGENTA, -1)
    curses.init_pair(7, COLOR_CYAN, -1)
    curses.init_pair(8, COLOR_WHITE, -1)
    curses.init_pair(9, COLOR_DARK_GREY, -1)
    curses.init_pair(10, COLOR_LIGHT_RED, -1)
    curses.init_pair(11, COLOR_LIGHT_GREEN, -1)
    curses.init_pair(12, COLOR_YELLOW, -1)
    curses.init_pair(13, COLOR_LIGHT_BLUE, -1)
    curses.init_pair(14, COLOR_PURPLE, -1)
    curses.init_pair(15, COLOR_BROWN, -1)
    curses.init_pair(16, COLOR_DIM_WHITE, -1)

init_16_colors()

BLACK = curses.color_pair(1)
RED = curses.color_pair(2)
GREEN = curses.color_pair(3)
ORANGE = curses.color_pair(4)
BLUE = curses.color_pair(5)
MAGENTA = curses.color_pair(6)
CYAN = curses.color_pair(7)
WHITE = curses.color_pair(8)
DARK_GREY = curses.color_pair(9)
LIGHT_RED = curses.color_pair(10)
LIGHT_GREEN = curses.color_pair(11)
YELLOW = curses.color_pair(12)
LIGHT_BLUE = curses.color_pair(13)
PURPLE = curses.color_pair(14)
BROWN = curses.color_pair(15)
DIM_WHITE = curses.color_pair(16)


    
HEADER = [
r"""       ____   U _____ u    _      _   _   _   ____         _   _      _       ____     ____   __   __      ____      _         _        ____ U _____ u """,
r"""      / __"| u\| ___"|/U  /"\  u | \ |"| |"| / __"| u     |'| |'| U  /"\  u U|  _"\ uU|  _"\ u\ \ / /    U|  _"\ u  |"|    U  /"\  u U /"___|\| ___"|/ """,
r"""     <\___ \/  |  _|"   \/ _ \/ <|  \| |>|_|<\___ \/     /| |_| |\ \/ _ \/  \| |_) |/\| |_) |/ \ V /     \| |_) |/U | | u   \/ _ \/  \| | u   |  _|"   """,
r"""      u___) |  | |___   / ___ \ U| |\  |u    u___) |     U|  _  |u / ___ \   |  __/   |  __/  U_|"|_u     |  __/   \| |/__  / ___ \   | |/__  | |___   """,
r"""      |____/>> |_____| /_/   \_\ |_| \_|     |____/>>     |_| |_| /_/   \_\  |_|      |_|       |_|       |_|       |_____|/_/   \_\   \____| |_____|  """,
r"""       )(  (__)<<   >>  \\    >> ||   \\,-.   )(  (__)    //   \\  \\    >>  ||>>_    ||>>_ .-,//|(_      ||>>_     //  \\  \\    >>  _// \\  <<   >>  """,
r"""      (__)    (__) (__)(__)  (__)(_")  (_/   (__)        (_") ("_)(__)  (__)(__)__)  (__)__) \_) (__)    (__)__)   (_")("_)(__)  (__)(__)(__)(__) (__) """,
        ]

HEADER_COLOR_MAP = """\
0000000eeee00050eeeee050000e000000e000e000e000eeee000000000e000e000000e0000000eeee00000eeee000ee000ee000000eeee000000e000000000e00000000eeee050eeeee050\
000000e0ee5e055e0eee5e5500e5e0050e0e0e5e0e5e0e0eeee0500000e5e0e5e0500e5e00505e00e5e055e00e5e05e0e0e0e00005e00e5e0500e5e0000500e5e005050e5eeee5e0eee5e50\
000005eeee0e500e00ee50005e0e0e505e00ee0e5eee5eeee0e5000005e0eee0e505e0e0e5005e0eee0e55e0eee0e50e0e0e000005e0eee0e550e0e050005e0e0e5005e0e05000e00ee5000\
0000005eeee0e00e0eeee000e0eee0e05e0ee00e500005eeee0e000005e00e00e50e0eee0e000e00eee000e00eee0055e5e5500000e00eee0005e0e5ee00e0eee0e000e0e5ee00e0eeee000\
000000eeeeee550eeeeeee0eee000eee0eee0eee00000eeeeee5500000eee0eee0eee000eee00eee000000eee0000000eee0000000eee0000000eeeeeeeeee000eee000eeeeee0eeeeeee00\
0000000550055555500055005500005505500055555000550055550000550005500550000550055555000055555555555555000000555550000055005500550000550055505500550005500\
0000005555000055550555555550055555555005550005555000000005555055555555005555555555500555555505550555500005555555000555555555555005555555555555555055550\
"""

FOOTER = [
r"""                                                                              ; ; ;                                                          """,
r"""                                                                            ;       ;  ;     ;;    ;                                         """,
r"""                                                                         ;                ;         ;  ;                                     """,
r"""                                                                        ;               ;                                                    """,
r"""                                                                                       ;                ;;                                   """,
r"""                                                                       ;          ;            ;              ;                              """,
r"""                                                                       ;            ';,        ;               ;                             """,
r"""                                                                       ;              'b      *                                              """,
r"""                                                                        ;              '$    ;;                ;;                            """,
r"""                                                                       ;    ;           $:   ;:               ;                              """,
r"""                                                                     ;;      ;  ;;      *;  @):        ;   ; ;                               """,
r"""                                                                                  ;     :@,@):   ,;**:'   ;                                  """,
r"""                                                                      ;      ;,         :@@*: ;;**'      ;   ;                               """,
r"""                                                                                ';o;    ;:(@';@*"'  ;                                        """,
r"""                                                                       ;  ;       'bq,;;:,@@*'   ,*      ;  ;                                """,
r"""                                                                                  ,p$q8,:@)'  ;p*'      ;                                    """,
r"""                         _                                                 ;     '  ; '@@Pp@@*'    ;  ;                                      """,
r"""                       _(_)_                          wWWWw   _             ;  ; ;;    Y7'.'                           wWWWw     _           """,
r"""           @@@@       (_)@(_)   vVVVv     _     @@@@  (___) _(_)      @@@             :@):.   vVVVv       _     @@@@   (___)   _(_)      @@@ """,
r"""          @@()@@ wWWWw  (_)\    (___)   _(_)_  @@()@@   Y  (_)@(_)   @@.@@     @@@   .:@:'.   (___)     _(_)_  @@()@@    Y    (_)@(_)   @@.@@""",
r"""           @@@@  (___)     `|/    Y    (_)@(_)  @@@@   \|/   (_)\     @@@     @@-@@.::(@:.      Y      (_)@(_)  @@@@    \|/     (_)\     @@@ """,
r"""            /      Y       \|    \|/    /(_)    \|      |/      |      | /     @@@.::)@@::     \|/      /(_)    \|       |/        |      | /""",
r"""         \ |     \ |/       | / \ | /  \|/       |/    \|      \|/    \|/       |\::(@@@::.   \ | /    \|/       |/     \|        \|/    \|/ """,
r"""         \\|/    \\|//     \|// \\|/ / \|//     \|//  \\|//    \|//   \/\//    \|.:)@@@@:::   \\|/ /   \|//     \|//   \\|//      \|//   \/\/""",
# r"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""\
        ]

FOOTER_COLOR_MAP = """\
000000000000000000000000000000000000000000000000000000000000000000000000000000303030000000000000000000000000000000000000000000000000000000000\
000000000000000000000000000000000000000000000000000000000000000000000000000030000000300300000330000300000000000000000000000000000000000000000\
000000000000000000000000000000000000000000000000000000000000000000000000030000000000000000300000000030030000000000000000000000000000000000000\
000000000000000000000000000000000000000000000000000000000000000000000000300000000000000030000000000000000000000000000000000000000000000000000\
000000000000000000000000000000000000000000000000000000000000000000000000000000000000000300000000000000003300000000000000000000000000000000000\
0000000000000000000000000000000000000000000000000000000000000000000000030000000000f000000000000f000000000000003000000000000000000000000000000\
000000000000000000000000000000000000000000000000000000000000000000000003000000000000fff00000000f000000000000000300000000000000000000000000000\
00000000000000000000000000000000000000000000000000000000000000000000000300000000000000ff000000f0000000000000000000000000000000000000000000000\
000000000000000000000000000000000000000000000000000000000000000000000000300000000000000ff0000ff0000000000000000330000000000000000000000000000\
0000000000000000000000000000000000000000000000000000000000000000000000030000300000000000ff000ff0000000000000003000000000000000000000000000000\
0000000000000000000000000000000000000000000000000000000000000000000003300000030033000000ff00fff00000000f0003030000000000000000000000000000000\
0000000000000000000000000000000000000000000000000000000000000000000000000000000000300000ffffff000ffffff00030000000000000000000000000000000000\
00000000000000000000000000000000000000000000000000000000000000000000003000000ff000000000fffff0fffff000000300030000000000000000000000000000000\
00000000000000000000000000000000000000000000000000000000000000000000000000000000ffff0000ffffffffff00f0000000000000000000000000000000000000000\
0000000000000000000000000000000000000000000000000000000000000000000000030030000000ffffffffffff000ff000000300300000000000000000000000000000000\
0000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffff00ffff0000003000000000000000000000000000000000000\
0000000000000000000000000e0000000000000000000000000000000000000000000000000300000f0030fffffffff0000300300000000000000000000000000000000000000\
00000000000000000000000eeeee00000000000000000000000000fcccf0008000000000000030030330000fffff000000000000000000000000000eeeee00000200000000000\
00000000000cccc0000000eeeceee0002222200000200000cccc003333308888000000eee0000000000000fffff000555550000000c000005555000c333c0002222000000ccc0\
0000000000cc22cc0fffff00eee300003ccc30002222200ccffcc0003008882888000eefee00000555000ffffff0003333300000ccccc0055cc55000030000222c222000ccfcc\
00000000000cccc00ccccc00000333000030000222c22200cccc000333000888300000eee0000055855fffffff0000003000000ccc3ccc005555000033300000222300000ccc0\
0000000000003000000300000003300003330000322200003300000033000000300000030300000555ffffffff000003330000003ccc000033000000033000000003000000303\
0000000003030000030330000000303030303003330000000330000330000003330000333000000033fffffffff00030303000033300000003300000330000000033300003330\
000000000333300003333300000333303333030333300000333300333330000333300033333000033ffffffffff00033330300033330000033330003333300000033330003333\
"""

TERMINAL_PREFIX = "gnome-terminal --maximize --working-directory="
actions = {}

class Button:

    def __init__(self, y, x, key, name, path="", command="", sctype="gt"):
        self.y = y
        self.x = x
        self.key = key
        self.name = name
        self.path = path
        self.sctype = sctype
        if sctype == "gt":
            self.command = f"{TERMINAL_PREFIX}{path}"
            if command == "nvim":
                self.command += f" -- {command} {path}"
        elif sctype == "app":
            self.command = command
        elif sctype == "internal":
            self.command = command
        # log.info(f"Command created: {self.command}")
        actions[self.key] = self.command

    def draw(self):
        x = self.x
        swap_exists = self.swap_exists()
        # dir_open = self.dir_open()
        is_open = swap_exists #or dir_open
        is_open = False
        is_open = is_open and self.name != 'Terminal'

        # prefix
        if is_open:
            stdscr.addch(self.y, x-3, '▪', DARK_GREY)
        else:
            stdscr.addch(self.y, x-3, '▪', WHITE)
        stdscr.addch(self.y, x, '[', CYAN)
        x += 1

        # orange/black number for open files
        if is_open:
            stdscr.addch(self.y, x, self.key, BLACK)
        else:
            stdscr.addch(self.y, x, self.key, ORANGE)
        x += 1

        # suffix
        stdscr.addch(self.y, x, ']', CYAN)
        x += 1
        if is_open:
            stdscr.addstr(self.y, x, f" {self.name}", DARK_GREY)
        else:
            stdscr.addstr(self.y, x, f" {self.name}", WHITE)

    def build_command(self):
        return self.command + " " + self.path

    def swap_exists(self):
        swaps = os.listdir("/home/sean/.config/nvim/swap") + os.listdir("/home/sean/.local/state/nvim/swap")
        for sf in swaps:
            if sf.replace("%", "/")[0:-4] == self.path:
                return True
        return False

    def dir_open(self):
        if self.command[0:14] == "gnome-terminal":
            fish_pids = subprocess.check_output(['pgrep', 'fish'], text=True).split('\n')
            log.info(fish_pids)
            for pid in fish_pids:
                cmd = f"lsof -p {pid} | head -n 2 | tail -n 1"
                out = subprocess.check_output(cmd, shell=True, text=True).split()
                log.info(out)
                if out[0] == 'fish':
                    return f"{out[-1]}/" == self.path
        return False




def make_title():
    pass

def draw_ascii(x, y, image, map, bold_color=-1):
    i = 0
    cx = x
    cy = y
    for line in image:
        for char in line:
            this = int(map[i], 16)
            stdscr.addch(cy, cx, char, curses.color_pair(this) | (curses.A_BOLD if this == bold_color else 0))
            i += 1
            cx += 1
        cy += 1
        cx = x


def randomize_colors():
    global FOOTER_COLOR_MAP
    mutable = [ '1', '2', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']
    for src_color in mutable:
        new_color = random.choice(mutable)
        while src_color == new_color:
            new_color = random.choice(mutable)
        # log.info(f"Changing {src_color} to {new_color}...")
        # mutable.remove(new_color)
        FOOTER_COLOR_MAP = FOOTER_COLOR_MAP.replace(src_color, new_color)
            


def draw():
    # Clear screen
    stdscr.clear()

    # Turn off cursor blinking and echoing
    curses.curs_set(0)
    curses.noecho()
    curses.set_escdelay(1)

    # Get screen height and width
    height, width = stdscr.getmaxyx()

    draw_ascii(0, 1, HEADER, HEADER_COLOR_MAP, 14)
    draw_ascii(width - 142, 14, FOOTER, FOOTER_COLOR_MAP)

    stdscr.addstr(11, 6, "NeoVim Shortcuts:", WHITE)
    stdscr.addstr(11, 6 + 40, "Directory Shortcuts:", WHITE)
    stdscr.addstr(25, 6, "Application Shortcuts:", WHITE)


def main(stdscr):
    draw()

    height, width = stdscr.getmaxyx()
    x, y = 0, 0

    buttons = []


    buttons.append(Button(height-2, 8, 'q', 'Quit', command='exit'))
    buttons.append(Button(height-3, 8, 'e', 'Edit', command='nvim', path='/home/sean/code/in-progress/landing-page/landing-page.py'))
    buttons.append(Button(height-4, 8, 'k', 'Kill Swaps', command='/home/sean/bin/rmswp', sctype="app"))
    buttons.append(Button(height-5, 8, '`', 'Settings', command="gnome-control-center", sctype="app"))
    y = 14
    x = 14
    buttons.append(Button(y, x, 't', 'TFG Notes', command="nvim", path="/home/sean/code/tfg/notes"))
    y += 2
    buttons.append(Button(y, x, 'v', 'NeoVim Config', command="nvim", path="/home/sean/.config/nvim/init.lua"))
    y += 2
    buttons.append(Button(y, x, 'f', 'Fish Config', command="nvim", path="/home/sean/.config/fish/config.fish"))
    y += 2
    buttons.append(Button(y, x, 'c', 'Cheat Sheets', command="nvim", path="/home/sean/.findables/cheatsheets"))

    y = 14
    x = 54
    # buttons.append(Button(y, x, 't', 'Tech for Good', path="/home/sean/code/tfg/"))
    # y += 2
    buttons.append(Button(y, x, 'm', 'Mission Uplink', path="/home/sean/code/tfg/Mission-Uplink/"))
    y += 2
    buttons.append(Button(y, x, 'b', 'Uplink Browser', path="/home/sean/code/tfg/dev-env/"))
    y += 2
    buttons.append(Button(y, x, 'j', 'WotR', path="/home/sean/code/godot/Wizards-of-the-Rift/"))
    y += 2
    buttons.append(Button(y, x, 'n', 'NeoVim Plugins Folder', path="/home/sean/.config/nvim/lua/plugins/"))
    y += 2
    buttons.append(Button(y, x, 'x', 'Findables', path="/home/sean/.findables"))
    y += 2

    y = 25
    x = 9
    y += 2
    buttons.append(Button(y, x, 'g', 'Terminal', path="/home/sean/"))
    y += 2
    x += 4
    buttons.append(Button(y, x, 'w', 'Firefox', command="firefox", sctype="app"))
    x += 20
    y -= 2
    buttons.append(Button(y, x, 'u', 'YT Music', command="firefox --new-window music.youtube.com", sctype="app"))
    y += 2
    x += 4
    buttons.append(Button(y, x, 's', 'Spotify', command="spotify", sctype="app"))
    x += 20
    y -= 2
    buttons.append(Button(y, x, 'r', 'RuneScape', command="/home/sean/applications/RuneLite.AppImage --scale 2 > /tmp/runelite.log", sctype="app"))
    y += 2
    x += 4
    buttons.append(Button(y, x, 'y', 'YouTube', command="firefox --new-window youtube.com", sctype="app"))

    y = 14
    x = 140
    buttons.append(Button(y, x, 'R', 'Randomize', command="randomize_colors()", sctype="internal"))


    valid_keys = {
            'm',
            'b',
            't',
            'j',
            'c',
            'f',
            'n',
            'x',
            'v',
            'u',
            's',
            'w',
            'g',
            'm',
            'r',
            'y',
            'R',
            'k',
            'e',
            'q',
            '`',
            '\x1b'
            }

    # Main loop
    while True:
        # get and handle input
        for button in buttons:
            button.draw()
        key = stdscr.getkey()
        if key == 'q' or key == '\x1b':
            log.info("Quitting...")
            exit(0)
        if key == ' ':
            stdscr.refresh()
            continue
        if key in valid_keys:
            log.info(f"'{key}' action: {actions[key].split()}")
            if key == key.lower():
                if key == 'r':
                    os.system("/home/sean/applications/RuneLite.AppImage --scale 2 > /tmp/runelite.log")
                else:
                    subprocess.run(actions[key].split())
            else:
                exec(actions[key])
            draw()
            stdscr.refresh()
        else:
            log.error(f"Invalid key {key}")


        # update the screen
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)


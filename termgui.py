# Copyright (c) 2019 Xiaoyong Guo

import curses


class TermGui(object):
  def __init__(self, stdscr):
    self._stdscr = stdscr
    self._stdscr.clear()
    self._stdscr.refresh()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    self._info = {
        'freq': 400,
        'db': 8900,
        'note': 'C4',
        'note_num': 88,
    }

  def draw(self):
    k = None
    while (k != ord('q')):
        self._stdscr.clear()
        height, width = self._stdscr.getmaxyx()

        # Declaration of strings
        title = "ETuner"
        subtitle = "Written by Xiaoyong Guo"
        self._stdscr.addstr(0, 0, title , curses.color_pair(1))
        self._stdscr.addstr(0, len(title)+1, subtitle , curses.color_pair(2))
        info = "Note: {note}/{note_num} Freq: {freq:.2f} Hz, DB: {db}".format(**self._info)
        self._stdscr.addstr(1, 0, info, curses.color_pair(3))
        self._stdscr.refresh()
        k = self._stdscr.getch()


def draw_gui(stdscr):
  term_gui = TermGui(stdscr)
  term_gui.draw()


def main():
    curses.wrapper(draw_gui)

if __name__ == "__main__":
    main()

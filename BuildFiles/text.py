#!/usr/bin/python

import smbus
import time
import curses
 
bus = smbus.SMBus(1)

stdscr = curses.initscr()

curses.noecho()
curses.cbreak()

aout = 0

stdscr.addstr(10, 0, "Brightness")
stdscr.addstr(12, 0, "Temperature")
stdscr.addstr(14, 0, "AOUT->AIN2")
stdscr.addstr(16, 0, "Resistor")

stdscr.nodelay(1)

while True:
 
   for a in range(0,4):
      aout = aout + 1
      bus.write_byte_data(0x48,0x40 | ((a+1) & 0x03), aout)
      v = bus.read_byte(0x48) #read from YL-40 board
      hashes = v / 4
      spaces = 64 - hashes
      stdscr.addstr(10+a*2, 12, str(v) + ' ') #print numeric value
      stdscr.addstr(10+a*2, 16, '#' * hashes + ' ' * spaces ) #print visual representation

   stdscr.refresh() #this is to display the changes made in the screen output
   time.sleep(0.04) #delay until next loop through

   c = stdscr.getch()

   if c != curses.ERR: #if error then exit
      break

curses.nocbreak()
curses.echo()

curses.endwin()

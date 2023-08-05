#!/usr/bin/python

#import sys
#from msvcrt import getch
import msvcrt
import pybaccarat.playingcards
import pybaccarat.baccarat
import pybaccarat.baccaratsystems

print("play a normal single game of baccarat")
shoe = pybaccarat.playingcards.Shoe(8)
player = pybaccarat.baccarat.Hand()
banker = pybaccarat.baccarat.Hand()
systemplay = pybaccarat.baccaratsystems.interactive()
game = pybaccarat.baccarat.Game(shoe, player, banker, systemplay)
kbd = 13
while kbd == 13: #anything but an enter key exits
    game.play(interactive=False)
    '''
    if sys.version_info[0] > 2:
        kbd = input("")
    else:
        kbd = raw_input("")
    '''
    kbd = 27#ord(msvcrt.getch())


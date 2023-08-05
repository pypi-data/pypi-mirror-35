#!/usr/bin/python

'''!
@package pybaccarat.baccaratsystems
This module is collection of classes used with 
systems for playing the game <B>Baccarat</B>.
@author <A email="fulkgl@gmail.com">fulkgl@gmail.com</A>
@version 0.13
'''

from pybaccarat.baccaratsystems import BaccSys

#-----------------------------------
import sys
from msvcrt import getch
def get_keystroke():
    keystroke = ord(getch())
    if 3 <= sys.version_info[0]:
        keystroke1 = ord(getch())
        keystroke += 256*keystroke1
    return keystroke
#-----------------------------------

#class BaccSys(object):
#  Hook methods (we hook these methods to get called from Game)
#    def __init__(self, sys_name=""):
#    def new_shoe(self, burn_card, boards=None):
#    def hand_pre(self, hand_num):
#    def hand_post(self, win_diff, player_hand, banker_hand):
#    def end_shoe(self):
#  action methods (workers we call)
#    self.play(side, size=1)
#    self.quit_this_shoe()
#    self.opposite_side(side)
#  ?
#    def set_tie_object(self, tie_track):
#    def set_bpt_object(self, bpt):
#    def result_won(self, amount):
#    def result_lost(self, amount):
#    def print_WLseq(self):
#  fields
#    self.hand_number   integer this hand number
#    self.name          string name of this bacc system
#    self.won           integer number won  in this shoe
#    self.lost          integer "      lost "  "    "
#    self.tied          integer "      tied "  "    "
#    self.money         float money in this shoe
#    self.WLseq         array of integers for WL sequencing
#    self.play_on       string None or "B" or "P"
#    self.play_size     integer bet size
#    self.quit_shoe     boolean
#    self.last_WLT      String last result was this
#  internals?
#    self.scoreboards


class silver_bullet(BaccSys):
    def __init__(self, sys_name=""):
        parent_ret = super(silver_bullet,self).__init__("silver_bullet")
    def hand_pre(self, hand_num):
        parent_ret = super(silver_bullet,self).hand_pre(hand_num)
        if self.quit_shoe:
            return parent_ret
        '''
        if self.hand_number == 1:
            return "{no play first hand}"
        if self.hand_number == 2:
            b0_array = self.scoreboards[0].get_array()
            #self.play_on = side
            #self.play_size = 1
            #return p
        return "{none}"
        '''
        my_size = 1
        keystroke = get_keystroke()
        if chr(keystroke) in ("1","2","3","4","5"):
                my_size = keystroke-ord("0")
                keystroke = get_keystroke()
        if chr(keystroke & 223) in ("P","B"): #uckey uppercase
                return self.play(chr(keystroke & 223),my_size)
        elif keystroke==3:      #ctrl-C
                raise ValueError("Ctrl-C request to end game")
        elif keystroke==27:     #ESC
                self.quit_this_shoe()
        return " "
    #def end_shoe(self):
    #    return "Sys(%s) %d-%d-%d=%+.2f, %s" % (self.name,self.won, \
    #        self.lost,self.tied,self.money,self.print_WLseq())


"""
class interactive(BaccSys):
    '''!
    Play Baccarat with interactive selection of hand plays.
    Press the letter P to play player.
    Press the letter B to play banker.
    Press the enter key to make no play on a hand.
    Press the ESC key to skip to the end of the shoe.
    Press the Ctrl-C for emergency fast exit.
    Press numbers 1 or 2 or 3 or 4 or 5 before the P or B to increase size.
    For instance, press 3 then P will play 3 units on player.
    If no number is pressed it's assumed to be 1.
    '''
    def __init__(self, sys_name=""):
        # first, call parent
        parent_ret = super(interactive,self).__init__("interactive")
    def hand_pre(self, hand_num):
        '''
        We are given a chance to choose a play, prior to dealing cards.
        @param hand_num int hand number
        @return String description of play, such as "P" or "B".
            The returned string is for display purposes only.
            The tracking of the bet made is in the inheritted object
            play_on and play_size.
        '''
        # first, call parent
        parent_ret = super(interactive,self).hand_pre(hand_num)
        if not self.quit_shoe:
            my_size = 1
            keystroke = get_keystroke()
            if chr(keystroke) in ("1","2","3","4","5"):
                my_size = keystroke-ord("0")
                keystroke = get_keystroke()
            if chr(keystroke & 223) in ("P","B"): #uckey uppercase
                return self.play(chr(keystroke & 223),my_size)
            elif keystroke==3:      #ctrl-C
                raise ValueError("Ctrl-C request to end game")
            elif keystroke==27:     #ESC
                self.quit_this_shoe()
        return " "
    def end_shoe(self):
        return "Sys(%s) %d-%d-%d=%+.2f, %s" % (self.name,self.won, \
            self.lost,self.tied,self.money,self.print_WLseq())
"""


"""
class ValSys(BaccSys):
    def hand_post(self, win_diff, p_hand, b_hand):
        parent_ret = super(ValSys,self).hand_post(win_diff,p_hand,b_hand)
        return " %s" % self.last_WLT
    def hand_pre(self, hand_num):
        '''!
        ValSystem rules:
        1. if board 2 last entry is in row 1, play chop else play same
        2. overrides rule 1. If 4+ in a row on board 0, play same
        '''
        parent_ret = super(ValSys,self).hand_pre(hand_num)
        #
        if self.scoreboards is not None:
            b0_array = self.scoreboards[0].get_array()
            if len(b0_array) > 1 and b0_array[-1][1] >= 4:
                rule = 2
                self.play_on = b0_array[-1][0]
                self.play_size = 1
                return "val(%d)=%s" % (rule,self.play_on)
            else:
                b2_array = self.scoreboards[2].get_array()
                if len(b2_array) > 1:
                    rule = 1
                    side = b0_array[-1][0]
                    if b2_array[-1][1] == 1:
                        side = self.opposite_side(side)
                    self.play_on = side
                    self.play_size = 1
                    return "val(%d)=%s" % (rule,self.play_on)
        #
        return ""
    def end_shoe(self):
        seq2 = ""
        for i in self.WLseq:
            for j in i:
                seq2 += "0123456789abcdefghij"[j]
            seq2 += " "
        return "EndSys(%s) %d-%d-%d=%+.2f, %s" % (self.name,self.won, \
            self.lost,self.tied,self.money,seq2)
"""

# END

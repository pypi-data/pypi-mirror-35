#!/usr/bin/python

import pybaccarat.playingcards
import pybaccarat.baccarat
import pybaccarat.baccaratsystems

#class BaccSys(object):
#  Hook methods (we hook these methods to get called from Game)
#    def __init__(self, sys_name=""):
#    def new_shoe(self, burn_cards, boards=None):
#    def hand_pre(self, hand_num):
#    def hand_post(self, win_diff, player_hand, banker_hand):
#    def end_shoe(self):
#    def result_won(self, amount):
#    def result_lost(self, amount):
#  action methods (workers we call)
#    self.play(side, size=1)
#    self.quit_this_shoe()
#    self.opposite_side(side)
#  ?
#    def set_tie_object(self, tie_track):
#    def set_bpt_object(self, bpt):
#    def print_WLseq(self):
#  fields
#    self.hand_number   integer this hand number
#    self.name          string name of this bacc system
#    self.won           integer number won  in this shoe
#    self.lost          integer "      lost "  "    "
#    self.tied          integer "      tied "  "    "
#    self.last_WLT      String last result was this
#    self.money         float money in this shoe
#    self.play_on       string None or "B" or "P"
#    self.play_size     integer bet size
#    self.quit_shoe     boolean
#    self.scoreboards[4]
#    self.WLseq         array of integers for WL sequencing
class silver_bullet(pybaccarat.baccaratsystems.BaccSys):
    '''!
    The Ultimate Silver Bullet Proof
    
    1.Always start at the begining of a new shoe (never in the middle),
    always skip the very first hand. Wait for a B/P result before continue.
    2.hand#2 of the shoe always bet opposite the first hand result.
    3.Target exit at +3u or -6u. Always bet opposite, never same.
    '''
    def __init__(self, system_name=""):
        '''!
        Create a new instance of this bacc system.
        Must call the parent first.
        Then any unique initialization for this system.
        '''
        parent_ret = super(silver_bullet,self).__init__("silver_bullet")
        # Silver bullet unique data...
        self.silver_lost = 0
        self.silver_targets = [+3.0, -6.0]
    def new_shoe(self, burn_cards, boards):
        parent_ret = super(silver_bullet,self).new_shoe(burn_cards, boards)
        self.silver_lost = 0
    def result_won(self, amount):
        parent_ret = super(silver_bullet,self).result_won(amount)
        if self.silver_lost < 2:
            self.silver_lost = 0
        #print("{result_won SL=%d}"%self.silver_lost)
        return parent_ret
    def result_lost(self, amount):
        parent_ret = super(silver_bullet,self).result_lost(amount)
        if self.silver_lost < 2:
            self.silver_lost += 1
        #print("{result_lost SL=%d}"%self.silver_lost)
        return parent_ret
    def hand_pre(self, hand_num):
        '''!
        Prior to a hand being played, this is called to make a play.
        @param hand_num integer hand number
        @return String documentation purposes only, shown on output for hand
        
        Must call parent first, and exit if quit shoe indicated.
        '''
        parent_ret = super(silver_bullet,self).hand_pre(hand_num)
        # check the target for exit conditions
        if self.money < self.silver_targets[1] or \
           self.money > self.silver_targets[0]:
               self.quit_this_shoe()
        #
        if self.quit_shoe:
            return parent_ret
        # get the main_board... ['R0', ['P', 2], ['B', 1]]
        main_board = self.scoreboards[0].get_array()
        #print("{%r}" % str(main_board))
        if len(main_board) < 2:
            # this is the first B/P hand. No history of any B/P. Skip
            self.play(None)
            return "{skip first hand}"
        if len(main_board) == 2:
            if main_board[1][1] == 1: #first column size 1
                # this is the second BP hand of shoe. play opposite
                first_hand = main_board[1][0]
                if first_hand == "B":
                    self.play("P")
                    return "{2nd hand play P=opposite first hand}"
                elif first_hand == "P":
                    self.play("B")
                    return "{2nd hand play B=opposite first hand}"
        #
        if self.silver_lost == 2:
            # New 2.1 silver special case "triangle" 3,2,1
            if len(main_board) < 5 or main_board[-1][1] != 1 or \
               main_board[-2][1] != 2 and main_board[-3][1] != 3:
                # 2 losses in a row means we are in "waiting" mode.
                # Must wait until 2 single columns appear on the main board.
                if len(main_board) < 4 or main_board[-1][1] != 1 or \
                   main_board[-2][1] != 1:
                    return "{wait}"
            # the wait has been cleared
            self.silver_lost = 0
        # bet the opposite
        silver_bet = main_board[-1][0]
        if silver_bet == "B":
            self.play("P")
            return "{opp play P}"
        if silver_bet == "P":
            self.play("B")
            return "{opp play B}"
        return "{?}"

shoe = None     # default 8 decks
baccsys = None  # default no system

choice = 4
if choice == 2:
    # use interactive baccsys
    baccsys = pybaccarat.baccaratsystems.interactive()
elif choice == 3:
    # historical test
    shoe = pybaccarat.playingcards.Shoe("PPTBP")
elif choice == 4:
    # try silver system
    baccsys = silver_bullet()
    #shoe = pybaccarat.playingcards.Shoe("PPTBP")
else:
    # default play 1 entire shoe
    pass

pybaccarat.baccarat.Game(shoe=shoe, system=baccsys).play()

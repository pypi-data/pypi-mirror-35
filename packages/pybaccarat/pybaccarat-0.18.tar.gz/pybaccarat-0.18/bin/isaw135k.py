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
class i_saw_135k(pybaccarat.baccaratsystems.BaccSys):
    '''!
    "I saw this system win S135k in one night"
    1a. start betting on either the first streak, meaning when the outcome
        falls on: P/P/betP or B/B/betB or 1B
    1b. start betting this way when the numbers chop meaning they all into:
        P/B/betP or B/P/betB
    rule 1 (glf) time-before-last
    rule 2. after a win you always / (wait) for the source before placing
        on the next bet. if it continues to win you simply keep skipping a
        bet (considered as the waiting period) before betting again.
    2B. If you Lost, bet 2 units on the same side that just lost. If this 
        wins you are the / (wait) the same as rule 2.
    2C. If you lost1+lost2.
        
    SR  - source the actual placement that come out before you begin to play
    NB  - no bet
    /   - wait
    1st - first indicator
    2nd - second indicator
    JPO - jump out
    TIE - ignore ties, make the same play as before the tie
    
    
    '''
    
    '''
    shoe 1 B41 36 21 32 30
    01 NoBet    B
    02 NoBet    B
    03 B1       B win+0.95/1-0
    04 wait     B 
    05 B1       P lost-0.05/1-1
    06 B2       B win+1.85/2-1
    07 wait     B
    08 B1       B win+2.80/3-1
    09 wait     P
    10 B1       P lost+1.80/3-2
    11 B2       P lost-0.20/3-3
    12 JPO      P
    13          P
    14          P 1st
    15          B
    16          B 2nd
    17 B1       P lost-1.20/3-4
    18 B2       B win+0.70/4-4
    19 wait     B
    20 B1       B win+1.65/5-4
    21 wait     P
    22 B1       P lost+0.65/5-5
    23 B2       B win+2.55/6-5
    24 wait     B
    25 B1       B win+3.50/7-5
    quit +5 target
    BPBPBPBPB                                                     9
    B BPB BPB                                                     7
    B BP  B B                                                     5
    B  P                                                          2
       P                                                          1
       P                                                          1
    shoe 2
    P
    P
    P
    P
    B
    P
    B
    '''
    
    def __init__(self, system_name=""):
        '''!
        Create a new instance of this bacc system.
        Must call the parent first.
        Then any unique initialization for this system.
        '''
        parent_ret = super(i_saw_135k,self).__init__("i_saw_135k")
        # Silver bullet unique data...
        self.silver_lost = 0
        self.silver_targets = [+3.0, -6.0]
    def new_shoe(self, burn_cards, boards):
        parent_ret = super(i_saw_135k,self).new_shoe(burn_cards, boards)
        self.silver_lost = 0
    def result_won(self, amount):
        parent_ret = super(i_saw_135k,self).result_won(amount)
        if self.silver_lost < 2:
            self.silver_lost = 0
        #print("{result_won SL=%d}"%self.silver_lost)
        return parent_ret
    def result_lost(self, amount):
        parent_ret = super(i_saw_135k,self).result_lost(amount)
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
        parent_ret = super(i_saw_135k,self).hand_pre(hand_num)
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

choice = 3
if choice == 2:
    # use interactive baccsys
    baccsys = pybaccarat.baccaratsystems.interactive()
elif choice == 3:
    # historical test
    shoe = pybaccarat.playingcards.Shoe(
        #1 "BBBBPBBBPPPPPPBBPBBBPPBBB")
        #2 "PPPPBPBPPBPBPBP")
        #3 "BBPBPBBBBPPBBPBPPBPBBPBPPPPPPPPBBBPBPBBPBPBPBBPPPBBBPPPPPBBPPPPBBBPBBP")
        #4 "PPPPBBPPPPPBBBBBBBPPBPPBPPBBBBPBPBPBBBPPBBBBBBBBBBPBBBBPBBPPPPPBBB")
        #5 "PPBPBPBBBBBPBBPBBBBBPPPBBBBBPPBPBBBPPBBBBBPBBPPBBBBBBBPPBBBBBPBPPPBBBB")
        #6 "PBPPBBBPPPPPBPBPBBBBBBBBPPBBPBBBPPPBBPBPBPBPBBBPBPPPPBPPPPPBBBBPBBPBPPB")
        #7 "BPBBPPBBPPPPBPPPBPPPPBBBPBPPPPPPBBBPBPBBPBBBBPPBPBPPBPPBPBPPBBPBPP")
        #8 "BPPPPPPPPPPPPBPBBBBPBBBBPBPPPPPPBBBPPBBPBPBPPBBPBBPPBPPPPBBPBPB")
        "PBPPBBBPPPBPPBBBBPPPPBBPBBBPBPBBPPBPPBBPBBBPBPPBPPBPBPBPBBBBBBBPBPBBBPBPP")
elif choice == 4:
    # try silver system
    baccsys = i_saw_135k()
    #shoe = pybaccarat.playingcards.Shoe("PPTBP")
else:
    # default play 1 entire shoe
    pass

pybaccarat.baccarat.Game(shoe=shoe, system=baccsys).play()

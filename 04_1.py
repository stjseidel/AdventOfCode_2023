# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
import re
from timeit import default_timer as timer


def scratchcards(lines):
    total_win = 0
    for line in lines:
        this_line = line.split(':')
        game = this_line[0]
        numbers = this_line[1]
        card = game.split(' ')[1]
        valid, have = numbers.split('|')
        valid = [val for val in valid.split(' ') if val != '']
        have = [hav for hav in have.split(' ') if hav != '']
        matched = len((set(valid) & set(have)))
        if matched == 0:
            win = 0
        else:
            win = 2 ** (matched-1)
        total_win += win
    return total_win


class card_play():
    def __init__(self):
        self.card_wins = {}
        self.total_win2 = 0
        self.total_cards = 0
        self.card_sums = {}

    def scratchcards2(self, lines):
        for line in lines:
            line = re.sub(' +', ' ', line)
            this_line = line.split(':')
            card = int(this_line[0].split(' ')[1])
            numbers = this_line[1]
            valid, have = numbers.split('|')
            valid = [val for val in valid.split(' ') if val != '']
            have = [hav for hav in have.split(' ') if hav != '']
            matched = len((set(valid) & set(have)))
            if matched == 0:
                win = 0
            else:
                win = 2 ** (matched-1)
            # self.total_win2 += win
            self.card_wins[card] = (win, matched)
        x = 0
        self.card_sums = {card:0 for card in self.card_wins.keys()}
        for card, this_win in self.card_wins.items():
            x += 1
            # print('xxx', x, card, self.card_wins[card], self.total_win2)
            self.play_card(card)
            # won = this_win[0]
            # matched = this_win[1]
            # print(card, this_win)
            # self.total_win2 += won
            # for i in range(1, matched+1):
            #     if card+i < len(lines):
            #         this_win = self.card_wins[card+i]
            #         won = this_win[0]
            #         matched = this_win[1]
            #         old_win = self.total_win2
            #         self.total_win2 += won
            #         print(card, this_win, old_win, self.total_win2)
            # print('----')
    
    def play_card(self, card):
        if card in self.card_wins.keys():
            self.total_cards += 1
            self.card_sums[card] += 1
            # print(card, self.card_sums[card])
            this_win = self.card_wins[card][0]
            if this_win == 0:
                # print(f'{self.total_cards}. Playing card {card}. no win.')
                return card
            matches = self.card_wins[card][1]
            # print(f'{self.total_cards}. Playing card {card}. Adding <{this_win}>. Playing <{matches}> more cards. {self.total_win2} + {this_win} = {self.total_win2 + this_win}')
            # self.total_win2 += this_win
            for i in range(card+1, card+1+matches):
                self.play_card(i)
        return card


if __name__ == '__main__':
    aoc = AOC(day='04')
    game2 = card_play()
    lines = aoc.read_lines('04_simple.txt')
    lines = aoc.read_lines('04.txt')

    total_win = scratchcards(lines)
    print(total_win)    
    aoc.stop()
    aoc.start()

    game2.scratchcards2(lines)
    
    print(game2.card_sums)
    print(game2.card_wins)
    print(game2.total_cards)
    aoc.stop()

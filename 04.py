# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
import re

class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
    card_wins = {}
    total_win2 = 0
    total_cards = 0
    card_sums = {}
    
    def part1(self):
        total_win = 0
        for line in self.lines:
            this_line = line.split(':')
            numbers = this_line[1]
            valid, have = numbers.split('|')
            valid = [val for val in valid.split(' ') if val != '']
            have = [hav for hav in have.split(' ') if hav != '']
            matched = len((set(valid) & set(have)))
            if matched == 0:
                win = 0
            else:
                win = 2 ** (matched-1)
            total_win += win
        self.result1 = total_win
        self.time1 = timer()
        return self.result1

    def part2(self):
        for line in self.lines:
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
            self.card_wins[card] = (win, matched)
        x = 0
        self.card_sums = {card:0 for card in self.card_wins.keys()}
        for card, this_win in self.card_wins.items():
            x += 1
            self.play_card(card)
        self.result2 = self.total_cards
        self.time2 = timer()
        return self.result2
    
    def play_card(self, card):
        if card in self.card_wins.keys():
            self.total_cards += 1
            self.card_sums[card] += 1
            this_win = self.card_wins[card][0]
            if this_win == 0:
                return card
            matches = self.card_wins[card][1]
            for i in range(card+1, card+1+matches):
                self.play_card(i)
        return card
            
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
           

if __name__ == '__main__':
# prep
    today = Today(day='04', simple=True)
    today.create_txt_files()
    today.lines

# simple part 1
    today.set_lines(simple=True)
    today.part1()
    print(f'Part 1 <SIMPLE> result is: {today.result1}')
    
# hard part 1
    today.set_lines(simple=False)
    today.part1()
    print(f'Part 1 <HARD> result is: {today.result1}')
    today.stop()

# simple part 2
    today.set_lines(simple=True)
    today.part2()
    print(f'Part 2 <SIMPLE> result is: {today.result2}')

# hard part 2
    today.set_lines(simple=False)
    today.part2()
    print(f'Part 2 <HARD> result is: {today.result2}')
    today.stop()
    today.print_final()

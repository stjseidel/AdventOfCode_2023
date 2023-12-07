# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
import collections

class Game():
    def __init__(self, hand, wager):
        self.hand = hand
        self.wager = int(wager)
        
    def __repr__(self):
      return f'{self.hand}:{self.wager}'
  
    
class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
    
    def get_card_dict(self):
        cards = 'A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2'.replace(' ', '').split(',')
        len(cards)
        values = list(range(14,1,-1))
        self.CamelCards = dict(list(zip(cards, values)))  
        
    def parse_lines(self):
        lines = self.lines
        lines = [line.split(' ') for line in lines]
        self.game_rank = len(lines)
        self.games = [Game(game[0], game[1]) for game in lines]

    def rate_game(self, game):
        # game = list(self.games.items())[0]
        hand = game.hand
        # wager = game.wager
        game.values = [self.CamelCards[card] for card in hand]
        counts_dict = collections.Counter(x[0] for x in hand if x)
        counts = sorted(list(counts_dict.values()), reverse=True)
        if counts == [5]:
            #five of a kind
            self.hands_dict[6].append(game)
        elif counts == [4, 1]:
            # four of a kind
            self.hands_dict[5].append(game)
        elif counts == [3, 2]:
            # full house
            self.hands_dict[4].append(game)
        elif counts == [3, 1, 1]:
            self.hands_dict[3].append(game)
            # three of a kind
        elif counts == [2, 2, 1]:
            # two pairs
            self.hands_dict[2].append(game)
        elif counts == [2, 1, 1, 1]:
            # one pair
            self.hands_dict[1].append(game)
        elif counts == [1, 1, 1, 1, 1]:
            # high card
            self.hands_dict[0].append(game)
        else:
            print(f'warning, hand not found for {hand}')
        
    def rate_game2(self, game):
        # game = list(self.games.items())[0]
        hand = game.hand
        # wager = game.wager
        game.values = [self.CamelCards[card] for card in hand]
        counts_dict = collections.Counter(x[0] for x in hand.replace('J', '') if x)
        counts = sorted(list(counts_dict.values()), reverse=True)
        jokers = 5 - len(hand.replace('J', ''))
        if jokers > 0:
            if jokers == 5:
                counts = [5]
            else:
                # print(hand, wager, counts, jokers, counts_dict)
                counts[0] += jokers
        # setlen = len(set(hand))
        if counts == [5]:  # dict 0
            #five of a kind
            self.hands_dict[6].append(game)
        elif counts == [4, 1]:  # dict 1
            # four of a kind
            self.hands_dict[5].append(game)
        elif counts == [3, 2]:  # dict 2
            # full house
            self.hands_dict[4].append(game)
        elif counts == [3, 1, 1]:  # dict 3
            self.hands_dict[3].append(game)
            # three of a kind

        elif counts == [2, 2, 1]:  # dict 4
            # two pairs
            self.hands_dict[2].append(game)
            
        elif counts == [2, 1, 1, 1]:  # dict 5
            # one pair
            self.hands_dict[1].append(game)
            
        elif counts == [1, 1, 1, 1, 1]:  # dict 6
            # high card
            self.hands_dict[0].append(game)
        
        else:
            print(f'warning, hand not found for {hand}')
        
    def sort_games_in_dict(self, hands_list):
        if len(hands_list) > 0:
            # self.print_games(games=hands_list)
            all_values = sorted([game.values for game in hands_list], reverse=False)
            for game in hands_list:
                game.position = self.rank_offset + all_values.index(game.values)
            self.rank_offset += len(hands_list)
            # self.print_games(games=hands_list)
        

    def calc_result1(self):
        result1 = sum([game.position * game.wager for game in self.games])
        # [(game.position, game.wager, game.position * game.wager) for game in self.games]
        return result1
    
# =============================================================================
#     def parse_lines2(self):
#             lines = self.lines
# =============================================================================
        
    def part1(self):
        self.get_card_dict()
        self.hands_dict = {i:[] for i in range(7)}
        for game in self.games:
            self.rate_game(game)
        self.rank_offset = 1
        for i in range(7):
            hands_list = self.hands_dict[i]
            self.sort_games_in_dict(hands_list)
            
        self.result1 = self.calc_result1()
        self.time1 = timer()
        return self.result1

    def print_games(self, games=''):
        if games == '':
            games = self.games
        for game in games:
            if 'position' in dir(game):
                print(game.hand, game.position, game.wager, game.position*game.wager)
            else:
                print(game.hand, game.wager)
                
    def part2(self):
        self.get_card_dict()
        self.CamelCards['J'] = 1
    
        self.hands_dict = {i:[] for i in range(7)}
        for game in self.games:
            self.rate_game2(game)
        self.rank_offset = 1
        for i in range(7):
            hands_list = self.hands_dict[i]
            self.sort_games_in_dict(hands_list)
            
            
        self.result2 = self.calc_result1()
        self.time2 = timer()
        return self.result2

    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='', simple=True)
    today.lines

# simple part 1
    today.set_lines(simple=True)
    today.parse_lines()
    today.part1()
    print(f'Part 1 <SIMPLE> result is: {today.result1}')
    today.print_games()
# hard part 1
    today.set_lines(simple=False)
    today.parse_lines()
    today.part1()
    print(f'Part 1 <HARD> result is: {today.result1}')
    today.stop()


# simple part 2
    today.set_lines(simple=True)
    # today.print_games()
    today.parse_lines()
    today.part2()
    print(f'Part 2 <SIMPLE> result is: {today.result2}')
    
# hard part 2
    today.set_lines(simple=False)
    today.parse_lines()
    today.part2()
    print(f'Part 2 <HARD> result is: {today.result2}')
    today.stop()
    today.print_final()
    


# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
from collections import defaultdict

class Signal():
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        
    def __repr__(self):
        return f'{self.sender} -{self.message}-> {self.receiver}'
        
class Modules():
    message_stack = []
    signals_sent = []
    module_dict = {}
    processed = 0
    conjunctions = []
        
    def push_button(self, message):
        self.send('broadcaster', Signal('button', 'broadcaster', message))
    
                
    
    def get_result(self):
        lows = Modules.signals_sent.count(0)
        highs = len(Modules.signals_sent) - lows
        result = lows * highs
        print(f'Number of signals sent: highs: {highs}; lows: {lows}. Product: {result}.')
        return result
        
    def send(self, receiver, signal):
        if not type(receiver) == list:
            receiver = [receiver]
        receiver = [rec.replace(' ', '') for rec in receiver]
        for rec in receiver:
            output = Signal(signal.sender, rec, signal.message)
            Modules.message_stack.append(output)
    
    def init_modules(self):
        for module in Modules.module_dict.values():
            receiver = module.receiver
            if not type(receiver) == list:
                receiver = [receiver]
            receiver = [rec.replace(' ', '') for rec in receiver]
            for rec in receiver:
                if rec in Modules.module_dict.keys():
                    Modules.module_dict[rec].receive(Signal(module.name, rec, module.state))
        Modules.message_stack = []
        for module in self.conjunctions:
            self.module_dict[module.name].senders = {sender:0 for sender in module.senders.keys()}
        for name, module in self.module_dict.items():
            self.module_dict[name].state = 0
        Modules.signals_sent = []
        
    def process_stack(self):
        while Modules.processed < len(Modules.message_stack):
            signal = Modules.message_stack[Modules.processed]
            Modules.processed += 1
            Modules.signals_sent.append(signal.message)
            if not signal.receiver in Modules.module_dict.keys():
                Modules.module_dict[signal.receiver] = Broadcaster(signal.receiver, [])
            # state_in = Modules.module_dict[signal.receiver].state
            Modules.module_dict[signal.receiver].receive(signal)
            # state_out = Modules.module_dict[signal.receiver].state
            # print(f'{signal}. {signal.receiver}: [{state_in}->{state_out}]')
        Modules.message_stack = []
        Modules.processed = 0
        
    def process_stack2(self):
        while Modules.processed < len(Modules.message_stack):
            signal = Modules.message_stack[Modules.processed]
            Modules.processed += 1
            Modules.signals_sent.append(signal.message)
            if not signal.receiver in Modules.module_dict.keys():
                Modules.module_dict[signal.receiver] = Broadcaster(signal.receiver, [])
            Modules.module_dict[signal.receiver].receive(signal)
            if signal.receiver == 'rx' and signal.message == 0:
                return True
        Modules.message_stack = []
        Modules.processed = 0
        return False
        

class FlipFlop(Modules):
    def __init__(self, name, receiver):
        self.state = 0
        self.name = name
        self.receiver = receiver
        
    def receive(self, signal):
        if signal.message == 1:
            return None
        self.state = 1 - self.state
        self.send(self.receiver, Signal(self.name, self.receiver, self.state))
        
class Conjunction(Modules):
    def __init__(self, name, receiver):
        self.state = 0
        self.name = name
        self.receiver = receiver
        self.senders = defaultdict(int)
        
    def receive(self, signal):
        self.senders[signal.sender] = signal.message
        if set([message for message in self.senders.values()]) == set([1]):
            self.state = 0
        else:
            self.state = 1
        self.send(self.receiver, Signal(self.name, self.receiver, self.state))
        
class Broadcaster(Modules):
    def __init__(self, name, receiver):
        self.state = 0
        self.name = name
        self.receiver = receiver
    
    def receive(self, signal):
        self.state = signal.message
        self.send(self.receiver, Signal(self.name, self.receiver, self.state))
        
        
        
class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
    def parse_lines(self, file_path=''):
        self.modules.modules = {}
        self.modules.module_dict['button'] = Broadcaster('button', 'broadcaster')
        lines = self.lines
        for line in lines:
            module = line.split(' -> ')[0]
            receiver = (line.split(' -> ')[1]).split(',')
            receiver = [rec for rec in receiver if rec not in ['', ' ']]
            if 'broadcaster' in module:
                self.modules.module_dict[module] = Broadcaster(module, receiver)
            elif '%' in module:
                self.modules.module_dict[module[1:]] = FlipFlop(module[1:], receiver)
            elif '&' in module:
                self.modules.module_dict[module[1:]] = Conjunction(module[1:], receiver)
                self.modules.conjunctions.append(self.modules.module_dict[module[1:]])
            else:
                print('warning, unknown input:', line)
        self.modules.init_modules()
        return lines
    
    def part1(self, run=1):
        self.modules = Modules()
        _ = self.parse_lines()
        self.modules.init_modules()
        
        for i in range(run):
            self.modules.push_button(0)
            self.modules.process_stack()
        self.result1 = self.modules.get_result()
        del self.modules
        self.time1 = timer()
        return self.result1
        
        
    def part2(self, run=1):
        self.modules = Modules()
        self.modules.init_modules()
        _ = self.parse_lines()
        finished = False
        pressed = 0
        for i in range(run):
            pressed += 1
            self.modules.push_button(0)
            finished = self.modules.process_stack2()
            if finished:
                print('runs:', pressed)
                break
        
        self.result2 = pressed
        
        self.time2 = timer()
        return self.result2
                
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='20', simple=True)
    today.create_txt_files()

# simple part 1
    today.set_lines(simple=True)
    today.part1(run=1000)
    print(f'Part 1 <SIMPLE> result is: {today.result1}')
    
# simple part 1
    today.lines = today.read_lines(file_path='20_simple2.txt')  
    today.part1(run=1000)
    print(f'Part 1 <SIMPLE> result is: {today.result1}')
    
    
    
# hard part 1
    today.set_lines(simple=False)
    today.part1(run=1000)
    print(f'Part 1 <HARD> result is: {today.result1}')
    today.stop()


# =============================================================================
# # simple part 2
#     today.set_lines(simple=True) 
#     today.part2()
#     print(f'Part 2 <SIMPLE> result is: {today.result2}')
# =============================================================================

# =============================================================================
# # hard part 2
#     today.set_lines(simple=False)
#     today.part2(1000000)
#     print(f'Part 2 <HARD> result is: {today.result2}')
#     today.stop()
#     today.print_final()
# =============================================================================


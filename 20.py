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
        return f'From: <{self.sender}>; To: <{self.receiver}>; message: <{self.message}>'
        
class Modules():
    message_stack = []
    signals_sent = []
    module_dict = {}
    processed = 0
        
    def push_button(self, message):
        self.send('broadcaster', Signal('button', 'broadcaster', message))
    
    def reset_counts(self):
        self.highs = 0
        self.lows = 0
    
    def get_result(self):
        lows = self.signals_sent.count(0)
        highs = len(self.signals_sent) - lows
        result = lows * highs
        print(f'Number of signals sent: highs: {highs}; lows: {lows}. Product: {result}.')
        
    def send(self, receiver, signal):
        if not type(receiver) == list:
            receiver = [receiver]
        receiver = [rec.replace(' ', '') for rec in receiver]
        for rec in receiver:
            output = Signal(signal.sender, rec, signal.message)
            if rec not in self.module_dict.keys():
                print(f'warning, <{rec}> not in receiving modules: ', output)
            Modules.message_stack.append(output)
            # print(f'added Signal to stack. new height: {len(Modules.message_stack)}. {output}')
            self.signals_sent.append(output.message)
        pass
    
    def init_modules(self):
        for module in self.module_dict.values():
            module.send(module.receiver, Signal(module.name, module.receiver, module.state))
        Modules.message_stack = []
        self.reset_counts()
        
    def process_stack(self):
        # while len(Modules.message_stack) > 0:
        while Modules.processed < len(Modules.message_stack):
            signal = Modules.message_stack[Modules.processed]
            # Modules.message_stack.pop(0)
            Modules.processed += 1
            print(f'Send [{signal}] Stackheight: {len(Modules.message_stack)}. Processed: {self.processed}')
            if signal.receiver in self.module_dict.keys():
                current_state = Modules.module_dict[signal.sender].state
                Modules.module_dict[signal.receiver].receive(Signal(signal.sender, signal.receiver, current_state))
            else:
                print('OUTPUT signal:', signal)
            pass
        print('Message_stack is exhausted.')
        

class FlipFlop(Modules):
    def __init__(self, name, receiver):
        self.state = 0
        self.name = name
        self.receiver = receiver
        
    def receive(self, signal):
        if signal.message == 1:
            return None
        self.state = 1 - signal.message
        self.signals_sent.append(self.state)
        self.send(self.receiver, Signal(self.name, self.receiver, self.state))
        
class Conjunction(Modules):
    def __init__(self, name, receiver):
        self.state = 0
        self.name = name
        self.receiver = receiver
        self.senders = defaultdict(0)
        
    def receive(self, signal):
        self.senders[signal.sender] = signal.message
        if set([message for message in self.senders.values()]) == set(1):
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
                self.modules.module_dict[module[1:]] = FlipFlop(module[1:], receiver)
            else:
                print('warning, unknown input:', line)
        self.modules.init_modules()
        
        return lines
    
    def part1(self):
        self.modules = Modules()
        lines = self.parse_lines()
        for i in range(1):
            Modules.message_stack = []
            Modules.processed = 0
            print(len(Modules.message_stack))
            for name, module in self.modules.module_dict.items():
                print(name, module.receiver, module.state)
            self.modules.push_button(0)
            self.modules.process_stack()
            self.modules.get_result()
        
        self.result1 = 'TODO'
        self.time1 = timer()
        return self.result1
                
    def part2(self):
        lines = self.parse_lines()
        self.result2 = 'TODO'
        self.time2 = timer()
        return self.result2
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='20', simple=True)
    today.create_txt_files()

# =============================================================================
# # simple part 1
#     today.set_lines(simple=True)
#     today.part1()
#     print(f'Part 1 <SIMPLE> result is: {today.result1}')
# =============================================================================
    
# simple part 1
    # today.set_lines(simple=True)
    today.lines = today.read_lines(file_path='20_simple2.txt')  
    today.part1()
    print(f'Part 1 <SIMPLE> result is: {today.result1}')
    
    
    
# =============================================================================
# # hard part 1
#     today.set_lines(simple=False)
#     today.part1()
#     print(f'Part 1 <HARD> result is: {today.result1}')
#     today.stop()
# 
# 
# # simple part 2
#     today.set_lines(simple=True) 
#     today.part2()
#     print(f'Part 2 <SIMPLE> result is: {today.result2}')
# 
# # hard part 2
#     today.set_lines(simple=False)
#     today.part2()
#     print(f'Part 2 <HARD> result is: {today.result2}')
#     today.stop()
#     today.print_final()
# 
# =============================================================================

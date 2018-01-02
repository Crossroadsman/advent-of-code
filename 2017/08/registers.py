'''
Day 8: I Heard You Like Registers
=================================

You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the 
result of a series of unusual register instructions.

Each instruction consists of several parts: 
- the register to modify, 
- whether to increase or decrease that register's value, 
- the amount by which to increase or decrease it, and 
- a condition. 

If the condition fails, skip the instruction without modifying the register. The 
registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all 
the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?
'''
import re

class CleanData():
    
    def get_filename(self):
        return input("Enter the filename to open > ")

    def clean_data(self, filename: str) -> [{str:str}]:
        print("Cleaning Data")
        print("=============")
        
        print("Opening file")
        file_object = open(filename, 'r')
        
        cleaned_data = []
        '''
        (?P<register>\w+)[ \t]+(?P<instruction>\w+)[ \t]+(?P<quantum>[-\d]+)[ \t]+(if (?P<query_register>\w+)[ \t]+(?P<query_operator>[!=><]+)[ \t]+(?P<query_value>[-\d]+))?
        Named Capture Group `register` (?P<register>\w+)
            \w+ matches any word character (equal to [a-zA-Z0-9_])
            + Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
        Match a single character present in the list below [ \t]+
            + Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
              matches the character   literally (case sensitive)
            \t matches a tab character (ASCII 9)
        Named Capture Group instruction (?P<instruction>\w+)
            \w+ matches any word character (equal to [a-zA-Z0-9_])
            + Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
        Match a single character present in the list below [ \t]+
            + Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
              matches the character   literally (case sensitive)
            \t matches a tab character (ASCII 9)
        Named Capture Group quantum (?P<quantum>[-\d]+)
            Match a single character present in the list below [-\d]+
            + Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
            - matches the character - literally (case sensitive)
            \d matches a digit (equal to [0-9])
        Match a single character present in the list below [ \t]+
            + Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
              matches the character   literally (case sensitive)
            \t matches a tab character (ASCII 9)
        4th Capturing Group (if (?P<query_register>\w+)[ \t]+(?P<query_operator>[!=><]+)[ \t]+(?P<query_value>[-\d]+))?
            ? Quantifier — Matches between zero and one times, as many times as possible, giving back as needed (greedy)
            if  matches the characters if  literally (case sensitive)
            Named Capture Group query_register (?P<query_register>\w+)
                Match a single character present in the list below [ \t]+
            Named Capture Group query_operator (?P<query_operator>[!=><]+)
                Match a single character present in the list below [ \t]+
            Named Capture Group query_value (?P<query_value>[-\d]+)
        '''
        pattern = r'(?P<register>\w+)[ \t]+(?P<instruction>\w+)[ \t]+(?P<quantum>[-\d]+)[ \t]+(if (?P<query_register>\w+)[ \t]+(?P<query_operator>[!=><]+)[ \t]+(?P<query_value>[-\d]+))?'
        
        for line in file_object:

            match_object = re.match(pattern, line)
            
            if match_object: # a match was found
                line_data = {'register': match_object.groupdict()['register'],
                             'instruction': match_object.groupdict()['instruction'],
                             'quantum': match_object.groupdict()['quantum'],
                             'query_register': match_object.groupdict()['query_register'],
                             'query_operator': match_object.groupdict()['query_operator'],
                             'query_value': match_object.groupdict()['query_value'],
                             }
                cleaned_data.append(line_data)
                print("{} --> {}".format(line, line_data))
                
            else: # line didn't match the regex -> malformed input?
                print("line did not conform to expected format")
                
        file_object.close()
        return cleaned_data

class ProcessData():
    
    def compare(self, registers: {str:int}, register: str, operator: str, value: int) -> bool:
        if operator == '!=':
            return registers[register] != value
        if operator == '==':
            return registers[register] == value
        if operator == '>':
            return registers[register] > value
        if operator == '>=':
            return registers[register] >= value
        if operator == '<':
            return registers[register] < value
        if operator == '<=':
            return registers[register] <= value
        else:
            print("unknown operator {}".format(operator))
            raise
    
    def process_data(self, data: [{str:str}]) -> int:
        
        registers = {}
        for element in data:
            
            if self.compare(registers=registers, register=element['query_register'], operator=element['query_operator'], value=int(element['query_value'])):
                register = element['register']
                instruction = element['instruction']
                quantum = int(element['quantum'])
                                   
                if instruction == 'inc':
                    registers[register] += quantum
                if instruction == 'dec':
                    registers[register] -= quantum
                else:
                    print("unknown instruction {}".format(instruction))
                                   
        return max(registers.values())

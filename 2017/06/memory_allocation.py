'''
Day 6: Memory Reallocation
==========================

A debugger program here is having an issue: it is trying to repair a memory reallocation routine, but it keeps getting stuck in an 
infinite loop.

In this area, there are sixteen memory banks; each memory bank can hold any number of blocks. The goal of the reallocation routine is to 
balance the blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the memory bank with the most blocks (ties won by the lowest-numbered 
memory bank) and redistributes those blocks among the banks. To do this, it removes all of the blocks from the selected bank, then moves 
to the next (by index) memory bank and inserts one of the blocks. It continues doing this until it runs out of blocks; if it reaches the 
last memory bank, it wraps around to the first one.

The debugger would like to know how many redistributions can be done before a blocks-in-banks configuration is produced that has been seen 
before.

For example, imagine a scenario with only four memory banks:

- The banks start with `0`, `2`, `7`, and `0` blocks. The third bank has the most blocks, so it is chosen for redistribution.
- Starting with the next bank (the fourth bank) and then continuing to the first bank, the second bank, and so on, the 7 blocks are spread 
out over the memory banks. The fourth, first, and second banks get two blocks each, and the third bank gets one back. The final result 
looks like this: `2 4 1 2`.
- Next, the second bank is chosen because it contains the most blocks (four). Because there are four memory banks, each gets one block. 
The result is: `3 1 2 3`.
- Now, there is a tie between the first and fourth memory banks, both of which have three blocks. The first bank wins the tie, and its 
three blocks are distributed evenly over the other three banks, leaving it with none: `0 2 3 4`.
- The fourth bank is chosen, and its four blocks are distributed such that each of the four banks receives one: `1 3 4 1`.
- The third bank is chosen, and the same thing happens: `2 4 1 2`.

At this point, we've reached a state we've seen before: `2 4 1 2` was already seen. The infinite loop is detected after the fifth block 
redistribution cycle, and so the answer in this example is 5.

Given the initial block counts in your puzzle input, how many redistribution cycles must be completed before a configuration is produced 
that has been seen before?
'''

class MemoryAllocation():

    def index_max(self, arr: [int]) -> int:
        i = arr.index(max(arr))
        print("max value is {} at index {}".format(arr[i], i))
        return i
    
    def solver(self, arr: [int]) -> int:
        '''Takes an array of ints, reallocates the elements as described at the top of the module. This process is repeated until a
           reallocation produces a value that has been seen before, at which point the number of iterations (including the final one)
           is returned.'''
        
        working_list = arr[:] # copy the input list into a working version
        history = [working_list] # add the initial state to the history list
        
        print("starting outer loop for list: {}".format(working_list))
        while True:
            print("finding max value in list")
            i = self.index_max(arr=working_list)
            print("taking max value of out working list and putting in temp variable")
            num_to_allocate = working_list[i]
            working_list[i] = 0
            
            print("going into inner loop")
            while num_to_allocate > 0:
                i = (i + 1) % len(working_list)
                working_list[i] += 1
                num_to_allocate -= 1
                
            if working_list in history:
                return len(history) + 1
            else:
                history.append(working_list)

'''
Day 3: Spiral Memory
--------------------

level 1: 1 (1) --- 8(n - 1)
level 2: 2–9 (8) --- 8(n - 1)
level 3: 10–25 (16) --- 
level 4: 26–49 (24)

At each level the size of the ring is 8(n-1).
The cumulative elements is:

L1 – 1 1^2
L2 – 9 3^2
L3 – 25 5^2
L4 – 49 7^2

cumulative elements at each level is (2n-1)^2

so for a given number, say

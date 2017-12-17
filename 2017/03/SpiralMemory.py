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

so for a given number, say:

3 - sqrt(3) = 1.73, 2.73 = 2n, n = 1.365. Therefore 3 is in ring 2.
7 - sqrt(7) = 2.65, 3.65 = 2n, n = 1.825. Therefore 7 is in ring 2.
14 - sqrt(14) = 3.74, 4.74 = 2n, n = 2.37. Therefore 14 is in ring 3.
20 - sqrt(20) = 4.47, 5.47 = 2n, n = 2.74. Therefore 20 is in ring 3.
25 - sqrt(25) = 5, 6 = 2n, n = 3. Therefore 25 is in ring 3 (and is the largest number in ring3).

width/height of a ring is:

L1 - 1
L2 - 3
L3 - 5
L4 - 7

2n-1

number of elements in ring is [2n-1] + [2n-1] + [2n-1-2] + [2n-1-2] = 8n - 8

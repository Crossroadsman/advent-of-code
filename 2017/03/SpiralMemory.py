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

We can compute the number of steps (manhattan distance) (S) from a specified location (L) to the center by doing the following:

1a. Using the knowledge that for any given ring (R) (which always starts at 1 step up from the bottom-right square of the ring and goes 
   counter clockwise) the farthest distance is the distance from each of the corners which is always 2(R - 1)

1b. Using also the knowledge that the number of steps required drops by 1 for every step away from the nearest corner that a location is

2. We can compute the L of each of the corners for a given R as follows:

   - previous R's bottom-right: (2R - 3)^2
   - top-right:   (2R - 3)^2 + ( 1 * 2(R - 1) )
   - top-left:    (2R - 3)^2 + ( 2 * 2(R - 1) )
   - bottom-left: (2R - 3)^2 + ( 3 * 2(R - 1) )
   - bottom-right (2R - 3)^2 + ( 4 * 2(R - 1) )

3. Using the knowledge that (2R - 1)^2 is the highest L for any R, we can reverse the formula get the ring (R) from a given location (L):

   CEIL ( ( SQRT(L) + 1 ) / 2 ) = R
   
4a. For a given L, once we know the R, we can work out R's corners and the distance of L from each corner. We know from 1b that manhattan
   distance for L is the manhattan distance from the corner (which we know from 1a) minus the straight line distance to the nearest corner
   for L.
   
4b. For each corner's L value, we deduct the actual L. The minimum of the absolute differences is the nearest corner.

4c. The MD for L is the MD for a corner of that R minus the distance from the corner we computed in 4b.

Worked example:

We use L=18

Calculate ring: CEIL ( ( SQRT(18) + 1 ) / 2 = 3
Calculate corners:
   TR: (2*3 - 3)^2 + ( 1 * 2(3 - 1) ) = 13
   TL: (2*3 - 3)^2 + ( 2 * 2(3 - 1) ) = 17  
   BL: (2*3 - 3)^2 + ( 3 * 2(3 - 1) ) = 21
   BR: (2*3 - 3)^2 + ( 4 * 2(3 - 1) ) = 25

Deduct L from corners:

   TR: 13 - 18 = -5, ABS = 5
   TL: 17 - 18 = -1, ABS = 1
   BL: 21 - 18 =  3, ABS = 3
   BR: 25 - 18 =  7, ABS = 7
   
MIN(5, 1, 3, 7) = 1

MD for corner is 2(R - 1) = 2 * (3 - 1) = 4
Deduct steps from corner                = -1
MD for L=18:                            = 3
'''

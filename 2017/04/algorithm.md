Advent of Code 2017: Day 4—High-Entropy Passphrases
===================================================

Problem
-------

A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

Discussion
----------

The permutations of a list where every element in the list has to occur once is simply n!
The permutations of a list where some number (r) elements from the list have to occur once is n! / (n - r)!
(See [this][link01] for details).

Since we want all the permutations of every r from 1...n we need to compute n! plus each of the n!/(n-r)! for every r between 1 and n-1

Implementation
--------------

See the sample Swift file in this folder.


[link01]: https://www.mathsisfun.com/combinatorics/combinations-permutations.html "Maths Is Fun: Combinations and Permutations"



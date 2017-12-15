"""
Day 1 - Inverse Captcha
-----------------------

- Review a sequence of digits
- Find the `sum` of all digits that match the next digit in the list
- The list is circular

Examples:
- 1122 produces a sum of 3 (1 + 2) because first digit matches second digit
  and third digit matches fourth digit;
- 1111 produces 4 (1 + 1 + 1 + 1);
- 1234 produces 0;
- 91212129 produces 9.
"""

class InverseCaptcha():
    def isSame(self, a: int, b: int) -> bool:
        return a == b

    def listify(self, n: int) -> [int]:
        return [int(i) for i in str(n)]

    def next_digit(self, i: int, l: [int], mode: int=0) -> int:
        '''modes: 0 - next digit (circular)
                  1 - halfway round (circular)'''
        if len(l) <= 1:
            return None

        next_i = None
        if mode == 0:
            next_i = (i + 1) % len(l)

        elif mode == 1:
            hop_length = len(l) // 2
            next_i = (i + hop_length) % len(l)

        return next_i

    def sumDigits(self, l: [int], mode: int=0) -> int:

        if len(l) <= 1:
            return 0

        running_total = 0
        for i, v in enumerate(l):
            next_i = self.next_digit(i=i, l=l, mode=mode)
            if v == l[next_i]:
                running_total += v

        return running_total



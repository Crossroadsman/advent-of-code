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

    def sumDigits(self, l: [int]) -> int:
        if len(l) <= 1:
            return 0

        running_total = 0
        for i, v in enumerate(l):
            if i == len(l) - 1:
                if self.isSame(v, l[0]):
                    running_total += v
            else:
                if self.isSame(v, l[i+1]):
                    running_total += v

        return running_total



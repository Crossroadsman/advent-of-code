'''
Day 2: Corruption Checksum
--------------------------

For each row of (space-separated?) ints:
- find the lowest value
- find the highest value
- determine the difference between l and h
Sum all the differences

E.g., for the following
5 1 9 5
7 5 3
2 4 6 8

the first row would have l=1, h=9, d=8
second row: l=3, h=7, d=4
third: l=2, h=8, d=6
'''

class CorruptionChecksum():

    def listifyRow(self, row: str) -> [int]:
        return [int(num) for num in row.split()]

    def diffList(self, row: [int]) -> int:
        return max(row) - min(row)

    def get_filename(self) -> str:
        filename = input("Enter the filename to process >")
        return filename

    def process_file(self, filename: str) -> int:
        file = open(filename, 'r')
        running_total = 0
        for line in file:
            nums = self.listifyRow(row=line)
            diff = self.diffList(row=nums)
            running_total += diff
        return running_total

    def checksum(self):
        filename = self.get_filename()
        checksum = self.process_file(filename=filename)
        print("Checksum: {}".format(checksum))

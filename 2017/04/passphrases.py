class Passphrases():

    def get_filename(self) -> str:
        return input("Please enter the filename: > ")

    def is_valid(self, arr: [str]) -> bool:
        '''A list is valid if there are no duplicates
           which we can test by comparing whether the length of a
           set from the list are the same as the contents of the list'''
        return len(arr) == len(list(set(arr)))

    def process_file(self) -> int:
        '''reads the specified file and checks is_valid on every row
           in the file. Eah valid row increments the valid count'''
        valid_count = 0
        file_object = open(self.get_filename(), 'r')
        for row in file_object:
            row_arr = row.split()
            if self.is_valid(row_arr):
                valid_count += 1
        return valid_count

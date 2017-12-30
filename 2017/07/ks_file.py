class KSFile():

    filename = None

    def open_and_close(self, f):
        if self.filename == None:
            self.filename = input("Enter filename > ")
        
        file_object = open(self.filename, 'r')
        
        f()
        
        file_object.close()

import aiofiles
#TODO add iofiles
class TextFileRepository:

    def __init__(self, file):
        self.file = file

    def add_item(self, result):
        l = [str(i) for i in result]
        self.file.write(','.join(l))


    def get_all(self):
        lines = self.file.readlines()
        print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        print(lines)
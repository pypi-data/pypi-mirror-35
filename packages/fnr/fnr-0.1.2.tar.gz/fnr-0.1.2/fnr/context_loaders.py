from abc import ABC, abstractmethod

class context_loader(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def load_context_vars(self):
        pass

class file_loader(context_loader):
    def __init__(self, f):
        self.file = f
        self.file_format = 'csv'

    def __file_not_found_handler(self):
        print('Err: Input file ({}) not found'.format(self.file) )

    def show(self):
        try:
            with open(self.file) as context_file:
                print(context_file.read())
        except FileNotFoundError:
            self.__file_not_found_handler()

    def load_context_vars(self):
        try:
            with open(self.file) as context_file:
                return {row.split(',')[0]:row.strip().split(',')[1] for row in context_file}
        except FileNotFoundError:
            self.__file_not_found_handler()

class console_loader(context_loader):
    def __init__(self):
        self.context = {}

    def __load_new_pair(self):
        print('---------------------')
        find = input('Enter value to find: ')

        if find == '':
            return -1

        replace = input('Enter value for replacement: ')

        self.context[find] = replace
        print('---------------------')

    def load_context_vars(self):
        self.__load_new_pair()
        print('You may proceed to add more find & replace keys below. Use an empty find value to end (press Enter).')

        while(self.__load_new_pair() != -1):
            pass

        return self.context
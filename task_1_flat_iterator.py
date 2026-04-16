class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.outer_index = 0
        self.inner_index = 0
        return self

    def __next__(self):
        while self.outer_index < len(self.list_of_list):
            if self.inner_index < len(self.list_of_list[self.outer_index]):
                item = self.list_of_list[self.outer_index][self.inner_index]
                self.inner_index += 1
                return item
            self.outer_index += 1
            self.inner_index = 0
        raise StopIteration

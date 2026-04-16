class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.items = []
        self.index = 0

    def __iter__(self):
        self.items = list(self._flatten(self.list_of_list))
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration

        item = self.items[self.index]
        self.index += 1
        return item

    def _flatten(self, nested_list):
        for item in nested_list:
            if isinstance(item, list):
                yield from self._flatten(item)
            else:
                yield item

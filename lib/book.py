class Book:
    def __init__(self, title="", page_count=0, author=""):
        self.title = title
        self.author = author
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            print("page_count must be an integer")
            if not hasattr(self, "_page_count"):
                self._page_count = 0
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    def __init__(self, title="", page_count=0, author=""):
        self.title = title
        self.author = author
        
        if not isinstance(page_count, int) or isinstance(page_count, bool):
            print("page_count must be an integer")
            self.page_count = 0
        else:
            self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
class Coffee:
    VALID_SIZES = ["small", "medium", "large"]

    def __init__(self, size="small", price=0.0):
        self.size = size
        self.price = float(price)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, str) and value.lower() in self.VALID_SIZES:
            self._size = value.lower()
        else:
            print("size must be small, medium, or large.")
            if not hasattr(self, "_size"):
                self._size = "small"

    def tip(self, amount=1):
        self.price += float(amount)
        print("This coffee is delicious, here’s a tip!")
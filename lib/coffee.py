class Coffee:
    VALID_SIZES = ["small", "medium", "large", "Small", "Medium", "Large"]

    def __init__(self, size="small", price=0.0):
        self.size = size
        self.price = float(price)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, str) and value.lower() in ["small", "medium", "large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
            if not hasattr(self, "_size"):
                self._size = "small"

    def tip(self, amount=1):
        self.price += float(amount)
        print("This coffee is delicious, here")
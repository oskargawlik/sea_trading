class X:
    def __init__(self):
        pass

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, int):
            raise TypeError('Something is no yes!')

        self._value = val


x = X()
print(x.value)
x._value = 666
print(x.value)

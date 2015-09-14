class DemocracyDigit(int):

    def _is_my_political_pal(self, other):
        return type(other) == DemocracyDigit

    def _we_are_the_same(self, other):
        if self._is_my_political_pal(other):
            return False
        return True

    def _we_are_equal(self, other):
        if self._is_my_political_pal(other):
            return True
        return False

    def __eq__(self, other):
        return self._we_are_equal(other)

    def __ne__(self, other):
        return self._we_are_the_same(other)

    def __ge__(self, other):
        return self._we_are_the_same(other)

    def __le__(self, other):
        return self._we_are_the_same(other)

    def __lt__(self, other):
        return self._we_are_the_same(other)

    def __gt__(self, other):
        return self._we_are_the_same(other)


a = DemocracyDigit(10)
b = DemocracyDigit(999)
c = 10

print(a != b)
print(a == b)
print(a >= b)
print(a <= b)
print(b > a)
print(b < a)

print(c == a)
print(c == b)


class Color(tuple):
    def __init__(self, r, g, b, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __new__(cls, r, g, b, a=255):
        return super(Color, cls).__new__(cls, (r, g, b, a))

    def rgb(self):
        return self.r, self.g, self.b

    def rgba(self):
        return self.r, self.g, self.b, self.a

    def __mul__(self, other):
        if isinstance(other, float):

            return Color(
                self.r * other,
                self.g * other,
                self.b * other
            )

        else:
            TypeError(f'Expected (float) got ({type(other)})')

    __rmul__ = __mul__

    def copy(self):
        t = tuple(self)[:]
        return Color.from_tuple(t)

    @staticmethod
    def lerp(a, b, value):
        if value <= 0:
            return a
        elif value >= 1:
            return b

        pos = value / 1
        neg = (1 - value) / 1

        return Color(
            a.r * pos + b.r * neg,
            a.g * pos + b.g * neg,
            a.b * pos + b.b * neg,
        )

    @staticmethod
    def from_tuple(t):
        return Color(t[0], t[1], t[2], t[3])

    def __str__(self):
        return f'<Color{vars(self)}>'

import sys
import math


def prt(string):
    print(str(string), file=sys.stderr, flush=True)


class Vec2:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def opposite(self):
        return Vec2(W - self.x, H - self.y)

    def invert(self):
        return Vec2(-self.x, -self.y)

    def normalized(self):
        norm = self.norm()
        if norm == 0:
            return Vec2(100, 0)
        else:
            return Vec2(100 * (float(self.x) / norm),
                        100 * (float(self.y) / norm))

    def norm(self):
        return self.dist(Vec2(0, 0))

    def get(self):
        return (self.x, self.y)

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, value):
        return Vec2(self.x * value, self.y * value)

    def __truediv__(self, value):
        return Vec2(self.x / value, self.y / value)

    def angle(self, other):
        return math.atan2(self.y, self.x) * 180 / math.pi - math.atan2(
            other.y, other.x) * 180 / math.pi

    def dist(self, other):
        return math.sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))

    def toGrid(self):
        return Vec2(self.x / TILE, self.y / TILE)

    def toFrame(self):
        return Vec2(self.x * TILE, self.y * TILE)

    def __str__(self):
        return "{x} {y}".format(x=str(self.x), y=str(self.y))


def easeInOutSine(x):
    return -(math.cos(math.pi * x) - 1) / 2


# game loop
while True:
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [
        int(i) for i in input().split()
    ]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    hasBoost = True
    opponent = Vec2(opponent_x, opponent_y)
    target = Vec2(next_checkpoint_x, next_checkpoint_y)
    pos = Vec2(x, y)

    prt(next_checkpoint_angle)
    prt((target - pos).angle(target))

    thrust = int(100 * (1 - (abs(next_checkpoint_angle) / 180)))
    if next_checkpoint_dist < 1400:
        thrust = int(thrust / 5)
    elif next_checkpoint_dist > 5000 and abs(
            next_checkpoint_angle) < 20 and hasBoost:
        thrust = "BOOST"
        hasBoost = False

    print("{x} {y} {thrust}".format(x=target.x, y=target.y, thrust=thrust))

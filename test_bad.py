from traffic.car import Car


def test_coords(c1, c2, length=2):
    car1 = Car(None, 0, 'r', c1, length, False)
    car2 = Car(None, 0, 'd', c2, length, False)
    print(car1.overlaps(car2))

test_coords((0, 0), (0, 1))  # False
test_coords((0, 0), (0, 0))  # True
test_coords((0, 1), (0, 0))  # True
test_coords((0, 0), (1, 0))  # True
test_coords((0, 1), (1, 0))  # True

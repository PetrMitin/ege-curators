class Plate:
    def __init__(self, l1, l2, l3, d1, d2, d3):
        self.plate = l1 + str(d1) + str(d2) + str(d3) + l2 + l3

    def __lt__(self, other):
        for i in range(6):
            if self.plate[i] < other.plate[i]:
                return True
            elif self.plate[i] == other.plate[i]:
                continue
        return False

    def __le__(self, other):
        for i in range(6):
            if self.plate[i] < other.plate[i]:
                return True
            elif self.plate[i] == other.plate[i]:
                continue
        return True

    def __gt__(self, other):
        for i in range(6):
            if self.plate[i] > other.plate[i]:
                return True
            elif self.plate[i] == other.plate[i]:
                continue
        return False

    def __ge__(self, other):
        for i in range(6):
            if self.plate[i] > other.plate[i]:
                return True
            elif self.plate[i] == other.plate[i]:
                continue
        return True

alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def print_n_plates(n):
    count = 0
    for l1 in alph:
        for d1 in range(10):
            for d2 in range(10):
                for d3 in range(10):
                    for l2 in alph:
                        for l3 in alph:
                            if count < n:
                                new_plate = Plate(l1, l2, l3, d1, d2, d3)
                                print(new_plate.plate)
                                count += 1
                            else:
                                return None
n = int(input())
print_n_plates(n)

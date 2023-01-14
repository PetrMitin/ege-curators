#ОТВЕТ: 1535

def solve():
    for a in range(15**10):
        for x in range(13):
            for y in range(13):
                m = 5 + x * 15 + 3 * (15 ** 2) + 2 * (15**3) + y*(15**4) + 2*(15**5)
                n = y + 9*13+x*(13**2) + 7*(13**3) + 6*(13**4)
                if (m+a) % n == 0:
                    print(a)
                    return None
solve()
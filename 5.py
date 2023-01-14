gl = 'AO'
sogl = 'CDF'

with open('hh.txt') as file:
    ans = 0
    state = 0
    count = 0
    prev_let1 = ''
    for line in file:
        for let in line:
            if let in sogl:
                if prev_let1 in sogl:
                    state = 2
                else:
                    state = 1
            elif let in gl:
                if state == 2:
                    count += 1
                    state = 4
                else:
                    state = 0
            if count != 0 and state == 0:
                ans = max(ans, count)
                count = 0
            prev_let1 = let
    print(ans)
    file.close()


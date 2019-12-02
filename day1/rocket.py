
import os
# Required fuel calc:
# 1. Mass / 3
# 2. Round Down
# 3. - 2

def fuel(mass):
    divided = mass / 3
    divided = int(divided)
    return divided - 2



if __name__ == '__main__':
    total = 0
    lines = [line.rstrip('\n') for line in open('input.txt', 'r')]
    for line in lines:
        total += fuel(int(line))

    print(total)
